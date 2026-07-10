import pandas as pd
def find_s_algorithm(file_path):
     data = pd.read_csv(file_path)
     print("Training data:")
     print(data)
     attributes = data.columns[:-1]
     class_label = data.columns[-1]
     hypothesis = ['?' for _ in attributes]
     for index, row in data.iterrows():
         if row[class_label] == 'yes':
             for i, value in enumerate(row[attributes]):
                 if hypothesis[i] == '?' or hypothesis[i] == value: 
                     hypothesis[i] = value
                 else:
                     hypothesis[i] = '?'
                     return hypothesis
file_path =' C:/Users/DELL/Desktop/cd040/Downloads/data.csv'
hypothesis = find_s_algorithm("C:/Users/DELL/Desktop/cd040/Downloads/data.csv")

print("\nThe final hypothesis is:", hypothesis)

