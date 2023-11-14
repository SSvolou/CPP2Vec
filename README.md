# CPP2Vec
CPP2Vec is a Word2Vec-based CPP prediction method, designed for handling: CPP-Classification, Uptake-Efficiency and PMO-Delivery tasks.

## Requirements
The scripts are written in Python 3.8.8 (Anaconda Version==4.11.0) and run on Ubuntu 18.04.6 LTS (GNU/Linux 5.10.0-23-amd64 x86_64).

- To construct our proposed models we utilised the following Python packages:
```
numpy==1.23.5
pandas==1.5.2
scikit_learn==1.0.2
scipy==1.10.0
pytorch==1.9.0
seaborn==0.13.0
matplotlib==3.6.2
notebook==6.5.2
Pillow==9.3.0
gensim==4.0.1
```
## Table of Contents
- ./Data: the processed datasets that we used in our study.
- ./Proposed models: all the models (Word2Vec and Machine Learning) we propose to predict unknown CPP sequences.
- ./Notebooks: Jupyter notebooks that can be used to evaluate our proposed trained models.
- ./Results: includes the calculated evaluation metrics and PCA plots for Validation and Test Datasets.
