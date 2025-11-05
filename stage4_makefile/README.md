# **Stage 4: Makefile - DevOps Assignment**

## Overview

This Makefile builds and runs the Stage 3 Python Docker script.

* **hello mode** – fetch `/hello` from Flask API and save locally.
* **random mode** – fetch `/random` and save to a remote VM via SSH key.
* **build** – rebuild the Docker image when `script.py` or dependencies change.
* Dynamic variables allow switching between VMs.

---

## Usage

### 1. Build Docker image

```bash
make build
```

### 2. Hello mode (local)

```bash
make hello
```

Saves `/hello` response to `output/` folder in Stage 3 Docker folder.

### 3. Random mode (remote via SSH key)

```bash
make random REMOTE_HOST=<VM-IP> REMOTE_USER=<USER>
```

Saves `/random` response to `/home/<USER>/random.txt` on the VM.
Example:

```bash
make random REMOTE_HOST=192.168.20.130 REMOTE_USER=ahmed
```

---

## Variables

| Variable      | Default                                                              | Description   |
| ------------- | -------------------------------------------------------------------- | ------------- |
| `REMOTE_HOST` | 192.168.20.131                                                       | VM IP         |
| `REMOTE_USER` | floki                                                                | VM user       |
| `SSH_KEY`     | $(HOME)/.ssh/id_rsa                                                  | Private key   |
| `API_URL`     | [http://host.docker.internal:5000](http://host.docker.internal:5000) | Flask API URL |

---

## Notes

* Stage 3 Docker folder must contain `script.py`, `requirements.txt`, and `Dockerfile`.
* For WSL2, mount SSH key properly (`/mnt/c/Users/ahmed/.ssh/id_rsa`).
* `hello` saves locally; `random` uses SSH key for remote VM.

