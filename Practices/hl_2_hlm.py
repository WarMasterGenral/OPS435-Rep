import pyperclip

raw_emails = pyperclip.paste()
emails_list = raw_emails.split('\r')
#new_raw_emails = []

for i in range(len(emails_list)):
    single_email = emails_list[i] #single_email is now <str>
    single_email_list = list(single_email)
    indext = single_email_list.index('@')
    modified_single_email_list = single_email_list.insert(indext,'m')
    single_email_str = ''.join(single_email_list)

    single_email_str = single_email_str + '\n'
    #new_raw_emails.append(single_email_str)
    print(single_email_str)
    #emails_str =''
    #for i in range(len(emails_list)):
    #emails_str = emails_str + single_email_str
    
