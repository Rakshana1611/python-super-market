print("SEKAR SUPER MARKET")
print("welcome sir/mam")
def main():
  try:
    press=int(input("press 1 to continue or else press 2 to view the total or else press 0:"))
    if press==1:
      import re
      f=open("grocery.txt","r")
      grocery=f.read()
      your_order=str(input("enter ur order:"))
      x=re.search(your_order,grocery)
      print(x)
      if your_order=="household items":
        import super_market
        super_market.household_items()
      elif your_order=="dhal items":
        import super_market
        super_market.dhal_items()
      elif your_order=="fresh products":
        import super_market
        super_market.fresh_products()
      elif your_order=="mens wears":
        import super_market
        super_market.mens_wears()
      elif your_order=="women wears":
        import super_market
        super_market.women_wears()
    elif press==2:
      cost1=int(input("enter the 1st purchase total or else enter the amount 0:"))
      cost2=int(input("enter the 2nd purchase total or else enter the amount 0:"))
      cost3=int(input("enter the 1st purchase total or else enter the amount 0:"))
      cost4=int(input("enter the 1st purchase total or else enter the amount 0:"))
      cost5=int(input("enter the 1st purchase total or else enter the amount 0:"))
      cost6=int(input("enter the 1st purchase total or else enter the amount 0:"))
      cost7=int(input("enter the 1st purchase total or else enter the amount 0:"))
      total_purchase=cost1+cost2+cost3+cost4+cost5+cost6+cost7
      print(f"the total amount is {total_purchase}")
      import smtplib
      def email_sending():
        try:
          receiver_mails=["kmugil0507@gmail.com"]
          for i in receiver_mails:
            total_purchase=cost1+cost2+cost3+cost4+cost5+cost6+cost7
            print(i,total_purchase)
            s=smtplib.SMTP('smtp.gmail.com',587)
            s.starttls()
            s.login("rakshana0211@gmail.com","tzvh pljg nfbu yunn")
            message=f"your purchase amount in sekar super market is {total_purchase}"
            s.sendmail("rakshana0211@gmail.com", i, message)
            s.quit()
            print("mail sent successfully")
        except:
          print("mail not sending")
      email_sending()
    else:
      print("thank u for visiting")
  except:
    print("pls enter valid type only")
main()







