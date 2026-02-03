import requests

# count = 0
# english_text = "Hello world!"
# # url = "http://127.0.0.1:8000/hello-world-1"
# url = "http://127.0.0.1:8000/worker_app"
#
# def call():
#     global count
#
#     response = requests.post(url, json=english_text)
#     french_text = response.text
#     count += 1
#     print(f"{count}: {french_text}")
#
# if __name__ == '__main__':
#     for i in range(10):
#         call()


count = 0
url = "http://127.0.0.1:8000/?duration=0.5"

def call():
    global count

    response = requests.get(url)
    result = response.text
    count += 1
    print(f"{count}: {result}")

if __name__ == '__main__':
    from concurrent.futures import ThreadPoolExecutor

    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(lambda: call()) for _ in range(4)]
        for future in futures:
            future.result()



