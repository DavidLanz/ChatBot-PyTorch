import pickle
import datetime
from collections import Counter

def get_q_a_tok_no_repeat(Q_, A_):
    questions_tok = []
    answers_tok = []
    all_text = []
    with open(Q_, 'r', encoding="utf-8") as q:
        questions_tok = q.readlines()
    questions_tok = [i.replace('\n','').replace('\ufeff','').replace('\x1a','') for i in questions_tok]

    with open(A_, 'r', encoding="utf-8") as a:
        answers_tok = a.readlines()
    answers_tok = [i.replace('\n','').replace('\ufeff','').replace('\x1a','') for i in answers_tok]

    Q_A_dict={}
    questions_tok_no_repeat,answers_tok_no_repeat=[],[]
    for i in range(len(questions_tok)):
        Q=tuple(questions_tok[i])
        A=tuple(answers_tok[i])
        if Q in Q_A_dict:
            pass
        else:
            Q_A_dict[Q] = A
            all_text.append(questions_tok[i]+answers_tok[i])

    for x in Q_A_dict:
        questions_tok_no_repeat.append(x)
        answers_tok_no_repeat.append(Q_A_dict[x])
    save_corpus_tuple(questions_tok_no_repeat, answers_tok_no_repeat)
    return all_text

def get_words(content):
    seg_list = list(content)
    word_index_dict = {}
    tmp_list = []
    c = Counter()
    for x in seg_list:
        if len(x)>0 and x != '\r\n' and x !='\r' and x !='\n' and x != '\x1a' and x !='\ufeff':
            c[x] += 1
    temp_dic = dict(c)
    word_index_dict = {}
    index_word_dict = {}
    for k,v in enumerate(temp_dic):
        index_word_dict[k] = v
        word_index_dict[v] = k
    return word_index_dict, index_word_dict

def save_corpus_tuple(questions_tok_no_repeat, answers_tok_no_repeat):
    with open("pickle/Q_no_repeat_all.pkl","wb") as f:
        pickle.dump(questions_tok_no_repeat,f,protocol=pickle.HIGHEST_PROTOCOL)

    with open("pickle/A_no_repeat_all.pkl","wb") as f:
        pickle.dump(answers_tok_no_repeat,f,protocol=pickle.HIGHEST_PROTOCOL)

def save_word_index(word_index_dict, index_word_dict):
    with open("pickle/word_index_dict_all.pkl","wb") as f:
        pickle.dump(word_index_dict,f,protocol=pickle.HIGHEST_PROTOCOL)

    with open("pickle/index_word_dict_all.pkl","wb") as f:
        pickle.dump(index_word_dict,f,protocol=pickle.HIGHEST_PROTOCOL)


if __name__ == "__main__": 
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    all_text_list = get_q_a_tok_no_repeat("data/Q_no_repeat_raw_tw.txt", "data/A_no_repeat_raw_tw.txt")
    all_text = " ".join(all_text_list)
    word_index_dict = {}
    index_word_dict = {}
    word_index_dict, index_word_dict = get_words(all_text)
    save_word_index(word_index_dict, index_word_dict)
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    
