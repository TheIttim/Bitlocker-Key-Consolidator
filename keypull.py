import pathlib
import os
for txt_file in pathlib.Path("C:\\Users\\example\\Desktop\\Test").glob('**/*.txt'):
    entry_name = txt_file.stem  # Removes extension
    entry_cleaned = entry_name.split(" ", 1)[0]
    bitname = (entry_cleaned)  # saves as var
    with open(txt_file, "r") as openfile:  # Open file
        lines = len(openfile.readlines())
        if lines < 24:
            skiplist = open("skiplist.txt", "a")
            skiplist.write(os.path.abspath(bitname)+ "\n") #Creates lists of skipped files.
            skiplist.close() # Closes File
        else:
            openfile = open(txt_file)
            content = openfile.readlines()
            bitid = (content[12])
            bitid = (bitid.strip())
            bitkey = (content[24])  # Find bitlocker key, which is default on 24
            bitkey = (bitkey.strip())  # Strips spaces around key
            openfile.close()  # Close file
            bitfile = bitname + bitkey + bitid  # Combines PC name & key to 1 line.
            keylist = open("keylist.txt", "a")  # Creates/Opens new txt
            keylist.write(bitfile + "\n")  # Appends name+key to new line in file
            keylist.close() # Closes File
