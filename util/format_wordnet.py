import configparser
import glob
import re

config = configparser.ConfigParser()
config.read('./config.ini')
files = glob.glob(config['DEFAULT']['wordnet_loc'] + '/*.xml')
outf = config['DEFAULT']['def_loc']

defs = dict()
terms = []
t = re.compile('<term>(.+)</term>')
d = re.compile('<orig>(.+)</orig>')

for file in files:
	with open(file, 'r') as f:
		for line in f:
			line = line.strip()
			m1 = t.match(line)
			if m1:
				terms.append(m1.group(1).lower())
			m2 = d.match(line)
			if m2:
				defn = m2.group(1)
				for term in terms:
					p = re.compile(r'\b' + term + r'\b')
					defn = p.sub('_', defn)
				for term in terms:
					if term in defs:
						defs[term] = defs[term] + [defn]
					else:
						defs[term] = [defn]
				terms = []

spaces = re.compile(r'\s+')
with open(outf, 'w') as f:
	for wd, ds in defs.items():
		wd = spaces.sub("_", wd)
		for df in ds:
			f.write(wd + "\t" + df + "\n")
