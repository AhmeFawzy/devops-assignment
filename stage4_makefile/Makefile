# Stage 4 Makefile
# Builds and runs the Python Docker script for Stage 3

IMAGE_NAME=devops-python-script:stage3
STAGE3_DIR=../stage3_python_script_dockerfile
OUTPUT_DIR=$(STAGE3_DIR)/output
API_URL=http://host.docker.internal:5000
SSH_KEY=$(HOME)/.ssh/id_rsa
REMOTE_FILE=/home/floki/random.txt

# Allow overriding REMOTE_HOST and REMOTE_USER from the command line
REMOTE_HOST=192.168.20.131
REMOTE_USER=floki

# Build Docker image
build:
	docker build -t $(IMAGE_NAME) $(STAGE3_DIR)

# Run /hello mode and save output locally
hello:
	mkdir -p $(OUTPUT_DIR)
	docker run --rm \
		-v $(OUTPUT_DIR):/app/output \
		$(IMAGE_NAME) \
		--mode hello --api-url $(API_URL) --local-file /app/output/hello.txt

# Run /random mode via SSH key
random:
	docker run --rm \
		-v $(SSH_KEY):/root/.ssh/id_rsa:ro \
		$(IMAGE_NAME) \
		--mode random \
		--api-url $(API_URL) \
		--remote-host $(REMOTE_HOST) \
		--remote-user $(REMOTE_USER) \
		--ssh-key /root/.ssh/id_rsa \
		--remote-file $(REMOTE_FILE)
