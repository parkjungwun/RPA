import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
import seaborn as sns

hat = pd.read_csv('ch4-2.csv')

font_path = 'malgun.ttf'
font_name = font_manager.FontProperties(fname = font_path).get_name()
plt.rc('font', family = font_name)

plt.figure(figsize=(10, 17))
plt.subplot(1,2,1) # 한 화면에 출력 맨 뒤에 숫자에 따라서 출력되는 화면 순서가 달라짐 ex) 1 = 첫 번쨰
plt.hist(hat.weight,bins=7)
plt.title('B 부화장 병아리 무세 분포 현황', fontsize = 17)
plt.xlabel('병아리 무게(g)')
plt.ylabel('마릿 수')

#sns.distplot(hat.weight) 라인 히스토 그램으로 보기

#plt.show()

print("---------------------------------------------------------------")

# 상자그림 그리기

#plt.figure(figsize=(8,10))
plt.subplot(1,2,2) # 2 = 두 번째
plt.boxplot(hat.weight)
plt.title('B hatchery chick weight box', fontsize = 17)
plt.ylabel('weight(g)')
plt.show()

print(hat.describe(), end="\n\n")

