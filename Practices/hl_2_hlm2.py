"""This code will use input the clipboard as a string.
    It splits the input based on the new line character '\n'.
    function "hlm" will take an email in the form of a string and it will
    look for the '@' and will add 'm' before it.
    Then in a foor loop we'll use the hlm function to modify all of our emails"""

import pyperclip,sys

raw_emails = pyperclip.paste() #raw_emails is <str>

list_of_emails = raw_emails.split('\r') #creating a list of emails based on new line character
     
def hlm(email):
	email_list = list(email)
	indext = email_list.index('@')
	email_list.insert(indext,'m')
	return ''.join(email_list)


new_raw_emails=''    
for i in range(len(list_of_emails)):
    single_email = list_of_emails[i]
    new_raw_emails += hlm(single_email)

pyperclip.copy(new_raw_emails)

