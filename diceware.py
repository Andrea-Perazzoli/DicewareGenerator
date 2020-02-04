import argparse
import secrets
import sys
from time import sleep

import pyperclip as pyperclip

d = {}

def loadFile(file="default.txt"):
	global d
	with open(file, 'r') as f:
		for line in f:
			line = line.split(" ")
			key = str(line[0])
			if key.isdigit():
				val = str(line[-1]).replace("\n", "")
				d[key] = val
	if not d:
		raise RuntimeError("[-] Dict not populated!")

def generateRandomNumberInString(maxDigit=6):
	return str(secrets.randbelow(maxDigit) + 1)

def generateWord(dictKeyLen=5):
	global d
	key_gen = ""
	for i in range(dictKeyLen):
		key_gen += generateRandomNumberInString()
	return d[key_gen]

def generatePassphrase(file="default.txt", separator=" ", passPhraseWords = 5):
	passphrase = ""
	loadFile()
	for i in range(passPhraseWords):
		if passphrase != "":
			passphrase += separator
		passphrase += generateWord()
	return passphrase

def copyToClipboard(what):
	pyperclip.copy(what)

def eraseClipboard(seconds=7):
	for i in range(seconds, 0, -1):
		print("\r", end="[+] Erasing clipboard in " + str(i) + " seconds...")
		sleep(1)
	pyperclip.copy("")
	print("\n[+] Clipboard erased!")

if __name__ == '__main__':
	try:
		parser = argparse.ArgumentParser(prog='Diceware Password generator')
		parser.add_argument('-o', help='Print passphrase to stdout', action="store_true")
		parser.add_argument('-f', metavar="FILE", help='File path to Diceware words')
		parser.add_argument('-s', metavar="SEPARATOR", help='Separator')
		parser.add_argument('-n', metavar="N_WORDS", help='Number of words')
		args = parser.parse_args()

		separator = " "
		file = "default.txt"
		nWords = 5

		if args.f: file = args.f
		if args.s: separator = args.s
		if args.n: nWords = args.n

		passw = generatePassphrase(file=file, separator=separator, passPhraseWords=nWords)
		if args.o:
			print(passw)
		copyToClipboard(passw)
		eraseClipboard(10)

	except KeyboardInterrupt:
		pyperclip.copy("")
		print("\n[+] Clipboard erased!")



