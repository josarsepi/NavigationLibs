import os

# Simple Navigation
def ls(path=None):
	# Add try around ifs.  Except add "os.getcwd()+"/"+path" to fix issues with simulated storage.
	if path == None:
		loc = os.getcwd()
		dirlist = os.listdir(loc)
		for each in dirlist:
			print(each)
	if path != None:
		loc = str(os.getcwd()+path)
		dirlist = os.listdir(loc)
		for each in dirlist:
			print(each)
		
def cd(path):
	os.chdir(str(path))
	print("You are now in "+str(os.getcwd()))
	
def pwd():
	print(str(os.getcwd()))

def mkdir(newfile):
	os.mkdir(str(newfile))
	
def rm(file2delete):
	try:
		os.remove(file2delete)
	except:
		os.rmdir(file2delete)
	
# File Manipulation

############
### Bugs ###
############
