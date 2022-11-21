import os

entries = os.listdir('Master Directory')
os.chdir('Directory with key files')
for entry in entries:
    entry = entry.upper()
    if entry.endswith("TXT"): ## Limits scope to only .txts files, becuase that is bitlocker default.
        entry_name = entry.split(".TXT", 1)[0] ## Removes extension
        entry_cleaned = entry_name.split(" ", 1)[0] ## Removes all characters after first space because techs usually put PC name, then space, then rest of file name
        bitname = (entry_cleaned) # saves as var
        with open(entry, "r") as openfile: #Open file
            openfile = open(entry)
            content = openfile.readlines()
            bitkey = (content[24]) #Find bitlocker key, which is defualt on 24
            bitkey = (bitkey.strip()) # Strips spaces around key
            openfile.close() # Close file
            bitfile = bitname + bitkey ## Combines PC name & key to 1 line.
            keylist = open("keylist.txt", "a") # Creates/Opens new txt
            keylist.write(bitfile + "\n") # Appends name+key to new line in file
            keylist.close(), #Closes File
            continue 
    ## Needs work to dig in subdirs.
    # elif not entry.endswith("pdf" or "rtf"):
    #     for directory in entries:
    #          for entry2 in directory:
    #              entry2 = entry2.upper()
    #              if entry2.endswith("TXT"):
    #                  entry_name2 = entry2.split(".TXT", 1)[0]
    #                  entry_cleaned2 = entry_name2.split(" ", 1)[0]
    #                  bitname2 = (entry_cleaned2)
    #                  with open(entry2, "r") as openfile:
    #                      openfile2 = open(entry2)
    #                      content2 = openfile2.readlines()
    #                      bitkey2 = (content2[24])
    #                      bitkey2 = (bitkey2.strip())
    #                      print(bitkey2)
    #                      openfile2.close()
    #                      bitfile2 = bitname2 + bitkey2
    #                      print(os.getcwd)
    #                      keylist = open("keylist.txt", "a")
    #                      keylist.write(bitfile2 + "\n")
    #                      keylist.close(),
    else: 
        pass
