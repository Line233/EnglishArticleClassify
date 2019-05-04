from nltk.corpus import brown
import nltk
news_text=nltk.corpus.brown.words()
news_text2=nltk.corpus.reuters.words()
news_text3=nltk.corpus.gutenberg.words()
news_text4=nltk.corpus.webtext.words()
fdist=nltk.FreqDist([w.lower() for w in news_text])
fdist2=nltk.FreqDist([w.lower() for w in news_text2])
fdist3=nltk.FreqDist([w.lower() for w in news_text3])
fdist4=nltk.FreqDist([w.lower() for w in news_text4])
f=open('PureVocabulary.txt','r')
f2=open('aaa.txt','w')
i=0
j=0
z=0
for line in f:
    word=line[:-1]
    
    n=fdist[word]+fdist2[word]+fdist3[word]+fdist4[word]
    if n==0:
        i=i+1
    else: 
        if n==1:
            j=j+1
        else: 
            if n<10:
                z=z+1
    f2.write(word)
    f2.write('\t')
    f2.write(str(n))
    f2.write('\n')
print('0',i,'\n')
print('1',j,'\n')
print('1<x<10',z,'\n')
print('\nover')

# def write(text,file):
#     file.write(text)
#     file.writh('\n')