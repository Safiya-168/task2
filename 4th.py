'''Print characters from a string that are present at an even index number'''
string=(input("enter the string: "))
print("original string",string)
size=len(string)
print(string[0::2])
for i in range(0,size-1,2):
                        print("index[",i,"]",string[i])