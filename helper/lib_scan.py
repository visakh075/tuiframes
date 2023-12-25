# scan through sub lib directories
#/usr/bin/python3
import os
import sys
import pathlib
import re
class buid_system:
	def __init__(self,project_path):
		self.PrjPath=project_path
		self.PrjName=os.path.basename(self.PrjPath)
		self.Libs=Scan(project_path)
		self.filter_libs()
		
	def filter_libs(self):
		self.SubLibs=[]
		self.PrjLibs=[]
		for Lib in self.Libs:
			if(self.Libs[Lib].ModulePath==self.PrjPath):
				self.PrjLibs.append(self.Libs[Lib])
			else:
				self.SubLibs.append(self.Libs[Lib])
	def show(self):
		print("PROJECT {}".format(self.PrjName))
		print("__Modules")
		for module in self.PrjLibs:
			module.print()
		print("__SubModules")
		for module in self.SubLibs:
			module.print()
   
	# Generator functions
	def IncludePaths(self):
		for Lib in self.Libs:
			# include needs -I for each directory
			print("-I {}".format(self.Libs[Lib].LibPath),end=" ")
	
	def IncludesListAll(self):
		for Lib in self.Libs:
			# include needs -I for each directory
			print("{}".format(self.Libs[Lib].LibName),end=" ")

	def PrjModuleList(self):
		for Lib in self.PrjLibs:
			# include needs -I for each directory
			print("{}".format(Lib.LibName),end=" ")
	
	def SubModuleList(self):
		for Lib in self.SubLibs:
			# include needs -I for each directory
			print("{}".format(Lib.LibName),end=" ")
	
	def genObjectPathSubModules(self):
		for Lib in self.SubLibs:
			print(Lib.Object,end=" ")

	def genObjectPath(self):
		self.genObjectPathPrjModules()
		self.genObjectPathSubModules()

	def genObjectPathPrjModules(self):
		for Lib in self.PrjLibs:
			print(Lib.Object,end=" ")
   
	def getBuildPath(self,library_path):
		for Lib in self.SubLibs:
			# print(Lib.LibPath)
			if(Lib.Object==library_path):
				print(Lib.ModulePath)
	
	def getBuildPathM(self,module_name):
		for Lib in self.SubLibs:
			# print(Lib.LibPath)
			if(Lib.LibName==module_name):
				print(Lib.ModulePath)
		for Lib in self.PrjLibs:
			if(Lib.LibName==module_name):
				print(Lib.ModulePath)
	
	def getStatModule(self,module_name):
		for Lib in self.SubLibs:
			# print(Lib.LibPath)
			if(Lib.LibName==module_name):
				return(Lib.Stat)
		for Lib in self.PrjLibs:
			if(Lib.LibName==module_name):
				return(Lib.Stat)
	
	def getPrjNameModule(self,module_name):
		for Lib in self.SubLibs:
			# print(Lib.LibPath)
			if(Lib.LibName==module_name):
				print(Lib.ModuleName)
		for Lib in self.PrjLibs:
			if(Lib.LibName==module_name):
				print(Lib.ModuleName)
	
	def getObjectPath(self,module_name):
		for Lib in self.Libs:
			if(self.Libs[Lib].LibName==module_name):
				print(self.Libs[Lib].Object)
    
	def getHeaderPath(self,module_name):
		for Lib in self.Libs:
			if(self.Libs[Lib].LibName==module_name):
				print(self.Libs[Lib].Header)
    
	def getPrjName(self):
		print(self.PrjName)
		
class library_item:
	def __init__(self,LibraryName,Directory,Sources):
		self.LibName=LibraryName
		self.LibPath=Directory
		self.SRCs=Sources
		self.ModulePath=os.path.dirname(self.LibPath)
		self.ModuleName=os.path.basename(self.ModulePath)
		self.Stat="Non-Exist"
		self.generate()
	def generate(self):
		self.Header=os.path.join(self.LibPath,"{}.h".format(self.LibName))
		self.Object=os.path.join(self.ModulePath,"obj","{}.o".format(self.LibName))		
		
		if(os.path.exists(self.Object)):
			self.Stat="Exist"
		else:
			self.Stat="Non-Exist"

	def print(self):
		print("LibName :",self.LibName)
		print("LibPath :",self.LibPath)
		print("ModuleName :",self.ModuleName)
		print("ModulePath :",self.ModulePath)
		print("SRCs :",self.SRCs)
		print("Header File :",self.Header)
		print("Object File :",self.Object)
		print()
	
