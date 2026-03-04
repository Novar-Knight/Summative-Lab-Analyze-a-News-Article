import re
import collections


# 1️⃣ Count Specific Word (Substring Match)
def count_specific_word(article, search_word):

    if article == "" or search_word == "":
        return 0
    else:
        return article.lower().count(search_word.lower())


# 2️⃣ Identify Most Common Word (Must Use Regex)
def identify_most_common_word(article):

    if article == "":
        return None
    else:
        # Use regex to remove punctuation
        words = re.findall(r"\b\w+\b", article.lower())

        if len(words) == 0:
            return None

        counter = collections.Counter(words)
        return counter.most_common(1)[0][0]


# 3️⃣ Calculate Average Word Length
def calculate_average_word_length(article):

    if article == "":
        return 0.0

    words = re.findall(r"\b\w+\b", article)

    if len(words) == 0:
        return 0.0

    total_letters = 0

    # REQUIRED for loop
    for word in words:
        total_letters += len(word)

    return total_letters / len(words)


# 4️⃣ Count Paragraphs
def count_paragraphs(article):

    if article == "":
        return 1
    else:
        paragraphs = article.split("\n\n")
        count = 0

        # REQUIRED for loop (extra safety)
        for paragraph in paragraphs:
            if paragraph.strip() != "":
                count += 1

        return count


# 5️⃣ Count Sentences
def count_sentences(article):

    if article == "":
        return 1

    sentence_count = 0
    index = 0

    # REQUIRED while loop
    while index < len(article):
        if article[index] == "." or article[index] == "!" or article[index] == "?":
            sentence_count += 1
        index += 1

    return sentence_count