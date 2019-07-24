from zeep import Client,Settings

settings=Settings(strict=False,xml_huge_tree=True)
client=Client("http://my-wsdl/wsdl",settings=settings)
with client.settings(raw_response=True):
    response = client.service.myoperation()
