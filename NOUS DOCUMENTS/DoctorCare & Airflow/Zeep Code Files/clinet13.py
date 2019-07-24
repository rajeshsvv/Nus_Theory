from zeep import Client
from zeep import xsd


client = Client('https://ws.conf.ebs.health.gov.on.ca:1443/EDTService/EDTService?wsdl')
service2 = client.bind('SecondService', 'Port12')
service2.someOperation(myArg=1)
