import sys

from helper import *
from eigen import *
from random_surfer import *

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])

    ranks, time_taken = time_execution(sample_pagerank, corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    print(f"Time taken: {time_taken:.4f} seconds")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.8f}")

    ranks, time_taken = time_execution(iterate_pagerank, corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    print(f"Time taken: {time_taken:.4f} seconds")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.8f}")
    
    ranks, time_taken = time_execution(eigen_pagerank, corpus, DAMPING)
    print(f"PageRank Results from Eigenvalue")
    print(f"Time taken: {time_taken:.4f} seconds")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.8f}")


if __name__ == "__main__":
    main()
