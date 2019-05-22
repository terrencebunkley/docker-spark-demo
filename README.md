# Docker Spark Demo

#### Clone this repo

Via Terminal / Command Prompt

`git clone ehttps://github.com/terrencebunkley/docker-spark-demo.git`

### Starting the container
Go to the root directory and run: 

`docker run --name spark-master --rm -it  -p 4040:4040/tcp -p 8080:8080/tcp -p 8081:8081/tcp --mount type=bind,source="$(pwd)",target=/docker-spark-demo birgerk/apache-spark 
`
#### Log into the container

`docker exec -it spark-master /bin/bash
`
#### Navigate to Spark Exe
`cd /usr/local/spark/bin`

#### Execute one of examples with spark-submit 
`./spark-submit /docker-spark-demo/src/main/pi_count.py `