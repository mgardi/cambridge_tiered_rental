from leven import levenshtein       
import numpy as np
from sklearn.cluster import DBSCAN
from ngram import NGram
import nltk

offset = 0

def assign_clusters(labels,column_name,dataset):
  global offset
  offset = max(labels)
  def get_cluster(k):
    global offset
    if k < 0:
      offset = offset + 1
      return offset
    else:
      return k

  return {dataset[i]:get_cluster(k) for i,k in enumerate(labels)}

def text_similarity(data,metric='lev',threshold=5): # an array of strings

  X = np.arange(len(data)).reshape(-1, 1)

  def jaccard_metric(x,y):
    i, j = int(x[0]), int(y[0])
    l = min(len(data[i]),len(data[j]))
    #print(data[i],":",data[j],(1.0 - NGram.compare(data[i][:l].strip(),data[j][:l].strip())) * 10)
    return (1.0 - NGram.compare(data[i][:l].strip(),data[j][:l].strip())) * 10 

  def lev_metric(x, y):
    i, j = int(x[0]), int(y[0])     # extract indices
    l = min(len(data[i]),len(data[j]))
    if l <= threshold:
      return 999
    else:
      return levenshtein(data[i][:l].strip(), data[j][:l].strip())

  if metric == 'lev':
    return DBSCAN(threshold, metric=lev_metric, min_samples=2, algorithm='ball_tree').fit(X)
  else:
    return DBSCAN(threshold, metric=jaccard_metric, min_samples=2, algorithm='ball_tree').fit(X)

def cluster_strings(myColumnArray,column_name,metric='lev',threshold=5):
  clusters = text_similarity(myColumnArray,metric,threshold)
  print("rows:",len(clusters.labels_),"clusters:",max(set(clusters.labels_)))
  return assign_clusters(clusters.labels_,column_name,myColumnArray) 