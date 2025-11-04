# Stage 1: API Server - DevOps Assignment

## Overview
This project implements a simple Flask API server as Stage 1 of the DevOps assignment.  
The server has two endpoints and is deployed on a Linux VM using Ansible. Nginx and port forwarding can be configured later to expose the server externally.

---

## Steps Completed

1. **GitHub Repository**
   - Created a GitHub repo to host the project.

2. **VM Setup**
   - Created a Linux VM using VMware Workstation.
   - Configured SSH access for deployment.

3. **Python & Flask**
   - Installed Python 3.13.9 on the VM.
   - Installed Flask locally and verified the API server works.

4. **Move App to VM**
   - Used `scp` to copy the `app` folder to the VM.
   - Installed Python requirements: `pip install -r requirements.txt`.
   - Tested `python3 server.py` to ensure the server runs correctly.

5. **Ansible Inventory**
   - Created `inventory.ini` with VM IP address and private key path.
   - Supports dynamic inventory for AWS in later stages.

6. **Ansible Playbook**
   - Installs Python 3 and pip if missing.
   - Creates application directory on VM.
   - Copies the Flask app files to the target folder.
   - Installs required Python packages in a virtual environment.
   - Kills any existing Flask process.
   - Starts the Flask app in the background.
   - Verifies the Flask app is running successfully and displays the URL.

7. **Accessing the App**
   - The app can be accessed locally via `http://127.0.0.1:5000` on the VM.
   - With port forwarding and/or Nginx, the app can be accessed from other devices on the network or public internet.

---

## Flask API Endpoints

1. **GET /hello**
   - Returns: `"hello"`

2. **GET /random**
   - Returns a random string.

---

## Folder Structure

stage1_api_server/
│
├── app/
│ ├── server.py
│ └── requirements.txt
│
└── ansible/
├── inventory.ini
└── playbook.yml

---

## Running the Project

1. Ensure the VM is running and accessible via SSH.
2. Run the Ansible playbook from the `ansible` folder:

```bash
ansible-playbook -i inventory.ini playbook.yml --ask-become-pass
```
## After running the playbook
3. Once the playbook completes, the Flask app will be running on the VM.
4. Open a browser or use curl to access the endpoints:
        curl http://127.0.0.1:5000/hello
        curl http://127.0.0.1:5000/random

Notes
    The playbook is idempotent: it can be run multiple times safely.

    The Flask app runs in a virtual environment to avoid system-wide package conflicts.

