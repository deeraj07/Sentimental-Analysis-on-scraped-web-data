from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
import re
import csv
import pandas as ky
col_list = ["URL_ID","URL"]
hyt = ky.read_csv("intern.csv",usecols=col_list)
colour_count = 0
ki = hyt["URL"]
stoplist = stopwords.words('english')
#thewriter.writeheader()
ps = []
ns = []
pols = []
ss = []
asl = []
pocw = []
fi = []
aws = []
cwc = []
wc = []
spw = []
pp = []
awl = []
cc = []
import pandas as pd
df = pd.read_csv("nu.csv")
#print(df)
x = df.iloc[:,-8].values #positive values
#o = df.iloc[:,-2].values
y = df.iloc[:,-9].values #negative values
z = df.iloc[:,-16].values #words
#print(z)
additional_stopwords = """! “ ” # $ % & ’ ( ) * + , — - . . / : ; < = > ? @ [ \ ] ^ _ ` { | } ~"""
stoplist += additional_stopwords.split()
#print(stoplist)
for a in range(170):
      colour_count = colour_count+1
      cc.append(colour_count)
      file = open('D:\OneDrive\Desktop\work\inter'+str(a)+'.txt',encoding='utf-8',errors='ignore')
      text = file.read()
      k = 0
      for b in sent_tokenize(text):
            k = k+1
      #print(k) count of sentences
      positivedict=[]
      negativedict=[]
      for d in range(len(z)):
              if x[d]!= 0 and y[d]==0 and z[d].lower() not in stoplist:
                      positivedict.append(z[d].lower())
              elif y[d]!= 0 and x[d]==0 and z[d].lower()not in stoplist:
                      negativedict.append(z[d].lower())
      #print(positivedict)positive dictionary from master dictionary
      #print(negativedict)negative dictionary from master dictionary
      word_tokens = word_tokenize(text)

      filtered_sentence = [w for w in word_tokens if not w.lower() in stoplist if w.isalnum()]

      filtered_sentence = []

      for w in word_tokens:
              if w not in stoplist:
                   if w.isalnum():
                       filtered_sentence.append(w.lower())
      #print(len(filtered_sentence))Total number of words or cleaned words
      wc.append(len(filtered_sentence))
      s = sum([len(lo) for lo in filtered_sentence])
      #print(s)Sum of the total number of characters in each word
      a3 = []#positive words list
      count=0
      for e in range(0,len(positivedict)):
          count=0
          for h in range(0,len(filtered_sentence)):
                if positivedict[e] in filtered_sentence[h]:
                       count=count+1
          a3.append(count)
      positivescore = sum(a3)
      ps.append(positivescore)
      #print(sum(a3)) positivescore
      a4 = []#negative words list
      count1=0
      for l in range(0,len(negativedict)):
          count1=0
          for m in range(0,len(filtered_sentence)):
                if negativedict[l] in filtered_sentence[m]:
                       count1=count1+1
          a4.append(count1)
      negativescore = sum(a4)
      ns.append(negativescore)
      #print(sum(a4)) negativescore       
      polarityscore = (positivescore - negativescore)/ ((positivescore + negativescore) + 0.000001)
      #print(polarityscore) polarityscore
      pols.append(polarityscore)
      subjectivityscore = (positivescore + negativescore)/ ((len(filtered_sentence)) + 0.000001)
      #print(subjectivityscore)
      ss.append(subjectivityscore)
      averagenumberofwordspersentence = len(filtered_sentence) / k
      #print(averagenumberofwordspersentence)
      aws.append(averagenumberofwordspersentence)
      averagesentencelength = len(filtered_sentence)/ k
      #print(averagesentencelength)
      asl.append(averagesentencelength)
      o = [] 
      for n in filtered_sentence:
          syllable_count=0
          if(n.endswith("es") or n.endswith("ed")):
                syllable_count=syllable_count-1
          for t in n:
            if(t=='a' or t=='e' or t=='i' or t=='o' or t=='u'):
                  syllable_count=syllable_count+1
          o.append(syllable_count)        

      #print(sum(o)) #syllable count per word
      spw.append(sum(o))
      c = []
      for v in range(len(o)):
           if o[v] > 2 :
                 c.append(o[v])
      cwc.append(len(c)) 
      PercentageofComplexwords = (len(c) / len(filtered_sentence))*100
      pocw.append(PercentageofComplexwords)
      FogIndex = 0.4 * (averagesentencelength + PercentageofComplexwords)
      fi.append(FogIndex)
      pattern = 'I'
      p = len(re.findall(pattern, text))
      pattern = 'we'
      q = len(re.findall(pattern, text))
      pattern = 'my'
      g = len(re.findall(pattern, text))
      pattern = 'ours'
      e = len(re.findall(pattern, text))
      pattern = 'us'
      r = len(re.findall(pattern, text))
      f = p+q+g+e+r 
      #print(f) Personal Pronouns
      pp.append(f)
      averagewordlength = s/len(filtered_sentence)
      #print(averagewordlength)
      awl.append(averagewordlength)
      file.close()

hi = pd.DataFrame(list(zip(cc,ki,ps,ns,pols,ss,asl,pocw,fi,aws,cwc,wc,spw,pp,awl)),columns =['URL_ID', 'URL','POSITIVE SCORE','NEGATIVE SCORE','POLARITY SCORE','SUBJECTIVITY SCORE','AVG SENTENCE LENGTH','PERCENTAGE OF COMPLEX WORDS','FOG INDEX','AVG NUMBER OF WORDS PER SENTENCE','COMPLEX WORD COUNT','WORD COUNT','SYLLABLE PER WORD','PERSONAL PRONOUNS','AVG WORD LENGTH'])
hi.to_csv('saideeraj.csv',index=False)




