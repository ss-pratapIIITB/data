import pandas as pd
from pandas import Series
from pandas import DataFrame
import numpy as np

store = pd.read_csv(open('../node.csv', 'r'))

count = {}

for item in store['term1']:
    count[item] = 1 + count.get(item, 0)

for item in store['term2']:
    count[item] = 1 + count.get(item, 0)

s = pd.Series([count[item] for item in store['term1']])

t = pd.Series([count[item] for item in store['term2']])

test = store
test['term1_cnt'] = s
test['term2_cnt'] = t

test['PMI'] = np.log2(test['edge_weight'] * 1560000/(test['term1_cnt'] * test['term2_cnt']))
fr = open('PMI_data.csv', 'w')

test.to_csv(fr, sep = ',')

resdset = test[test.PMI > 3]
save = resdset.drop('PMI', 1)
save = save.drop('term1_cnt', 1)
save = save.drop('term2_cnt', 1)
fr = open('PMIedited.csv', 'w')
save.to_csv(fr, sep = ",", index = False)

s = pd.read_csv('PMI_data.csv')
t = s[s.PMI > 3]

k = t.sort(columns='PMI', ascending = False)[['term1', 'term2', 'PMI']]

k.to_csv('sortPMI.csv', sep = ',')
#k = s.drop('term1_cnt', 1)
#k = k.drop('term2_cnt', 1)
#k = k.drop('edge_weight', 1)
#k = k[k.PMI > 3]

read = raw_input('')
x = k[k.term1 == read]
print x
    


