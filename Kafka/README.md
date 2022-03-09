
# Kafka

This portion of the project generates docker containers for setting up a kafka event streaming pipeline and interacts with them using the producer.py and consumer.py files.

These producer and consumer programs will react to incoming data from the system's sensors and machine learning algorithm by saving the incoming data to the system's database and sending messages the system's main controller.


## Deployment

This deployment requires docker installed and a working internet connection.

To deploy this project run:

```bash
  cd docker_compose_file
  docker-compose up
```

