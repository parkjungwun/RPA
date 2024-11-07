import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

# 상관분석 = 두 변수 간의 선형관계가 존재하는지 또는 존재하지 않는지를 분석 
# *변수들 간의 선형성의 강도에 대한 통계적 분석이라 할 수 있음
#  ex) 가계소득과 저축간 관계 흡연량과 폐암발병률 관계
# *인과성은 다른 이야기다
# 편차를 평균 낸 것이 분산.

w = pd.read_csv('ch5-1.csv')
print(w, end = "\n\n")
print(w.head(10), end="\n\n")

w_n = w.iloc[:,1:5]
print(w_n,end='\n\n')
w_cor = w_n.corr(method= 'pearson')
print(w_cor, end= '\n\n')

sns.pairplot(w_n)


plt.figure(figsize = (10,7))
sns.heatmap(w_cor, annot= True, cmap= 'Blues')
plt.show()