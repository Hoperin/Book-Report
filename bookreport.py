import requests
from bs4 import BeautifulSoup
import arrow

URL = "https://www.goodreads.com/review/list/34342685-nick-carraway-llc"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

bookstable = soup.find(id="booksBody")

#print (bookstable.prettify())

books = bookstable.find_all("tr", class_="bookalike review")

year = arrow.now().year
startDate = arrow.Arrow(year, 1, 1)
endDate = arrow.Arrow(year, 12, 31)




for book in books:

    name = book.find("td", class_="field title")
    nameValue = name.find("div", class_="value")
    adjustedNameValue = nameValue.get_text().replace("title","").strip()
    dateStarted = book.find("td", class_="field date_started")
    dateStartedValue = dateStarted.find("span", class_="date_started_value")
    dateFinished = book.find("td", class_="field date_read")
    dateFinishedValue = dateFinished.find("span", class_="date_read_value")

    if dateFinishedValue == None:
        continue
    if dateStartedValue == None:
        continue



    bookStartDate = arrow.get(dateStartedValue.string, ['MMM DD, YYYY', 'MMM YYYY', 'YYYY'])
    bookEndDate = arrow.get(dateFinishedValue.string, ['MMM DD, YYYY', 'MMM YYYY', 'YYYY'])
    #if "2021" in dateFinishedValue.string:
    if bookEndDate >= startDate and bookEndDate <= endDate:
        print (adjustedNameValue)
        print (dateStartedValue.get_text() + " to " + dateFinishedValue.get_text())
        print (bookEndDate - bookStartDate)



