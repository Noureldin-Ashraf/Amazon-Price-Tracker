import requests
from bs4 import BeautifulSoup
import email_notification as notify

# URL for the product you want to Track
PRODUCT_URL = 'https://www.amazon.eg/-/en/Other-Python-Mug-Porcelain-Teacups/dp/B091C33F2W/ref=sr_1_1?crid=845GBRQQ1523&keywords=python&qid=1686565780&sprefix=python%2Caps%2C192&sr=8-1'
# The target price for the product which the script will track and send an email if the price is lower
PRODUCT_TARGET_PRICE = 100

# Some websites like amazon requires a user agent and language to show the appropriate webpage, so we need to send them in the request header
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
accept_language = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"

headers = {
    "User-Agent": user_agent,
    "Accept-Language": accept_language,
}

response = requests.get(PRODUCT_URL, headers=headers, verify=False)
product_webpage = response.text

# Get Product Title and Availability
soup = BeautifulSoup(product_webpage, "html.parser")
title = soup.select_one(selector="#productTitle").getText().lstrip().rstrip()
availability = soup.select_one(selector="#availability").getText().lstrip().rstrip()


# Check if the product is out of stock
if "Currently unavailable" in availability:
    message = f"Subject:Amazon Price Alert \n\n{title} is unfortunately Out Of Stock\n {PRODUCT_URL}"
    notify.send_email(message)
else:
    # Get the current product price
    current_price = soup.select_one(selector=".a-price-whole").getText().replace(',', '').replace('.', '')
    # Check if price is less than the target price
    if int(current_price) < PRODUCT_TARGET_PRICE:
        message = f"Subject:Amazon Price Alert \n\n{title} is now {current_price}\n {PRODUCT_URL}"
        notify.send_email(message)




