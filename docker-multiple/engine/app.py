import argparse
from fastapi import FastAPI
import uvicorn
import time
import socket
from datetime import datetime, timedelta, timezone

app = FastAPI()


def fetchdetails():
    hostname = socket .gethostname()
    host_ip = socket.gethostbyname(hostname)

    return str(hostname), str(host_ip)

def get_time_now():
    now = datetime.now(timezone.utc) + timedelta(hours=5, minutes=30)
    return now.isoformat()

@app.get("/")
async def root():
    hostname, ip = fetchdetails()
    return f"This is Engine! Host: {hostname} IP: {ip} VER:1.0"

@app.get("/delay/")
async def read_item(delay: int = 0):
    start_time = get_time_now()
    time.sleep(delay)
    return {
        "start_time": start_time,
        "delayed": delay,
        "end_time": get_time_now()
    }

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--ip', help='Server IP Address', type=str, default='0.0.0.0')
    parser.add_argument('--port', help='Server Port Number', type=int, default=5000)
    args = parser.parse_args()

    _ip_address = args.ip
    _port = args.port
    print("=" * 80)
    print(f"Swagger url: http://{_ip_address}:{_port}/docs")
    print("=" * 80)
    uvicorn.run(app, host=_ip_address, port=int(_port))


if __name__ == "__main__":
    main()