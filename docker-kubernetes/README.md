# docker-kubernetes
# Docker
Docker is a set of platform as a service products that use OS-level virtualization to deliver software in packages called containers. Containers are isolated from one another and bundle their own software, libraries and configuration files; they can communicate with each other through well-defined channels.
## How to install docker in MacOs?
Download from below link
https://docs.docker.com/docker-for-mac/install/

After successfully download and install Docker in Mac
Open Terminal and type below command to check, installation has happened properly or not

`docker version`

 response will be as below
```aidl
Client: Docker Engine - Community
Cloud integration: 1.0.7
Version:           20.10.2
API version:       1.41
Go version:        go1.13.15
Git commit:        2291f61
Built:             Mon Dec 28 16:12:42 2020
OS/Arch:           darwin/amd64
Context:           default
Experimental:      true
```
## How to run docker image?
`docker run <Image Name>`
## Some Useful Command 
* `docker run <Image Name> ls`: List all folder inside container
* `docker ps`: List all running docker images
* `docker ps --all`: Show the all docker images create ever
* `docker create <Image Name>`: If not created then create Image and return ID
* `docker start -a <Image Id>`: It will run Image.
* `docker system prune`: Delete all unused images from cache, we can get back from docker hub
* `docker ps -aq`: List all active Image Ids
* `docker stop $(docker ps -aq) or docker kill <Container ID>`: Stop all active images
* `docker rm $(docker ps -aq)`: Remove all active images
* `docker system prune`: clean up any resources — images, containers, volumes, and networks — that are dangling (not associated with a container)
* `docker system prune -a`: To additionally remove any stopped containers and all unused images (not just dangling images), add the -a flag to the command:
* `docker images -a`: List Image
* `docker rmi Image Image`: Remove Image
* `docker images -f dangling=true`: List with dangling images
* `docker images -a |  grep "pattern"`: List with pattern
* `docker images -a | grep "pattern" | awk '{print $3}' | xargs docker rmi`: Remove with pattern
* `docker images -a`: List Image
* `docker rmi $(docker images -a -q)`: Remove Image
* `docker run --rm image_name`: Run and Remove Images
* `docker ps -a -f status=exited`: List with status existed
* `docker rm $(docker ps -a -f status=exited -q)`: Remove with status existed
* `docker ps -a -f status=exited -f status=created`: List with created and exited
* `docker rm $(docker ps -a -f status=exited -f status=created -q)`: Remove created and exited.
* `docker stop $(docker ps -a -q)`: Stop all container
* `docker rm $(docker ps -a -q)`: Delete all container
* `docker volume ls`: List volume
* `docker volume rm volume_name volume_name`: Remove volume
* `docker build -f <give custom name of Dockerfile>`: By this command we can create image using non Dockerfile





### Example if system doesn't have redis install in local and want to run thru Docker
* `docker run redis`: To download image and run it.
* now we can run command inside container like `docker exec -it 711488938d05 redis-cli`

### How to enable shell promot inside Docker Container?
* `docker exec -it <Container Id> sh`: It will provide shell terminal to execute any command inside docker container.
  * `sh` is program which runs inside container and allow user to run any command inside container.
  
_Note: Every container is isolated to each other default,container can't share file system_ 

### How to create custom Docker Image?
Dockerfile-->Docker Client(CLI)-->Docker Server-->Usable Image
* Steps
  * Create any directory like `redis-image`
  * Navigate to directory
  * Create `Dockerfile` with below content
  
```aidl
    # Use existing image as base

    FROM alpine

    # Download and install dependency . apk is package manager program

    RUN apk add --update redis

    # Tell to image what to do when start container

    CMD ["redis-server"]
```
* `docker build .` or `docker build -t test:latest .` to build the image

_Note: `alpine` act like OS after that we can install any software in container and Dockerfile keep track of order of statement top to bottom while creating image_

### How to create Docker Image Manually ?
Let's assume that we have container running with ID 92f5759a269e98
Use below command for case of redis

`docker commit -c 'CMD ["redis-server"]' <Container ID>`

It will create a new Image!
_Note: `alpine` in Docker world it is compress version of image, every repository try to release this version


_Note: `docker run -p 8080:8080 <name>/node-web-app` port forwarding while launching application inside application. and run app as deamon `docker run -p 8080:8080 -d dharmu/node-web-app`_

### Docker Compose
Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application’s services. Then, with a single command, you create and start all the services from your configuration.

* `docker-compose up`: To run docker image using compose file.          
* `docker-compose up --build`: Build and run docker Image.
* `docker-compose up -d`: Run in background
* `docker-compose down`: Down all container
##### If docker container crashed then how to restart?
There are four attributes given to handle it
* `no`: never start 
* `always`:  always start if conytainer stopped by any reason
* `on-failure`: If exit with error code.
* `unless-stopped`: Forcibly stopped by user.

For that we can add attribute in `docker-compose.yml` file like `restart: always` for each service if we want to restart each service
or choose particular
