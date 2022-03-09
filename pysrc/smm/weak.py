#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import re 
from OutputCycler import * 
import texTools as tex

oc = OutputCycler()
base = 'data/smm/weak/'
files = ['ip', 'cg', 'rt_bicg', 'hrt']
files += list(map(lambda s: s + '_diff', files))

d = {}
for file in files:
	f = open(base + file + '.txt', 'r')
	s = f.read()
	Ne = list(map(int, re.findall(r'global NE = ([0-9]*)', s)))
	out = re.findall(r'np =\s*([0-9]*), it = ([0-9]*)', s)
	nproc = [] 
	it = [] 
	for ele in out:
		nproc.append(int(ele[0]))
		it.append(int(ele[1]))
	d[file] = {'Ne': Ne, 'it': it, 'np': nproc}

# table = tex.Tabular('Processors', '$N_e$', *['IP', 'CG', 'RT', 'HRT']*2)
table = tex.Tabular('Processors', '$N_e$', *['VEF', 'Diff.']*4)
ele = d[files[0]]['Ne']
nproc = d[files[0]]['np']
for i in range(len(ele)):
	s = [str(nproc[i]), tex.utils.writeNumber(ele[i], '{}')] 
	# for f in files:
		# s.append(str(d[f]['it'][i]))
	for j in range(int(len(files)/2)):
		s.append(str(d[files[j]]['it'][i]))
		s.append(str(d[files[j]+'_diff']['it'][i]))
	table.AddRow(*s)
# table.AddColumnGroup('VEF', 2, 4)
# table.AddColumnGroup('Diffusion', 6, 4)
table.AddColumnGroup('IP', 2, 2)
table.AddColumnGroup('CG', 4, 2)
table.AddColumnGroup('RT', 6, 2)
table.AddColumnGroup('HRT', 8, 2)
if (oc.Good()):
	table.Write(oc.Get())
else:
	print(table)