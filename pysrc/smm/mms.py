#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from mpltools import annotation
import re 
import yaml 
import pandas as pd
from OutputCycler import * 
oc = OutputCycler()

files = ['ip', 'cg', 'rt', 'hrt']
markers = ['-o', '->', '-^', '-*']
d = [] 
for f in files:
	with open('data/smm/mms/' + f + '.txt', 'r') as stream:
		db = yaml.safe_load(stream)
	opts = db.pop('Options used')
	vtype = re.findall(r'--vef\s(\S*)', opts)[0]
	db['vtype'] = vtype.replace('sm', '')
	d.append(db) 

for p in range(1,4):
	fig, ax = plt.subplots()
	for i in range(len(files)):
		df = pd.DataFrame(d[i][p])
		plt.loglog(df['h'], df['err'], markers[i], label=d[i]['vtype'].upper())

	df = pd.DataFrame(d[1][p])
	h = np.array(df['h'])
	E = np.array(df['err'])
	annotation.slope_marker((h[0]/1.05, E[0]*1.05), (p+1,1), invert=True, size_frac=.1)
	ax.set_xscale('log', base=2)
	plt.legend()
	plt.xlabel('$h$')
	plt.ylabel('Scalar Flux L2 Error')
	if (oc.Good()):
		plt.savefig(oc.Get())
if not(oc.Good()):
	plt.show()