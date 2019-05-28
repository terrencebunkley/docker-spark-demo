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

#### Download the data from Google storage and extract into a folder named "data" in the project folder 'docker-spark-demo'
https://storage.googleapis.com/twsg-data-eng-bootcamp-data/data.zip

There should be different folders (ie. "credit_card", "crimes") under "docker-spark-demo/data/ 

### Starting the container
Navigate inside cloned directory 

Using Mac: `cd docker-spark-demo`
 
Run the container (Command explained near bottom of this README) 
 
`docker run --name spark-master --rm -it  -p 4040:4040/tcp -p 8080:8080/tcp -p 8081:8081/tcp --mount type=bind,source="$(pwd)",target=/docker-spark-demo birgerk/apache-spark 
`

Once the above command is ran the console will only output the result of starting the container. 

You can only exit this by pressing "Control-D" to shut down the container. (MacOS)

## Running Spark inside the container
### All of the following instructions are to be run inside the terminal

Open a new Terminal / Command Prompt window

Log into the container

`docker exec -it spark-master /bin/bash`

## Overwrite the logging settings for this demo
`cp /docker-spark-demo/container_conf/log4j.properties /usr/local/spark/conf/`

### Navigate to Spark executable directory

`cd /usr/local/spark/bin`

### Execute one of examples with spark-submit executable
Execution Format

`./spark-submit <full-path-to-filename.py>`

Example :

`./spark-submit /docker-spark-demo/src/main/pi_count.py `

## Editing the files outside the container (on the host)
#### You can edit the files inside ./src/main/ using any text editor and they will be updated inside the container automatically

## Docker arguments Explained
`--name` -- Creates the container with the specified name which can be used to reference it

`-it` -- Instructs Docker to allocate a pseudo-TTY connected to the container’s stdin; creating an interactive bash shell in the container

`-p` -- Binds specified of the container to corresponding port of the host machine. 

`--mount` --  Attach a filesystem mount to the container, in this case we are mounting the host's filesystem
 