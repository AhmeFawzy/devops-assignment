# Stage 5: Jenkins CI/CD Pipeline

This stage automates building and running the Stage 3 Dockerized Python script using Jenkins.

---

## Prerequisites

* Jenkins installed **as a Docker container** with access to Docker (`/var/run/docker.sock`) to build images and run containers.
* SSH setup between Jenkins and GitHub for repository access.
* SSH credentials configured in Jenkins for remote VM access (`acronis-vm-ssh`).
* Stage 3 Dockerized Python script in `stage3_python_script_dockerfile/`.

---

## Pipeline Overview

**Parameters:**

| Name        | Description                             |
| ----------- | --------------------------------------- |
| MODE        | `hello` (local) or `random` (remote VM) |
| REMOTE_HOST | VM IP address for random mode           |
| REMOTE_USER | VM username for random mode             |

**Stages:**

1. **Build Docker Image** – builds `devops-python-script:stage3`.
2. **Run Container** –

   * HELLO mode: runs locally, outputs in `output/hello.txt`.
   * RANDOM mode: runs on remote VM via SSH, outputs in `/home/<VM_USER>/random.txt`.

---

## How to Run

1. Open the Jenkins job and click **Build with Parameters**.
2. Select mode and provide VM details if needed.
3. Monitor the console for build and execution logs.


