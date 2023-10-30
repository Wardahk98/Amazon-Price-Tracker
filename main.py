from data_manager import Datamanager
from inputimeout import inputimeout
from amazon_scraper import AmazonScraper
from notification import Notification

id_url = 1
try:
    new_entry = inputimeout(prompt="Do you want to track the price of any new project? Y/N:", timeout=5)

except:
    print("Times Up!")

else:
    user_email = input("Add your email: ")
    while new_entry == "Y" or new_entry == "y":

        user_input_url = input("Add the URL of Product you want to track: ")
        scraper = AmazonScraper(url=user_input_url)
        product_name = scraper.product_name
        
        try:
            product_price = scraper.product_price
            # print(product_price)
            price_float = float(product_price.split("$")[1])

        except IndexError:
            print("Seller do not want to reveal the price.")

        else:
            print(f"The product you want: {product_name}")
            print(f"The product price is: {product_price}")
            user_input_discount = input("Enter the reduced amount: $")
            entry = Datamanager()
            entry.add_data(a_url=user_input_url, p_name=product_name, p_price=product_price,
                           r_price=float(user_input_discount), u_email=user_email)
        id_url += 1
        new_entry = input("Do you want to track any new product for price tracking? Y/N: ")

finally:
    data = Datamanager()
    notify = Notification()
    get_data = data.data["sheet1"]
    for x in get_data:
        link = x["amazonLink"]
        check_price = AmazonScraper(url= link)
        price = float(check_price.product_price.split("$")[1])
        if float(price) >= float(x["reducedPrice"]):
            print("Price is met")
            notify.send_email(email=x["userEmail"], product_name=x["productName"], product_price=price)