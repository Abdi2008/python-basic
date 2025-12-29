#number1=4
#number2=6
#firstname="Abdirahman "
#surname="Abshir "
#lastname="Husssein"
#print(firstname + surname + lastname)
#print("The Sum of the two are " + str(number1+number2))
#name="John"
#for character in name:
    #print(character)
# for alphabets in range(0,100,2):
#     #print(alphabets)
#     if alphabets == 50:
#         continue
#     print(alphabets)
# title="This is a Python programming language"
# word="python"
# if word in title:
#     print(f"The Word {word} is in '{title}'")
# else:
#     print(f"The Word {word} is not in '{title}'")
def main():

    item_name="banana"
    quantity=5
    discount_rate=0.1
    eligible_items = "Orange banana carrot"
    item_price= 2   #usd
    #arithmetic operators
    subtotal=item_price* quantity
    print(f"The item name {item_name} and the subtotal is {subtotal}")

    discount=0
    #membership Operators
    if item_name in eligible_items:
        discount=subtotal*discount_rate
    else:
        print(f"This item: {item_name} is not eligable for discount")
    print("The discount is : "+ str(discount))
    #Comparison Operators
    was_discount_applied= discount>0
    print(f"Was discount applied? {was_discount_applied}")
    #Logical Operators
    does_free_shipping_apply= quantity> 5 and item_name=="banana"
    print(f"does free shipping apply? {does_free_shipping_apply}")
main()