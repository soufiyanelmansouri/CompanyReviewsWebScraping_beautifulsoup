# Create CSV and write headers and data into the file
import csv



def convert_to_csv(name, price, market_cap, today, header):
    data = [name, price, market_cap, today]
    with open('BinanceWebScraperDataset.csv', 'w', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(data)
        
def add_data_without_overrite(name, price, market_cap, today):
    data = [name, price, market_cap, today]
    with open('BinanceWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)
def adding_head(head):
    with open('BinanceWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(head)        