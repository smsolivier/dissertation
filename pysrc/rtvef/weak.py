#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import re 
from OutputCycler import * 
import texTools as tex

oc = OutputCycler()
base = 'data/rtvef/weak/'
files = ['rt', 'rt_diff', 'hrt', 'hrt_diff']

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

table = tex.Tabular('Processors', '$N_e$', *['VEF', 'Diffusion']*2)
ele = d[files[0]]['Ne']
nproc = d[files[0]]['np']
for i in range(len(ele)):
	s = [str(nproc[i]), tex.utils.writeNumber(ele[i], '{}')] 
	for f in files:
		s.append(str(d[f]['it'][i]))
	table.AddRow(*s)
table.AddColumnGroup('RT', 2, 2)
table.AddColumnGroup('HRT', 4, 2)
if (oc.Good()):
	table.Write(oc.Get())
else:
	print(table)