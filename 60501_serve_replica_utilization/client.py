import requests

count = 0
english_text = "Hello world!"
url = "http://127.0.0.1:8000/hello-world-1"

def call():
    global count

    response = requests.post(url, json=english_text)
    french_text = response.text
    count += 1
    print(f"{count}: {french_text}")

if __name__ == '__main__':
    for i in range(1000):
        call()
