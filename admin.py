#admin page function
def admin_page():
        print("\nPlease choose the suitable option(1 or 2)")
        print('''1.) Look at the availibility of the stock
2.) Contact the manufacturers\n
*Press 0 to exit the program''')
        laptops=[]     
        with open('admin_list.txt', 'r') as f:
            for line in f:
                parts = line.strip().split(', ')
                stock = int(parts[0])
                name = parts[1]
                brand = parts[2]
                price = float(parts[3].replace('$', ''))
                processor = parts[4]
                graphics = parts[5]
                laptops.append({'stock': stock, 'name': name, 'brand': brand, 'price': price, 'processor': processor, 'graphics': graphics})
        option=int(input("--->"))

        if option==0:
            return True
        
        elif option==1 and option!=0:
            with open("admin_list.txt") as f:
                admin_content=f.read()
                print(admin_content)
                print("\nHere is the list you requested for\n")
                return True
     
        elif option==2 and option!=0:
            print("Choose the name of the laptop you want to order from the manufacturer\n")
            with open("customer_list.txt") as f:
                 data=f.read()
                 print(data)
                 print("*Press 0 to exit the program")         
            order=input("-->")
            if order=="0":
                return True
            elif order=="1" or order.lower()[0]=="b":
                print("How many of the Razer Blade do you want to order?\n")
                number=int(input("-->"))
                for laptop in laptops:
                    if laptop['name']=="Blade":
                        laptop['stock'] += number
                        break
                with open('admin_list.txt', 'w') as f:
                    for laptop in laptops:
                        f.write(f"{laptop['stock']}, {laptop['name']}, {laptop['brand']}, ${laptop['price']}, {laptop['processor']}, {laptop['graphics']}\n") # Harek 5 ota huncha
                        
        

            elif order=="2" or order.lower()[0]=="x":
                print("How many of the XPS do you want to order?\n")
                number=int(input("-->"))
                for laptop in laptops:
                    if laptop['name']=="XPS":
                        laptop['stock'] += number
                        break
                with open('admin_list.txt', 'w') as f:
                    for laptop in laptops:
                        f.write(f"{laptop['stock']}, {laptop['name']}, {laptop['brand']}, ${laptop['price']}, {laptop['processor']}, {laptop['graphics']}\n")
                        

            elif order=="3" or order.lower()[0]=="s":
                print("How many of the Swift 7 do you want to order?\n")
                number=int(input("-->"))
                for laptop in laptops:
                    if laptop['name']=="Swift 7":
                        laptop['stock'] += number
                        break
                with open('admin_list.txt', 'w') as f:
                    for laptop in laptops:
                        f.write(f"{laptop['stock']}, {laptop['name']}, {laptop['brand']}, ${laptop['price']}, {laptop['processor']}, {laptop['graphics']}\n")
                        

            elif order=="4" or order.lower()[0]=="m":
                print("How many of the Macbook Pro 16 do you want to order?\n")
                number=int(input("-->"))
                for laptop in laptops:
                    if laptop['name']=="Macbook Pro 16":
                        laptop['stock'] += number
                        break
                with open('admin_list.txt', 'w') as f:
                    for laptop in laptops:
                        f.write(f"{laptop['stock']}, {laptop['name']}, {laptop['brand']}, ${laptop['price']}, {laptop['processor']}, {laptop['graphics']}\n")
                        
            
            elif order=="5" or order.lower()[0]=="h":
                print("How many of the Helios 300 do you want to order?\n")
                number=int(input("-->"))
                for laptop in laptops:
                    if laptop['name']=="Helios 300":
                        laptop['stock'] += number
                        break
                with open('admin_list.txt', 'w') as f:
                    for laptop in laptops:
                        f.write(f"{laptop['stock']}, {laptop['name']}, {laptop['brand']}, ${laptop['price']}, {laptop['processor']}, {laptop['graphics']}\n")
                        
            elif order=="6" or order.lower()[0]=="l":
                print("How many of the Legion 5 pro do you want to order?\n")
                number=int(input("-->"))
                for laptop in laptops:
                    if laptop['name']=="Legion 5 pro":
                        laptop['stock'] += number
                        break
                with open('admin_list.txt', 'w') as f:
                    for laptop in laptops:
                        f.write(f"{laptop['stock']}, {laptop['name']}, {laptop['brand']}, ${laptop['price']}, {laptop['processor']}, {laptop['graphics']}\n") 
                        
            elif order=="7" or order.lower()[0]=="t":
                print("How many of the Asus TUF DASH F15 do you want to order?\n")
                number=int(input("-->"))
                for laptop in laptops:
                    if laptop['name']=="TUF DASH":
                        laptop['stock'] += number
                        break
                with open('admin_list.txt', 'w') as f:
                    for laptop in laptops:
                        f.write(f"{laptop['stock']}, {laptop['name']}, {laptop['brand']}, ${laptop['price']}, {laptop['processor']}, {laptop['graphics']}\n")   
            
            elif order=="8" or order.lower()[0]=="g":
                print("How many of the MSI GP76 Leopard do you want to order?\n")
                number=int(input("-->"))
                for laptop in laptops:
                    if laptop['name']=="GP76 Leopard":
                        laptop['stock'] += number
                        break
                with open('admin_list.txt', 'w') as f:
                    for laptop in laptops:
                        f.write(f"{laptop['stock']}, {laptop['name']}, {laptop['brand']}, ${laptop['price']}, {laptop['processor']}, {laptop['graphics']}\n")
            
            elif order=="9" or order.lower()[0]=="a":
                print("How many of the Alienware M15 do you want to order?\n")
                number=int(input("-->"))
                for laptop in laptops:
                    if laptop['name']=="Alienware M15":
                        laptop['stock'] += number
                        break
                with open('admin_list.txt', 'w') as f:
                    for laptop in laptops:
                        f.write(f"{laptop['stock']}, {laptop['name']}, {laptop['brand']}, ${laptop['price']}, {laptop['processor']}, {laptop['graphics']}\n")
            
            elif order=="10" or order.lower()[0]=="n":
                print("How many of the Nitro 5 do you want to order?\n")
                number=int(input("-->"))
                for laptop in laptops:
                    if laptop['name']=="Nitro 5":
                        laptop['stock'] += number
                        break
                with open('admin_list.txt', 'w') as f:
                    for laptop in laptops:
                        f.write(f"{laptop['stock']}, {laptop['name']}, {laptop['brand']}, ${laptop['price']}, {laptop['processor']}, {laptop['graphics']}\n")
            
            elif order=="11" or order.lower()[0]=="v":
                print("How many of the HP Victus 16 do you want to order?\n")
                number=int(input("-->"))
                for laptop in laptops:
                    if laptop['name']=="Victus 16":
                        laptop['stock'] += number
                        break
                with open('admin_list.txt', 'w') as f:
                    for laptop in laptops:
                        f.write(f"{laptop['stock']}, {laptop['name']}, {laptop['brand']}, ${laptop['price']}, {laptop['processor']}, {laptop['graphics']}\n")
            
            elif order=="12" or order.lower()[0]=="d":
                print("How many of the Dell G3 do you want to order?\n")
                number=int(input("-->"))
                for laptop in laptops:
                    if laptop['name']=="Dell G3":
                        laptop['stock'] += number
                        break
                with open('admin_list.txt', 'w') as f:
                    for laptop in laptops:
                        f.write(f"{laptop['stock']}, {laptop['name']}, {laptop['brand']}, ${laptop['price']}, {laptop['processor']}, {laptop['graphics']}\n")
                        
            elif order=="13" or order.lower()[0]=="r":
                print("How many of the  ASUS ROG do you want to order?\n")
                number=int(input("-->"))
                for laptop in laptops:
                    if laptop['name']=="ROG":
                        laptop['stock'] += number
                        break
                with open('admin_list.txt', 'w') as f:
                    for laptop in laptops:
                        f.write(f"{laptop['stock']}, {laptop['name']}, {laptop['brand']}, ${laptop['price']}, {laptop['processor']}, {laptop['graphics']}\n")
            
            elif order=="14" or order.lower()[0]=="p":
                print("How many of the MSI Pulse do you want to order?\n")
                number=int(input("-->"))
                for laptop in laptops:
                    if laptop['name']=="Pulse":
                        laptop['stock'] += number
                        break
                with open('admin_list.txt', 'w') as f:
                    for laptop in laptops:
                        f.write(f"{laptop['stock']}, {laptop['name']}, {laptop['brand']}, ${laptop['price']}, {laptop['processor']}, {laptop['graphics']}\n")
            
            