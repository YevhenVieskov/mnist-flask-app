# prefix commands with sudo if user is not in docker group
# build docker image
docker build -t app .

# check docker image
docker images | grep app

# run docker container
docker run -p 8888:5000 --name app
