# from requests import Session
# from zeep import Client
# from zeep.transports import Transport
# session = Session()
# session.cert = 'C:\\Users\\rajeshvs\\Desktop\\RootChain_SHA2'
# transport = Transport(session=session)
# client = Client(
# 'http://my.own.sslhost.local/service?WSDL',
# transport=transport)

#
# from zeep import Client
# from zeep.transports import Transport
# transport = Transport(timeout=10)
# client = Client(
# 'https://ws.conf.ebs.health.gov.on.ca:1443/EDTService/EDTService?wsdl',
# transport=transport)


from zeep import Client
from zeep.cache import SqliteCache
from zeep.transports import Transport
transport = Transport(cache=SqliteCache())
client = Client(
'http://www.webservicex.net/ConvertSpeed.asmx?WSDL',
transport=transport)

