import csv 

def get_reviews_count(word):    
    count = ""
    for w in word:
        if w == '\n':
            break
        else:
            count += w
    return count

def review_or_reviews(number):
    if int(number) > 1:
        return 'reviews'
    return 'review'

def extract_reviews(reviews):
    for review in reviews:
        name = review.find('div', class_="typography_typography__QgicV typography_bodysmall__irytL typography_weight-medium__UNMDK typography_fontstyle-normal__kHyN3 styles_consumerName__dP8Um").text.strip()
        country = review.find('span', class_="typography_typography__QgicV typography_weight-inherit__iX6Fc typography_fontstyle-inherit__ly_HV").text.strip()
        
        #what user says about the product
        try:            
            review_text = review.find('p', class_="typography_typography__QgicV typography_body__9UBeQ typography_color-black__5LYEn typography_weight-regular__TWEnf typography_fontstyle-normal__kHyN3").text.strip()
        except:
            review_text = review.find('a', class_="link_internal__7XN06 typography_typography__QgicV typography_weight-inherit__iX6Fc typography_fontstyle-inherit__ly_HV link_notUnderlined__szqki typography_color-inherit__TlgPO").text.strip()
        review_text = str(review_text).replace('  ', '').replace('\n\n', '\n')
        
        #number of reviews the user give to the product   
        reviews_count = review.find('span', class_="typography_typography__QgicV typography_bodysmall__irytL typography_color-gray-6__TogX2 typography_weight-regular__TWEnf typography_fontstyle-normal__kHyN3").text.strip()
        reviews_count = get_reviews_count(reviews_count)
        reviews_count = reviews_count + ' ' + review_or_reviews(reviews_count)
        
        # print data
        from_text_to_csv(name, country, reviews_count, review_text)
    
# Create CSV and write headers and data into the file
def from_text_to_csv(name, country, reviews_count, review_text):
        # create cvs file and add data
        data = [name, country, reviews_count, review_text]
        # header = ['User Name', 'User Country', 'User Rating', 'User Review']
        # with open('CompanyReviewsDataset.csv', 'w', newline='', encoding='UTF8') as f:
        #     writer = csv.writer(f)
        #     writer.writerow(header)
        #     writer.writerow(data)
        # -----------------------------------------
        #Now we are appending data to the csv
        with open('CompanyReviewsDataset.csv', 'a+', newline='', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(data)