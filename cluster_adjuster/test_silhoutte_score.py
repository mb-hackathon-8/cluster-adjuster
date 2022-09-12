from statistics import mean
from sklearn import datasets, metrics
from sklearn.cluster import KMeans
import numpy as np

# Load Iris dataset to test on
X, y = datasets.load_iris(return_X_y=True)

# Fit and predict a KMeans with three clusters (example for Iris dataset)
# KMeans poorly distinguishes between label 0&2, but properly separates label 1 for this dataset.
identified_labels = KMeans(n_clusters=3, random_state=1).fit_predict(X)
#print("identified_clusters:", identified_labels)
#print("labels:", y)

# Determine overall silhouette score (mean over all samples)
#Note: if X is the DM itself (diagonal must be 0) the method is 'precomputed'
silhouette_avg = metrics.silhouette_score(X, identified_labels, metric='euclidean')
print(f"overall silhouette score: {silhouette_avg}")

# Determine silhouette value for each sample and then sort in a list per cluster
#Note: if X is the DM itself (diagonal must be 0) the method is 'precomputed'
sample_silhouette_values = metrics.silhouette_samples(X,identified_labels, metric='euclidean')

for i in range(3):
    ith_cluster_silhouette_values = sample_silhouette_values[identified_labels == i]
    i_th_cluster_mean = mean(ith_cluster_silhouette_values)
    print(f"{i}th cluster silhouette score: {i_th_cluster_mean}")
