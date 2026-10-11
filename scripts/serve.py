#!/usr/bin/env python3
"""Preview public pages only; never expose Git metadata or internal legal templates."""

import argparse
from http import HTTPStatus
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import unquote, urlsplit

from site_common import ROOT, public_files


class PublicHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def send_head(self):
        request_path = unquote(urlsplit(self.path).path)
        candidate = (ROOT / request_path.lstrip("/")).resolve()
        if not candidate.is_relative_to(ROOT):
            self.send_error(HTTPStatus.NOT_FOUND)
            return None
        if candidate.is_dir():
            candidate = candidate / "index.html"
        if candidate not in public_files():
            self.send_error(HTTPStatus.NOT_FOUND)
            return None
        return super().send_head()

    def send_error(self, code, message=None, explain=None):
        if code != HTTPStatus.NOT_FOUND:
            return super().send_error(code, message, explain)
        body = (ROOT / "404.html").read_bytes()
        self.send_response(HTTPStatus.NOT_FOUND)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(body)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()
    server = ThreadingHTTPServer(("127.0.0.1", args.port), PublicHandler)
    print(f"Vista pública local: http://127.0.0.1:{args.port}/", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
