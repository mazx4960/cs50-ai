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
    print(f"Time taken (100 runs): {time_taken:.8f} seconds")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")

    ranks, time_taken = time_execution(iterate_pagerank, corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    print(f"Time taken (100 runs): {time_taken:.8f} seconds")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    
    ranks, time_taken = time_execution(eigen_pagerank, corpus, DAMPING)
    print(f"PageRank Results from Eigenvalue")
    print(f"Time taken (100 runs): {time_taken:.8f} seconds")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


if __name__ == "__main__":
    main()
