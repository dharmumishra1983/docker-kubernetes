# Prerequisite 
### make sure below environment should be available or install in local
```commandline
python
Kubernetes
Docker Desktop
minikube
```
This is Python based web App(Flash) to test Docker and Kubernetes functionality
Testing this app using Docker and also how Docker image is getting deployed into Kubernetes Cluster
Once it gets deployed into Kubernetes , how we can access using minikube

Create docker image of project using `Dockerfile` using below command
`docker build -t webapp:1.0 .`
or
`docker-compose build`
`docker-compose up -d` run the app
`docker-compose down` terminate app

## Now how we can deploy into APP kubernetes cluster
 - Go to kubernetes directory and refer `service.yml` and `deployment.yml`
 - Execute command `kubectl apply -f deployment.yml`
 - Execute command `kubectl apply -f service.yml`
 - Execute command `minikube service list`
 - get service name from previous command and execute `minikube service  web-service --url` and get url and check application
 
more details: https://www.youtube.com/watch?v=9H_kwRiImPQ&ab_channel=DevOpsMadeEasy
