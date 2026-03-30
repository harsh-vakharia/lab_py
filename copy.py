src = open("HARSH.txt","r")
data=src.read()
src.close()

dst = open("ATMIYA.txt","w")
dst.write(data)
dst.close()
print("file copied successfully.")