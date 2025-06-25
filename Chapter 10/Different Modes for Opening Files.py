#Read Mode (r): This opens the file for reading only. If the file does not exist, it generates an error.
file = open("./data/example.txt", "r")
content = file.read()
file.close()

#Write Mode (w): )This opens the file for writing. If the file already exists, 
#it will be truncated (overwritten). If the file does not exist, it creates a new one.
file = open("./data/example.txt", "w")
file.write("Hello, World!")
file.close()

#Append Mode (a): Opens the file for writing, adding new material to the end if it already exists. 
#If the file does not exist, it creates a new one.
file = open("./data/example.txt", "a")
file.write("Hello again!")
file.close()

#Binary Read Mode (rb): Opens the file for binary reading. This is handy for non-text files such as graphics and executables.
file = open("./data/example.jpg", "rb")
content = file.read()
file.close()

#Binary Write Mode (wb): Opens the file for binary writing. If the file already exists, it will be truncated. 
#If the file does not exist, it creates a new one.
file = open("./data/example.jpg", "wb")
file.write(b"\x00\x01\x02\x03")
file.close()

#Binary Append Mode (ab): Opens the file in binary mode and appends new content to its end if it already exists. 
#If the file does not exist, it creates a new one..
file = open("./data/example.jpg", "ab")
file.write(b"\x04\x05\x06\x07")
file.close()
