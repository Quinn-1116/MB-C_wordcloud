# coding:utf-8

from os import path
from gen_cloud import plotWordcloud
from chnSegment import chnSegment

if __name__ == '__main__':
    # 读取文件
    d = path.dirname(__file__)

    text = path.join(d, 'ben_c.csv')
    # 若是中文文本，则先进行分词操作
    text = chnSegment.word_segment(text)
    # 生成词云
    plotWordcloud.generate_wordcloud(text)
