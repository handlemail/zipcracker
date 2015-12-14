# coding=utf-8

import subprocess, argparse, os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

parser = argparse.ArgumentParser()
parser.add_argument("-z", "--zipfile", help="Ficheiro ZIP")
parser.add_argument("-d", "--dicionario", help="Dicionário")
parser.add_argument("-s", "--silence", help="Não apresenta nada na consola excepto se não conseguir achar a palavra passe do zip", action="store_true")
args = parser.parse_args()

if args.silence:
	with open(args.dicionario) as fp:
	    for linha in fp:
	        line = linha.rstrip('\n')
	        p = subprocess.Popen(['7z', 'x', args.zipfile, '-p' + line, '-y'], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
	        out, err = p.communicate()
	        if 'Ok' in out:
	        	break
else:
	if args.zipfile and args.dicionario:
		count = 1
		with open(args.dicionario) as fp:
		    for linha in fp:
		        line = linha.rstrip('\n')
		        p = subprocess.Popen(['7z', 'x', args.zipfile, '-p' + line, '-y'], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
		        out, err = p.communicate()
		        if 'Wrong' in out:
					print '' + `count` + ' - ' + line + ': ' + bcolors.FAIL + 'ERRADA' + bcolors.ENDC
		        else:
		            print '' + `count` + ' - ' + line + ': ' + bcolors.OKGREEN + 'CERTA' + bcolors.ENDC
		            break
		        count += 1
	else:
		print u'A sintaxe correta é: python script.py -z <Ficheiro ZIP> -d <Dicionário>'
