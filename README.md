# Spacehw_python
Python apps for browsing NASA OSDR hardware data and creating vocabulary files

The data file osdr_short.json is a subset of NASA's Open Source Data Repository's (OSDR) hardware list. It
is a list of hardware items used in NASA's scientific missions. This set includes only the names and
descriptions of the items. The list is not readily available from NASA but I have compiled it from different souces.
Note also that it is only a snapshot from September 2024.

In this repository there are Jypyter Notebook and plain Python versions of browser app. They can be used to
browse the data file and to create vocabularies from the data.

## Browsing apps:
* osdr_browser3.ipynb
* osdr.py

## Vocabulary creation apps:
* osdr_vocabulary.ipynb
* vocab.py

Python 3 is required.

requirements.txt lists the needed Python packages, To install them locally or in a virtual environment, run:

`pip install -r requirements.txt`

If you are using Anaconda, you can install them in Anaconda Navigator. Note that most of the packages are dependcies to
other packages and Anaconda can resolve them automatically. The list of main packages:

* nltk==3.9.1
* numpy==2.1.1
* pandas==2.2.2
* tabulate==0.9.0

You might need to download some nltk resources manually. If you get any errors regarding nltk when running the programs, there
is usually a download command listed in the error message.

A list of nltk's word tags:
https://gist.github.com/amnrzv/9a701f419ad004e066e2d6007dae40ad
