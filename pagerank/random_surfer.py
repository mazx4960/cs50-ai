import random
from helper import *


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
