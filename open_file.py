file = open("sample.txt" , 'r')
print file.readline()

file = open("blank.rtf" , 'w')
file.write("this is a test \n")
file.write("and this is the second test")
