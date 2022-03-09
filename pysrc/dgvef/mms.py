#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from mpltools import annotation
import re 
import yaml 
import pandas as pd
from scipy.interpolate import interp1d 
from OutputCycler import * 
oc = OutputCycler()

files = ['ip', 'br2', 'mdldg', 'cg']
markers = ['-o', '->', '-*', '-^']
d = [] 
for f in files:
	with open('data/dgvef/mms/' + f + '.txt', 'r') as stream:
		db = yaml.safe_load(stream)
	opts = db.pop('Options used')
	vtype = re.findall(r'--vef\s(\S*)', opts)[0]
	db['vtype'] = vtype 
	d.append(db) 

for p in range(1,4):
	fig, ax = plt.subplots()
	for i in range(len(files)):
		df = pd.DataFrame(d[i][p])
		plt.loglog(df['h'], df['err'], markers[i], label=d[i]['vtype'].upper())

	df = pd.DataFrame(d[0][p])
	h = np.array(df['h'])
	E = np.array(df['err'])
	annotation.slope_marker((h[0]/1.05, E[0]*1.05), (p+1,1), invert=True, size_frac=.1)
	ins = 2 
	dx = (h[0] - h[-1])/100
	axin = ax.inset_axes([.225, .7, .25, .25])
	for i in range(len(files)):
		df = pd.DataFrame(d[i][p])
		axin.loglog(df['h'], df['err'], markers[i])
	axin.set_xlim(h[ins]-dx, h[ins]+dx)
	logEint = interp1d(np.log(h), np.log(E))
	Eint = lambda x: np.exp(logEint(np.log(x)))
	axin.set_ylim(Eint(h[ins]-dx), Eint(h[ins]+dx))
	axin.set_xscale('log', base=2)
	ax.indicate_inset_zoom(axin)
	ax.set_xscale('log', base=2)
	plt.legend()
	plt.xlabel('$h$')
	plt.ylabel('Scalar Flux L2 Error')
	if (oc.Good()):
		plt.savefig(oc.Get())
if not(oc.Good()):
	plt.show()