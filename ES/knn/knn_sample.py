import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

best_k = 10

iris = pd.read_csv('iris.csv')
print(iris[20:25])


X = iris.drop(columns=['species'])
Y = iris['species']

print(X[20:25])
print(Y[20:25])

X_train, X_val, Y_train, Y_val = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=20)

scaler = StandardScaler()
scaler.fit_tranform(X_train)
scaler.transform(X_val)

KNN_model = KNeighborsClassifier(n_neighbors=best_k, n_jobs=-1)
KNN_model.fit(X_train, Y_train)

pred = KNN_model.predict(X_val)
print("Accuracy={}%".format(sum(Y_val == pred) / Y_val.shape[0] * 100))


from sklearn import neighbors 
from sklearn.metrics import f1_score,confusion_matrix,roc_auc_score
f1_list=[]
k_list=[]
for k in range(1,10):
    clf=neighbors.KNeighborsClassifier(n_neighbors=k,n_jobs=-1)
    clf.fit(X_train,Y_train)
    pred=clf.predict(X_val)
    f=f1_score(Y_val,pred,average='macro')
    f1_list.append(f)
    k_list.append(k)


best_f1_score=max(f1_list)
best_k=k_list[f1_list.index(best_f1_score)]        
print("Optimum K value=",best_k," with F1-Score=",best_f1_score)


KNN_model=neighbors.KNeighborsClassifier(n_neighbors=3,n_jobs=-1)
KNN_model.fit(X_train,Y_train)
pred=KNN_model.predict(X_val)
print("Accuracy={}%".format((sum(Y_val==pred)/Y_val.shape[0])*100))