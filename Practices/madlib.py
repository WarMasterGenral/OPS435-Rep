import os, re

def start():
    #os.chdir('.\\my_codes')
    #print(os.getcwd())
    fileName = input('Enter the file name: ')
    exist_fileName = os.path.abspath(fileName)
    if os.path.exists(exist_fileName) == True:

        text_file = open(exist_fileName)
        text_content = text_file.read()
        text_file.close()
        print(text_content)


        text_regex = re.compile(r'ADJECTIVE|NOUN|VERB|ADVERB')
        match_text = text_regex.findall(text_content)

        for match in match_text:
            user_input = input('Enter ' + match + ': ')
            text_content = text_content.replace(match, user_input, 1)
        print(text_content)

        new_fileName = 'new_' + fileName
        new_file = open(new_fileName, 'w')
        new_file.write(text_content)
        new_file.close()

    else:
        print('The file you have entered does not exist. Please enter a valid file name.')
        start()

start()
