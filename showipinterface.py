import paramiko
import time

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# For loop and range() function to connect to multiple devices
for device in range(11, 12):
    host = "172.16.10." + str(device)
    print("\n##### Connecting to the device " + host + " #####")

    client.connect(
        hostname=host, 
        username="admin", 
        password="cisco", 
        look_for_keys=False, 
        allow_agent=False,
    )

    ssh_client = client.invoke_shell()
    ssh_client.send("show ip int brief\n")
    time.sleep(3)
    output = ssh_client.recv(65000)
    print(output.decode("ascii"))
    client.close()
