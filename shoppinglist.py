from food import foodNDD

def create_listNDD(): #function 1
    shopping_list=[] #creating empty list
    
    item_quantity = int(input("How many items will you order today? "))
    while item_quantity<1:  #input loop
        print("Number of items must be at least 1.")
        item_quantity = int(input("How many items will you order today? "))
    
    for i in range(item_quantity):
        while True:
            item_name=input("Enter food: ")
            item_amount=eval(input("Enter amount of pounds: ")) 
            item=foodNDD(item_name,item_amount)
            if item_amount<0:
                print("Amount of pounds must be greater than 0.")
                item_amount=eval(input("Enter amount of pounds: ")) #input loop
                item=foodNDD(item_name,item_amount)
            else:
                break
        shopping_list.append(item) #append item with food class to list 
        
    return shopping_list
    
def displayNDD(list_of_items):
    print("Here's a summary of the items purchased: ")
    print("-"*28)
    for i in range(len(list_of_items)):
        print(f"Item #{i+1}")
        print(list_of_items[i].__str__()+"\n") #print all
        
def get_totalNDD(list_of_items):
    total=0
    for i in range(len(list_of_items)):
        total+=list_of_items[i].totalNDD() #calculate total
    return total
    
shopping_list=create_listNDD()
displayNDD(shopping_list)
print(f"Total cost: ${get_totalNDD(shopping_list)}") #call all functions
