from zeep import Client
from zeep import xsd
client = Client('http://my-endpoint.com/production.svc?wsdl')
service = client.create_service(
'{http://my-target-namespace-here}myBinding',
'http://my-endpoint.com/acceptance/')
service.submit('test')