import requests
import smtplib
import ssl
from email.message import EmailMessage
import os

def send_email(subject, body):
    sender = "muneeburrehmanaltaf1@gmail.com"
    password = os.environ.get("PASSWORD")  # Access the environment variable
    receiver = "muneeburrehmanaltaf1@gmail.com"
    context = ssl.create_default_context()
    host = "smtp.gmail.com"
    port = 465

    message = EmailMessage()
    message["Subject"] = subject
    message["From"] = sender
    message["To"] = receiver
    message.set_content(body)

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(sender, password)
        server.send_message(message)
topic="tesla"
url = "https://newsapi.org" \
      "/v2/everything?" \
      f"q={topic}&" \
      "from=2023-06-29&sortBy" \
      "=publishedAt&apiKey=8b4149f77a11476d892e43591efc7ee5&language=en"# by adding parameter we restrict the info to english

api_key = "8b4149f77a11476d892e43591efc7ee5"

request = requests.get(url)
content = request.json()# it gives the dictionary request.text gives the stringi
body = " "

for article in content["articles"][:20]:
    if article["title"] is not None:
        body = body + article["title"] + "\n"
    if article["description"] is not None:
        body = body + " Explanation: " + article["description"]+"\n"+ article["url"] + "\n\n"

# Set the subject for the email
subject = "News Summary"

# Call the send_email function with the subject and body
send_email(subject, body)
