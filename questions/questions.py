import nltk
import sys
import os
import math
import string
import heapq

FILE_MATCHES = 1
SENTENCE_MATCHES = 1


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python questions.py corpus")

    # Calculate IDF values across files
    files = load_files(sys.argv[1])
    file_words = {
        filename: tokenize(files[filename])
        for filename in files
    }
    file_idfs = compute_idfs(file_words)

    # Prompt user for query
    query = set(tokenize(input("Query: ")))

    # Determine top file matches according to TF-IDF
    filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES)

    # Extract sentences from top files
    sentences = dict()
    for filename in filenames:
        for passage in files[filename].split("\n"):
            for sentence in nltk.sent_tokenize(passage):
                tokens = tokenize(sentence)
                if tokens:
                    sentences[sentence] = tokens

    # Compute IDF values across sentences
    idfs = compute_idfs(sentences)

    # Determine top sentence matches
    matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
    for match in matches:
        print(match)


def load_files(directory):
    """
    Given a directory name, return a dictionary mapping the filename of each
    `.txt` file inside that directory to the file's contents as a string.
    """
    files = {}
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            with open(os.path.join(directory, filename), encoding="utf8") as f:
                files[filename] = f.read()
    return files


def tokenize(document):
    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.

    Process document by coverting all words to lowercase, and removing any
    punctuation or English stopwords.
    """
    words = nltk.word_tokenize(document.lower())
    return list(filter(lambda word: word not in nltk.corpus.stopwords.words('english') and word not in string.punctuation, words))


def compute_idfs(documents):
    """
    Given a dictionary of `documents` that maps names of documents to a list
    of words, return a dictionary that maps words to their IDF values.

    Any word that appears in at least one of the documents should be in the
    resulting dictionary.
    """
    idfs = {}
    for document in documents:
        for word in set(documents[document]):
            idfs.setdefault(word, 0)
            idfs[word] += 1
    for word in idfs:
        idfs[word] = math.log(len(documents) / idfs[word])
    return idfs


def top_files(query, files, idfs, n):
    """
    Given a `query` (a set of words), `files` (a dictionary mapping names of
    files to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the filenames of the the `n` top
    files that match the query, ranked according to tf-idf.
    """
    return sorted(files, key=lambda filename: tfidf(query, files[filename], idfs), reverse=True)[:n]


def tfidf(query, document, idfs):
    """
    Compute the TF-IDF score of a `document` relative to a `query`:
    """
    score = 0
    for word in query:
        if word in document:
            score += idfs[word] * document.count(word)
    return score


def top_sentences(query, sentences, idfs, n):
    """
    Given a `query` (a set of words), `sentences` (a dictionary mapping
    sentences to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the `n` top sentences that match
    the query, ranked according to idf. If there are ties, preference should
    be given to sentences that have a higher query term density.
    """
    results = []  # list of tuples (score, query_density, sentence)
    for sentence in sentences:
        score = idf(query, sentences[sentence], idfs)
        query_density = len([1 for word in sentences[sentence]
                            if word in query]) / len(sentences[sentence])

        cur_lowest_score, cur_lowest_query_density, _ = results[0] if results else (
            float('-inf'), float('-inf'), None)
        if len(results) < n:
            heapq.heappush(results, (score, query_density, sentence))
        # This check can be skipped as we are using a min heap, the first element is always the lowest. However, this is done to avoid the need to sort the heap
        elif score > cur_lowest_score or (score == cur_lowest_score and query_density > cur_lowest_query_density):
            heapq.heappushpop(results, (score, query_density, sentence))
    return [result[2] for result in heapq.nlargest(n, results)]


def idf(query, document, idfs):
    """
    Compute the IDF score of a `document` relative to a `query`:
    """
    score = 0
    for word in query:
        if word in document:
            score += idfs[word]
    return score


if __name__ == "__main__":
    main()
