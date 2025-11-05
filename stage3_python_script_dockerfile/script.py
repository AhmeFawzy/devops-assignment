import argparse
import requests  # type: ignore
import paramiko  # type: ignore
import os

# ----------------------------
# Helper functions
# ----------------------------

def get_hello(api_url, local_file):
    response = requests.get(f"{api_url}/hello")
    if response.status_code == 200:
        with open(local_file, "w") as f:
            f.write(response.text)
        print(f"Saved /hello response to {local_file}")
    else:
        print(f"Failed to fetch /hello: {response.status_code}")

def get_random_and_ssh(api_url, remote_host, remote_user, ssh_key_path, remote_file):
    response = requests.get(f"{api_url}/random")
    if response.status_code == 200:
        # Expand ~ in case key path uses tilde
        ssh_key_path = os.path.expanduser(ssh_key_path)
        if not os.path.exists(ssh_key_path):
            raise FileNotFoundError(f"SSH key not found: {ssh_key_path}")
        
        # Initialize SSH client with key
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        try:
            private_key = paramiko.RSAKey.from_private_key_file(ssh_key_path)
            client.connect(remote_host, username=remote_user, pkey=private_key)
            
            sftp = client.open_sftp()
            with sftp.file(remote_file, "w") as f:
                f.write(response.text)
            sftp.close()
            client.close()
            print(f"✅ Saved /random response to {remote_host}:{remote_file} via SSH key.")
        except Exception as e:
            print(f"❌ SSH connection failed: {e}")
    else:
        print(f"Failed to fetch /random: {response.status_code}")

# ----------------------------
# CLI Argument parsing
# ----------------------------
parser = argparse.ArgumentParser(description="Fetch /hello or /random from Flask API")
parser.add_argument("--mode", choices=["hello", "random"], required=True)
parser.add_argument("--api-url", required=True)
parser.add_argument("--local-file", default="hello.txt")
parser.add_argument("--remote-host")
parser.add_argument("--remote-user")
parser.add_argument("--ssh-key", help="Path to SSH private key file (e.g., ~/.ssh/id_rsa)")
parser.add_argument("--remote-file", default="/tmp/random.txt")

args = parser.parse_args()

if args.mode == "hello":
    get_hello(args.api_url, args.local_file)
elif args.mode == "random":
    if not all([args.remote_host, args.remote_user, args.ssh_key]):
        print("Remote host, user, and ssh-key required for random mode")
    else:
        get_random_and_ssh(args.api_url, args.remote_host, args.remote_user, args.ssh_key, args.remote_file)