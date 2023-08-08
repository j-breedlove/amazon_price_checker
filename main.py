import requests
from bs4 import BeautifulSoup
import smtplib
from decouple import config

# Environment variables
MY_EMAIL = config('MY_EMAIL')
PASSWORD = config('PASSWORD')

# Constants
SET_PRICE_FLOAT = 75
URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9"
}


def fetch_product_price(url, headers):
    try:
        page = requests.get(url, headers=headers)
        page.raise_for_status()
        soup = BeautifulSoup(page.content, "html.parser")
        get_price = soup.find_all("span", class_="a-size-medium a-color-price")
        price_list = [float(price.text.replace('$', '')) for price in get_price if float(price.text.replace('$', '')) < SET_PRICE_FLOAT]
        return min(price_list) if price_list else None
    except requests.RequestException as e:
        print(f"Error fetching product price: {e}")
        return None


def send_email(email, password, deal, url):
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(from_addr=email, to_addrs=email, msg=f"Subject:Amazon Price Alert!\n\n${deal}\n{url}")
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")


if __name__ == "__main__":
    deal_price = fetch_product_price(URL, HEADERS)
    if deal_price:
        send_email(MY_EMAIL, PASSWORD, deal_price, URL)
    else:
        print("No deal found or there was an error fetching the product price.")
