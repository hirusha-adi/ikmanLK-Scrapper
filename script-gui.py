from tkinter import *
from bs4 import BeautifulSoup
import requests
import tkinter.font as font

root = Tk()
root.title("ikman.lk Scrapper")
root.resizable(False, False)
try:
    root.iconbitmap("icon.ico")
except:
    pass


def ikmainlkScrapper():
    # weblink = "https://ikman.lk/en/ads/sri-lanka/vehicles?sort=date&buy_now=0&urgent=0&page=1"

    weblink = elink.get()

    r = requests.get(str(weblink))
    c = r.content
    soup = BeautifulSoup(c, "html.parser")

    item_list_names = soup.find_all("h2", {"class": "heading--2eONR heading-2--1OnX8 title--3yncE block--3v-Ow"})
    item_list_images = soup.find_all("img", {"class": "normal-ad--1TyjD"})
    item_list_price = soup.find_all("div", {"class": "price--3SnqI color--t0tGX"})
    item_list_description = soup.find_all("div", {"class": "description--2-ez3"})
    list_updated_time = soup.find_all("div", {"class": "updated-time--1DbCk"})
    list_links_to_itms = soup.find_all("a", {"class":"card-link--3ssYv gtm-ad-item"})

    try:
        file = open('ikmanScraped.txt', 'r+', encoding="utf8")
        for  i in range(len(item_list_names)):
            list_item_names_tmain = item_list_names[i].text
            # print(list_item_names_tmain)
            tmain.insert(END, "\n\n" + list_item_names_tmain + "")
            file.write("\n\n" + list_item_names_tmain + "\n")

            price_list_index = item_list_price[i]
            price_list_tmain = price_list_index.find("span").text
            # print(price_list_index.find("span").text)
            tmain.insert(END, "Price: " + price_list_tmain + "\n")
            file.write("Price: " + price_list_tmain + "\n")
    
            links_to_sites_index = list_links_to_itms[i]
            sites_links_tmain = "https://ikman.lk/" + links_to_sites_index.get('href')
            # print("https://ikman.lk/" + links_to_sites_index.get('href'))
            tmain.insert(END, "Link: " + sites_links_tmain + "\n")
            file.write("Link: " + sites_links_tmain + "\n")


            try:
                image_links_in_index = item_list_images[i] # if i don't do this, an error will occcur as this is a whole list
                # print(image_links_in_index.get('src')) # so we index it and call a value and we get the src in it!
                image_links_tmain = image_links_in_index.get('src')
                tmain.insert(END, "Image: " + image_links_tmain + "\n")
                file.write("Image: " + image_links_tmain + "\n")
            except:
                print("\n")
                file.write("")

            description_list = item_list_description[i]
            description_list_tmain = description_list.text
            # print(description_list.text)
            tmain.insert(END, "More: " + description_list_tmain + "\n")
            file.write("More: " + description_list_tmain + "\n")

            try:
                updated_time_index = list_updated_time[i]
                updated_time_tmain = updated_time_index.text
                # print(updated_time_index.text)
                tmain.insert(END, updated_time_tmain)
                file.write("Updated Date: " + updated_time_tmain)
            except:
                print("\n")
                file.write("")

            # print("\n\n\n\n")
        file.close()

    except Exception as e:
        print("error: ", e)

def clearall():
    tmain.delete(0, END)
    elink.delete(0, END)

fontforbtns = font.Font(family="Arial", size="15", weight="bold")
fontfort = font.Font(size="13", weight="bold")


ltop = Label(root, text="ikman.lk Web Scrapper by ZeaCeR#5641")
ltop.grid(row=0, column=0, columnspan=2)

lenterlinkbelow = Label(root, text="Enter the link below:")
lenterlinkbelow.grid(row=1, column=0, columnspan=2)

elink = Entry(root, width=70, borderwidth=10)
elink.grid(row=5, column=0 ,columnspan=2)

tmain = Text(root, width=52, height=15)
tmain.grid(row=6, column=0, columnspan=2)

bscrap = Button(root, text="Scrap", command=ikmainlkScrapper, padx=76)
bscrap['font'] = fontforbtns
bscrap.grid(row=7, column=0, columnspan=1)

bsavetofile = Button(root, text="Clear", command=clearall, padx=76)
bsavetofile['font'] = fontforbtns
bsavetofile.grid(row=7, column=1, columnspan=1)


root.mainloop()