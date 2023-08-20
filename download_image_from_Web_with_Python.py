import requests
url="https://kinsta.com/wp-content/uploads/2019/08/jpg-vs-jpeg.jpg"
response=requests.get(url)
with open("image.jpg","wb") as file:
    file.write(response.content)