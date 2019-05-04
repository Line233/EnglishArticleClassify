def ReadWeights(filename):
    weightfile=open(filename,'r')
    dictx=dict()
    for line in weightfile:
        info=line.split("\t")
        dictx[info[0]]=int(info[1])
    weightfile.close()
    return dictx
from nltk.corpus import wordnet as wn
def is_noun(tag):
    return tag in ['NN', 'NNS', 'NNP', 'NNPS']

def is_verb(tag):
    return tag in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']

def is_adverb(tag):
    return tag in ['RB', 'RBR', 'RBS']

def is_adjective(tag):
    return tag in ['JJ', 'JJR', 'JJS']

def penn_to_wn(tag):
    if is_adjective(tag):
        return wn.ADJ
    elif is_noun(tag):
        return wn.NOUN
    elif is_adverb(tag):
        return wn.ADV
    elif is_verb(tag):
        return wn.VERB
    return wn.NOUN


def CountSimplicity(sent,dictx):
    from nltk.corpus import stopwords
    import nltk
    from nltk.stem import WordNetLemmatizer
    stopword=set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()

    learned=0
    unlearned=0
    over=0
    sent=nltk.pos_tag(sent)
    for ws in sent:
        w=ws[0]
        tag=ws[1]
        if not (tag[0]>='A' and tag[0]<='Z'):
            continue
        w=w.lower()
        w=lemmatizer.lemmatize(w,penn_to_wn(tag))
        if w in stopword:
            continue
        if w in dictx:
            if dictx[w]>1:
                learned+=1
                # print('learned:',w,'\n')
            else:
                unlearned+=1
                # print('unlearned:',w,"\n")
        else:
            over+=1
            print('over:',w,"\n")
    big=learned+unlearned+over
    r=0
    if big==0:
       r=0 
    else:
        r=int(unlearned/big*100)
    return [r,learned,unlearned,over]
    # if big!=0:
    #     return learned/(learned+unlearned+over)*100
    # else:
    #     return 0


# files=open('bbb.txt','w')
# dictx=ReadWeights('Weight.txt')
# from nltk.corpus import brown
# sents=brown.sents()
# j=1
# for sent in sents:
#     j=j+1
#     if j>5:
#         break
#     print(' '.join(sent),'\n')
#     i=CountSimplicity(sent,dictx)
#     print(i,'\n\n')
#     # files.write('{}\t{}\t{}\t{}\n'.format(str(i[0]),str(i[1]),str(i[2]),str(i[3])))

import nltk
dictx=ReadWeights('Weight.txt')
filex=open('test.txt','r',encoding='utf-8')
for line in filex:
    tokens = nltk.word_tokenize(line)
    i=CountSimplicity(tokens,dictx)
    print(i,'\n')
    