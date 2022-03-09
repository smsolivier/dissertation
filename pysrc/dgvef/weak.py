#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import re 
import pandas as pd 
from OutputCycler import * 
import texTools as tex

oc = OutputCycler()
base = 'data/dgvef/weak/'
files = ['ip', 'ip_sym', 'ip_diff', 'cg', 'cg_diff']

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

df = pd.DataFrame(d) 
table = tex.Tabular('Processors', '$N_e$', 'USC', 'USC-S', 'Diffusion', 'AMG', 'Diffusion')
ele = df[files[0]]['Ne']
nproc = df[files[0]]['np']
for i in range(len(ele)):
	s = [str(nproc[i]), tex.utils.writeNumber(ele[i], '{}')] 
	for f in files:
		s.append(str(df[f]['it'][i]))
	table.AddRow(*s)
table.AddColumnGroup('IP', 2, 3)
table.AddColumnGroup('CG', 5, 2)

if (oc.Good()):
	table.Write(oc.Get())
else:
	print(table)