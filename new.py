__author__ = 'Balaji'
import requests
from bs4 import BeautifulSoup
import urllib.request
from tkinter import *
from PIL import Image,ImageTk

new_flip_list = []
new_amazon_list = []
new_snap_list = []
url_product = []
url_snap_product = []
url_flip_product = []
url_amazon_product = []



def flipkart(product_name):
    while True:
        try:
            if product_name in ('',None,' '):
                new_flip_list.append('Enter a valid product')
                break

            product_name.rstrip(' ')
            product_name.lstrip(' ')


            product_name.replace(' ', '+')

            # Does flipkart search
            product_url = 'http://www.flipkart.com/search?q=' + product_name

            try:
                product_url_page = requests.get(product_url)
            except:
                new_flip_list.append('Internet connection aborted')
                break

            product_url_html = product_url_page.text
            soup_main = BeautifulSoup(product_url_html)
            try:
                if (soup_main.find('div', {'class': 'noResults fk-text-center tmargin20 bmargin20 fk-uppercase omniture-field'}))!= None:
                    new_flip_list.append('No product found')
                    break
            except:
                pass

            product_id = soup_main.find('a', {'data-tracking-id': 'prd_title'})

            counter_internet= 10

            #Image Search
            print('The best available match was :')
            image_link = soup_main.find('a',{'data-tracking-id':'prd_img'})
            print('Low res image')
            print(image_link.find('img').get('data-src'))
            low_res = image_link.find('img').get('data-src')
            high_res =''
            if(low_res.find('125x125')!= -1):
                high_res = low_res.replace('125x125','400x400')
                print('High res image')
                print(high_res)
            elif(low_res.find('200x200')!= -1):
                high_res = low_res.replace('200x200','400x400')
                print('High Res image')
                print(high_res)
            else:
                print('No high res image available')
                high_res = low_res
                print('hello')
            urllib.request.urlretrieve(high_res,'100.jpeg')


            # Accesses the product
            if product_id != None:
                new_flip_list.append(product_id.get('title'))
                print(product_id.get('title'))
                source_code = requests.get('http://flipkart.com' + product_id.get('href'))
                url_flip_product.append('http://flipkart.com' + product_id.get('href'))
            else:
                if counter_internet == 0:
                    break
                else:
                    counter_internet = counter_internet-1
                    continue

            page = source_code.text
            soup_product = BeautifulSoup(page)

            price = soup_main.find('div', {'class': 'pu-final font-dark-color fk-inline-block'})
            if price != None:
                new_flip_list.append(price.find('span', {'class': 'fk-font-12'}).string+'.00')
                print(price.find('span', {'class': 'fk-font-12'}).string+'.00')
            else:

                price = soup_product.find('span', {'class': 'selling-price omniture-field'})
                new_flip_list.append(price.string+'.00')
                print(price.string)

            rating = soup_product.find('div', {'class': 'bigStar'})
            if rating != None:
                new_flip_list.append('Product Rating: ' + rating.string + '/ 5.0')
                print('Product Rating: ' + rating.string + '/ 5.0')

            author = soup_main.find('div', {'class': 'pu-extra fk-font-11'})
            if author != None:
                author_new = author.string.lstrip('\n')
                author_new = author_new.lstrip(' ')
                author_new = author_new.rstrip(' ')
                author_new = author_new.rstrip('\n')
                new_flip_list.append(author_new)
                print(author.string)

            seller = soup_product.find('div', {'class': 'seller-badge omniture-field'})
            if seller != None:
                new_flip_list.append('Seller: ' + seller.get('data-prop44'))
                print('Seller: ' + seller.get('data-prop44'))
                new_flip_list.append('Seller Rating : ' + seller.get('data-evar66') + '/ 5.0')
                print('Seller Rating : ' + seller.get('data-evar66') + '/ 5.0')

            print('hello')
            print(new_flip_list)
            break
        except:
            break

