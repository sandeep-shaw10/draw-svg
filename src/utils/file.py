# read file and compress
def readFile(path):
    f = open(path, "r", encoding='utf-8')
    data = f.read()
    val=''
    for i in data:
        temp=i.replace('\n','')
        temp=temp.replace('\t','')
        val+=temp
    f.close()
    return val


def simpleReadFile(path):
    f = open(path, "r", encoding='utf-8')
    data = f.read()
    f.close()
    return data


def writeFile(data, filePath):
    f = open(filePath, "a", encoding='utf-8')
    f.write(data)
    f.close()


def appendFile(data, filePath):
    f = open(filePath, "x", encoding='utf-8')
    f.write(f'{str(data)}\n')
    f.close()