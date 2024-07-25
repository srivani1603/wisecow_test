
#Build the Docker image using the Dockerfile.
docker build -t wisecow-app .

#Test the Docker image by running a container.
docker run -p 3000:3000 wisecow-app