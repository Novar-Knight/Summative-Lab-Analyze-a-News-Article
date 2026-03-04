import collections
import re


# Count the number of occurrences of a specific word in a text
def count_specific_word(article, search_word):
    """
    Returns the number of times search_word appears in article.
    Case-insensitive.
    Returns 0 if no matches are found.
    """
    if not article or not search_word:
        return 0

    cleaned_text = re.sub(r"[^\w\s]", "", article)
    word_list = cleaned_text.lower().split()

    return word_list.count(search_word.lower())


# Identify the most common word in a text
def identify_most_common_word(article):
    """
    Returns the most common word in the article.
    Returns None if article is empty.
    """
    if not article.strip():
        return None

    cleaned_text = re.sub(r"[^\w\s]", "", article)
    word_list = cleaned_text.lower().split()

    if not word_list:
        return None

    most_common_word = collections.Counter(word_list).most_common(1)[0][0]
    return most_common_word


# Calculate average word length
def calculate_average_word_length(article):
    """
    Returns the average word length as a float.
    Excludes punctuation.
    Returns 0 for empty string.
    """
    if not article.strip():
        return 0.0

    cleaned_text = re.sub(r"[^\w\s]", "", article)
    word_list = cleaned_text.split()

    if not word_list:
        return 0.0

    total_letters = sum(len(word) for word in word_list)
    return total_letters / len(word_list)


# Count the number of paragraphs
def count_paragraphs(article):
    """
    Returns the number of paragraphs.
    Paragraphs are separated by empty lines.
    Returns 1 for empty string.
    """
    if not article.strip():
        return 1

    paragraphs = re.split(r"\n\s*\n", article.strip())
    return len(paragraphs)


# Count number of sentences
def count_sentences(article):
    """
    Returns the number of sentences.
    Sentences end with '.', '!', or '?'.
    Returns 1 for empty string.
    """
    if not article.strip():
        return 1

    sentences = re.findall(r"[.!?]+", article)
    return len(sentences)