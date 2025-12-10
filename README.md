# CPP2Vec
**CPP2Vec** is a **Word2Vec-based prediction framework** for **Cell-Penetrating Peptides (CPPs)**.
It has been designed to handle three different tasks:

1. **CPP Classification** – Predict whether a peptide is a **CPP** or **Non-CPP**.
2. **Uptake Efficiency** – Predict the cellular uptake efficiency of CPPs (**High/Low**).
3. **PMO Delivery** – Predict the efficiency of CPPs in delivering PMOs (**1 = ≥ 3-fold improvement, 0 = < 3-fold improvement**).

You can run interactive tutorials for each task using the corresponding Jupyter Notebook:

| Task                 | Tutorial Notebook                          |
|----------------------|-------------------------------------------|
| **CPP Classification**   | [CPP2Vec_Classification_Tutorial_Notebook.ipynb](https://github.com/SSvolou/CPP2Vec/blob/main/Notebooks/CPP2Vec_Classification_Tutorial_Notebook.ipynb) |
| **Uptake Efficiency**    | [CPP2Vec_Uptake_Efficiency_Tutorial_Notebook.ipynb](https://github.com/SSvolou/CPP2Vec/blob/main/Notebooks/CPP2Vec_Uptake_Efficiency_Tutorial_Notebook.ipynb) |
| **PMO Delivery**         | [CPP2Vec_PMO_Delivery_Tutorial_Notebook.ipynb](https://github.com/SSvolou/CPP2Vec/blob/main/Notebooks/CPP2Vec_PMO_Delivery_Tutorial_Notebook.ipynb) |

[![DOI](https://zenodo.org/badge/716505452.svg)](https://doi.org/10.5281/zenodo.15401028)

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
- ./Data: the processed datasets that we used in our study & CPP2Vec-GenSet.
- ./Proposed models: all the models (Word2Vec and Machine Learning) we propose to predict unknown CPP sequences based on the task that is studied (CPP-Classification, Uptake-Efficiency and/or PMO-Delivery).
- ./Notebooks: Jupyter notebooks that can be used to evaluate our proposed trained models & Tutorial Notebooks.
- ./Results: includes the calculated evaluation metrics and PCA & UMAP plots for Validation and Test Datasets.
- ./Custom Scripts: contains Python Scripts that we used to construct and evaluate our proposed models.
