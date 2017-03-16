import os, sys


print("Starting corrupter: \n")

datatypes = {
	',' : ';',
	'corrupt' : "null\n",
	'normal.\n': 'normal\n',
	'back.\n': 'back\n',
	'buffer_overflow.\n': 'buffer_overflow\n',
	'ftp_write.\n': 'ftp_write\n',
	'guess_passwd.\n': 'guess_passwd\n',
	'imap.\n': 'imap\n',
	'ipsweep.\n': 'ipsweep\n',
	'land.\n': 'land\n',
	'loadmodule.\n': 'loadmodule\n',
	'multihop.\n': 'multihop\n',
	'neptune.\n': 'neptune\n',
	'nmap.\n': 'nmap\n',
	'perl.\n': 'perl\n',
	'phf.\n': 'phf\n',
	'pod.\n': 'pod\n',
	'portsweep.\n': 'portsweep\n',
	'rootkit.\n': 'rootkit\n',
	'satan.\n': 'satan\n',
	'smurf.\n': 'smurf\n',
	'spy.\n': 'spy\n',
	'teardrop.\n': 'teardrop\n',
	'warezclient.\n': 'warezclient\n',
	'warezmaster.\n': 'warezmaster\n'
}


files = [f for f in os.listdir('.') if os.path.isfile(f)]

for f in files:
	if f == 'kddcup.data_10_percent_corrected':
		with open(f, "rt") as fin:
			with open("kddcup.data_10_percent_corrupted.txt", "wt") as fout:
				i = 1
				for line in fin:
					line_list = line.split(",")
					status = line_list[-1]
					line_list[-1] = datatypes[status] if (i%20 != 0) else datatypes['corrupt']

					fout.write(";".join([str(i)] + line_list))
					i = i+1
