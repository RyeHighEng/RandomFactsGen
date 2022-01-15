import requests
import smtplib
import myconfig

def jokes(url: str, header: str) -> str:
    resp = requests.get(url, headers={"Accept": "application/json"})
    data = resp.json()
    return data[header]


joke = jokes(myconfig.url, myconfig.header)


# Canadian Carriers that I needed.
carriers = {
    'koodo':    '@msg.telus.com',
    'bell': ' @txt.bell.ca',
}
# Function to send the message from Gmail to the destination phone number.


def send(message: str, number: int,  carrier: dict):
    # Replace the number with your own, or consider using an argument\dict for multiple people.
    to_number = f'{number}{carriers[carrier]}'
    # establish a secure connection with gmail
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # login with gmail account
    server.login(myconfig.email, myconfig.password)
    # Send text message through SMS gateway of destination number
    server.sendmail(myconfig.email, to_number, message)

send(joke, myconfig.contact1[0], myconfig.contact1[1])
send(joke, myconfig.contact2[0], myconfig.contact2[1])
send(joke, myconfig.contact3[0], myconfig.contact3[1])
send(joke, myconfig.contact4[0], myconfig.contact4[1])