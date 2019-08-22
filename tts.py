#! /usr/bin/python3
# -*- coding: utf-8 -*- 
from api import AipSpeech
import sys
import os
from os.path import join

AppID='11378601'
APPKEY="5KuYlT9jzIgnPGv3jw05rrRT"
APPSECRET="ONIQz4BT783zkxcLOEFS74VSZZOoDyqE"

SPEAKER=0	# 发音人选择, 0为普通女声，1为普通男生，3为情感合成-度逍遥，4为情感合成-度丫丫
SPEED=5		# Speed, 0 ~ 15; 语速，取值0-15
PITCH=5		# Pitch, 0 ~ 15; 音调，取值0-15
VOLUME=15	# Volume, 0 ~ 15; 音量，取值0-15
AUE=3		# Aue,下载音频的格式 3为mp3格式(默认)； 4为pcm-16k；5为pcm-8k；6为wav（内容同pcm-16k）;
                # 注意AUE=4或者6是语音识别要求的格式，但是音频内容不是语音识别要求的自然人发音，所以识别效果会受影响。
FORMATS = {3:".mp3",4:".pcm",5:".pcm",6:".wav"}


def readFile(fileName):
    """
    用于读取文件内容
    """
    with open(fileName,'r',encoding='utf-8') as file_object:
        data = file_object.read().splitlines()
    return data


if __name__ == '__main__':
    client = AipSpeech(AppID, APPKEY, APPSECRET)
    names = readFile('name.txt')
    texts = readFile('text.txt')
    base_dir = os.getcwd()
    save_dir = join(base_dir, 'save')
    formatStr = FORMATS[AUE]

    if len(names) != len(texts):
        print("name.txt->len != text.txt->len")
        sys.exit(1)

    if not os.path.exists(save_dir):
        os.mkdir(save_dir)

    for name, text in zip(names, texts):
        fname = os.path.join(save_dir,str(name)+formatStr)
        result = client.synthesis(text, 'zh', 1, {'per': SPEAKER, 'spd': SPEED, 'pit': PITCH, 'vol': VOLUME, })
        if name != '' and text != '':
            if not isinstance(result, dict):
                print("文件名：" + fname)
                with open(fname, 'wb') as fp:
                    fp.write(result)
