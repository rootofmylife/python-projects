import gensim
from pprint import pprint

with open('./Roy_VnTokenizer-master/scripts/word_segment.txt') as f:
    mylist = f.read().splitlines()

'''Remove [] and replace _'''

mylist = [line.split(' ') for line in mylist]
removed_b_list = []

for s in mylist:
    temp_arr = []
    word_more_than_2 = []
    global c1
    c1 = 0
    global c2
    c2 = 0
    for item in s:
        c1 += item.count('[')
        c2 += item.count(']')
        if ((c1 + c2) == 2) and (len(word_more_than_2) == 0):
            temp_arr.append(item.replace('[','').replace(']',''))
            c1 = c2 = 0
        elif ((c1 + c2) == 2) and (len(word_more_than_2) != 0):
            temp_s = ""
            for i in word_more_than_2:
                temp_s += i + "_"
            temp_s += item
            temp_arr.append(temp_s.replace('[','').replace(']',''))
            c1 = c2 = 0
            word_more_than_2 = []
        elif (c1 + c2) < 2:
            word_more_than_2.append(item)
    removed_b_list.append(temp_arr)

removed_b_list = [' '.join(s) for s in removed_b_list]

removed_b_list = [s.split(' ') for s in removed_b_list]

model = gensim.models.Word2Vec(removed_b_list, size=100, window=5, min_count=1)
pprint(model.wv.similar_by_word('cổ_trang',topn=3))