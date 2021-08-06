def is_phone_number(text):
    if len(text) != 12:
        return False
    for i in range(3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True


message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'



test2='''Select a phone number
Refresh the list of numbers
enter the desired phone number

+1437-886-1147

+1437-886-1863

+1437-8862-942

+1437-370-1889

+1437-370-1729

+1437-886-1347

+1437-886-1274

+1437-886-1645

+1437-886-1543

+1437-886-3164

+1437-886-2401

+1437-886-1390
Connection fee
....
$0
Monthly fee for the number in Toronto
....
$2
All rates are shown in USD, including taxes

Note: The option to receive SMS messages can be activated on phone numbers purchased for the minimum of 3 months.

Activation happens after the verification of the details you entered.

Why do you need the phone number in Toronto?
The phone number will allow you to open a virtual office in Toronto in 5 minutes. Clients and partners will call their local landline phone number, while you can receive their calls anywhere in the world with a reliable internet connection.
Select any type of connection:
PBX, call forwarding, or using the internet
Advantages of Zadarma virtual phone numbers in Toronto:
free cloud PBX
call forwarding to another phone number or SIP server
3 or more incoming channels (multichannel number)
free incoming calls
ability to receive SMS for free
trustworthy network operator with 1.5 million clients and 13 years of experience'''


for i in range(len(test2)):
    chunk = test2[i:i+12]
    if is_phone_number(chunk):
        print('Phone number found: ' + chunk)
print('Done')

