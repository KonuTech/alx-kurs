import requests
from bs4 import BeautifulSoup


print("BOOTCAMPY:\n")
strona = requests.get("https://www.alx.pl/")
soup = BeautifulSoup(strona.content, "html.parser")

# lista bootcampow

# sip1 = soup.find_all("p", {"class", "lp-homepageParagrafStyle"})
# sip2 = soup.find_all(class_="lp-homepageParagrafStyle")

# # print(sip1.get_text())
# print(sip2[-1])
# print(sip2[-1].get_text())

# soup = soup.find_all("div", {"class", "expand"})
# soup = soup.find_all(class_="main-nav")
sip1 = soup.find("ul", {"class", "main-nav"})
sip2 = sip1.find("div")
sip3 = sip2.find_all("a")

print(sip3,'\n')
print(type(sip3),'\n')

for i, t in enumerate(sip3):
    print(f"{i}: {t.get_text()}")

# kontakt
print("KONTAKT:\n")
strona = requests.get("https://www.alx.pl/kontakt")
soup = BeautifulSoup(strona.content, "html.parser")
sip1 = soup.find_all("p", {"class", "tel"})
# print(sip1)
for i, s in enumerate(sip1):
    # print(s)
    print(s.find("strong").get_text())
