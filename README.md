# baidu_tts_batch
利用百度语音合成平台提供的API进行批量语音合成,[语音合成-百度AI开放平台](https://ai.baidu.com/tech/speech/tts).

# run
'''python
python3 tts_one.py
'''

## name
生成的mp3文件命名储存在fileName.txt文件中，以换行符为分隔/<br>
    赤壁-杜牧
    乌衣巷-刘禹锡
    江雪-柳宗元

## text
将需要转换成语音的文本储存在text.txt中，以换行符为分隔/<br>
    折戟沉沙铁未销，自将磨洗认前朝。东风不与周郎便，铜雀春深锁二乔。
    朱雀桥边野草花，乌衣巷口夕阳斜。 旧时王谢堂前燕，飞入寻常百姓家。
    千山鸟飞绝，万径人踪灭。孤舟蓑笠翁，独钓寒江雪。
