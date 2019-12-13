import requests
import xml.etree.ElementTree as etree
import json

xml = bytearray(b'''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <Ping xmlns="http://MetroService/">
      <login>1234admin1234metro1234service</login>
      <password>43211234</password>
    </Ping>
  </soap:Body>
</soap:Envelope>''')

headers = {'Content-Type': 'text/xml', 'SOAPAction': "http://MetroService/Ping"}
resp = requests.post("http://metroservice.somee.com/WebService/MetroService.asmx?op=Ping", data=xml, headers=headers).text
with open('www.xml', 'w', encoding='utf-8') as f:
    f.write(resp)

context = etree.iterparse('www.xml', events=('end',))

for event, elem in context:
    if type(elem.text) == str:
        jObjStr = elem.text

jDict = json.loads(jObjStr)
print(jDict['error'], ':', jDict['message'])



