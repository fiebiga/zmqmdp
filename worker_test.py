from zmqmdp import MDPWorker
import gevent

client = MDPWorker("testservice")
client.start()
gevent.sleep(500)