from gensim.models.keyedvectors import KeyedVectors
import numpy as np
import pandas as pd
"""
词和向量库
"""
def cosine_similarity(x,y):
    # 矩阵乘
    num = x.dot(y.T)
    # 矩阵或向量范数
    denom = np.linalg.norm(x) * np.linalg.norm(y)
    return num / denom


if __name__ == '__main__':
    # file = 'F:\\迅雷下载\\tencent-ailab-embedding-zh-d200-v0.2.0\\tencent-ailab-embedding-zh-d200-v0.2.0.txt'
    # wv_from_text = KeyedVectors.load_word2vec_format(file, binary=False)
    """
    将内存中的word vector直接以二进制形式保存到磁盘，下次直接读取二进制文件，速度快很多。
    """
    # 保存
    # wv_from_text.save('./word_vectors.bin')
    # 读取
    wv_from_text = KeyedVectors.load('./word_vectors.bin')
    data = pd.read_excel('./所有配件工时名称去重.xlsx', sheet_name=0)
    # print("**********\n", type(wv_from_text), "\n**********")
    # vec1 = wv_from_text["汽车"]
    # vec2 = wv_from_text["气车"]
    # print('vec1 ', vec1)
    # print('vec2 ', vec2)
    # print("cosine_similarity(vec1, vec2) ", cosine_similarity(vec1, vec2))
    # print('-------------------')
    #
    # while True:
    #     word = input("name1 name2\n")
    #     word1 = word.split(' ')[0]
    #     word2 = word.split(' ')[1]
    #     vec1 = wv_from_text[word1]
    #     vec2 = wv_from_text[word2]
    #     print('word1 ', word1, 'vec1', vec1)
    #     print('word2 ', word2, 'vec2', vec2)
    #     print('cosine_similarity(vec1, vec2) ', cosine_similarity(vec1, vec2))
    #     print('-------------------')
    keys = wv_from_text.__dict__.get('index_to_key')
    num1 = 0
    num2 = 0
    word_list = []
    word = []

    for line in data['配件名称']:
        # print('line\n', line)
        if line in keys:
            word_list.append(line)
            num1 += 1
            print(line)
        else:
            num2 += 1
    print('存在\n', num1, '不存在\n', num2, '比例num1/(num1+num2)', num1/(num1+num2))
    result_excel = pd.DataFrame({'存在': word_list})
    # print(result_excel)
    result_excel.to_excel('存在.xlsx', index=False)

