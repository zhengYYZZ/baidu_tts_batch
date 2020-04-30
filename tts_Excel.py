import openpyxl
import xlrd
import os
from api import AipSpeech
import sys
import os
from os.path import join,basename

AppID='11378601'
APPKEY="5KuYlT9jzIgnPGv3jw05rrRT"
APPSECRET="ONIQz4BT783zkxcLOEFS74VSZZOoDyqE"

SPEAKER=0	# 发音人选择, 0为普通女声，1为普通男生，3为情感合成-度逍遥，4为情感合成-度丫丫，默认为普通女声
SPEED=5		# Speed, 0 ~ 15; 语速，取值0-9，默认为5中语速
PITCH=5		# Pitch, 0 ~ 15; 音调，取值0-9，默认为5中语调
VOLUME=8	# Volume, 0 ~ 9; 音量，取值0-9，默认为5中音量
AUE=3		# Aue,下载音频的格式 3：mp3(default) 4： pcm-16k 5： pcm-8k 6. wav


# 检索xlsx目录中的文件
def fileName(path=None):
    if path is None:
        file_directory = os.path.join(os.getcwd(), 'xlsx')
        file = os.listdir(file_directory)
        if len(file) == 1:
            return os.path.join(file_directory, file.pop())
        else:
            print(' Number of files > 1.' + '\n' + file_directory)
            for f in file:
                print(f)
            exit(0)
    if os.path.isfile(path):
        return path
    else:
        print('file does not exist')
        exit(0)


# 打开Excel文档并读取数据
def ExcelData(path):
    file_name = os.path.basename(path)
    file_str = file_name[-4:]
    if 'xlsx' in file_str:
        data = ExcelDataXlsx(path)
    else:
        data = ExcelDataXls(path)
    return data


# Microsoft Excel 2007-2013 XML(.xlsx)
def ExcelDataXlsx(path):
    excel = openpyxl.load_workbook(path)
    sheet1 = excel.get_sheet_by_name('Sheet1')
    data1 = []
    for row in range(2, sheet1.max_row + 1):
        name = sheet1['A' + str(row)].value
        text = sheet1['B' + str(row)].value

        data_dict = {'name': name, 'text': text}
        data1.append(data_dict)
        '''
         [{name:xxx,text:xxx}
         {name:xxx,text:xxx}
         {name:xxx,text:xxx}
          ...]
        '''

    return data1


# Microsoft Excel 97-2003(.xls)
def ExcelDataXls(path):
    excel = xlrd.open_workbook(path)
    sheet1 = excel.sheet_by_name('Sheet1')
    data2 = []
    for row in range(2, sheet1.nrows):
        name = sheet1['A' + str(row)].value
        text = sheet1['B' + str(row)].value

        data_dict = {'name': name, 'text': text}
        data2.append(data_dict)

    return data2


# 转换为语音文件
def tts_to_xlsx():

    file = fileName()
    data = ExcelData(file)
    client = AipSpeech(AppID, APPKEY, APPSECRET)
    base_dir = os.getcwd()
    save_base_dir = join(base_dir, 'save')

    if not os.path.exists(save_base_dir):
        os.mkdir(save_base_dir)

    for v in data:
        name = v.get('name','None')
        text = v.get('text','None')
        fname = os.path.join(save_base_dir,str(name)+'.mp3')
        result = client.synthesis(text, 'zh', 1, {'per': SPEAKER, 'spd': SPEED, 'pit': PITCH, 'vol': VOLUME, })
        if name != None and text != None:
            if not isinstance(result, dict):
                print("文件名：" + fname)
                with open(fname, 'wb') as fp:
                    fp.write(result)

if __name__ == '__main__':
    tts_to_xlsx()
