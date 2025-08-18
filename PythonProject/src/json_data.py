import urllib.request, urllib.parse, urllib.error
import json, http, ssl

service_url='http://py4e-data.dr-chuck.net/opengeo?'

# Ignore SSL cert errors (PY4E style)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address=input('Enter location: ')
    if len(address) < 1 : break

    address=address.strip()
    parms=dict()
    parms['q']=address

    url=service_url+urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh=urllib.request.urlopen(url)
    data=uh.read().decode()
    print('Retrieved',len(data),'characters',data[:20].replace('\n',' '))

    try:
        js = json.loads(data)
    except:
        js = None

    print(json.dumps(js,indent=4))
    if not js or 'features' not in js:
        print('==== Download error ===')
        print(data)
        break

    if len(js['features']) == 0:
        print('==== Object not found ====')
        print(data)
        break
    print(json.dumps(js, indent=4))
    lat=js['features'][0]['properties']['lat']
    lng=js['features'][0]['properties']['lon']
    print('lat',lat,'lng',lng)
    location=js['features'][0]['properties']['formatted']
    print(location)