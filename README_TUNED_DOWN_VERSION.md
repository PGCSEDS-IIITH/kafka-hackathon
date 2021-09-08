# KAFKA

Install Kafka as shown in README.md

## Run the Example

Now we are ready to run the example. Since we will be running multiple processes at once, we will have several terminals open at once. If your terminal emulator supports tabs, I recommend using that, but seperate terminal windows also works fine.

---
* ### Terminal 1 -- Zookeeper

In your first terminal window/tab, we need to start a Zookeeper instance. This is required for running a Kafka cluster

```bash
~$ cd kafka/
~/kafka$ bin/zookeeper-server-start.sh config/zookeeper.properties
```

This will write a lot of output to the console. As long as you don't hit an error and are returned to the prompt, it should be working. Keep this process running, and open a new terminal window/tab.

---
* ### Terminal 2 -- Kafka Broker

Now we need to start the Kafka broker.

```bash
~$ cd kafka/
~/kafka$ bin/kafka-server-start.sh config/server.properties
```

This will also write a lot of output to the console. If you didn't hit an error, keep this server running and open a new terminal. 

---
* ### Terminal 3 -- Kafka Config

Now that we have our Kafka cluster running, we need to create the topic that will hold our tweets.

First check if any topics exist on the broker (this should return nothing if you just started the server)

```bash
~/kafka$ bin/kafka-topics.sh --list --bootstrap-server localhost:9092
```

Now make a new topic named `tweets`

```bash
~/kafka$ bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic tweets
```

Run the `--list` command from above to make sure the `tweets` topic was successfully created.

You can either close this terminal, or just keep it open and use it for the next step.

---
### Terminal 4 -- Run Kafka Producer

```bash
~/hackathon$ python send_data.py
```

### Terminal 5 -- Run Kafka Consumer

```bash
~/hackathon$ python consumer.py
```


