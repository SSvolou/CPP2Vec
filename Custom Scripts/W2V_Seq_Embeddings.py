"""In this script we define the functions that we used to generate sequence embeddings given the Word2Vec model."""

import numpy as np
import pandas as pd
from gensim.models import word2vec
import scipy


def seq_balance(file, seqlen, index_col=None):
    
    # Takes as an input a dataset in .csv format and returns a dataframe where the sequences have all the same length (maximum).
    
    # file parameter: dataset to be analysed in .csv format.
    # seqlen parameter: the value of the largest peptide in length between training sequences.
    # index_col parameter: when "None" then it will start from 0 to add a new column.
    
    # Read and save amino acid sequences.
    df_ret = pd.read_csv(file, delimiter=';', index_col=index_col)
    seq = df_ret.loc[:, 'seq'].tolist()

    # Data trimming and padding. Fill up the sequence with "X"'s until reach seqlen or remove extra amino acids.
    for i in range(len(seq)):
        if len(seq) > seqlen:
            seq[i] = seq[i][0:seqlen]
        seq[i] = seq[i].ljust(seqlen, 'X')

    for i in range(len(seq)):
        df_ret.loc[i, 'seq'] = seq[i]
    return df_ret

def w2v_emb_gen(seq_list, w2v_model, kmer):
    
    # Generates and returns the embeddings of the sequences given the Word2Vec model. 
    
    # seq_list parameter: a list with all sequences after padding.
    # w2v_model parameter: to load Word2Vec model from proposed models
    # kmer parameter: Substring of length k contained within the amino acid sequences. Based on the task that is studied we provide an optimal value that arose after our experimentation.
    
    # Number of provided peptides on dataset.
    num_seq = len(seq_list)

    # Calculates sequence embeddings.
    for j in range(num_seq):
        seq = seq_list[j]
        if j == 0:
            seq_emb = np.array([np.array(w2v_model.wv[seq[i:i + kmer]]) for i in range(len(seq) - kmer + 1)])

        else:
            # A helpful array to save computed sequence embeddings before append them to sequence embedding array.
            seq_enc = np.array([np.array(w2v_model.wv[seq[i:i + kmer]]) for i in range(len(seq) - kmer + 1)])
            seq_emb = np.append(seq_emb, seq_enc, axis=0)

    seq_emb = seq_emb.reshape(num_seq, len(seq) - kmer + 1, -1)
    
    # Removes all the elements of length one from sequence embeddings.
    seq_emb = seq_emb.reshape(num_seq, 1, -1).squeeze()
    
    return seq_emb
