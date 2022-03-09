#!/usr/bin/env python3

import numpy as np
import re 
import yaml 
import pandas as pd
import texTools as tex 
from OutputCycler import * 
oc = OutputCycler()

files = ['ip', 'br2', 'mdldg', 'cg']
d = [] 
for f in files:
	with open('data/dgvef/mms/' + f + '.txt', 'r') as stream:
		db = yaml.safe_load(stream)
	opts = db.pop('Options used')
	vtype = re.findall(r'--vef\s(\S*)', opts)[0]
	db['vtype'] = vtype 
	d.append(db) 

for p in range(1,4):
	table = tex.Tabular('$h$', 'IP', 'BR2', 'MDLDG', 'CG', 'Deviation')
	df = [] 
	for i in range(len(files)):
		df.append(pd.DataFrame(d[i][p]))
	h = df[0]['h']

	for i in range(len(h)):
		s = [tex.utils.writeNumber(h[i], '{:.3e}')]
		for j in range(len(files)):
			s.append(tex.utils.writeNumber(df[j]['err'][i], '{:.3e}'))
		errs = np.array([d['err'][i] for d in df])
		s.append(tex.utils.writeNumber(np.std(errs), '{:.3e}'))
		table.AddRow(*s) 

	order = ['Order'] 
	const = ['Constant']
	for i in range(len(files)):
		fit = np.polyfit(np.log(h), np.log(df[i]['err']), 1)
		order.append((fit[0], '{:.3f}'))
		const.append((np.exp(fit[1]), '{:.3f}'))
	order.append('')
	const.append('')
	table.AddLineSpace()
	table.AddRow(*order)
	table.AddRow(*const)
	table.AddColumnBreak(0)
	table.AddColumnBreak(len(files))
	if (oc.Good()):
		table.Write(oc.Get())
	else:
		print(table)