import helper
import convert_to_csv
import datetime


helper.driver.get("https://www.binance.com/en/markets/")
top_gainer_header = ['Name', 'Price', 'Change', 'Date']
def get_list_of_coins():
    click_on_top_gainer =  helper.driver.find_element(helper.By.XPATH, '//*[@id="__APP"]/div/div/main/div/div[1]/div[2]/div/div[3]/div[1]/div')
    click_on_top_gainer.click()
    tops = helper.driver.find_elements(helper.By.XPATH, '//*[@id="__APP"]/div/div/main/div/div/div[2]/div/div/div[1]/div')
    stop = False
    for top in tops:
        print("----------------------------------")
        head = top.find_element(helper.By.XPATH, 'div/div[1]/div[1]').text
        print(head)
        convert_to_csv.adding_head([head])     
        coins = top.find_elements(helper.By.XPATH, 'div/div[2]/div/div')
        today = datetime.date.today()
        for i in range(1, len(coins)):
            number = coins[i].find_element(helper.By.XPATH, 'div/div[1]/div/div').text
            name = coins[i].find_element(helper.By.XPATH, 'div/div[2]/div/div').text
            price = coins[i].find_element(helper.By.XPATH, 'div/div[3]/div/div').text
            change = coins[i].find_element(helper.By.XPATH, 'div/div[4]/div/div').text
            print(number + "    " + name + "    " + price + "    " + change + "    ")
            if stop == False:
                convert_to_csv.convert_to_csv(name, price, change, today, top_gainer_header)
                stop = True
            else:
                convert_to_csv.add_data_without_overrite(name, price, change, today)
                    
# click on accept
helper.accept_terms()
# geting the list of data
get_list_of_coins()