def amazon(product_name):
    while True:
        try:
            if product_name in ('',None,' '):
                new_amazon_list.append('Enter a valid product')
                break


            product_name.replace(' ', '+')

            # Does amazon search
            product_url = 'http://www.amazon.in/s/ref=nb_sb_ss_c_0_12?url=search-alias%3Daps&field-keywords=' + product_name

            try:
                product_url_page = requests.get(product_url)
            except:
                new_amazon_list.append('Internet connection aborted')
                break

            product_url_html = product_url_page.text
            soup_main = BeautifulSoup(product_url_html)

            try:
                if (soup_main.find('h1', {'id': 'noResultsTitle'}))!= None:
                    new_amazon_list.append('No product found')
                    break
            except:
                pass

            product_id = soup_main.find('a', {'class': 'a-link-normal s-access-detail-page  a-text-normal'})

            counter_internet= 10

            # Accesses the product
            if product_id != None:
                print('The best available match was :')
                new_amazon_list.append(product_id.get('title'))
                print(product_id.get('title'))
                source_code = requests.get(product_id.get('href'))
                url_amazon_product.append(product_id.get('href'))
            else:
                if counter_internet == 0:
                    break
                else:
                    counter_internet = counter_internet-1
                    continue


            price = str(soup_main.find('span', {'class': 'a-size-base a-color-price s-price a-text-bold'}))
            if price != None:
                new_price = re.split('</span>| ',price)
                for i in new_price:
                    try:
                        print(float(i.replace(',','')))
                        k = 'Rs. ' + str(i)
                        new_amazon_list.append(k)
                    except:
                        pass

                #print(isinstance(new_price_mod,double))
            page = source_code.text
            soup_product = BeautifulSoup(page)
            try:
                image_link = soup_product.find('div',{'class':'imgTagWrapper'}).find('img').get('data-a-dynamic-image')
                new_img_list = re.split('"',image_link)
                print(image_link)
                print(new_img_list[1])
                urllib.request.urlretrieve(new_img_list[1],'101.jpeg')
            except:
                try:
                    image_link = soup_product.find('div',{'id':'img-canvas'}).find('img').get('src')
                    print(image_link)
                    urllib.request.urlretrieve(image_link,'101.jpeg')
                except:
                    pass

            rating = soup_product.find('span', {'id': 'acrPopover'})
            if rating != None:
                product_rating = rating.get('title').replace(' out of ','/ ')
                product_rating = product_rating.replace(' stars','.0')
                new_amazon_list.append('Product Rating: ' + product_rating)
                print(rating.get('title'))

            author = soup_main.find('a', {'class': 'a-link-normal contributorNameID'})
            if author != None:
                new_amazon_list.append(author.string)
                print(author.string)

            seller = soup_product.find('div', {'id': 'merchant-info'})
            print(seller)
            seller_list = re.split('<|>',str(seller))
            print(seller_list)
            if seller != None:
                new_amazon_list.append('Seller: ' + seller.find('a').string)
                try:
                    seller_list[6] = seller_list[6].replace(' out of ','/ ')
                    seller_list[6] = seller_list[6].replace('(','')
                    new_amazon_list.append('Seller Rating:' + seller_list[6]+'.0' )
                except:
                    pass
                print('Seller: ' + seller.find('a').string)
                #new_amazon_list.append('Seller Rating : ' + seller.get('data-evar66') + '/ 5.0')
                #print('Seller Rating : ' + seller.get('data-evar66') + '/ 5.0')

            print('hello')
            print(new_amazon_list)
            break
        except:
            break

def snapdeal(product_name):
    while True:
        try:
            if product_name in ('',None,' '):
                new_snap_list.append('Enter a valid product')
                break

            product_name.replace(' ', '+')

            # Does amazon search
            product_url = 'http://www.snapdeal.com/search?keyword=' + product_name + '&santizedKeyword=&catId=175&categoryId=&suggested=true&vertical=p&noOfResults=20&clickSrc=go_header'

            try:
                product_url_page = requests.get(product_url)
            except:
                new_snap_list.append('Internet connection aborted')
                break

            product_url_html = product_url_page.text
            soup_main = BeautifulSoup(product_url_html)
            try:
                if (soup_main.find('div', {'class': 'noSearchMatching-text'}))!= None:
                    new_snap_list.append('No product found')
                    break
            except:
                pass

            product_id = soup_main.find('div', {'class': 'product-title'})

            counter_internet= 10

            # Accesses the product
            if product_id != None:
                print('The best available match was :')
                new_snap_list.append(product_id.find('a').string.rstrip('\n'))
                print(product_id.find('a').string.rstrip('\n'))
                source_code = requests.get(product_id.find('a').get('href'))
                url_snap_product.append(product_id.find('a').get('href'))
            else:
                if counter_internet == 0:
                    break
                else:
                    counter_internet = counter_internet-1
                    continue

            price = soup_main.find('p', {'id': 'price'})
            if price != None:
                new_snap_list.append(price.string+'.00')
            else:
                new_snap_list.append('Price not available')

            page = source_code.text
            soup_product = BeautifulSoup(page)
            try:
                image_link = soup_main.find('img',{'class':' gridViewImage'}).get('src')
                image_link2 = image_link.replace('166x194/','')
                urllib.request.urlretrieve(image_link2,'102.jpeg')
            except:
                    pass

            rating = soup_product.find('div', {'class': 'pdp-main-ratings av-rating'})
            if rating != None:
                product_rating = rating.find('span').get('md-data-rating')
                new_snap_list.append('Product Rating: ' + product_rating)
                print(product_rating)

            #author = soup_main.find('a', {'class': 'a-link-normal contributorNameID'})
            #if author != None:
            #   new_amazon_list.append(author.string)
            #    print(author.string)

            seller = soup_product.find('a', {'class': 'pdp-e-seller-info-name reset-margin'})
            print(seller.string)
            if seller != None:
                new_snap_list.append('Seller: ' + seller.string)

            seller_rating = soup_product.find('div', {'class': 'ow-fluid pdp-e-seller-info-score clear'})
            if seller_rating!=None:
                new_snap_list.append('Seller Rating: ' + seller_rating.find('label').find('b').string + '/5.0')


            print('hello')

            for i in range(len(new_snap_list)):
                try:
                    n = new_snap_list[i].replace('\r\n\t\t\t','')
                    new_snap_list[i] = n

                except:
                    pass

            print(new_snap_list)

            break
        except:
            break


def image_view(parent):
    logo = ImageTk.PhotoImage(Image.open("100.jpeg"))
    textbox3 = Label(parent,image = logo )
    textbox3.pack(side = TOP)

