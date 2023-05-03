from customer import *
from admin import *
import stdiomask
def purchase():
    print('''\nAre you an admin?(y/n)
     \n''')
    a=input("Enter your response: \n")
    admin=""
    customer=""
    if a.lower()[0]=='y':
        password=stdiomask.getpass()
        if password=="admin123":
            admin=admin_page()
        else:
            print("\nYou are not authorized to access the content!!\n")
            exit()   
    
    elif a.lower()[0]=='n':
       customer=customer_page()
    else:
        print("\nEnter a valid option!!!")
        exit()
    
    if admin==True:
        print("\nThank You for choosing us!!\n")
    elif customer==True:
        print("\nSorry we currently dont have enough laptops in stock")       

def response():
    print('''\n\t\t\t\t|Welcome to LAPTOP GHAR|\t\t\t\t
\t\t\t\t\t|Lazimpat|\t\t\t\t''')
    print("\t\t\t\t|Hunt the best laptop|\t\t\t\t\t")
    print('''\nDo you want to purchase a laptop?
---> Yes(y)
---> No(n)
     \n''')
    a=input("Enter your response: ")
    if a.lower()[0]=='y':
        purchase()
    elif a.lower()[0]=='n':
        print("Thank you for choosing LAPTOP GHAR! Hope we can help you anytime")
        exit()
    else:
        print("Enter a valid response")
        exit()    

response()

