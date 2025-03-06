
logs = [
{"username": "alice", "ip": "192.168.1.1", "status": "success", },
{"username": "bob", "ip": "192.168.1.2", "status": "failure", },
{"username": "alice", "ip": "192.168.1.3", "status": "failure", },
{"username": "carol", "ip": "192.168.1.4", "status": "success", },
{"username": "bob", "ip": "192.168.1.2", "status": "failure", },
{"username": "alice", "ip": "192.168.1.1", "status": "failure", },
{"username": "dave", "ip": "192.168.1.5", "status": "failure", },
{"username": "bob", "ip": "192.168.1.6", "status": "failure", },
]
# Task 1: Find the unique IPs in the logs
unique_ips ={log["ip"] for log in logs}
print("Unique IPs:", unique_ips)

# Task 2: look for special ip address (192.168.1.4) 
special_ip = "192.168.1.4"
if special_ip in unique_ips:
    print("Special IP exists")
else:
    print("Special IP does not exist")

# Task 3: count of failed login attempts per user
failed_attempts = {}

for log in logs:
    if log["status"] == "failure":
        username = log["username"]
        if username not in failed_attempts:
            failed_attempts[username] = 0
        failed_attempts[username] += 1

print("Failed login attempts per user:" , failed_attempts)
















