# """This script demonstrates the use of Python functions. 
# The create_shoe function takes a list of materials as input and 
# determines the type of shoe created based on those materials. 
# """
# def main():
#     # Determine the shoe types based on the materials provided
#     materials_1 = ['leather', 'rubber']
#     materials_2 = ['grgegre', 'ewewr', 12]
#     materials_3 = ['mesh', 'rubber']
    
#     # Use the create_shoe function and check the result
#     shoe_1 = create_shoe(materials_1)
#     shoe_2 = create_shoe(materials_2)
#     shoe_3 = create_shoe(materials_3)
    
#     shoes = [shoe_1, shoe_2, shoe_3]
#     for shoe in shoes:
#         if shoe['type'] == 'unknown':
#             print(f"Unknown shoe type for the given materials: {shoe['materials']}")
#         else:
#             print(f"Shoe created of type: {shoe['type']}")
    
# def create_shoe(materials_list):
#     shoe_type = ''
    
#     if 'leather' in materials_list and 'rubber' in materials_list:
#         shoe_type = 'boots'
#     elif 'mesh' in materials_list and 'rubber' in materials_list:
#         shoe_type = 'sneakers'
#     else:
#         shoe_type = 'unknown'
        
#     return {'type': shoe_type, 'materials': materials_list}
    

    
# # if __name__ == '__main__':
# main()
# def looping():
#     numbers=5
#     num=2
#     print("I'm about to loop")
#     while num < numbers:
#         print(f"num {num} is smaller than numbers {numbers}")
#         num+=1
# looping()
# def loops(number):
#     num=1
#     while num < number:
#         print(f"num {num} is smaller than number {number}")
#         num+=1
# loops(6)
#i've finally understood how function works 


# def display_message():
#     print("I'm Learning Functions in this Chapter")
# display_message()

# def favourite_book(title):
#     print(f"My Favourite book is {title}")
# favourite_book("Alice In Boderland")
def vet(animal_name,gender,species):
    print(f"This {animal_name} is {gender} is {species}")

vet("CROW","FEMALE","BIRD")