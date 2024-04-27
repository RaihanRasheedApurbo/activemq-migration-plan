import stomp
import os
import uuid
import time

# Environment variables for connection details
activemq_host = os.environ.get('ACTIVEMQ_HOST', 'localhost')
activemq_port = int(os.environ.get('ACTIVEMQ_PORT', 61614))


destination = "/topic/my-topic"  # Replace with your topic name

# Create a connection
conn = stomp.Connection([(activemq_host, activemq_port)])
conn.connect()

while True:
    time.sleep(0.1)
    newUUId = uuid.uuid4()
    conn.send(body=f"Your random UUID is: {newUUId}", destination=destination)
    print(f"Message sent with uuid: {newUUId}")
