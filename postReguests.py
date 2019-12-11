import requests

xml = bytearray(b'''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <Ping xmlns="http://MetroService/">
      <login>string</login>
      <password>string</password>
    </Ping>
  </soap:Body>
</soap:Envelope>''')

headers = {'Content-Type': 'text/xml', 'SOAPAction': "http://MetroService/Ping"}
resp = requests.post("http://metroservice.somee.com/WebService/MetroService.asmx?op=Ping", data=xml, headers=headers).text
print(resp)





#print(resp)
#
## инициируем запрос на получение токена
#r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
#                  data={
#                      "client_id": client_id,
#                      "client_secret": client_secret
#                  })
#
## разбираем ответ сервера
#j = json.loads(r.text)
#
## достаем токен
#token = j["token"]


