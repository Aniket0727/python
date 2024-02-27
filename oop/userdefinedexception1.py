class IncorrectPassword(Exception):
    def __init__(self):
        self.error="Incorrect Password"

actual_password='Abc123'
password=input('Enter Password: ')
try:
    if password !=actual_password:
        raise IncorrectPassword
    else:
        print("You have entered correct password")
except IncorrectPassword as e:
    print(e.error)
