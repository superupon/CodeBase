import urllib
import time
import requests
import winsound

def search_retail_store(retail_code):
    url = "http://ir.weip.tech/Home/GetStoreiPhoneList"
    values = {}
    values['storecode'] = retail_code
    values['regioncode'] = 'CN'
    values['onlyshowavailability'] = 'false'
    freq = 1500
    dur = 500

    return_data = requests.post(url, values)
    data_dict = return_data.json()
    if data_dict['Result'] is True:
        for data_list in data_dict['Data']:
            if data_list['CanReserve'] is True \
            and 'iPhone 7' in data_list['Name'] \
            and '32GB' in data_list['Name']:
                print data_list
                if 'Plus' in data_list['Name']:
                    print "!!!!!!!!!!!!!"
                    FILE.write(time.ctime() + data_list['Name'].encode('utf-8') + '\n')
                    FILE.flush()
                    winsound.Beep(freq, dur)
    else:
        print 'Error in returning data!\n'

def main():
    retail_dict = {}
    retail_dict['PuDong'] = 'R389'
    retail_dict['HuanQiu'] = 'R683'
    retail_dict['WuJiaoChang'] = 'R581'
    retail_dict['NanJinDongLu'] = 'R359'
    retail_dict['HuanMao'] = 'R401'
    retail_dict['XiangGang'] = 'R390'

    FILE = open('log.txt', 'w+')
    UserAgent = 'Mozilla/5.0 (Windows NT 6.3; WOW64)'
    headers = {'User-Agent' : UserAgent,
               'Referer' : "http://ir.weip.tech"}
    data = urllib.urlencode(values)
    while True:
        try:
            print "Sleeping"
            time.sleep(20)
            i = 1
            for retailName, retailCode in retail_dict.items():
                print str(i) + "\t" + retailName + " Searching!"
                i = i + 1
                search_retail_store(retailCode)
        except KeyboardInterrupt:
            FILE.close()
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
