username = 'Santhosh.kumar@fcpc.edu.ph'
password = 'Helel_013'

userid = input('Enter username: ')
passwd = input("Enter the password: ")

if userid == username :
    if passwd == password :
        print('Welcome! Login Successful.')
    else :
        print('Incorrect password.')
else :
    print('incorrect username.')
