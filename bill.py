from datetime import datetime
def end_page():
    print('''\nThank You for choosing our Laptop Shop!!!

Your bill has already been sent to you in a text file''')

def billing(selection,item):
    price=0
    email=input("\nPlease enter your email: \n")
    address=input("\nPlease enter your address: \n")
    while True:
        try:
            phone=int(input("\nPlease enter your phone number: \n"))
            break
        except ValueError:
            print("\nPlease enter a valid number\n")
            continue

    name=input("\nPlease enter your name: \n")
    
    if selection=="1" or selection.lower()[0]=='b':
        time=datetime.now()
        price=item*2000
        with open(f"Bill_of_{name}","w") as f:
            f.write(f'''---------------------------
-------------------------|
     | LAPTOP Ghar | 
      
  |Hunt the best laptops|

      |9812345670|
   
Purhased by | {name} |

Purchased at | {time} |
 
Contact info | {phone} |

Email Address | {email} | 

Address | {address} |

Price of Razer Blade | $2000 |

Brand Name | Razer |

Price without VAT | ${price} |

Price with VAT | ${((13/100)*price)+price} |
----------------------------------------
----------------------------------------
 ''')
            end_page() 

        
    elif selection=="2" or selection.lower()[0]=='x':
        time=datetime.now()
        price=item*1975
        with open(f"Bill_of_{name}","w") as f:
            f.write(f'''---------------------------
-------------------------|
     | LAPTOP Ghar | 
      
  |Hunt the best laptops|

      |9812345670|
   
Purhased by | {name} |

Purchased at | {time} |
 
Contact info | {phone} |

Email Address | {email} | 

Address | {address} |

Price of XPS | $1975 |

Brand Name | Dell |

Price without VAT | ${price} |

Price with VAT | ${((13/100)*price)+price} |
----------------------------------------
----------------------------------------
 ''')
            end_page() 
    
    elif selection=="3" or selection.lower()[0]=='s':
        time=datetime.now()
        price=item*900
        with open(f"Bill_of_{name}","w") as f:
            f.write(f''''---------------------------
-------------------------|
     | LAPTOP Ghar | 
      
  |Hunt the best laptops|

      |9812345670|
   
Purhased by | {name} |

Purchased at | {time} |
 
Contact info | {phone} |

Email Address | {email} | 

Address | {address} |

Price of Swift 7 | $900 |

Brand Name | Dell |

Price without VAT | ${price} |

Price with VAT | ${((13/100)*price)+price} |
----------------------------------------
----------------------------------------
 ''')
            end_page()

    elif selection=="4" or selection.lower()[0]=='m':
        time=datetime.now()
        price=item*900
        with open(f"Bill_of_{name}","w") as f:
            f.write(f'''---------------------------
-------------------------|
     | LAPTOP Ghar | 
      
  |Hunt the best laptops|

      |9812345670|
   
Purhased by | {name} |

Purchased at | {time} |
 
Contact info | {phone} |

Email Address | {email} | 

Address | {address} |

Price of Macbook Pro 16 | $3500 |

Brand Name | Apple |

Price without VAT | ${price} |

Price with VAT | ${((13/100)*price)+price} |
----------------------------------------
----------------------------------------
 ''')
            end_page()

    elif selection=="5" or selection.lower()[0]=='h':
        time=datetime.now()
        price=item*900
        with open(f"Bill_of_{name}","w") as f:
            f.write(f'''---------------------------
-------------------------|
     | LAPTOP Ghar | 
      
  |Hunt the best laptops|

      |9812345670|
   
Purhased by | {name} |

Purchased at | {time} |
 
Contact info | {phone} |

Email Address | {email} | 

Address | {address} |

Price of Helios 300 | $1200 |

Brand Name | Acer |

Price without VAT | ${price} |

Price with VAT | ${((13/100)*price)+price} |
----------------------------------------
----------------------------------------
 ''')
            end_page()        

            
    elif selection=="6" or selection.lower()[0]=='l':
        time=datetime.now()
        price=item*1200
        with open(f"Bill_of_{name}","w") as f:
            f.write(f'''---------------------------
-------------------------|
     | LAPTOP Ghar | 
      
  |Hunt the best laptops|

      |9812345670|
   
Purhased by | {name} |

Purchased at | {time} |
 
Contact info | {phone} |

Email Address | {email} | 

Address | {address} |

Price of Legion 5 Pro | $1269 |

Brand Name | Lenovo |

Price without VAT | ${price} |

Price with VAT | ${((13/100)*price)+price} |
----------------------------------------
----------------------------------------
 ''')
            end_page() 
            
    elif selection=="7" or selection.lower()[0]=='t':
        time=datetime.now()
        price=item*1200
        with open(f"Bill_of_{name}","w") as f:
            f.write(f'''---------------------------
-------------------------|
     | LAPTOP Ghar | 
      
  |Hunt the best laptops|

      |9812345670|
   
Purhased by | {name} |

Purchased at | {time} |
 
Contact info | {phone} |

Email Address | {email} | 

Address | {address} |

Price of TUF Dash F15 | $999 |

Brand Name | Asus |

Price without VAT | ${price} |

Price with VAT | ${((13/100)*price)+price} |
----------------------------------------
----------------------------------------
 ''')
            end_page() 
            
    elif selection=="8" or selection.lower()[0]=='g':
        time=datetime.now()
        price=item*1200
        with open(f"Bill_of_{name}","w") as f:
            f.write(f'''---------------------------
-------------------------|
     | LAPTOP Ghar | 
      
  |Hunt the best laptops|

      |9812345670|
   
Purhased by | {name} |

Purchased at | {time} |
 
Contact info | {phone} |

Email Address | {email} | 

Address | {address} |

Price of GP76 Leopard | $1699 |

Brand Name | MSI |

Price without VAT | ${price} |

Price with VAT | ${((13/100)*price)+price} |
----------------------------------------
----------------------------------------
 ''')
            end_page() 
            
    elif selection=="9" or selection.lower()[0]=='a':
        time=datetime.now()
        price=item*1200
        with open(f"Bill_of_{name}","w") as f:
            f.write(f'''---------------------------
-------------------------|
     | LAPTOP Ghar | 
      
  |Hunt the best laptops|

      |9812345670|
   
Purhased by | {name} |

Purchased at | {time} |
 
Contact info | {phone} |

Email Address | {email} | 

Address | {address} |

Price of Alienware M15 | $2400 |

Brand Name | Alienware |

Price without VAT | ${price} |

Price with VAT | ${((13/100)*price)+price} |
----------------------------------------
----------------------------------------
 ''')
            end_page() 
            
    elif selection=="10" or selection.lower()[0]=='n':
        time=datetime.now()
        price=item*1200
        with open(f"Bill_of_{name}","w") as f:
            f.write(f'''---------------------------
-------------------------|
     | LAPTOP Ghar | 
      
  |Hunt the best laptops|

      |9812345670|
   
Purhased by | {name} |

Purchased at | {time} |
 
Contact info | {phone} |

Email Address | {email} | 

Address | {address} |

Price of Nitro 5 | $799 |

Brand Name | Acer |

Price without VAT | ${price} |

Price with VAT | ${((13/100)*price)+price} |
----------------------------------------
----------------------------------------
 ''')
            end_page() 
            
    elif selection=="11" or selection.lower()[0]=='v':
        time=datetime.now()
        price=item*1200
        with open(f"Bill_of_{name}","w") as f:
            f.write(f'''---------------------------
-------------------------|
     | LAPTOP Ghar | 
      
  |Hunt the best laptops|

      |9812345670|
   
Purhased by | {name} |

Purchased at | {time} |
 
Contact info | {phone} |

Email Address | {email} | 

Address | {address} |

Price of Victus 16 | $1370 |

Brand Name | HP |

Price without VAT | ${price} |

Price with VAT | ${((13/100)*price)+price} |
----------------------------------------
----------------------------------------
 ''')
            end_page() 
            
    elif selection=="12" or selection.lower()[0]=='d':
        time=datetime.now()
        price=item*1200
        with open(f"Bill_of_{name}","w") as f:
            f.write(f'''---------------------------
-------------------------|
     | LAPTOP Ghar | 
      
  |Hunt the best laptops|

      |9812345670|
   
Purhased by | {name} |

Purchased at | {time} |
 
Contact info | {phone} |

Email Address | {email} | 

Address | {address} |

Price of Dell G3 | $1345 |

Brand Name | DELL |

Price without VAT | ${price} |

Price with VAT | ${((13/100)*price)+price} |
----------------------------------------
----------------------------------------
 ''')
            end_page() 
            
    elif selection=="13" or selection.lower()[0]=='r':
        time=datetime.now()
        price=item*1200
        with open(f"Bill_of_{name}","w") as f:
            f.write(f'''---------------------------
-------------------------|
     | LAPTOP Ghar | 
      
  |Hunt the best laptops|

      |9812345670|
   
Purhased by | {name} |

Purchased at | {time} |
 
Contact info | {phone} |

Email Address | {email} | 

Address | {address} |

Price of ASUS ROG | $1349 |

Brand Name | Asus |

Price without VAT | ${price} |

Price with VAT | ${((13/100)*price)+price} |
----------------------------------------
----------------------------------------
 ''')
            end_page()
            
    elif selection=="14" or selection.lower()[0]=='p':
        time=datetime.now()
        price=item*1200
        with open(f"Bill_of_{name}","w") as f:
            f.write(f'''---------------------------
-------------------------|
     | LAPTOP Ghar | 
      
  |Hunt the best laptops|

      |9812345670|
   
Purhased by | {name} |

Purchased at | {time} |
 
Contact info | {phone} |

Email Address | {email} | 

Address | {address} |

Price of Pulse | $1240 |

Brand Name | MSI |

Price without VAT | ${price} |

Price with VAT | ${((13/100)*price)+price} |
----------------------------------------
----------------------------------------
 ''')
            end_page() 
            