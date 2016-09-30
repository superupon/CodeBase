'''This is a Project for python spider, You could use it to
   search which site has the iphone you wanted.
'''
#import urllib
import time
import requests
import winsound

class Log(object):
    '''
    This Class is used to log information into the file system
    '''
    log_file = None
    @staticmethod
    def log_init():
        '''
        log_init
        '''
        file_name = time.strftime('%Y-%m-%d-%H%M%S')
        file_name = 'Spider' + file_name + '.log'
        Log.log_file = open(file_name, 'w+')
    @staticmethod
    def log_write(string):
        '''
        log_write
        '''
        if string is not None:
            Log.log_file.write(string)
            Log.log_file.flush()
    @staticmethod
    def log_close():
        '''
        log_close
        '''
        Log.log_file.close()

def search_retail_store(retail_code):
    """
    It will search the retail and output result
    Parameters:
    @retail_code  retail code you could get when you use chrome to see the action
    when you open a website
    """
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
                    Log.log_write(time.ctime() + ' ' + data_list['Name'].encode('utf-8') + '\n')
                    winsound.Beep(freq, dur)
    else:
        print 'Error in returning data!\n'

def main():
    '''
    Main Function
    '''
    retail_dict = {}
    retail_dict['PuDong'] = 'R389'
    retail_dict['HuanQiu'] = 'R683'
    retail_dict['WuJiaoChang'] = 'R581'
    retail_dict['NanJinDongLu'] = 'R359'
    retail_dict['HuanMao'] = 'R401'
    retail_dict['XiangGang'] = 'R390'

    Log.log_init()
    #user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64)'
    #headers = {'User-Agent' : UserAgent,
    #           'Referer' : "http://ir.weip.tech"}
    #data = urllib.urlencode(values)
    while True:
        try:
            print "Sleeping"
            time.sleep(20)
            i = 1
            Log.log_write('######Start Loging############\n')
            for retail_name, retail_code in retail_dict.items():
                print str(i) + "\t" + retail_name + " Searching!"
                i = i + 1
                Log.log_write("Retail Name:" + retail_name + "\n")
                search_retail_store(retail_code)
        except KeyboardInterrupt:
            Log.log_close()
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
#print 'Ending...\n'
if __name__ == "__main__":
    main()
