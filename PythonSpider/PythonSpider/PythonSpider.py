
import urllib2
import urllib
import requests
import sys
import json


file = open('log.txt', 'w+')
url = "http://ir.weip.tech/Home/GetStoreiPhoneList"
user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64)'
headers = {'User-Agent' : user_agent,
           'Referer' : "http://ir.weip.tech"}
values = {}
values['storecode'] = 'R389'
values['regioncode'] = 'CN'
values['onlyshowavailability'] = 'false'
data = urllib.urlencode(values)

return_data = requests.post(url, values)
#reload(sys)
#sys.setdefaultencoding('utf-8')

dataDict = json.load(return_data.text)
#print dataDict['Data']

#file.write(return_data.text.encode('utf-8'))
#file.close()
#print return_data.text.encode('utf-8')
#request = urllib2.Request(url, data, headers)
#response = urllib2.urlopen(request)
#print response.read()
print 'Ending...\n'