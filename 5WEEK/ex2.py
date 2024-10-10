import pandas as pd
import matplotlib.pylab as plt
import matplotlib.font_manager as font_manager

def addtext(x, y):
    for i in range(len(x)):
        plt.text(i, y[i] + 0.5, y[i], ha='center')

famous = pd.read_csv('singer_youtube.csv')
print(famous.head(), end="\n\n")

famous.columns = [col.replace(" ", "_") for col in famous.columns]
print(famous.columns)

font_path = "malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()

plt.rc('font', family=font_name)
plt.figure(figsize=(15, 10))
plt.bar(famous['name'], famous['youtube_count'], color=('red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple', 'black', 'white'))
plt.title('Famous Cherry Statistics')
plt.xlabel('Famous Cherry')
plt.ylabel('YouTube Count')

addtext(famous['name'], famous['youtube_count'])
plt.show()
