def validate_password(password):
    #check if characters are at least 8
    if len(password) > 7 and any(char.isupper() for char in password) and any(char.islower() for char in password) and any(char.isdigit() for char in password) and " " not in password:
        return True
    
    else:
        return False
    
print(validate_password("Password1"))