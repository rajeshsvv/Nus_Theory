from zeep import Client,Settings
from zeep import xsd
settings=Settings(strict=False,xml_huge_tree=True)
#client=Client("http://www.soapclient.com/xml/soapresponder.wsdl",settings=settings)
client=Client("http://webservices.daehosting.com/services/TemperatureConversions.wso?WSDL",settings=settings)
result1=client.service.CelsiusToFahrenheit(26)
result2=client.service.FahrenheitToCelsius(23)
print(result1)
print(result2)
#print(client.service["Method1"]('vijay','do'))
'''by default zeep picks first binding in wsdl to use non default bindings, we use
service2=client.bind('secondservice','port12')

client.service.operationname(param)'''
#new service proxy can be created by using ;service= client.create_proxy()  and use service.submit("something")
#@building an xml using zeep is done as follows, client.create_message(client.service,'operationName')


