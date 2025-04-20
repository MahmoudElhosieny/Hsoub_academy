import re
email = 'user_name236@gmail.com'

exp = r'^[^@]+@[^@]+\.[^@]+$'   # I got it from stack overflow
new_exp = r'^[^@]+(@)(\w+)(\.)(\w+)$'  # mixture between main and stack overflow
exp2 = r'^(\w+)(\d?)(@)(\w+)(\.)(\w+)$' # this is main


def email_checker(new_exp):
    email_check = re.findall(f'{new_exp}', email)
    if email_check:
        print(f'This email: {email}, Is valid email.')
    else:
        print(f'This email: {email}, Is not valid email.')
print('##### Email check #####')
email_checker(new_exp)

##################################################################33
visa_number = '5111 2225 3332 8594'

visa_exp = r'^(\d{4})(\s)(\d{4})(\s)(\d{4})(\s)(\d{4})$'


def visa_checker(visa_exp):
    visa_check = re.findall(f'{visa_exp}', visa_number)
    if visa_check:
        print(f'This is a valid Card number: {visa_number}')
    else:
        print(f'This is not valid Card number: {visa_number}')
print('##### Visa card number check #####')
visa_checker(visa_number)
###############################################################################3

pass_word= r'#Ahnhjj25'

password_exp = r'^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$'
password_exp02= r'[A-Za-z0-9@#$%^&+=]{8,}'




print('##### Password check #####')
def password_checker(password_exp02):
    password_check = re.findall(f'{password_exp}', pass_word)
    if password_check:
        print(f'This is a valid password.')
    else:
        print('This is Not valid password.')


password_checker(pass_word)