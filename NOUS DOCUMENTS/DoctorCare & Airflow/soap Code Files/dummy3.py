from zeep import Client
from zeep.cache import SqliteCache
from zeep.transports import Transport
from zeep.exceptions import Fault
from zeep.plugins import HistoryPlugin
from requests import Session
from requests.auth import HTTPBasicAuth
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning
from lxml import etree

disable_warnings(InsecureRequestWarning)

username = 'confsu+356@gmail.com'
password = 'Password0!'
# If you're not disabling SSL verification, host should be the FQDN of the server rather than IP
host = '204.41.14.79'

#wsdl = 'https://ws.conf.ebs.health.gov.on.ca:1443/EDTService/EDTService?wsdl'
wsdl = 'C:\\Users\\vijaykanth\\Desktop\\MCEDT CONFORMANCE\\EDTService.wsdl'
location = 'https://{host}:1443/EDTService/EDTService'.format(host=host)
binding = "http://schemas.xmlsoap.org/soap/http"

# Create a custom session to disable Certificate verification.
# In production you shouldn't do this,
# but for testing it saves having to have the certificate in the trusted store.
session = Session()
session.verify = False
session.auth = HTTPBasicAuth(username, password)

transport = Transport(cache=SqliteCache(), session=session, timeout=20)
history = HistoryPlugin()
client = Client(wsdl=wsdl, transport=transport, plugins=[history])
service = client.create_service(binding, location)


def show_history():
    for item in [history.last_sent, history.last_received]:
        print(etree.tostring(item["envelope"], encoding="unicode", pretty_print=True))