#match function

def planet(id):
    name = ''
    
    match 'kartoshka':
        case 1 :  # თუ id  გაუტოლდა  1-ს , name-ს მიენიჭება ცვლადი 'mercury' 
            name= 'Mercury' 
        case 2 :
            name = 'Venera'
        case 'kartoshka': #თუ id გაუტოლდება 'kartoshkas', name გახდეს 'marwyvi'-ს ტოლი 
            name = 'marwyvi'
    print(name)
    
print(planet('kartoshka'))

#goa
name = input("enter your name :")
def planets(name):
    match name:
        case "goa":
            print("shexvedi administracis eqauntze")


print(name)