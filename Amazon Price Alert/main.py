from bs4 import BeautifulSoup
import requests
import lxml
import smtplib
import pandas

if __name__ == '__main__':
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"

    amazon_page = input("Which Amazon listing would you like to keep an eye on? ")

    browser_headers = {
        "User-Agent": user_agent,
        "Accept-Language": "en-US,en;q=0.9"
    }
    response = requests.get(amazon_page, headers=browser_headers)
    response.raise_for_status()
    listing = response.text

    soup = BeautifulSoup(listing, "lxml")
    price = float(soup.find("span", class_="a-offscreen").getText().replace("$", ""))
    product = soup.find("span", id="productTitle").getText().strip()

    try:
        watchlist_df = pandas.read_csv("previous_price.csv")
        watchlist = watchlist_df["product"].tolist()

    except FileNotFoundError:
        listings_dict = {
            "product": [product],
            "price": [price],
            "link": [amazon_page],
        }

        listing_df = pandas.DataFrame(listings_dict)
        listing_df.to_csv('previous_price.csv')

    else:
        if product in watchlist:
            found_product_data = watchlist_df[watchlist_df["product"] == product]
            previous_price = float(found_product_data["price"].item())
            if price < previous_price:
                with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                    connection.starttls()
                    connection.login("foo", "foo")
                    connection.sendmail(from_addr="foo",
                                        to_addrs="foo",
                                        msg=f"Subject: Price Alert!\n\n the {product} is down to ${price} in price")
            else:
                print("No notable price changes")

        else:
            print("Product not found, Adding")
            listings_dict = pandas.DataFrame({
                "product": [product],
                "price": [price],
                "link": [amazon_page],
            })
            with open('previous_price.csv', 'a') as f:
                listings_dict.to_csv(f, header=False)
