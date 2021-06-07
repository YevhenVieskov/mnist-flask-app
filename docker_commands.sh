# prefix commands with sudo if user is not in docker group
# build docker image
docker build -t mnist_microservice .

# check docker image
docker images | grep mnist_microservice

# run docker container
docker run -p 8888:5000 --name mnist_microservice 
