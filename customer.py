#customer page function
from bill import *
def customer_page():
    with open("customer_list.txt") as f:
        content=f.read()
        print(f"{content}\n")
        print('''Choose the serial number or the name of the laptop you want to purchase\n
*Press 0 to exit program''')
        selection=input("-->")
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
        if selection=="0":
            print("Thank You for choosing us!!")
            exit()
        elif selection=="1" or selection.lower()[0]=="b":
            print("How many of the Razer Blade do you want to purchase?\n")
            item=int(input("-->"))
            if item<0:
                print("Enter a valid number")
            else:    
                for laptop in laptops:
                    if laptop['name']=="Blade":
                        laptop['stock'] -=item
                        if laptop['stock']<0:
                            return True
                            
                        else:
                            billing(selection,item)    
                            break
            with open('admin_list.txt', 'w') as f:
                for laptop in laptops:
                    f.write(f"{laptop['stock']}, {laptop['name']}, {laptop['brand']}, ${laptop['price']}, {laptop['processor']}, {laptop['graphics']}\n")
                    
                    

        elif selection=="2" or selection.lower()[0]=="x":
            print("How many of the XPS do you want to purchase?\n")
            item=int(input("-->"))
            if item<0:
                print("Enter a valid number")
            else:    
                for laptop in laptops:
                    if laptop['name']=="XPS":
                        laptop['stock'] -= item
                        if laptop['stock']<0:
                            return True
                        else:
                            billing(selection,item)    
                            break
            with open('admin_list.txt', 'w') as f:
                for laptop in laptops:
                    f.write(f"{laptop['stock']}, {laptop['name']}, {laptop['brand']}, ${laptop['price']}, {laptop['processor']}, {laptop['graphics']}\n")
                    
                    

        elif selection=="3" or selection.lower()[0]=="s":
            print("How many of the Swift 7 do you want to purchase?\n")
            item=int(input("-->"))
            if item<0:
                print("Enter a valid number")
            else:    
                for laptop in laptops:
                    if laptop['name']=="Swift 7":
                        laptop['stock'] -=item
                    if laptop['stock']<0:
                       return True
                    else:
                        billing(selection,item)    
                        break
            with open('admin_list.txt', 'w') as f:
                for laptop in laptops:
                    f.write(f"{laptop['stock']}, {laptop['name']}, {laptop['brand']}, ${laptop['price']}, {laptop['processor']}, {laptop['graphics']}\n")
                    
                    

        elif selection=="4" or selection.lower()[0]=="m":
            print("How many of the Macbook Pro 16 do you want to purchase?\n")
            item=int(input("-->"))
            
            for laptop in laptops:
                if laptop['name']=="Macbook Pro 16":
                    laptop['stock'] -=item
                    if laptop['stock']<0:
                        return True
                    else:
                        billing(selection,item)     
                        break
            with open('admin_list.txt', 'w') as f:
                for laptop in laptops:
                    f.write(f"{laptop['stock']}, {laptop['name']}, {laptop['brand']}, ${laptop['price']}, {laptop['processor']}, {laptop['graphics']}\n")
                    
                    
        
        elif selection=="5" or selection.lower()[0]=="h":
            print("How many of the Helios 300 do you want to purchase?\n")
            item=int(input("-->"))
            for laptop in laptops:
                if laptop['name']=="Helios 300":
                    laptop['stock'] -=item
                    if laptop['stock']<0:
                        return True
                    else:
                        billing(selection,item)     
                        break
            with open('admin_list.txt', 'w') as f:
                for laptop in laptops:
                    f.write(f"{laptop['stock']}, {laptop['name']}, {laptop['brand']}, ${laptop['price']}, {laptop['processor']}, {laptop['graphics']}\n")
                    billing(selection,item)
                    
        elif selection=="6" or selection.lower()[0]=="l":
            print("How many of the Legion 5 PRO do you want to purchase?\n")
            item=int(input("-->"))
            for laptop in laptops:
                if laptop['name']=="Legion 5 PRO":
                    laptop['stock'] -=item
                    if laptop['stock']<0:
                        return True
                    else:
                        billing(selection,item)     
                        break
            with open('admin_list.txt', 'w') as f:
                for laptop in laptops:
                    f.write(f"{laptop['stock']}, {laptop['name']}, {laptop['brand']}, ${laptop['price']}, {laptop['processor']}, {laptop['graphics']}\n")
        
        elif selection=="7" or selection.lower()[0]=="t":
            print("How many of the TUF Dash F15 do you want to purchase?\n")
            item=int(input("-->"))
            for laptop in laptops:
                if laptop['name']=="TUF Dash F15":
                    laptop['stock'] -=item
                    if laptop['stock']<0:
                        return True
                    else:
                        billing(selection,item)     
                        break
            with open('admin_list.txt', 'w') as f:
                for laptop in laptops:
                    f.write(f"{laptop['stock']}, {laptop['name']}, {laptop['brand']}, ${laptop['price']}, {laptop['processor']}, {laptop['graphics']}\n")
        
        elif selection=="8" or selection.lower()[0]=="g":
            print("How many of the GP76 Leopard do you want to purchase?\n")
            item=int(input("-->"))
            for laptop in laptops:
                if laptop['name']=="GP76 Leopard":
                    laptop['stock'] -=item
                    if laptop['stock']<0:
                        return True
                    else:
                        billing(selection,item)     
                        break
            with open('admin_list.txt', 'w') as f :
                for laptop in laptops:
                    f.write(f"{laptop['stock']}, {laptop['name']}, {laptop['brand']}, ${laptop['price']}, {laptop['processor']}, {laptop['graphics']}\n")
        
        elif selection=="9" or selection.lower()[0]=="a":
            print("How many of the Alienware M15 do you want to purchase?\n")
            item=int(input("-->"))
            for laptop in laptops:
                if laptop['name']=="Alienware M15":
                    laptop['stock'] -=item
                    if laptop['stock']<0:
                        return True
                    else:
                        billing(selection,item)     
                        break
            with open('admin_list.txt', 'w') as f:
                for laptop in laptops:
                    f.write(f"{laptop['stock']}, {laptop['name']}, {laptop['brand']}, ${laptop['price']}, {laptop['processor']}, {laptop['graphics']}\n")
                    
        elif selection=="10" or selection.lower()[0]=="n":
            print("How many of the Nitro 5 do you want to purchase?\n")
            item=int(input("-->"))
            for laptop in laptops:
                if laptop['name']=="Nitro 5":
                    laptop['stock'] -=item
                    if laptop['stock']<0:
                        return True
                    else:
                        billing(selection,item)     
                        break
            with open('admin_list.txt', 'w') as f:
                for laptop in laptops:
                    f.write(f"{laptop['stock']}, {laptop['name']}, {laptop['brand']}, ${laptop['price']}, {laptop['processor']}, {laptop['graphics']}\n")
        
        elif selection=="11" or selection.lower()[0]=="v":
            print("How many of the Victus 16 do you want to purchase?\n")
            item=int(input("-->"))
            for laptop in laptops:
                if laptop['name']=="Victus 16":
                    laptop['stock'] -=item
                    if laptop['stock']<0:
                        return True
                    else:
                        billing(selection,item)     
                        break
            with open('admin_list.txt', 'w') as f:
                for laptop in laptops:
                    f.write(f"{laptop['stock']}, {laptop['name']}, {laptop['brand']}, ${laptop['price']}, {laptop['processor']}, {laptop['graphics']}\n")
        
        elif selection=="12" or selection.lower()[0]=="d":
            print("How many of the Dell G3 do you want to purchase?\n")
            item=int(input("-->"))
            for laptop in laptops:
                if laptop['name']=="Dell G3":
                    laptop['stock'] -=item
                    if laptop['stock']<0:
                        return True
                    else:
                        billing(selection,item)     
                        break
            with open('admin_list.txt', 'w') as f:
                for laptop in laptops:
                    f.write(f"{laptop['stock']}, {laptop['name']}, {laptop['brand']}, ${laptop['price']}, {laptop['processor']}, {laptop['graphics']}\n")
        
        elif selection=="13" or selection.lower()[0]=="r":
            print("How many of the ASUS ROG do you want to purchase?\n")
            item=int(input("-->"))
            for laptop in laptops:
                if laptop['name']=="ROG":
                    laptop['stock'] -=item
                    if laptop['stock']<0:
                        return True
                    else:
                        billing(selection,item)     
                        break
            with open('admin_list.txt', 'w') as f:
                for laptop in laptops:
                    f.write(f"{laptop['stock']}, {laptop['name']}, {laptop['brand']}, ${laptop['price']}, {laptop['processor']}, {laptop['graphics']}\n")
        
        elif selection=="14" or selection.lower()[0]=="p":
            print("How many of the MSI Pulse do you want to purchase?\n")
            item=int(input("-->"))
            for laptop in laptops:
                if laptop['name']=="Pulse":
                    laptop['stock'] -=item
                    if laptop['stock']<0:
                        return True
                    else:
                        billing(selection,item)     
                        break
            with open('admin_list.txt', 'w') as f:
                for laptop in laptops:
                    f.write(f"{laptop['stock']}, {laptop['name']}, {laptop['brand']}, ${laptop['price']}, {laptop['processor']}, {laptop['graphics']}\n")
                    
                    