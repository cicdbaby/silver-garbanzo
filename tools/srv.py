import threading,http.server,functools,socketserver
def serve(d='/home/claude/silver-garbanzo/dist',port=8765):
    H=functools.partial(http.server.SimpleHTTPRequestHandler,directory=d)
    H.log_message=lambda *a:None
    socketserver.TCPServer.allow_reuse_address=True
    s=socketserver.ThreadingTCPServer(('127.0.0.1',port),H);threading.Thread(target=s.serve_forever,daemon=True).start();return s
