f = open("one.txt","w")
f.write("hello student\n")
f.write("welcome to python file handling.\n")
f.write("learning is fun\n")
f.close()

f = open("one.txt","w")
f.write("new content only.\n")
f.close()

f = open("one.txt","w")
lines = [
"python programming\n"
"file handling\n"
"error handling\n"
"expectation handling\n"
]

