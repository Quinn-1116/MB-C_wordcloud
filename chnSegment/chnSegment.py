# coding:utf-8
from collections import Counter
from os import path
import jieba
import pandas as pd
from bs4 import BeautifulSoup
# jieba.load_userdict(path.join(path.dirname(__file__), './/userdict.txt'))  # 导入用户自定义词典

def word_segment(text):
    '''
    通过jieba进行分词并通过空格分隔,返回分词后的结果
    '''
    d = path.dirname(__file__)
    stopword_path = path.join(d, 'stopwords.txt')
    data = pd.read_csv(text, encoding='utf-8')
    # print(data.shape[0])
    soups = []
    for i in range(data.shape[0]):
        soup = BeautifulSoup(data.content.iloc[i])
        soups.append(soup.text)
    # 返回分词后的结果 读入 stopword
    jieba_word = jieba.cut(''.join(soups), cut_all=False)  # cut_all是分词模式，True是全模式，False是精准模式，默认False
    with open(stopword_path, 'r') as f_stop:
        f_stop_text = f_stop.read()
        f_stop_seg_list = f_stop_text.splitlines()  # 返回一个包含各行作为元素的列表
    seg_list = ''
    for word in jieba_word:
        if word not in f_stop_seg_list:
            seg_list += word
            seg_list += ' '
    return seg_list

