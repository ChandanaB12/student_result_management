import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

#step1: Load the california Housing dataset from local directory
file_path = r"C:/Users/CHANDANA/Downloads/housing.csv"

#check if the file exists
if os.path.exists(file_path):
    data = pd.read_csv(file_path)
else:
    print(f"File not found:{file_path}")
    exit()
    
#step2:compute the correlation matrix
correlation_matrix=data.corr(numeric_only=True)

#step3: Visualize the correlation
plt.figure(figsize=(10,8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('correlation Matrix of califronia housing features')
plt.show()

#step4
sns.pairplot(data, diag_kind='kde',plot_kws={'alpha':0.5})
plt.suptitle('Pair plot of california housing features,y=1.02')
plt.show()
