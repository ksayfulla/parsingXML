import requests
import xml.etree.ElementTree as etree
import json
import HttpServer


print('Введите метод :', end=' ')
method = input()
print('логин :', end=' ')
login = input()
print('пароль :', end=' ')
password = input()


def requestMs(meth, hed, link):
    xml = (f'''<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
      <soap:Body>
    {meth}
      </soap:Body>
    </soap:Envelope>''')

    headers = hed
    try:
        resp = requests.post(link, data=xml, headers=headers).text
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
    meth, hed, link = HttpServer.PingParams(login, password)
    requestMs(meth, hed, link)
elif method.lower() == 'get':
    print('sekret key :', end=' ')
    sekretKey = input()
    meth, hed, link = HttpServer.GetDcParams(sekretKey, login, password)
    requestMs(meth, hed, link)
else:
    print('Неверный ввод метода: используйте get или ping')





