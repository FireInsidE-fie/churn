import re

def extract_markdown_images(text):
    parsed_data = []
    images = re.findall(r"!\[[^\[\]]+]?\([^()]+\)", text)
    for image in images:
        alt_text = re.search(r"!\[[^\[\]]+]", image)
        url = re.search(r"\([^()]+\)", image)
        parsed_data.append((alt_text, url))
    return parsed_data