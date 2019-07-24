from zeep import CachingClient as Client
from zeep.wsse.signature import Signature
from zeep.transports import Transport
from requests import Session, Request

session = Session()
session.verify = 'C:\\Users\\vijaykanth\\Desktop\\MCEDT CONFORMANCE\\root chain certificates\\server.cer'
transport = Transport(session=session)

c = Client('https://ws.conf.ebs.health.gov.on.ca:1443/EDTService/EDTService?wsdl', transport=transport)
#print(c.service.info(123))
print(c.service.info([1,2,3]))