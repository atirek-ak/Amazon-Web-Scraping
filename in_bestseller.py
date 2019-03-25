from bs4 import BeautifulSoup
import requests
import os
import csv

file = open('in_book.csv', 'w')
file.write('Name' + ";" + 'URL' + ";" + 'Author' + ";" + 'Price' +
           ";" + 'Number of Ratings' + ";" + 'Average Rating' + "\n")

print("Please wait while the process completes. A file in_book.csv will be generated in the current folder.")

for i in range(1, 6):

    for var in BeautifulSoup(requests.get('https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_pg_{0}?ie=UTF8&pg={0}'.format(i)).text, 'lxml').find('div', id='zg_centerListWrapper').find_all('div', class_='zg_itemWrapper'):
        try:
            name = var.find(
                'div', class_='p13n-sc-truncate p13n-sc-line-clamp-1').string.strip()

        except Exception as e:
            name = var.find(
                'div', class_='p13n-sc-truncate p13n-sc-line-clamp-2').string.strip()

        except Exception as e:
            name = "Not Available"

        file.write(str(name) + ";")

        try:
            url_val = 'https://www.amazon.in{0}'.format(
                var.find('a', class_='a-link-normal')['href'].strip())

        except Exception as e:
            url_val = "Not Available"
        file.write(url_val + ";")

        try:
            author_val = var.find('div', class_='a-row a-size-small').text

        except Exception as e:
            author_val = "Not Available"

        except Exception as AttributeError:
            author_val = "Not Available"

        file.write(str(author_val) + ";")

        try:
            price = var.find('span', class_='p13n-sc-price').text.strip()

        except Exception as e:
            price = "Not Available"
        file.write("Rs. " + price + ";")

        try:
            n_o_r = var.find(
                'a', class_='a-size-small a-link-normal').string.strip()

        except Exception as e:
            n_o_r = "Not Available"
        file.write(n_o_r + ";")

        try:
            avg_rat = var.find('div', class_='a-icon-row a-spacing-none').find(
                'a', class_='a-link-normal')['title'].strip()

        except Exception as e:
            avg_rat = "Not Available"
        file.write(avg_rat + "\n")


file.close()
