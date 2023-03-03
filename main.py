
import mechanicalsoup

browser = mechanicalsoup.Browser()
page = browser.get("https://stackoverflow.com/questions/tagged/python")
tag = page.soup.select("#questions")[0]
result = tag.text

print(f"The questions are: {result}")