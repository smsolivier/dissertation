#!/usr/bin/env python3

import numpy as np
import yaml 
import pandas as pd
import texTools as tex
from OutputCycler import * 
oc = OutputCycler()
base = oc.GetOpt(0, 'data/smm/mms/')

files = ['rt', 'hrt']
d = []
for f in files:
	with open(base + f + '.txt', 'r') as stream:
		db = yaml.safe_load(stream)
	opts = db.pop('Options used')
	d.append(db)

orders = list(d[0].keys())
table = tex.Tabular('Value', *['RT', 'HRT']*3)
table.SetRowGroupTitle('$p$')
app = tex.Tabular('$h$', *['RT', 'HRT']*3)
app.SetRowGroupTitle('$p$')
keys = ['err', 'perr', 'Jerr']
for j,p in enumerate(orders):
	order = ['Order']
	const = ['Constant']
	for key in keys:
		for i in range(len(files)):
			df = pd.DataFrame(d[i][p])
			fit = np.polyfit(np.log(df['h']), np.log(df[key]), 1)
			order.append((fit[0], '{:.3f}'))
			const.append((np.exp(fit[1]), '{:.3f}'))
	table.AddRow(*order)
	table.AddRow(*const) 
	table.AddRowGroup(str(p), 2*j, 2, False)

	n = len(df['h'])
	for i in range(n):
		s = [tex.utils.writeNumber(df['h'][i], '{:.3e}')]
		for key in keys:
			for f in range(len(files)):
				s.append(tex.utils.writeNumber(d[f][p][i][key], '{:.3e}'))
		app.AddRow(*s) 
	app.AddRowGroup(str(p), n*j, n, False)

for t in [table, app]:
	t.AddColumnGroup(r'$\| \varphi - \varphi_\text{ex}\|$', 1, len(files))
	t.AddColumnGroup(r'$\| \varphi - \Pi \varphi_\text{ex}\|$', 1+len(files), len(files))
	t.AddColumnGroup(r'$\| \vec{J} - \vec{J}_\text{ex}\|$', 1+2*len(files), len(files))
	t.AddColumnBreak(0)
if (oc.Good()):
	table.Write(oc.Get())
	app.Write(oc.Get())
else:
	print(table)
	print(app)