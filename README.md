# gap-minder
Generate novel words to plug lexical gaps.

### Get started

1. [Install conda](https://conda.io/docs/user-guide/install/index.html) if necessary and then navigate to this repo in a terminal and run `conda env create -f environment.yml`. Once the installation is complete, activate it with `source activate gap`. If you need to update `environment.yml`, you can update your installations with `conda env update -f environment.yml`.
2. For a demo trained on WordNet definitions and GloVe vectors trained on Common Crawl, you can run `python ./demo.py` from the home directory.

### Train your own word generator

3. Edit the [config file](./config.ini) to match the locations for your in and out files.
4. Get words with definitions, e.g. [WordNet's tagged glosses](http://wordnet.princeton.edu/glosstag.shtml). Lines must be in format `word\tdefinition`, which you can get from WordNet's "merged" XML files (`/WordNet-3.0/glosstag/merged`) using the [formatting script](util/format_wordnet.py) in this repository.
5. Get word vectors, e.g. [pretrained GloVe vectors](https://nlp.stanford.edu/projects/glove/). In case you roll your own, each line contain a single token and its vector values, whitespace-separated, e.g. `give_up 1.2 -2.9 0.0...`. If you use `word2vec` vectors, the first line of the vector file will by default record the size of the vocabulary and the vector length, but the scripts are written to ignore that line.
6. To train your own word creator, run `python ./train.py`. This will probably take a lot of time. You can run on GPU (rather than CPU, the default) by changing the `gpu = false` to `gpu = true` in the [config file](./config.ini).
7. To generate new words and definitions from your trained creator, run `python ./generate.py N` where `N` is the number of new words to generate. It's recommended to redirect this generation to some output file, e.g. `python ./generate.py 100 > new_words.txt`.

### References

Christiane Fellbaum. 1998. *WordNet: An Electronic Lexical Database*. Cambridge, MA: MIT Press.

George A. Miller. 1995. WordNet: A Lexical Database for English. *Communications of the ACM* 38(11): 39–41.

Jeffrey Pennington, Richard Socher, and Christopher D. Manning. 2014. [GloVe: Global Vectors for Word Representation](https://nlp.stanford.edu/pubs/glove.pdf).
