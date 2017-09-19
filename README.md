# gap-minder
Generate novel words to plug lexical gaps.

### Get started

1. Get words with definitions, e.g. [WordNet's tagged glosses](http://wordnet.princeton.edu/glosstag.shtml). Lines must be in format `word\tdefinition`, which you can get from WordNet's "merged" XML files (`/WordNet-3.0/glosstag/merged`) using the [formatting script](util/format_dict.py) in this repository. Be sure to edit the [config file](./config.txt) to match the locations for your in and out files.
2. Get word vectors, e.g. [pretrained GloVe vectors](https://nlp.stanford.edu/projects/glove/). In case you roll your own, the format of the first line should be `W D` where `W` is the vocabulary size and `D` is the vector dimension size, e.g. `50000 300`. Every line after that should contain a single token and its vector values, whitespace-separated, e.g. `give_up 1.2 -2.9 0.0...`.
3. TBC...

### References

Christiane Fellbaum. 1998. *WordNet: An Electronic Lexical Database*. Cambridge, MA: MIT Press.

George A. Miller. 1995. WordNet: A Lexical Database for English. *Communications of the ACM* 38(11): 39–41.

Jeffrey Pennington, Richard Socher, and Christopher D. Manning. 2014. [GloVe: Global Vectors for Word Representation](https://nlp.stanford.edu/pubs/glove.pdf).
