---
title: "Reproducibility Engineering - Exercise Sheet 1"
tags:
  - practice
  - reproducibility-engineering
  - semester-1
course: "Reproducibility Engineering"
status: current
last_updated: 2026-06-02
---

# Exercise Sheet 1 — Docker Basics & Image Comparison

> **Note:** No official solutions available.

Lab Sessions: April 23/24, 2026

## Exercises

### 1. Prerequisites
Ensure you have a working Docker setup on your local machine or on the Docker server. Follow the instructions on the preliminary sheets in StudIP.

### 2. Introduction to Docker
**(a) Basic Concepts:** Understand the definitions:
- **Image:** A read-only template defining the contents of a container (blueprint).
- **Container:** A running instance of an image, isolated from other containers and the host.
- **Dockerfile:** A script containing instructions to build an image.

**(b) Docker Architecture:** Understand the layered architecture — application container → Docker engine → host file system → OS kernel. Containers share the host kernel but remain isolated through their own file systems.

**(c) Working with Containers:**
- Building images: `docker build` with a Dockerfile.
- Running containers: `docker run`.
- Copying files: `docker cp` between host and container.
- Bind mounts: Sharing directories using `-v`.

### 3. Setting Up a Docker Container

**(3.1) Notation:** Understand the prefixes `user@host$` (execute on host) and `user@container$` (execute inside container).

**(3.2) Building an Image:**
1. Clone the RepEng FIMGit Repository: `git clone https://git.fim.uni-passau.de/koehnen/RepEng`
2. Navigate to `LabSession1/`
3. Inspect the `Dockerfile`
4. Build with tag: `docker build -t lab1 .`
5. Verify: `docker image ls`

**(3.3) Running a Container from an Image:**
1. Run interactively: `docker run -it --name lab1-cont lab1`
2. Understand the command prompt elements (user, container ID, working directory)
3. Inspect contents: `ls -l`
4. Exit with `exit`

### 4. Working with Docker Containers: Image Comparison with Python

**(a) Visual Inspection:** Open `res/fox.jpg` and `res/fox_secret.jpg`. Compare visually, check timestamps and file sizes. Observe that the files appear identical by visual inspection and have the same size/timestamps.

**(b) Bitwise Comparison:** Compute SHA-256 checksums:
```
sha256sum res/fox.jpg
sha256sum res/fox_secret.jpg
```
Observe whether the checksums differ — this reveals the secret message embedded in one image.

**(c) Statistical Analysis with Python:**
1. Start the container: `docker start lab1-cont`
2. Enter: `docker exec -it lab1-cont bash`
3. Install: `pip3 install --user numpy pillow`
4. Write `correlation.py` that:
   - Loads both images with `Image.open`
   - Converts to grayscale arrays
   - Converts to NumPy arrays and flattens
   - Computes Pearson correlation with `numpy.corrcoef`
5. Execute: `python3 correlation.py`
6. Interpret the correlation value (close to 1.0 means nearly identical pixel values).

**(d) File Transfer with `docker cp`:**
1. Copy script to host: `docker cp lab1-cont:/home/repro/correlation.py ~`
2. Edit on host to add `print("Edited on host.")`
3. Copy back: `docker cp ~/correlation.py lab1-cont:/home/repro/correlation.py`
4. Run in container to verify the edit.

**(e) Bind Mounts:**
1. Create new container with mount: `docker run -it --name lab1-cont-mount -v /home/user/lab1-mount:/home/repro/mount lab1`
2. Create `test.sh` on host with `echo "Test passed!"`
3. In container: `sudo chmod +x mount/test.sh`
4. Execute: `./mount/test.sh`

### 5. Working with Docker Containers (Multiple Choice)

Given a Dockerfile and `experiment.sh` script, Alice (Debian 13, Intel i7) and Bob (Ubuntu 25, AMD Ryzen 9) build and run the same container.

**(a)** Which statement is correct?
- They will get the same output because the script is deterministic and the container provides the same environment.

**(b)** Which command shows that `experiment.sh` exists inside the container?
- `docker exec exp-cont ls /usr/local/bin/experiment.sh`

**(c)** After `docker cp exp-cont:/usr/local/bin/experiment.sh experiment_copy.sh`, which command shows the file?
- `user@host$ ls experiment_copy.sh`

## Related Lectures

- [[reproducibility-engineering-lecture-1]]
- [[reproducibility-engineering-lecture-2]]
