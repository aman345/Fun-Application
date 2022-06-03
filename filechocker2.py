import shutil
from cryptography.fernet import Fernet
import os
from os import walk
import ast

class FileEnCrypterAndDecrypter:

    def __init__(self, wd):
        self.wd = wd+"/"
        self.working_directory = wd+"/encodedfiles/"
        os.makedirs(self.working_directory,exist_ok=True)
        os.chdir(self.working_directory)
        self.keys_file = self.working_directory+'.filechockers.key'
        
    def encrypt(self, filename):
        key = Fernet.generate_key()
        f = Fernet(key)
        with open(self.wd+filename, 'rb') as file:
            print(self.wd+filename)
            file_data = file.read()
        encrypted_data = f.encrypt(file_data)

        with open(self.working_directory+"."+filename, 'wb') as file:
            print(self.working_directory+filename)
            file.write(encrypted_data)
        
        with open(self.keys_file, 'a') as f:
            f.write("."+filename+"%"+str(key)+"\n")
            
        os.remove(self.wd+filename)
        


    def decrypt(self, filename):
        print("decryption starts")
        key = self.search(filename)
        
        if key== -1 or filename=='filechockers.key':
           return
        key=ast.literal_eval(key)
        f = Fernet(key)

        with open(self.working_directory+filename, 'rb') as file:
            data = file.read()

        decryptdata = f.decrypt(data)

        with open(self.wd+filename.removeprefix('.'), 'wb') as file:
            file.write(decryptdata)
    	
        os.remove(self.working_directory+filename)
    	
    def search(self,filename):
        ff = open(self.keys_file, 'r').readlines()
        for x in ff:
            res = x.split("%")
            if res[0] == filename:
                return res[1].strip('\n')

        return -1  

    def functionofgenisis(self,filen,func):
        for f in filen:
            if(func=='enc'):
                self.encrypt(f)      
            if func=='dec':
                self.decrypt(f)
        
        if func=='dec':
            os.remove(self.keys_file)
            os.rmdir(self.working_directory)
if __name__ =="__main__":
    filen = []
    fd = 'your directory here'
    ch = input("Enter choice enc or dec")
    print("===========Started=============") 
    futil = FileEnCrypterAndDecrypter(fd)
    print(fd)
    for(dirpath, dirnames,filenames) in walk(fd): 
        filen.extend(filenames)
    futil.functionofgenisis(filen,ch)
    print("===========Completed=============") 
