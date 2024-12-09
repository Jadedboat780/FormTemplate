import requests

url = "http://127.0.0.1:8000/get_form"
headers = {
    "accept": "application/json",
    "Content-Type": "application/json"
}
data = [
    {
        "name": "Form1",
        "fields": {"phone": "+7-123-456-78-61", "email": "test1@example.com", }
    },
    {
        "name": "Form2",
        "fields": {"phone": "+7-123-456-78-90", "hello": "word", "date": "2023-12-01"}
    },
    {
        "name": "Form4",
        "fields": {"email": "test4@example.com", "mes": "goodby", "date": "2023-12-01"}
    }

]

for num, d in enumerate(data, start=1):
    response = requests.post(url, headers=headers, json=d)
    print("Test №", num)
    print(f"Status code: {response.status_code}")
    print(f"Response body: {response.json()}", "\n")
