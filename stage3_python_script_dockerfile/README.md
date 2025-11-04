# Stage 3: Dockerized Python Script - DevOps Assignment

## Overview

This stage wraps the Stage 2 Python script in a Docker container. The container allows two modes:

1. **`hello`** – Fetch `/hello` from the Flask API and save it locally.
2. **`random`** – Fetch `/random` from the Flask API and save it to a remote VM via SSH.

The image contains all dependencies, so you only need to specify the mode and relevant parameters.

---

## Build the Docker Image

```bash
docker build -t devops-python-script:stage3 .
```

---

## Usage

### 1. Hello Mode (Local File)

Create a folder on your host for output:

```powershell
mkdir output
```

Run the container:

```powershell
docker run --rm -v ${PWD}/output:/app/output devops-python-script:stage3 --mode hello --api-url http://host.docker.internal:5000 --local-file /app/output/hello.txt
```

* The file `hello.txt` will appear in `stage3_python_script_dockerfile/output/`.

---

### 2. Random Mode (Remote File via SSH)

```powershell
docker run --rm devops-python-script:stage3 `
  --mode random `
  --api-url http://host.docker.internal:5000 `
  --remote-host <VM-IP> `
  --remote-user <USER> `
  --remote-password <PASSWORD> `
  --remote-file /home/<USER>/random.txt
```

* Replace `<VM-IP>`, `<USER>`, `<PASSWORD>` with your VM details.
* Verify the file on the VM:

```bash
ssh <USER>@<VM-IP>
cat /home/<USER>/random.txt
```

---

## Notes

* `host.docker.internal` allows the container to reach the Flask API on your host.
* Use `--rm` for ephemeral containers.
* Mount a local folder to persist files written by the container.
