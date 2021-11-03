%pip install pdfminer.six
from pdfminer.high_level import extract_text
import numpy
import pandas
import matplotlib as mpl
from pandas import DataFrame
text=extract_text('TheDisinformation.pdf',page_numbers=range(6,40))
text=text.split()
dt=dict()
for line in text:
    line=line.split()
    for word in line:
        dt[word]=dt.get(word,0)+1
#print(dt)

new_dt=dict()
word_bank=['threat','conspiracy','alternative','mask','suspicious','deaths','microchips','safety','hesitancy','misinformation']

for key,value in dt.items():
    for x in word_bank:
        if x==key:
            new_dt[key]=value
print(new_dt)

jm_list = [0,0,1,0,0,0,0,0,0]
rfk_list = [1,0,0,0,1,2,0,0,2]
tcb_list = [0,1,0,0,0,2,1,0,1]
st_list = [0,0,0,5,0,0,0,2,0]
ri_list = [0,1,0,0,0,0,0,0,0]
rb_list = [0,1,0,0,0,0,0,0,0]
ee_list = [0,1,1,0,0,0,0,0,0]
sj_list = [1,0,1,0,0,0,0,0,1]
kb_list = [0,1,1,1,0,0,0,0,0]
cn_list = [0,0,1,0,0,0,0,0,0]
bt_list = [0,0,0,1,0,0,0,0,0]
kj_list = [1,1,0,1,0,0,0,0,0]

word_count = numpy.array([jm_list,rfk_list,tcb_list,st_list,ri_list,rb_list,ee_list,sj_list,kb_list,cn_list,bt_list,kj_list])
print(word_count)

df_word = DataFrame(word_count, index=['Joseph Merrcola', 'Robert Kennedy Jr','Ty Charlene Bollinger', 'Sherri Tenpenny', 'Rizza Islam', 'Rashid Buttar', 'Erin Elizabeth', 'Sayer Ji', 'Kelly Brogan', 'Christiane Northrup', 'Ben Tapper', 'Kevin Jenkins'], columns=['threat','conspiracy', 'alternative', 'mask', 'suspicious', 'deaths', 'microchips','safety','misinformation'])
print(df_word)

df_word.index.name = 'Name'
print(df_word)

df_word['threat']

df_word.mean()

df_word['threat'] = pandas.to_numeric
threat_count = df_word['threat'].value_counts(sort =False)

print(threat_count)

df_word.plot(y='mask', kind='bar')

