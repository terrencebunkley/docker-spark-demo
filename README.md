# Docker Spark Demo

### Requirements
Prework: 
Download and install Docker

Mac: https://docs.docker.com/docker-for-mac/release-notes/

Windows: https://docs.docker.com/docker-for-windows/release-notes/

Text editor, like Atom https://atom.io/

## Getting Started
#### Clone this repo (via Terminal / Command Prompt )
`git clone https://github.com/terrencebunkley/docker-spark-demo.git`


### Starting the container
Navigate inside cloned directory 

Using Mac: `cd docker-spark-demo`
 
Run the container
 
`docker run --name spark-master --rm -it  -p 4040:4040/tcp -p 8080:8080/tcp -p 8081:8081/tcp --mount type=bind,source="$(pwd)",target=/docker-spark-demo birgerk/apache-spark 
`

## Running Spark inside the container
### All of the following instructions are to be run inside the container

Open a new Terminal / Command Prompt window

Log into the container

`docker exec -it spark-master /bin/bash`

### Navigate to Spark execuable directory

`cd /usr/local/spark/bin`

### Execute one of examples with spark-submit executable
Execution Format

`./spark-submit <full-path-to-filename.py>`

Example :

`./spark-submit /docker-spark-demo/src/main/pi_count.py `

## Editing the files outside the container (on the host)
#### You can edit the files inside ./src/main/ using any text editor and they will be updated inside the container automatically