import datetime
def household_items():
    items=str(input("What items you want to purchase?"))
    menus={"soap":45,"washing powder":35,"bleaching powder":45,"dish wash bar":38,"shampoo":90}
    try:
        if items=="soap" or items=="washing powder" or items=="bleaching powder" or items=="dish wash bar" or items=="shampoo":
            print("yes,your order is available.")
            quantity=int(input("how much quantity you want?"))
            cost=menus[items]*quantity
            print(f"\n{items} is {cost}\n")
            gst_rate=int(input("enter the gst_rate:"))
            gst_amount=cost*gst_rate/100
            total=cost+gst_amount
            f=open("bill.txt","w")
            x=datetime.datetime.now()
            f.write(f"date:{x}\n")
            f=open("bill.txt","a")
            f.write(f"\n{items} is {cost}\n")
            f.write(f"\n{items} with gst amount is {total}\n")
            print(f"\n the total is{total}\n")
            import main
            main.main()
        else:
            print("your order is not available")
            import main
            main.main()
    except:
            print("pls enter valid type only")
def dhal_items():
    dhal={"toor dhal":243,"channa dhal":134,"urad dhal":178,"moong dhal":144}
    try:
        user=str(input("What items you want to purchase?"))
        if user=="toor dhal" or user=="channa dhal" or user=="urad dhal" or user=="moong dhal":
            print("yes,your order is available.")
            quantity=int(input("how much quantity you want?"))
            cost=dhal[user]*quantity
            print(f"\n{user} is {cost}\n")
            gst_rate=int(input("enter the gst_rate:"))
            gst_amount=cost*gst_rate/100
            total=cost+gst_amount
            f=open("bill.txt","w")
            x=datetime.datetime.now()
            f.write(f"date:{x}\n")
            f=open("bill.txt","a")
            f.write(f"\n{user} is {cost}\n")
            f.write(f"\n{user} with gst amount is {total}\n")
            print(f"\n the total is{total}\n")
            import main
            main.main()
        else:
            print("your item is not available")
            main.main()
    except:
            print("pls enter valid type only")
def fresh_products():
    fresh={"apple":200,"tomato":135,"onion":89,"carrot":70,"pineapple":45,"orange":45,"beetroot":42}
    try:
        user=str(input("What items you want to purchase?"))
        if user=="apple" or user=="tomato" or user=="onion" or user=="carrot" or user=="pineapple" or user=="orange" or user=="beetroot":
            print("yes,your order is available.")
            quantity=int(input("how much quantity you want?"))
            cost=fresh[user]*quantity
            print(f"\n{user} is {cost}\n")
            gst_rate=int(input("enter the gst_rate:"))
            gst_amount=cost*gst_rate/100
            total=cost+gst_amount
            f=open("bill.txt","w")
            x=datetime.datetime.now()
            f.write(f"date:{x}\n")
            f=open("bill.txt","a")
            f.write(f"\n{user} is {cost}\n")
            f.write(f"\n{user} with gst amount is {total}\n")
            print(f"\n the total is{total}\n")
            import main
            main.main()
        else:
            print("your item is not available")
            main.main()
    except:
            print("pls enter valid type only")
def mens_wears():
    dress={"shirt":432,"pant":700,"night suits":680,"hoodie":500}
    try:
        items=str(input("what items u want to purchase?"))
        if items=="shirt" or items=="pant" or items=="night suits" or items=="hoodie":
            print("yes,your order is available.")
            quantity=int(input("how much quantity you want?"))
            cost=dress[items]*quantity
            print(f"\n{items} is {cost}\n")
            gst_rate=int(input("enter the gst_rate:"))
            gst_amount=cost*gst_rate/100
            total=cost+gst_amount
            f=open("bill.txt","w")
            x=datetime.datetime.now()
            f.write(f"date:{x}\n")
            f=open("bill.txt","a")
            f.write(f"\n{items} is {cost}\n")
            f.write(f"{items} with gst amount is {total}\n")
            print(f"\n the total is{total}\n")
            import main
            main.main()
        else:
            print("your order is not available")
            main.main()
    except:
        print("pls enter valid type only")
def women_wears():
    dress={"salwar":700,"pant":700,"night suits":680,"sarees":800,"frock":1000,"lehenga":1500}
    try:
        items=str(input("what items u want to purchase?"))
        if items=="salwar" or items=="pant" or items=="night suits" or items=="sarees" or items=="frock" or items=="lehenga":
            print("yes,your order is available.")
            quantity=int(input("how much quantity you want?"))
            cost=dress[items]*quantity
            print(f"\n{items} is {cost}\n")
            gst_rate=int(input("enter the gst_rate:"))
            gst_amount=cost*gst_rate/100
            total=cost+gst_amount
            f=open("bill.txt","w")
            x=datetime.datetime.now()
            f.write(f"date:{x}\n")
            f=open("bill.txt","a")
            f.write(f"\n{items} is {cost}\n")
            f.write(f"{items} with gst amount is {total}\n")
            print(f"\n the total is{total}\n")
            import main
            main.main()
        else:
            print("your order is not available")
            main.main()
    except:
        print("pls enter valid type only")

