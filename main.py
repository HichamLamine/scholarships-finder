from bs4 import BeautifulSoup
import requests
import time

htmlText = requests.get(
    "https://www.scholarshipsads.com/category/tags/morocco/https://www.scholarshipsads.com/category/tags/morocco/"
).text
soup = BeautifulSoup(htmlText, "lxml")
scholarships = soup.find_all("div", class_="card-warp")
# print("available scholarships \n")
for index, scholarship in enumerate(scholarships):
    name = scholarship.a.text
#    print(index + 1, ".", name)


def extractDetails(n):
    name = scholarships[n].a.text
    details = scholarships[n].ul.text.strip()
    state = scholarships[n].find("span", class_="card-deal-title").text
    print(name, "\nState: ", state, "\n")


def filter_by_amount(a):
    for index, scholarship in enumerate(scholarships):
        amount = scholarship.find("li").text
        if "Full" in amount:
            if a == "f":
                print("\n", index + 1, ".", scholarship.a.text)
        elif "Partial" in amount:
            if a == "p":
                print("\n", index + 1, ".", scholarship.a.text)


while True:
    print("Choose between [F]ull tuition fee or [P]artial Funding")
    type = input().lower()

    if type == "f":
        print("\nFull tuition fee")
        filter_by_amount(type)
        print("\n")
    elif type == "p":
        print("\nPartial Funding")
        filter_by_amount(type)
        print("\n")


# while True:
#    print ("Choose by number")
#    num = int(input()) - 1
#    extractDetails(num)
