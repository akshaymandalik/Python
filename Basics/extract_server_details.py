# import random
# import time

# ip_list = [
#     "192.168.1.10",
#     "192.168.1.11",
#     "192.168.1.12",
#     "192.168.1.13",
#     "192.168.1.14"
# ]

# servers = [
#     {
#         "ip": ip,
#         "hostname": f"server-{i+1}",
#         "os": random.choice(["Ubuntu 22.04", "RHEL 9", "Debian 12"]),
#         "cpu": random.choice(["4 vCPU", "8 vCPU", "16 vCPU"]),
#         "memory": random.choice(["8 GB", "16 GB", "32 GB", "64 GB"]),
#         "status": "Running",
#         "delay_seconds": random.randint(1, 15)
#     }
#     for i, ip in enumerate(ip_list)
# ]

# # Get the server details using IP.
# for ip in ip_list:
#         for server in servers:
#                 if ip == server["ip"]:
#                         time.sleep(server["delay_seconds"])
#                         print(server)
        

import time
import random
from concurrent.futures import ThreadPoolExecutor, as_completed

servers = [
    {"ip": "192.168.1.10", "delay": random.randint(1, 15)},
    {"ip": "192.168.1.11", "delay": random.randint(1, 15)},
    {"ip": "192.168.1.12", "delay": random.randint(1, 15)},
    {"ip": "192.168.1.13", "delay": random.randint(1, 15)},
]

def process_server(server):
    time.sleep(server["delay"])  # Simulate server work
    return f"{server['ip']} completed after {server['delay']}s"

with ThreadPoolExecutor(max_workers=4) as executor:
    futures = [executor.submit(process_server, server) for server in servers]

    for future in as_completed(futures):
        print(future.result())

