import subprocess
from datetime import datetime


def ping_server(address):
    # -c 1 to send one ping, otherwise it never stops on Linux
    command = ["ping", "-c", "1", address]
    result = subprocess.run(command, capture_output=True)
    # in this case 0 if the server answered
    if result.returncode == 0:
        return True
    else:
        return False


def check_server(server):
    if ping_server(server["address"]):
        server["status"] = "up"
    else:
        server["status"] = "down"

    now = datetime.now()
    server["last_checked"] = now.strftime("%Y-%m-%d %H:%M")


def check_all_servers(servers):
    for server in servers:
        check_server(server)
