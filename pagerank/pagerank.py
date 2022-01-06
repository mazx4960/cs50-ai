import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


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
            transition_probabilities[link] += damping_factor / len(corpus[page])
    else:
        for link in corpus:
            transition_probabilities[link] += damping_factor / len(corpus)

    return transition_probabilities


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    cur = random.choice(list(corpus.keys()))
    visited = dict()
    for i in range(n):
        visited.setdefault(cur, 0)
        visited[cur] += 1
        transition_probabilities = transition_model(corpus, cur, damping_factor)
        cur = random.choices(list(transition_probabilities.keys()), weights=list(transition_probabilities.values()), k=1)[0]
    ranks = {page: visited[page] / n for page in visited}
    return ranks


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    epsilon = 0.001
    ranks = {page: 1 / len(corpus) for page in corpus}
    new_ranks = dict()
    while True:
        can_break = True
        for page in corpus:
            new_ranks[page] = (1 - damping_factor) / len(corpus)
            parent_links = [link for link in corpus if page in corpus[link]]
            for link in parent_links:
                new_ranks[page] += damping_factor * ranks[link] / len(corpus[link])
            if abs(new_ranks[page] - ranks[page]) > epsilon:
                can_break = False
        ranks = new_ranks.copy()
        if can_break:
            break
    return ranks


if __name__ == "__main__":
    main()
