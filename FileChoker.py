import shutil
from cryptography.fernet import Fernet
import os
from os import walk
import ast

class FileEnCrypterAndDecrypter:

    def __init__(self, wd):
        self.wd = wd+"/"
        self.keys_file = self.wd+'filechockers.key'
        
    def encrypt(self, filename):
        key = Fernet.generate_key()
        f = Fernet(key)
        with open(self.wd+filename, 'rb') as file:
            file_data = file.read()
        encrypted_data = f.encrypt(file_data)

        with open(self.wd+filename, 'wb') as file:
            file.write(encrypted_data)
        
        with open(self.keys_file, 'a') as f:
            f.write(filename+"%"+str(key)+"\n")

    def decrypt(self, filename):
        key = self.search(filename)
        if key== -1 or filename=='filechockers.key':
           print("not found")
           return
        key  =ast.literal_eval(key)
        f = Fernet(key)

        with open(self.wd+filename, 'rb') as file:
            data = file.read()

        decryptdata = f.decrypt(data)

        with open(self.wd+filename, 'wb') as file:
            file.write(decryptdata)
    
    def search(self,filename):
        ff = open(self.keys_file, 'r').readlines()
        for x in ff:
            res = x.split("%")
            #print("resul:"+str(res[0])+":"+res[1])
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
if __name__ =="__main__":
    filen = []
    fd = 'path to file directory'
    print("===========Started=============") 
    futil = FileEnCrypterAndDecrypter(fd)
    for(dirpath, dirnames,filenames) in walk(fd): 
        filen.extend(filenames)
    futil.functionofgenisis(filen,'dec')

    print("===========Completed=============") 
