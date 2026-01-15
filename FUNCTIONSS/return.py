# def get_formatted_name(first_name, last_name): 
#     """Return a full name, neatly formatted.""" 
#     full_name = f"{first_name} {last_name}" 
#     return full_name.title() 
# musician = get_formatted_name('jimi', 'hendrix') 
# print(musician)
# def build_person(first_name, last_name): 
#     """Return a dictionary of information about a person.""" 
#     person = {'first': first_name, 'last': last_name} 
#     return person 
# musician = build_person('jimi', 'hendrix') 
# print(musician)
# def greeting(first_name, last_name, age, gender):
#     person={'firstName': first_name, 'LastName': last_name,'age': age, 'gender': gender }
#     return person
# while True:
#     print("Enter your Full details")
#     print("Enter q anytime to quite")
#     f_name=input("\tEnter your FirstName: ")
#     if f_name=="q":
#         break
#     l_name=input("\tEnter your SecondName: ")
#     if l_name=="q":
#         break
#     agee=input("\tEnter your Age: ")
#     genderr=input("\tEnter your Gender: ")
   

#     persona=greeting(f_name, l_name, agee, genderr)
#     print(f"Hello my names are {persona}")
def city_country(city_name,country):
    furr_name={'cityName': city_name, 'CountryName': country}
    return furr_name
while True:
    print("\tPress q if you want to quit")
    city_name=input("Enter City Name: ")
    if city_name=="q":
        break
    country=input("Enter Country Name: ")
    if country=="q":
        break
    full_name=city_country(city_name,country)
    print(full_name)

