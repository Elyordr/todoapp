FROM postman/newman:alpine

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

CMD ["run", "pm_collection.json"]