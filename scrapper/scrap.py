# Import modules
import requests
from bs4 import BeautifulSoup
import json
from pathlib import Path


# Define a function that checks if the class attribute contains a substring
def has_placeholder_twitter(tag):
    # Return False if the tag is not a div element
    if tag.name != "div":
        return False
    # Return False if the tag does not have a class attribute
    if not tag.has_attr("class"):
        return False
    # Return True if any of the class values contains the substring
    return any(
        "SocialConsentPlaceholder-SquareSocialConsentPlaceholder" in c
        for c in tag["class"]
    )


# Define a function that checks if the class attribute contains a substring
def has_placeholder_related_topics(tag):
    # Return False if the tag is not a div element
    if tag.name != "div":
        return False
    # Return False if the tag does not have a class attribute
    if not tag.has_attr("class"):
        return False
    # Return True if any of the class values contains the substring
    return any("LinksComponentWrappe" in c for c in tag["class"])


ARTICLES_FOLDER = "articles"
ARTICLES_SUBFOLDERS = ["bussiness", "technology"]

# Define base URL
base_url = "https://www.bbc.com"
sections_exclusions = {
    "/news/business": [
        # "Features & Analysis"
        "nw-c-Features&Analysis__title",
        # Watch/Listen
        "nw-c-Watch/Listen__title",
        # Special Reports
        "nw-c-Specialreports__title",
        # Around The BBC
        "nw-c-around-the-bbc-heading__title",
    ],
    "/news/technology": [
        # "Features & Analysis"
        "nw-c-Features&Analysis__title",
        # Watch/Listen
        "nw-c-Watch/Listen__title",
        # Around The BBC
        "nw-c-around-the-bbc-heading__title",
    ],
}

for (section_i, exclude), subfolder_article in zip(sections_exclusions.items(), ARTICLES_SUBFOLDERS):
    # Send GET request to base URL and get HTML content
    response = requests.get(base_url + section_i)
    html = response.text

    # Create BeautifulSoup object from HTML content
    soup = BeautifulSoup(html, "html.parser")

    # Find all links to articles on web page
    links = soup.find_all("a", class_="gs-c-promo-heading")

    # Loop through links and check if they are not in subsections links
    for link in links:
        # Get the href attribute of the link
        href = link["href"]
        # Find the parent div of the link
        parent = link.find_parent("div", role="region")
        # Check if parent has an aria-labelledby attribute that matches any of 
        # the exclude substrings
        if parent and parent.get("aria-labelledby"):
            label = parent["aria-labelledby"]
            if any(sub in label for sub in exclude):
                continue

        # Construct full URL by adding base URL and href
        full_url = base_url + href

        # Send GET request to full URL and get HTML content of article
        article_response = requests.get(full_url)
        article_html = article_response.content
        # Create BeautifulSoup object from article HTML content
        article_soup = BeautifulSoup(article_html, "html.parser")
        # Find the title element and get its text
        title = article_soup.find("title", {"data-rh": "true"}).text

        # Find the article element
        article = article_soup.find("article")

        # Try to remove the figure element
        try:
            article.find("figure").decompose()
        except AttributeError:
            print("Figure element not found")

        # Try to remove the aside element
        try:
            article.find("aside").decompose()
        except AttributeError:
            print("Aside element not found")

        # Try to remove the Twitter content element
        try:
            article.find(has_placeholder_twitter).decompose()
        except AttributeError:
            print("Twitter content not found")

        # Try to remove the related topics element
        try:
            divs = article.find_all_next(has_placeholder_related_topics)
            # Remove each div element from the soup object
            for div in divs:
                div.decompose()
        except AttributeError:
            print("Related topics not found")

        # Try to remove the footer element
        try:
            article.find("footer").decompose()
        except AttributeError:
            print("Footer element not found")

        # Find all the p elements inside the article
        paragraphs = article.find_all("p")

        # Join their text together with a newline character
        body = "\n".join(p.text for p in paragraphs)
        # Save title and body as JSON object in separate file
        # Use title as file name and add .json extension
        file_name = title + ".json"
        # Create JSON object with title and body keys
        json_object = {"title": title, "body": body}

        file_path = Path(ARTICLES_FOLDER, subfolder_article, file_name)
        file_path.parent.mkdir(parents=True, exist_ok=True)
        # Open file in write mode and dump JSON object into it
        with open(file_path, "w") as f:
            json.dump(json_object, f)
