fo = open("foo.txt", "wb")
str = raw_input("Enter your input: ")
fo.write( str)

#Close opend file 
fo.close()