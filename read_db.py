import os
import time
import pickle
import random
import argparse
import urllib.request
import feedparser

from utils import Config, safe_pickle_dump

try:
    db = pickle.load(open(Config.db_path, 'rb'))
except Exception as e:
    print('error loading existing database:')
    print(e)
    print('starting from an empty database')
    db = {}

count1=0
count2=0
count3=0
count4=0

tot_count=0

count_dic={}
for i in db:
    if i[:2] not in count_dic:
        count_dic[(i[:2])]=1
    else:
        count_dic[i[:2]]+=1
print (i)
print (count_dic)