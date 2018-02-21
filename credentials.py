# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions
# Author: Edward Jarosiewitz Knapp
# Created: 2018-2-21
def main():
# get user's first and last names
    first = input("Enter your first name (all lowercase): ")
    last = input("Enter your last name (all lowercase): ")
    uname = first + '.' + last
# ask user to create a new password
    passwd = input("Create a new password (must be at least 8 characters): ")
    if len(passwd) < 8:
         print("Fool of a Took! That password is feeble!")  
         passwd = input("Create a new password again: ")
    if len(passwd) > 8:
        print("The force is strong in this one…")
        print("Account configured. Your new email address is",
        uname + "@marist.edu")
main()
