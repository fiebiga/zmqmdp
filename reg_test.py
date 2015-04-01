from zmqmdp import BrokerRegistrationService
import gevent

client = BrokerRegistrationService()
client.start()
gevent.sleep(500)