from zeep import Client
from zeep import xsd
from requests import Session
from requests.auth import HTTPBasicAuth
#from zeep.cache import SqliteCache
from zeep.transports import Transport
session=Session()
session.auth = HTTPBasicAuth('confsu+356@gmail.com','Password0!' )
session.verify='C:\\Users\\vijaykanth\\Desktop\\MCEDT CONFORMANCE\\root chain certificates\\'
client=Client('https://ws.conf.ebs.health.gov.on.ca:1443/EDTService/EDTService?wsdl',transport=Transport(session=session))
print(client.namespaces)
print(client.plugins)
#print(client.service.download(1))
#print(client.service.info([1,2]))