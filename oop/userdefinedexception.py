class TooYoungException(Exception):
    def __init__(self,msg):
        self.msg=msg
class TooOldException(Exception):
    def __init__(self,msg):
        self.msg=msg
        
age=int(input('Enter age:'))

if age>60:
        raise TooOldException('Your age already crossed marriage age, No chance of getting match ')
    
elif age<18:
        raise TooYoungException('Please wait some more time, definitely u will get best match')
else:
        print("You will get match details soon by email !!!")

    
