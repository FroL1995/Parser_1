# Parser_1

imort requests

def main():
    url = ''
    response = requests.get(url)
    print(response.status_code)

    if name