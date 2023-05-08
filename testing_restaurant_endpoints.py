import requests

from restaurant.models import Menu

# Log in the user
# register_url = 'http://127.0.0.1:8010/register/'
# register_data = {
#     "first_name": "abdullah",
#     "last_name": "ahmed",
#     "username": "sirajjunior",
#     "email": "sirajjunior@gmail.com",
#     "user_type": '2',
#     "password": "6014",
#     "confirm_password": "6014"
# }
# login_response = requests.post(register_url, json=register_data)
# print("registration done")








login_url = 'http://127.0.0.1:8010/login/'
login_data = {
    "username": 'sirajjunior',
    "password": '6014'
}
login_response = requests.post(login_url, json=login_data)
access_token = login_response.json().get('access')
headers = {
        'Authorization': f'Bearer {access_token}'
     }
print('token generated')






create_restaurant = 'http://127.0.0.1:8010/restaurant/restaurants/'
#
restaurant_data = {
    "name": "Laziz Amarat",
    "phone_number": "+971503950224",
    "address": "dubai -jlt",
    "description": "free good restaurant",
    "is_active": True
}
response = requests.post(create_restaurant, headers=headers, json=restaurant_data)
print("restaurant_created")



create_menu = 'http://127.0.0.1:8010/restaurant/menus/'

excel_path = 'excel_files/gada_menu_hhs.xlsx'
with open(excel_path, 'rb') as excel_file:
    files = {'excel_file': excel_file}

menu_data = {
    "name": "fatoor menu",
    "excel_file": 'excel_files/gada_menu_hhs.xlsx',
    "version": "1.2",

}
headers = {
    'Content-Type': 'multipart/form-data',
    'Authorization': f'Bearer {access_token}'

}
response = requests.post(create_menu, headers=headers, json=menu_data)
print("menu created")

create_menu_item = 'http://127.0.0.1:8010/restaurant/menu-items/'
image_path = 'test_menu_image.jpeg'
with open(image_path, 'rb') as image_file:
    files = {'image': image_file}

menu_item_data = {
    "name": "Fool Sudani",
    "description": "Fool with sesame oil",
    "menu": '1',
    "price": 5.5,
    "is_active": True,

}
response = requests.post(create_menu_item, headers=headers, data=menu_item_data, files=files)
print("menu item created")