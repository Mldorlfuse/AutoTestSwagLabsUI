class CorrectLoginData:
    username ='standard_user'
    password = 'secret_sauce'

class LockedLoginData:
    username = 'locked_out_user'
    password = 'secret_sauce'
    error_message = 'Epic sadface: Sorry, this user has been locked out.'

class WrongLoginData:
    username = 'lorem'
    password = 'lorem'
    error_message = 'Epic sadface: Username and password do not match any user in this service'

class WithoutLoginData:
    username = ''
    password = 'lorem'
    error_message = 'Epic sadface: Username is required'

class WithoutPasswordData:
    username = 'lorem'
    password = ''
    error_message = 'Epic sadface: Password is required'