import requests


url = "http://127.0.0.1:5000/add"
url1 = "http://127.0.0.1:5000/response_json_test"
json_data = {'a': 1, 'b': 2}

# r = requests.post(url1, json=json_data)
# print(r.text)



file_data = {'image': open('aaa.png', 'rb')}

user_info = {'info': 'Lenna'}

r = requests.post("http://127.0.0.1:5000/upload", data=user_info, files=file_data)

print(r.text)