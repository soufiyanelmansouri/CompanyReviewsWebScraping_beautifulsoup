from helper import accept_terms, driver, By
import convert_to_csv
import datetime

driver.get("https://www.binance.com/en/markets/newListing")
new_listing_header = ['Name', 'Price', 'Market Cap', 'Date']

def get_list_of_coins():
    print("______________________________________") 
    coins = driver.find_elements(By.XPATH, '//*[@id="tabContainer"]/div[2]/div[2]/div/div[2]/div')
    print("Name    " + "price    " + "   Market Cap")
    print("--------------------------------------")
    stop = False
    for coin in coins:
        name = coin.find_element(By.XPATH, 'div/a/div[2]/div').get_attribute('innerHTML')
        price = coin.find_element(By.XPATH, 'div/div[1]/div').get_attribute('innerHTML')
        market_cap = coin.find_element(By.XPATH, 'div/div[4]/div').get_attribute('innerHTML')
        today = datetime.date.today()
        print(name + "    " + price + "    " + market_cap + "    ")
        if stop == False:
            convert_to_csv.convert_to_csv(name, price, market_cap, today, new_listing_header)
            stop = True
        else:
            convert_to_csv.add_data_without_overrite(name, price, market_cap, today)
        print("--------------------------------------")

# click on accept
accept_terms()
# geting the list of data
get_list_of_coins()