#!/usr/bin/python
# -*- encoding: utf-8 -*-
'''
@File    :   split_process.py
@Time    :   2024/12/10 17:07:40
@Author  :   Lifeng Xu 
@desc :   
'''
import re

def split_sentences(text):
    """
    分割文本为句子列表
    """
    # 正则表达式匹配中英文句子结尾标点
    endings_pattern = r'(?<![.?!。？！])[.?!。？！]'
    # 匹配所有的句子结尾标点位置
    sentence_end_positions = [m.end() for m in re.finditer(endings_pattern, text)]
    
    # 添加文本末尾位置以确保处理最后一个句子
    if text and text[-1] not in ".?!。？！":
        sentence_end_positions.append(len(text))
    
    # 分割句子
    sentences = [text[start:end] for start, end in zip([0] + sentence_end_positions[:-1], sentence_end_positions)]
    
    return sentences

if __name__ == '__main__':
    text_file = "./《天龙八部》【爱上阅读_www.isyd.net】.txt"
    with open(text_file, 'r', encoding='utf-8') as f:
        text = f.read()
    sentences = split_sentences(text)
    # 保存为txt
    with open('sentences.txt', 'w', encoding='utf-8') as f:
        for sentence in sentences:
            f.write(sentence + '\n')