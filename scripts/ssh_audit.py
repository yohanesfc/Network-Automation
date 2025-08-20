import socket
import sys

def check_ssh(host, port=22, timeout=3):
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except Exception:
        return False

if __name__ == "__main__":
    host = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
    ok = check_ssh(host)
    print(f"SSH on {host}: {'Open ✅' if ok else 'Closed ❌'}")