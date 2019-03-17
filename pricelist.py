pricelist = []
price = ""
while price != "kolar":
   print(""" \n\nThe following things are 
what you can do whith this program.
   	
   	   0 = Exit
   	   1 = Show pricelist
   	   2 = Add price
   	   3 = Delete pricelist
   	   4 = Sort pricelist """)
   choice = input(" \n Choice : ")
   if choice == "0":
      print ("\n ***GOOD BYE***")
   elif choice == "1":
      print ("\n The following is the list of this program \n")
      for item in pricelist:
         print (item)
   elif choice == "2":
      add = int(input("\n Add any price you like sir : "))
      pricelist.append(add)
   elif choice == "3":
      delete = int(input("\n Please Type number you wanna delete : "))
      if delete in pricelist:
         pricelist.remove(delete)
      else:
         print (delete), ("\n not in our pricelist")
   elif choice == "4":
      pricelist.sort()
      
      
   else:
      print ("\n Hello can't you read English \n yout choice is : ")  , 
      "choice"
      
   
   	  
