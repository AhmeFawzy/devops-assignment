# DevOps Assignment - Full Overview

## Overview

This project implements a multi-stage DevOps assignment, including a Flask API server, a Python script, Dockerization, Makefile automation, and CI/CD setup with Jenkins. The goal is to deploy, test, and run a simple REST API with automation, containerization, and command-line execution.

The project is structured into **five stages**, each in its own folder.

---

## Stage 1: API Server (Flask + Ansible)

**Goal:** Implement a simple REST API server and deploy it on a Linux VM.

* **Endpoints:**

  * `GET /hello` → returns `"hello"`
  * `GET /random` → returns a random string
* **Deployment:** Ansible playbook to a Linux VM
* **Access:**

  * Locally: `http://127.0.0.1:5000` on the VM
  * Remotely: Nginx reverse proxy + router port forwarding
* **Folder:** `stage1_api_server/`

---

## Stage 2: Python Script

**Goal:** Interact with the Flask API via a Python script.

* **Modes:**

  * `hello` → fetch `/hello` and save locally
  * `random` → fetch `/random` and save on a remote VM via SSH
* **Dependencies:** `requests`, `paramiko`
* **Folder:** `stage2_python_script/`
* **Usage example:**

```bash
# Local hello
python script.py --mode hello --api-url http://<VM-IP>:5000 --local-file hello.txt

# Remote random
python script.py --mode random --api-url http://<VM-IP>:5000 \
  --remote-host <VM-IP> --remote-user <USER> --remote-password <PASSWORD> --remote-file /home/<USER>/random.txt
```

---

## Stage 3: Dockerization

**Goal:** Wrap the Python script in a Docker container.

* **Docker image:** `devops-python-script:stage3`
* **Usage example:**

```bash
docker run --rm -v ./output:/app/output devops-python-script:stage3 \
  --mode hello --api-url http://host.docker.internal:5000 --local-file /app/output/hello.txt
```

* **Notes:** Use `host.docker.internal` to access the Flask API from the container. Output files are stored in a mounted `output` directory.

---

## Stage 4: Makefile Automation

**Goal:** Automate Docker builds and script execution.

* **Targets:**

  * `build` → build the Docker image
  * `hello` → run the script in hello mode
* **Usage example:**

```bash
# Build Docker image
make build

# Run hello mode
make hello
```

---

## Stage 5: Jenkins CI/CD

**Goal:** Automate builds and container execution with Jenkins.

* **Pipeline:** Parameterized pipeline to run `hello` or `random` modes.
* **Requirements:**

  * Jenkins running as a Docker container
  * SSH setup between Jenkins and GitHub
  * Docker access for building images and running containers
* **Features:**

  * Build Docker image for Python script
  * Run container in `hello` or `random` mode
  * Handle SSH keys for remote execution
* **Folder:** `stage5_jenkinsfile/`

---

