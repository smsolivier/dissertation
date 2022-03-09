#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import re 
import glob 
import texTools as tex 
import pandas as pd
from OutputCycler import OutputCycler
oc = OutputCycler() 
base = oc.GetOpt(0, 'data/rtvef/curved_solvers')

fnames = glob.glob(base + '/*')

df = {}
for fname in fnames:
	f = open(fname, 'r') 
	file = f.read()
	it = int(re.findall(r'inner = ([0-9]*)', file)[0])
	vtype = re.findall(r'--vef_type (.*)', file)[0]
	alpha = float(re.findall(r'--alpha (.*)', file)[0])
	fe_order = int(re.findall(r'--fe_order (.*)', file)[0])
	vtype = vtype.upper()
	if not(fe_order in df):
		df[fe_order] = {}
	if not(vtype in df[fe_order]):
		df[fe_order][vtype] = {'it':[it], 'alpha':[alpha]}
	else:
		df[fe_order][vtype]['it'].append(it)
		df[fe_order][vtype]['alpha'].append(alpha) 
fe_order = sorted(list(df.keys()))
for p in fe_order:
	for v in df[p]:
		idx = np.argsort(df[p][v]['alpha'])
		df[p][v]['it'] = np.array(df[p][v]['it'])[idx]
		df[p][v]['alpha'] = np.array(df[p][v]['alpha'])[idx]

tab = tex.Tabular()
head = ['Method'] 
df0 = df[fe_order[0]]
alpha = df0[list(df0)[0]]['alpha']
for i in range(len(alpha)):
	head.append((alpha[i], '{:.3f}'))
tab.SetHeader(*head) 
tab.SetRowGroupTitle('$p$')
for i,p in enumerate(fe_order):
	for key in ['H1', 'RT', 'HRT']:
		r = [key]
		for j in range(len(df[p][key]['it'])):
			it = df[p][key]['it'][j]
			r.append('--' if it==250 else str(it))
		tab.AddRow(*r) 
	tab.AddRowGroup(str(p), 3*i, 3, False)
tab.AddColumnGroup('Distortion Amount', 1, len(alpha))

if (oc.Good()):
	tab.Write(oc.Get())
else:
	print(tab) 