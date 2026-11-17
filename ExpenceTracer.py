# expence trackers : 

expencelist = [] # list of expences in form of dictionary 
print("\n Expences Trackers ")

def addItem(): # ADD ITEM 
    date = input("enter the date of the expences  : ")
    categories = input("categories of the expences (food ,  cosmatics , clothes  ) : ")
    discription = input("writing a brieff discription about what you bought : ")
    amount = float(input("enter the amount : "))

    expences = {
        "date":date,
        "categories":categories,
        "discription": discription,
        "amount":amount
    }
    expencelist.append(expences)
    print("\n expences is add sucessfully !")

def ViewAllExpences(): # VIEW EXPENCES 
    if len(expencelist) == 0:
        print("NO Iteam found in the expencesList ")
    else:
        count = 1
        for items in expencelist:
            print("\n expences number:",count)
            print(f"date : {items['date']}")
            print(f"categories : {items['categories']}")
            print(f"discription : {items['discription']}")
            print(f"amount : {items['amount']}")
           
            count+=1
        


def totalAmount(): # TOATLA AMOUNT 
    total = 0
    for items in expencelist:
        total = total + items["amount"]
    print("\n totla spending : " , total )

         




while True:
    print("===== MENU =====")
    print("1. ADD ITEAM : ")
    print("2 . VIEW ITEAM : ")
    print("3. TOTAL AMOUNT : ")
    print("4.EXIT ")

    choice = input("enter the choice (1-4) : ")

    if choice == "1":
        addItem()
    elif choice == "2":
        ViewAllExpences()
    elif choice == "3":
        totalAmount()
    elif choice == "4":
        print("THANK YOU FOR USING OUR EXPENCE TRACKER ")
        break

    else:
        print("invalid option ! ")
    
