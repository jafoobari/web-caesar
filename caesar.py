# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 16:36:55 2016

@author: user
"""


from sys import argv, exit
print("I know that these are the words the user typed on the command line: ", argv)

    
def encrypt(m, key):
    return ''.join([chr(((ord(char) - 65 + key) % 26) + 65) if char.isupper() else chr(((ord(char) - 97 + key) % 26) + 97) if char.islower() else char for char in m])
    
def user_input_is_valid(cl_args):
    if len(cl_args) == 1:
        return False
    elif cl_args[1].isdigit() == True:
        return True
    else:
        return False

        
    
    
def main(): 
    if user_input_is_valid(argv) == False:
        print("{} is not a valid rotation amount. Must be an integer.".format(argv[1]))
        exit()
    if type(argv[1]) == str:
        rot = int(argv[1])
        text = str(input("What's your message?\n"))
        print(caesar(text,rot))
    else:
        text = str(input("What's your message?\n"))
        rot = int(input("What do you want to rotate by?\n"))
        print(caesar(text,rot))
    
if __name__ == '__main__': 
    main()


        
            
        
    

