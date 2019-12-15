import requests
import xml.etree.ElementTree as etree
import json

method = input()
login = input()
password = input()


def requestMs(meth):
    xml = (f'''<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
      <soap:Body>
    {meth}
      </soap:Body>
    </soap:Envelope>''')

    headers = {'Content-Type': 'text/xml', 'SOAPAction': "http://MetroService/Ping"}
    try:
        resp = requests.post("http://metroservice.somee.com/WebService/MetroService.asmx?op=Ping", data=xml, headers=headers).text
        with open('www.xml', 'w', encoding='utf-8') as f:
            f.write(resp)

        context = etree.iterparse('www.xml', events=('end',))

        for event, elem in context:
            if type(elem.text) == str:
                jObjStr = elem.text

        jDict = json.loads(jObjStr)
        print(jDict['error'], ':', jDict['message'])
    except:
        print("Отсутствует соедение с сервером")


if method.lower() == 'ping':
    meth = (f'''<Ping xmlns="http://MetroService/">
      <login>{login}</login>
      <password>{password}</password>
    </Ping>''')
    requestMs(meth)
elif method.lower() == 'get':
    meth = (f'''<GetDocuments xmlns="http://MetroService/">
      <sekret_key>string</sekret_key>
      <login>{login}</login>
      <password>{password}</password>
    </GetDocuments>''')
    requestMs(meth)
else:
    print('Неверный ввод метода: используйте get или ping')





