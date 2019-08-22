import json
from tts import readFile


def jsonToList(file_name):
    """
    将json文件中内容读取到list
    """
    with open(file_name,'r',encoding='utf-8') as fp:
        name_text = json.load(fp)
        fp.close()
    name = list(name_text.keys())
    text = list(name_text.values())
    return name,text


def jsonToFiletxt(file_name):
    """
    将json内容写入到name.txt与text.txt
    """
    name,text = jsonToList(file_name)
    with open('name.txt','w',encoding='utf-8') as fp:
        for n in name:
            fp.write(n+'\n')
        fp.close()
    with open('text.txt','w',encoding='utf-8') as fp:
        for t in text:
            fp.write(t + '\n')
        fp.close()


def onetotwo(file_name):
    one = readFile(file_name)
    print(one)
    name = one[0::2]
    text = one[1::2]
    print(name)
    print(text)


class Proofread:
    def __init__(self,file_name,file_text):
        self.file_name = file_name
        self.file_text = file_text
        self.name = readFile(file_name)
        self.text = readFile(file_text)
        
    def lenEqual(self):
        len_name = len(self.name)
        len_text = len(self.text)
        if len_name == len_text:
            return True
        elif len_name > len_text:
            print("len_name > len_text")
            return False
        else:
            print("len_name < len_text")
            return False
        
    def getDict(self):
        if not self.lenEqual():
            print("File lengths are not equal")
            return
        file_dict = dict(zip(self.name,self.text))
        return file_dict
        
    def putFileJson(self):
        #写入到json文件
        Vidoe_dict = self.getDict()
        with open("proofead.json","w",encoding='utf-8') as fp:
            json.dump(Vidoe_dict,fp)
            
    def putCatFileTxt(self):
        #生成方便查看的文件proofead.txt
        if not self.lenEqual():
            return None
        with open("proofead.txt","w",encoding='utf-8') as fp:
            i,j = 0,0
            s = '-------------------------------------'
            for n, t in zip(self.name, self.text):
                i += 1
                fp.write(n+' ||| ')
                fp.write(t+'\n')
                if i%4==0:
                    j += 1
                    fp.write(s+str(j)+s+'\n')
            fp.close()
        print("Successfully write to proofead.txt")

    def putFileTxt(self):
        if not self.lenEqual():
            return None
        with open("name_text.txt","w",encoding='utf-8') as fp:
            for n, t in zip(self.name, self.text):
                fp.write(n+'\n')
                fp.write(t+'\n')
            fp.close()
        print("cat name_text.txt")
        
    def getName(self):
        return self.name
     
    def getText(self):
        return self.text


def fileProofread():
    #生成方便校对的文件
    testfile = Proofread("name.txt","text.txt")
    if testfile.lenEqual():
        testfile.putCatFileTxt()

def writeInJson():
    #储存到json文件
    testfile = Proofread("name.txt","text.txt")
    if testfile.lenEqual():
        testfile.putFileJson()

def readJson():
    #将json内容写入到name.txt与text.txt
    jsonToFiletxt("proofead.json")


if __name__ == '__main__':
    readJson()
