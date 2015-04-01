from zmqmdp import MDPBroker
import gevent

client = MDPBroker()
client.start()
gevent.sleep(500)