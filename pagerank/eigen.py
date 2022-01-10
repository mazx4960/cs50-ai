import numpy as np
from numpy.linalg import eig

from helper import *


def eigen_pagerank(corpus, damping_factor):
    A = transition_matrix(corpus, damping_factor)
    w, v = eig(A)
    if abs(w[0].real - 1) <= 0.001:
        raise Exception("Eigenvalue is not 1")

    result = normalize(v[:, 0].real)
    ranks = {page: result[i] for i, page in enumerate(corpus)}
    return ranks
