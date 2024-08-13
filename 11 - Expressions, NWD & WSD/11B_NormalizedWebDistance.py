# pip install pandas
# pip install textdistance
# pip install scikit-learn
# pip install sklearn

import numpy as np
import re
import textdistance
import sklearn
from sklearn.cluster import AgglomerativeClustering

# List of texts to be clustered
texts = ['Reliance supermarket', 'Reliance hypermarket', 'Reliance', 'Reliance', 'Reliance downtown', 'Reliance market',
         'Mumbai', 'Mumbai Hyper', 'Mumbai dxb', 'mumbai airport', 'k.m trading', 'KM Trading', 'KM trade',
         'K.M. Trading', 'KM.Trading']


def normalize(text):
    """ Keep only lower-cased text and numbers """
    return re.sub('[^a-z0-9]+', ' ', text.lower())


def group_texts(texts, threshold=0.4):
    """ Replace each text with the representative of its cluster """
    # Normalize the texts
    normalized_texts = np.array([normalize(text) for text in texts])

    # Compute the distance matrix using Jaro-Winkler distance
    distances = 1 - np.array([
        [textdistance.jaro_winkler(one, another) for one in normalized_texts]
        for another in normalized_texts])

    # Perform agglomerative clustering
    clustering = AgglomerativeClustering(
        distance_threshold=threshold,  # This parameter needs to be tuned carefully
        metric="precomputed", linkage="complete", n_clusters=None
    ).fit(distances)

    # Find the representative text for each cluster
    centers = dict()
    for cluster_id in set(clustering.labels_):
        index = clustering.labels_ == cluster_id
        centrality = distances[:, index][index].sum(axis=1)
        centers[cluster_id] = normalized_texts[index][centrality.argmin()]

    # Replace each text with the representative of its cluster
    return [centers[i] for i in clustering.labels_]


# Print the grouped texts
print(group_texts(texts))
