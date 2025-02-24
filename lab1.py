import requests  # εισαγωγή της βιβλιοθήκης

def more(text):
    count = 0
    for line in text.split('\n'):
        print(line)
        count += 1
        if count % 30 == 0:
            reply = input('Show more (y/n)? ')
            if reply == 'n':
                break

# with requests.get(url) as response:  # το αντικείμενο response
#     html = response.text
#     more(html)

url=input("give url:") #ζητάει από τον χρήστη ένα URL

if not url.startswith('https://'):
    url='https://'+url

print(url)

#erotima1
#πραγματοποιεί ένα αίτημα HTTP σε αυτό το URL
with requests.get(url) as response:
    print(f"\n=============== HTTP Headers====================\n")
    for key in response.headers:
        print(f"Name: {key}, Value: {response.headers[key]}")