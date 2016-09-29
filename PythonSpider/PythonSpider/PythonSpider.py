
import urllib2
import urllib
import requests
import sys
import json
import ast
import time
import win32api,win32con
import winsound

retailDict = {}
retailDict['PuDong'] = 'R389'
retailDict['HuanQiu'] = 'R683'
retailDict['WuJiaoChang'] = 'R581'
retailDict['NanJinDongLu'] = 'R359'
retailDict['HuanMao'] = 'R401'
retailDict['XiangGang'] = 'R390'

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
dataDict = return_data.json()
if dataDict['Result'] == True:
    for dataList in dataDict['Data']:
        if dataList['CanReserve'] == True and 'iPhone 7 Plus' in dataList['Name']:
            print dataList
else:
    print 'Error in returning data!\n'


def searchRetailStore(retailCode):
    url = "http://ir.weip.tech/Home/GetStoreiPhoneList"
    values = {}
    values['storecode'] = retailCode
    values['regioncode'] = 'CN'
    values['onlyshowavailability'] = 'false'
    Freq = 1500
    Dur = 500

    return_data = requests.post(url, values)
    dataDict = return_data.json()
    if dataDict['Result'] == True:
        for dataList in dataDict['Data']:
            gold_utf = '??'.encode("utf-8")
            if dataList['CanReserve'] == True and 'iPhone 7' in dataList['Name'] and '32GB' in dataList['Name']:
                print dataList
                if 'Plus' in dataList['Name']:
                    print "!!!!!!!!!!!!!"
                    file.write(time.ctime() + dataList['Name'].encode('utf-8') + '\n')
                    file.flush()
                    winsound.Beep(Freq,Dur)
    else:
        print 'Error in returning data!\n'



while True:
    try:
        print "Sleeping"
        time.sleep(20)
        i = 1
        for retailName, retailCode in retailDict.items():
            print str(i) + "\t" + retailName + " Searching!"
            i = i + 1
            searchRetailStore(retailCode)
    except (KeyboardInterrupt):
        file.close()
        exit()


#dataDict = ast.literal_eval(return_data.text.encode('utf-8'))
#reload(sys)
#sys.setdefaultencoding('utf-8')

#dataDict = json.load(return_data.text)
#print dataDict['Data']

#file.write(return_data.text.encode('utf-8'))
#file.close()
#print return_data.text.encode('utf-8')
#request = urllib2.Request(url, data, headers)
#response = urllib2.urlopen(request)
#print response.read()
print 'Ending...\n'