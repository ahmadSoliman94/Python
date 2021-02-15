#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[5]:


def resturant():
    f=  open("resturant.txt", "w") 
    f.write("Welcome to Paolos's Italian Restaurant!")
    f.write ("\n")
    f.write("\n" "Here is our menu of the day:")
    f.write("\n" "1. Fried Calamari ($30.5)"
            "\n" "2. Caesar Salad    ($26.5)"
            "\n" "3. Chicken Parmigiana ($30.5)"
            "\n" "4. Veal Scaloppine   ($32.5)"
            "\n" "5. Lasagna        ($35.5)"
            "\n" "6. Spaghetti Bolognese ($29.5)"
            "\n" "7. Rigatoni       ($30.5)"
            "\n" "8. Tiramisu       ($21.5)")
    
    
    
    menu = { "1" : "Fried Calamari", 
         "2" : "Caesar Salad",
         "3" : "Chicken Parmigiana",
         "4" : "Veal Scaloppine",
         "5" : "Lasagna",
         "6" : "Spaghetti Bolognese",
         "7" : " Rigatoni",
         "8" : "Tiramisu"}
    
    price = { "1" : "30.5", 
         "2" : "26.5",
         "3" : "30.5",
         "4" : "32.5",
         "5" : "35.5",
         "6" : "29.5",
         "7" : "30.5",
         "8" : "21.5"}
    
    
    order =input(" \n" " What would you like to order? ")
    f.write( "\n" "\n" " What would you like to order? "+ order)
    

    for i in menu:
        if i in order:
            f.write("\n""\n" "A " + menu[i] + " has been added to your order")
            order_summary = menu[i]
    for j in price: 
        if j in order:
            total_1 = float(price[j])
            f.write("\n" "Total: $" + str(total_1))
            
    more_items= input("\n" "\n" "\n" "Would you like to add more items? (y/n) ")
    f.write( "\n" "\n" "Would you like to add more items? " + more_items)
    if more_items == "y":
        
        order =input(" \n" " What would you like to order? ")
        f.write( "\n" "\n" " What would you like to order? "+ order)
        for l in menu:
            if l in order:
                f.write("\n""\n" "A " + menu[l] + " has been added to your order")
                order_summary += ", " + menu[l]
               
        for s in price:
            if s in order:
                total_2 = float(price[s])
                total_3 =  total_1 + total_2
                f.write("\n" "Total: $" + str(total_3))  
                
                
        
                        
                more_items= input("\n" "\n" "\n" "Would you like to add more items? (y/n) ")
                f.write( "\n" "\n" "Would you like to add more items? " + more_items)
                if more_items == "n":
                    pass
            
                f.write("\n" "\n" "*********************************************************************")
                f.write("\n" "your Order Summary: "  +  "{" + order_summary  + "}")
                f.write("\n" "Total Price: $ " + str(total_3))            
                             
                               
        
    elif more_items == "n":
         for i in menu:
                if i in order:
                    order_summary = menu[i]
                    f.write("\n" "\n" "*********************************************************************")
                    f.write("\n" "your Order Summary: "  +  "{" + order_summary  + "}")
                    f.write("\n" "Total Price: $ " + str(total_1))
            
    

resturant()    


# In[ ]:





# In[ ]:


xc

