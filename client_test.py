from zmqmdp import MDPClient
import gevent

client = MDPClient()
client.start()
gevent.sleep(500)