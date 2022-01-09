import numpy as np
import os
import re
import time


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    transition_probabilities = {}

    # every page have an equal opportunity of being picked
    for link in corpus:
        transition_probabilities[link] = (1 - damping_factor) / len(corpus)

    # probability of one of the links of the page being picked
    if corpus[page]:
        for link in corpus[page]:
            transition_probabilities[link] += damping_factor / \
                len(corpus[page])
    else:
        for link in corpus:
            transition_probabilities[link] += damping_factor / len(corpus)

    return transition_probabilities


def transition_matrix(corpus, damping_factor):
    """
    Return a transition matrix for this corpus. Transition probabilities
    should be stored in the order they appear in the corpus.
    """
    transition_matrix = []
    for link in corpus:
        probs = list(transition_model(corpus, link, damping_factor).values())
        transition_matrix.append(probs)
    return np.transpose(transition_matrix)


def normalize(vector):
    """
    Normalize a vector.
    """
    return vector / vector.sum()


def time_execution(func, *args, runs= 100):
    """
    Return the time it takes to execute the code.
    """
    start = time.time()
    for _ in range(runs):
        result = func(*args)
    end = time.time()
    return result, end - start
