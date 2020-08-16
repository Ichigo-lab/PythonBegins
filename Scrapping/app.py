from bs4 import BeautifulSoup

response = open("BMC-ContainmentZones (1).js", "r")
soup = BeautifulSoup(response, "lxml")
script = soup.find('script')
print(script)
