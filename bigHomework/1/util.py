#coding: utf-8

def count_f(y_pred, result):
    f = [[0, 0], [0, 0]]
    #相当于遍历y_pred X result <y_pred[0], result[0]> ...
    for i in xrange(0, len(result)):
        for j in xrange(0, len(result)):
            if result[i] == result[j]:
                #类相同
                if y_pred[i] == y_pred[j]:
                    #簇相同
                    f[1][1] = f[1][1] + 1
                else:
                    #簇不同:
                    f[1][0] = f[1][0] + 1
            else:
                #类不同
                if y_pred[i] == y_pred[j]:
                    #簇相同
                    f[0][1] = f[0][1] + 1
                else:
                    #簇相同
                    f[0][0] = f[0][0] + 1

    return [map(float, i) for i in f]

def ri(f):
    return (f[0][0]+f[1][1])/(f[0][0]+f[0][1]+f[1][0]+f[1][1])

def j(f):
    return (f[1][1])/(f[0][1]+f[1][0]+f[1][1])

def do_kmeans(datMat, result, n=3):
    '''
     get dataMat, n_clusters
     return set, ri, j
    '''
    from sklearn.cluster import KMeans
    from sklearn.metrics import adjusted_rand_score as ari
    i = 0
    pred=[]
    ari_count = []
    '''while i<6: 
        #做好多次以确认类标
        y_pred = KMeans(n_clusters=n, random_state=n).fit_predict(datMat)
        pred.append(y_pred)
        ari_count.append(ari(y_pred, result))
        i = i + 1
    '''
    y_pred = KMeans(n_clusters=n, random_state=n).fit_predict(datMat)
    #y_pred = pred[ari_count.index(max(ari_count))]
    f = count_f(y_pred, result)
    RI = ri(f)
    J = j(f)
    return y_pred, [RI, J]

def do_biKmeans(datMat, result, n=3):
    from kMeans import biKmeans
    from sklearn.metrics import adjusted_rand_score as ari
    import numpy as np
    import pandas as pd
    datMat = np.mat(datMat)
    i = 0
    pred=[]
    ari_count = []
    '''while i<6: 
            #做好多次以确认类标
        try:
            centList, clustAssing = biKmeans(datMat, n)
            y_pred = clustAssing.A[:, 0].astype(pd.np.int)
            pred.append(y_pred)
            ari_count.append(ari(y_pred, result))
        except:
            y_pred = []
            pred.append(y_pred)
            ari_count.append(0)
        i = i + 1
    '''
    centList, clustAssing = biKmeans(datMat, n)
    y_pred = clustAssing.A[:, 0].astype(pd.np.int)
    f = count_f(y_pred, result)
    RI = ri(f)
    J = j(f)
    return y_pred, [RI, J]
    