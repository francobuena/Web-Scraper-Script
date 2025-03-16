import requests
from bs4 import BeautifulSoup

def get_cat_names(url):
    cat_names = []

    # Send a GET request to the webpage
    response = requests.get(url)

    # Parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the HTML elements containing the cat names
    cat_name_elements = soup.find_all("h2", class_="entry-title")

    # Extract the cat names
    cat_names.extend(element.text.strip() for element in cat_name_elements)

    return cat_names

def get_total_pages(url):
    # Send a GET request to the webpage
    response = requests.get(url)

    # Parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the last page number
    last_page_link = soup.find("a", class_="page-numbers", string=lambda text: text.isdigit())
    total_pages = int(last_page_link.text.strip()) if last_page_link else 1

    return total_pages

def main():
    base_url = "https://www.awlnsw.com.au/animals/page/{}/?locations=55&type=2%2C15&age&gender=-1&end_size=1&mid_size=2"

    total_pages = get_total_pages(base_url.format(1))
    all_cat_names = []

    for page_number in range(1, total_pages + 2): # should be + 1 but something wrong with the script
        url = base_url.format(page_number)
        cat_names = get_cat_names(url)
        all_cat_names.extend(cat_names)

    total_cats = len(all_cat_names)

    # Print the list of cat names and the total number of cats
    print("List of cat names:")
    for cat_name in all_cat_names:
        print(cat_name)

    print("Total number of cats:", total_cats)
    print("Is my cat here?", "Scallops" in all_cat_names)

if __name__ == "__main__":
    main()
