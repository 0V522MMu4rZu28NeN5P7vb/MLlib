# 20220614
import pandas as pd
import pycorrector

if __name__ == '__main__':
    data = pd.read_excel('./所有配件工时名称去重.xlsx', sheet_name=0)
    # data = pd.read_excel('./纠错测试.xlsx', sheet_name=0)
    num = 0
    count = 0
    list_0 = []
    list_1 = []
    correct = []
    for line in data['配件名称']:
        count += 1
        corrected_sent, detail = pycorrector.correct(line)
        # 对传入的单词进行纠错
        if len(detail) != 0:
            num += 1
            list_0.append(line)
            list_1.append(detail)
            # 修改结果
            # for i in detail:
            #     list_word = list(i)
            #     word = word.replace(list_word[1], list_word[0])
            correct.append(corrected_sent)
        print('\n纠错字段', line, type(corrected_sent), '\n错误', detail, type(detail), '\n结果', corrected_sent, type(corrected_sent), '\n', num, count, num / count)

    result_excel = pd.DataFrame({'纠错字段': list_0, '错误': list_1, '结果': correct})
    result_excel.to_excel('纠错字段-错误-结果0615更正.xlsx', index=False)