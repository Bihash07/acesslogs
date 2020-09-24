from time import *

class Connect:
    def __init__(self,FileActIon,FileEncode = None):
        if FileEncode:
            self.fileopen = open(FileActIon , 'r' ,encoding = FileEncode)
        else:
            self.fileopen = open(FileActIon , 'r')

    def read(self):
        self.filereads = self.fileopen.readlines()

        return self.filereads

    def reads(self,value = '',timeout = None):
        Filereadline = self.fileopen.readlines()

        FileValue = ''

        if timeout:       

            timerunout = int(time()) 

            for i in Filereadline:
                FileValue += i + str(value)

                if timerunout + timeout <= time():
                    return FileValue
                

            return FileValue
        else:
            for i in Filereadline:
                FileValue += i + str(value)

            return FileValue

    def close(self):
        self.fileope.close()

class dsinct:
    def header(array):
        header_one = array[array.find('"')+1:]

        header = header_one[header_one.find('"')+2:]
        header = header[:header.find(' ')]

        return header

    def date(date):
        distinction = date[date.find('['):date.find(']')+1]

        return distinction

    def method(method):
        distinction_one = method[method.find('"')+1:]
        distinction = distinction_one[:distinction_one.find('"')]

        return distinction

    def ip(ip):
        distinction = ip[:ip.find('-')-1]
        
        return distinction

"""
file = Connect(r"C:\AutoSet10\server\logs\access.log","utf-8")

a = file.read()

for i in a:
    ip = dsinct.ip(str(i))
    metho = dsinct.method(str(i))
    head = dsinct.header(str(i))
    print(ip,metho,head)
"""
