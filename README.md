# BigData Project

**NOTE**: Make sure that the ports defined in the `compose.yaml` files for container does not collide with the current containers in your docker

### Running the cluster
Just run `docker compose up -d` in the project's root folder
## Kafka
### Connection to Kafka Producer and Consumer
#### To exec into the Kafka conatiner:
`docker-compose exec kafka bash`

#### Push messages to the *vidRecommender* Topic using Internal libraries

`kafka-console-producer.sh --producer.config /opt/bitnami/kafka/config/producer.properties --bootstrap-server kafka:9092 --topic vidRecommender`


`kafka-console-consumer.sh --consumer.config /opt/bitnami/kafka/config/consumer.properties --bootstrap-server kafka:9092 --topic vidRecommender --from-beginning`

## Mongodb

Run `docker exec -it mongo bash` to interact with mongo on terminal

To access mongoshell use `mongosh`


