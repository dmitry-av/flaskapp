from flask import Flask
from flask import request, escape
import requests
from bs4 import BeautifulSoup
import random

app = Flask(__name__)


@app.route("/")
def index():
    url_list = request.args.get("url_list", "")
    if url_list:
        listing = []
        for url in url_list.split(" "):
            listing.append(check_correct_page(url))
    else:
        listing = ""
    return (
        """<form action="" method="get">
                Type your URLs separated by space: <input type="text" name="url_list">
                <input type="submit" value="Check for correctness">
            </form>"""
        + "Result: "
        + '   '.join(listing)
        + """<form action="" method="get">
                Type your URLs separated by space: <input type="text" name="url_list">
                <input type="submit" value="Check for correctness">
            </form>"""
        + "Result: "
        + '   '.join(listing)
    )


def check_correct_page(url):
    try:
        result = requests.get(url).text
        soup = BeautifulSoup(result, "html.parser")
        box = soup.find('i', class_='symbol-classcentral-navy')
        if box:
            return f"{url}: PASS\n"
        else:
            return f"{url}: FAIL\n"
    except:
        return f"{url} - Cannot check URL {url}. Please check if this URL is correct (starts with https and so on..)\n"


def check_translation(url):
    result = requests.get(url).text
    soup = BeautifulSoup(result, "html.parser")
    link_list = [tag['href'] for tag in soup.find_all('a')]
    internal_list = [link for link in link_list if 'www' not in link]
    sample_list = random.sample(internal_list, 5)
    print(sample_list)
    result = []
    for link in sample_list:
        link = url+link
        page = requests.get(url).text
        soup = BeautifulSoup(page, "html.parser")
        box = soup.find(
            'a', class_='color-charcoal block large-up-inline-block large-up-margin-left-xsmall')
        text = box.get_text()
        if "गोपनीयता" in text:
            x = "PASS"
        else:
            x = "FAIL"
        result.append(x)
    return result


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
