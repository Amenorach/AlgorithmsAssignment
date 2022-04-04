#PROBLEM 2

import sys


def stringMatch(sentence, pattern):
	
	n = len(sentence)
	m = len(pattern)

	for i in range(n-m+1):
		j = 0
		while (j<m and pattern[j] == sentence[i+j]):
			j = j+1
		if j==m:
			return i
	return -1


#FIle Reading
def fileRead():
	fileName = raw_input("Enter the name of the file with .txt extension: ")
	fileInput = open(fileName, "r")
	fileOutput = open("AssOutput.txt","w")

	txtLines = fileInput.read()
	arrayList = txtLines.split('\n')
	i = 1

	while(i<=len(arrayList) -2):
		txt = arrayList[i].strip()
		result = arrayList[i+1].strip()
		searchResult = stringMatch(txt, result)
		fileOutput.writelines("{} \n".format(searchResult))
		i+=2


	fileOutput = open("AssOutput.txt","r")
	print(fileOutput.read())

def interactiveMode():
	sentence = raw_input("Enter a text: ")
	pattern = raw_input("Enter a pattern in the sentence: ")

	outputResult = stringMatch(sentence, pattern)
	print(outputResult)


argvlen = len(sys.argv)
if argvlen > 1:
	mode = sys.argv[1]
	if mode == "interactive":
		interactiveMode()
	else:
		fileRead()
else:
		interactiveMode()



