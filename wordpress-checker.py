#!/usr/bin/python

import sys, getopt
import urllib3
import requests
from colorama import Fore, Back, Style


inputfile = ''
outputfile = ''
wordlist = ''
url = ''
result = []
def main(argv):
	parse_args(argv)


def parse_args(argv):
	global inputfile
	global outputfile
	global wordlist
	global url

	try:
		opts, args = getopt.getopt(argv,"h:i:o:w:u:",["input=","output=","wordlist=","url="])
	except getopt.GetoptError:
		help_print()
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			help_print()
			sys.exit()
		elif opt in ("-i","--input"):
			inputfile = arg
		elif opt in ("-o","--output"):
			outputfile = arg
		elif opt in ("-w","--wordlist"):
			wordlist = arg
		elif opt in ("-u","--url"):
			url = arg
	if inputfile != '':
		scan(inputfile,None,wordlist)
	else:
		scan(None,url,wordlist)

def scan(inputfile,url,wordlist):
	global result
	http = urllib3.PoolManager()
	check_input(inputfile,url,wordlist)
	fuzzing_File = open(wordlist,'r')
	fuzzing_List = fuzzing_File.readlines()
	if inputfile != None:
		iFile = open(inputfile,'r')
		targets = iFile.readlines()
		for t in targets:
			for f in fuzzing_List:
				full_path = t[:-1]+'/'+f[:-1]
				r = requests.get('https://'+full_path)
				# r = http.request("GET",'https://'+full_path)
				if r.status_code == 200 or  r.status_code == 405:
					result.append((full_path,r.status_code))
					break
		iFile.close()
	else:
		fuzzing_File = open(wordlist,'r')
		fuzzing_List = fuzzing_File.readlines()
		for f in fuzzing_List:
			full_path = url+'/'+f[:-1]
			r = requests.get('https://'+full_path)
			# r = http.request("GET",'https://'+full_path)
			if r.status_code == 200 or  r.status_code == 405:
				result.append((full_path,r.status_code))
				break
	fuzzing_File.close()
	output()
def check_input(inputfile,url,wordlist):
	if wordlist == '' :
		print 'please enter wordlist'
		sys.exit(2)
	if url == None and inputfile == None:
		print 'please enter URl or input file'
		sys.exit(2)
def output():
	global result
	oFile = None
	outputFileIsGiven = False
	if output != '':
		outputFileIsGiven = True
	if outputFileIsGiven
		oFile = open(outputfile,'w')
	for i in result:
		if outputFileIsGiven:
			oFile.write(str(i[1])+'\t'.expandtabs(4)+i[0]+'\n')
		if i[1] == 200:
			print '%-27s'%(Fore.GREEN+i[0]),'-->  '+str(i[1])
			
		else:
			print '%-27s'%(Fore.RED+i[0]),'-->  '+str(i[1])
	if outputFileIsGiven:
		oFile.flush()
		oFile.close()

def help_print():
	print 'A simple wordpress checker on domains\n'
	print 'Usage: wordpress-checker.py [options]\n'
	print 'Options:'
	print '%-40s'%'\t-u, --url <example.com>'.expandtabs(4), 'URL must if there no input file'
	print '%-40s'%'\t-i, --input <in.txt>'.expandtabs(4), 'File of URLs (optional)'
	print '%-40s'%'\t-o, --output <out.txt>'.expandtabs(4), 'File to save output'
	print '%-40s'%'\t-w, --wordlist <wordlist.txt>'.expandtabs(4), 'Fuzzing list (must be like "wp-signup.php")'

if __name__ == "__main__":
   main(sys.argv[1:])