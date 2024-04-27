import stomp
import os

# Environment variables for connection details
activemq_host = os.environ.get('ACTIVEMQ_HOST', 'localhost')
activemq_port = int(os.environ.get('ACTIVEMQ_PORT', 61613))

# Construct hosts list using environment variables
hosts = [(activemq_host, activemq_port)]

topic = '/topic/my-topic'  # Replace with the topic name you want to subscribe to

class MessageListener(stomp.ConnectionListener):
    def on_error(self, frame):
        print('received an error "%s"' % frame.body)

    def on_message(self, frame):
        print('received a message "%s"' % frame.body)

conn = stomp.Connection(hosts)
conn.set_listener('mylistener', MessageListener())


# conn.connect(username='admin', password='admin', wait=True)  # Replace credentials if needed
conn.connect()
conn.subscribe(destination=topic, ack='auto', id=123)

# Keep the connection open to receive messages
while True:
  pass

conn.disconnect()
conn.stop()
