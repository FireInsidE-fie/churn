import re

def extract_markdown_images(text):
    parsed_data = []
    images = re.findall(r"!\[[^\[\]]+]?\([^()]+\)", text)
    if not images:
        return None
    for image in images:
        alt_text = re.findall(r"!\[[^\[\]]+]", image)[0][2:-1]
        url = re.findall(r"\([^()]+\)", image)[0][1:-1]
        parsed_data.append((alt_text, url))
    return parsed_data

def extract_markdown_links(text):
    parsed_data = []
    links = re.findall(r"\[[^\[\]]+]?\([^()]+\)", text)
    if not links:
        return None
    for link in links:
        alt_text = re.findall(r"\[[^\[\]]+]", link)[0][1:-1]
        url = re.findall(r"\([^()]+\)", link)[0][1:-1]
        parsed_data.append((alt_text, url))
    return parsed_data
