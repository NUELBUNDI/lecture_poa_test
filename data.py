from datetime import datetime


def calculate_age(birth_date,age):
    
    today = datetime.now().date()
    
    current_age  = today - birth_date
    if current_age != age:
        res= 'You are liar'
    
    return res
    

