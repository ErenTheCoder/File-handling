f = open("hello.txt","w")
f.write("hello")
f.close()

f = open("hello.txt","r")
print(f.read())
f.close()

f = open("hello.txt","a")
f.write("\n bye cya")
f.close()
