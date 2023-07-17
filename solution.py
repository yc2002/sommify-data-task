import fasttext
from typing import List, Tuple
import re
import pandas as pd

# Load pre-trained language model
MODEL = fasttext.load_model('lid.176.bin')

# Pre-compiled regular expression to split on " - " or parentheses containing non-digits
SPLITTER = re.compile(" - | \((?!\d+\)).*?\)")

def extract_titles(titles: list[str]) -> list[tuple[str, str]]:
    """
    Args:
        titles (list): List of titles to be processed.
    Returns:
        non_english_titles (list): List of non-english titles.
        english_titles (list): List of english titles.
    """
    # Your code here
    result = []
    for title in titles:
        parts = [part for part in SPLITTER.split(title) if part and any(c.isalpha() for c in part)]

        # Initialize English and Non-English title variables as None
        english_title, non_english_title = None, None

        for part in parts:
            # Predict the part's language using the FastText model
            part_lang, _ = MODEL.predict(part, k=1)

            # If the part is in English, set it as the English title
            if '__label__en' in part_lang:
                english_title = part if english_title is None else title #If both parts are in English, use the entire title
            # If the part is not in English, set it as the Non-English title
            else:
                non_english_title = part if non_english_title is None else title #Vice versa

        result.append((english_title, non_english_title))

    return result
