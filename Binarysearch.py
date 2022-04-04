#PROBLEM 1

import sys

def BinarySearching(array, target):
    return Recursion(array, target, 0, len(array) - 1)


def Recursion(array, target, left, right):
    if left > right:  
        return - 1

    middle = (left + right) // 2
    potentialMatch = array[middle]
    lefttNumber = array[left]
    rightNumber = array[right]
    if target == potentialMatch:
        return middle
    elif lefttNumber <= potentialMatch:
        if target < potentialMatch and target >= lefttNumber:
            return Recursion(array, target, left, middle - 1)
        else:
            return Recursion(array, target, middle + 1, right)
    else:
        if target > potentialMatch and target <= rightNumber:
            return Recursion(array, target, middle + 1, right)
        else:
            return Recursion(array, target, left, middle - 1)


#FIle Reading
def fileRead():
	fileName = raw_input("Enter the filename with a .txt extension: ")
	fileInput = open(fileName, "r")
	fileOutput = open("binarySearchOutput.txt", "w")

	txtLines = fileInput.read()
	arrayList = txtLines.split('\n')
	i = 1

	while(i <= len(arrayList) - 2):
		bracketRemoval = arrayList[i].replace("(", "")
		bracketRemoval = bracketRemoval.replace(")", "")

		listToInt = [int(k) for k in (bracketRemoval.split())]

		result = int(arrayList[i+1])
		searchResult = BinarySearching(listToInt, result)

		fileOutput.writelines("{} \n".format(searchResult))
		i += 2

	fileOutput = open("binarySearchOutput.txt", "r")
	print(fileOutput.read())


def interactiveMode():
	def integerNum(num):
		return int(num)

	arrayList = list(map(integerNum, raw_input("Enter numbers separated by space: ").split()))
	numSearch = int(raw_input("Enter a number to search for: "))

	outputResult = BinarySearching(arrayList, numSearch)
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
