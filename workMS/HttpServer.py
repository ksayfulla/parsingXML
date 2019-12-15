def GetDcParams(sekretKey, login, password):
    headers = {'Content-Type': 'text/xml', 'SOAPAction': "http://MetroService/GetDocuments"}
    link = 'http://metroservice.somee.com/WebService/MetroService.asmx?op=GetDocuments'
    meth = (f'''<GetDocuments xmlns="http://MetroService/">
      <sekret_key>{sekretKey}</sekret_key>
      <login>{login}</login>
      <password>{password}</password>
    </GetDocuments>''')
    return meth, headers, link

def PingParams(login, password):
    headers = {'Content-Type': 'text/xml', 'SOAPAction': "http://MetroService/Ping"}
    link = 'http://metroservice.somee.com/WebService/MetroService.asmx?op=Ping'
    meth = (f'''<Ping xmlns="http://MetroService/">
      <login>{login}</login>
      <password>{password}</password>
    </Ping>''')
    return meth, headers, link


