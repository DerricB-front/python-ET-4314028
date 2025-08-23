import pandas as pd

df1 = pd.read_csv("C:\\Users\\derik\\Downloads\\undersampled_kaggle_dataset\\undersampled_kaggle_dataset.csv")
df2 = pd.read_csv("C:\\Users\\derik\\Downloads\\undersampled_kaggle_dataset\\updated_pph.csv")

merged_df = pd.concat([df1, df2], ignore_index=True)

merged_df.to_csv('NewData.csv', index=False)