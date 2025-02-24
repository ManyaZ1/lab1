import requests  # εισαγωγή της βιβλιοθήκης
from datetime import datetime, timezone

def more(text):
    count = 0
    for line in text.split('\n'):
        print(line)
        count += 1
        if count % 30 == 0:
            reply = input('Show more (y/n)? ')
            if reply == 'n':
                break

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
    #ποιο είναι το λογισμικό που χρησιμοποιεί ο εξυπηρετητής (ο web server) για να απαντήσει στο αίτημα;
    print(f"\nServer: {response.headers.get('Server')}")
    #(β) αν η σελίδα χρησιμοποιεί cookies, και αν ναι
    print(f"\nHas cookies: {'Set-Cookie' in response.headers}")
    #(γ) το όνομα κάθε cookie και για πόσο διάστημα θα είναι έγκυρο.
    for cookie in response.cookies:
        if cookie.expires:
            dt = datetime.fromtimestamp(cookie.expires, tz=timezone.utc) #from utc (second form unix epoch) to datetime (readable format)
            #print(dt)  # Convert to readable UTC time
            print(f"Name: {cookie.name}, Expires: {dt}")
