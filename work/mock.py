import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
U={"id":"u1","displayName":"tester"}
SAVE={"payload":None}
class H(BaseHTTPRequestHandler):
    def _j(self,o,c=200):
        b=json.dumps(o).encode(); self.send_response(c); self.send_header("content-type","application/json"); self.send_header("content-length",str(len(b))); self.end_headers(); self.wfile.write(b)
    def do_GET(self):
        if self.path.startswith("/api/account/me"): return self._j({"user":U})
        if self.path.startswith("/api/save"): return self._j(SAVE)
        return self._j({"ok":True,"graves":[],"shinies":[]})
    def do_POST(self):
        n=int(self.headers.get("content-length") or 0); body=self.rfile.read(n)
        if self.path.startswith("/api/save"):
            try: SAVE["payload"]=json.loads(body).get("payload")
            except Exception: pass
            return self._j({"ok":True})
        return self._j({"user":U,"ok":True})
    do_PUT = do_POST
    def do_HEAD(self):
        self.send_response(404); self.end_headers()
    def log_message(self,*a): pass
ThreadingHTTPServer(("0.0.0.0",8001),H).serve_forever()