## the base element is header file,
## where the header is situated there we can have multiple c/cpp files with the same sarting
## eg lib_rtlog.h
## lib_rtlog.cpp - main cpp file
## lib_rtlog_subfiles.cpp
## lib_rtlog_filehandler.cpp
## all these files should come as part of same trasnlational unit
## g++ -o lib_rtlog.o -c 
def Scan(directory):
	libraries={}
	# print(directory)
	for walker in os.walk(directory):
		root,dir,files = walker
		libs=[]
		if(os.path.basename(root)=="lib"):
			# check for header files
			
			for file in files:
				base,extens=os.path.splitext(file)
				if(extens=='.h'):
					libs.append(base)
			for lib_item in libs:
				sources=[]
				for file in files:
					base,extens=os.path.splitext(file)
					if((extens=='.cpp' or extens=='.c') and base.startswith(lib_item)):
						sources.append(file)
				library=library_item(lib_item,root,sources)
				
				libraries[lib_item]=library
    
	return libraries

			
# OutputType
# 0 for normal inclusion 
# -I libXXX.h libYYYY.h ...
# 1 as list
# libXXX.h
# libYYY.h

item_types=['.h']
OutputType = 0
LibraryPath='lib'
WorkDir=os.getcwd()


k=buid_system(WorkDir)
# k.show()
# print(sys.argv)
if len(sys.argv) > 1:
	# Access the command-line arguments starting from index 1
	# sys.argv[0] is the script name itself
	# OutputType=sys.argv[1]
	if(sys.argv[1]=='IncludePaths'):
		# if(OutputType=='args'):
		k.IncludePaths()
		# else:		
			# k.IncludesListAll()

	if(sys.argv[1]=='PrjModules'):
		# if(OutputType=='list'):
		k.PrjModuleList()
		# else:		
		# k.IncludesListAll()

	if(sys.argv[1]=='SubModules'):
#		if(OutputType=='list'):
		k.SubModuleList()
#		else:		
#		k.IncludesListAll()


	if(sys.argv[1]=='PrjModuleObjects'):
		k.genObjectPathPrjModules()

	if(sys.argv[1]=='SubModuleObjects'):
		k.genObjectPathSubModules()
  
	if(sys.argv[1]=='AllObjects'):
		k.genObjectPath()
 
	if(sys.argv[1]=='getBuildPath'):
		# print(sys.argv[3])
		k.getBuildPath(sys.argv[2])
  
	if(sys.argv[1]=='getBuildPathM'):
		# print(sys.argv[3])
		k.getBuildPathM(sys.argv[2])

	if(sys.argv[1]=='getObjectPath'):
		# print(sys.argv[3])
		k.getObjectPath(sys.argv[2])

	if(sys.argv[1]=='getHeaderPath'):
		# print(sys.argv[3])
		k.getHeaderPath(sys.argv[2])
  
	if(sys.argv[1]=='getStatModule'):
		if(k.getStatModule(sys.argv[2])=='Exist'):
			#print("\033[0;32m")
			#print("✔")
			print("1")
		else:
			#print("✘")
			#print("\033[0;34m")
			print("0")
  
	if(sys.argv[1]=='getPrjName'):
		k.getPrjName()

	if(sys.argv[1]=='getPrjNameModule'):
		k.getPrjNameModule(sys.argv[2])
  
	if(sys.argv[1]=='show'):
		k.show()
# k.genIncludePath()
# print()
# k.genObjectPath()
# # return according to output type

# if(OutputType==0):
# 	#print as a normal inclusion
# 	if(len(ScanResult)):
# 		print('-I',end=' ')
# 	for item in ScanResult:
# 		# print(item,end=' ')
# 		print(re.sub(WorkDir+'/',"",item),end=' ')
# elif(OutputType==1):
# 	for item in ScanResult:
# 		# print(item)
# 		print(re.sub(WorkDir+'/',"",item),end='\n')

