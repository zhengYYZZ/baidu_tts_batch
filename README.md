# baidu_tts_batch
利用百度语音合成平台提供的API进行批量语音合成，[语音合成-百度AI开放平台](https://ai.baidu.com/tech/speech/tts_online).

## run
```python
python3 tts.py
```
## name
##### 生成的mp3文件命名储存在fileName.txt文件中，以换行符为分隔
    赤壁-杜牧
    乌衣巷-刘禹锡
    江雪-柳宗元

## text
##### 将需要转换成语音的文本储存在text.txt中，以换行符为分隔
    折戟沉沙铁未销，自将磨洗认前朝。东风不与周郎便，铜雀春深锁二乔。
    朱雀桥边野草花，乌衣巷口夕阳斜。 旧时王谢堂前燕，飞入寻常百姓家。
    千山鸟飞绝，万径人踪灭。孤舟蓑笠翁，独钓寒江雪。
    
    
## 从Excel表读入并生成语音文件  
将excel文件放入xlsx文件夹中  
.xlsx文件内容格式
|文件名|语音转换内容|
|-|-|
|赤壁-杜牧|折戟沉沙铁未销，自将磨洗认前朝。东风不与周郎便，铜雀春深锁二乔。|
```python3
python3 tts_Excel
```

## 合成参数设置
        SPEAKER=0   # 发音人选择, 0为普通女声，1为普通男生，3为情感合成-度逍遥，4为情感合成-度丫丫
        SPEED=5     # 语速，取值0-15
        PITCH=5     # 音调，取值0-15
        VOLUME=15   # 音量，取值0-15
        AUE=3       # 下载音频的格式： 3为mp3格式(默认)； 4为pcm-16k；5为pcm-8k；6为wav（内容同pcm-16k）

## 换取token
https://ai.baidu.com/docs#/TTS-API/top
