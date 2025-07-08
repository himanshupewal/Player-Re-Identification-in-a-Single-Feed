import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def compute_similarity(bbox1, bbox2):
    #bbox1 (list): [x1, y1, x2, y2]
    #bbox2 (list): [x1, y1, x2, y2]
    b1 = np.array(bbox1).reshape(1, -1)
    b2 = np.array(bbox2).reshape(1, -1)
    sim = cosine_similarity(b1, b2)
    return sim[0][0]
