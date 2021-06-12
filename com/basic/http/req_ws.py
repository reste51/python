from suds.client import Client
url="http://116.62.123.123:5080/WebService/?wsdl"
client = Client(url)
print(client)

client.set_options()
# client.factory.create()

client.set_options()

import  numpy as np
np.linspace


