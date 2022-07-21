
def password_check(passwd):
      
    SpecialSym =['$', '@', '#', '%','&','*','/','+','-','_','=',
                 '!','~','`','[',']','{','}','(',')','<','>','?',':',
                 ';',',','.','|','\\','\'','\"']
    val = True
    err1,err2,err3,err4,err5,err6=["","","","","",""]  
    if len(passwd) < 8:
        err1 = 'length should be at least 8'
        val = False
          
    if len(passwd) > 15:
        err2 = 'length should be not be greater than 15'
        val = False
          
    if not any(char.isdigit() for char in passwd):
        err3 = 'Password should have at least one numeral'
        val = False
          
    if not any(char.isupper() for char in passwd):
        err4 = 'Password should have at least one uppercase letter'
        val = False
          
    if not any(char.islower() for char in passwd):
        err5 = 'Password should have at least one lowercase letter'
        val = False
          
    if not any(char in SpecialSym for char in passwd):
        err6 = 'Password should have at least one of the symbols $@#%&*./+-_=!'
        val = False
    
    if val :
        return []
    else :
        return [err1 ,err2,err3,err4,err5,err6]