import os, sys

print("Starting aggregator: \n")

datatypes = {
	',' : ';',
	'normal.\n': 'normal;good\n',
	'back.\n': 'dos;bad\n',
	'buffer_overflow.\n':'u2r;bad\n',
	'ftp_write.\n': 'r2l;bad\n',
	'guess_passwd.\n': 'r2l;bad\n',
	'imap.\n': 'r2l;bad\n',
	'ipsweep.\n': 'probe;bad\n',
	'land.\n': 'dos;bad\n',
	'loadmodule.\n': 'u2r;bad\n',
	'multihop.\n': 'r2l;bad\n',
	'neptune.\n': 'dos;bad\n',
	'nmap.\n': 'probe;bad\n',
	'perl.\n': 'u2r;bad\n',
	'phf.\n': 'r2l;bad\n',
	'pod.\n': 'dos;bad\n',
	'portsweep.\n': 'probe;bad\n',
	'rootkit.\n': 'u2r;bad\n',
	'satan.\n': 'probe;bad\n',
	'smurf.\n': 'dos;bad\n',
	'spy.\n': 'r2l;bad\n',
	'teardrop.\n': 'dos;bad\n',
	'warezclient.\n': 'r2l;bad\n',
	'warezmaster.\n': 'r2l;bad\n'
}


files = [f for f in os.listdir('.') if os.path.isfile(f)]

for f in files:
	if f == 'kddcup.data_10_percent_corrected':
		with open(f, "rt") as fin:
			with open("kddcup.data_10_percent_formatted.txt", "wt") as fout:
				i = 1
				for line in fin:
					line_list = line.split(",")
					status = line_list[-1]

					line_list[-1] = datatypes[status]
					fout.write(";".join([str(i)] + line_list))
					i = i+1