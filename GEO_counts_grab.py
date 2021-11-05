import os
import pandas as pd

path = r"C:\Users\mythi\Documents\Work Google Drive\Research and Development projects\NASH liver RNA-seq\GSE135251_RAW"
newPath = path.replace("\\", "/")

print(newPath)

RNA_seq_read_counts = pd.DataFrame()
idx_list = []

for idx, file_name in enumerate(os.listdir(newPath)):
    if file_name.endswith(".txt"):
        file_path = newPath + "/" + file_name
        file_opened = pd.read_csv(file_path, delim_whitespace=True, header=None)
        print(idx)
        idx_list.append(2 * idx)
        RNA_seq_read_counts = pd.concat([RNA_seq_read_counts, file_opened], axis=1)

    else:
        pass

idx_list.pop(0)

RNA_seq_read_counts_2 = RNA_seq_read_counts
RNA_seq_read_counts_2.columns = range(RNA_seq_read_counts_2.shape[1])

RNA_seq_read_counts_2.drop(RNA_seq_read_counts_2.columns[idx_list], axis=1, inplace=True)

csv_file_path = newPath + "/RNA_seq_read_counts.csv"
RNA_seq_read_counts_2.to_csv(csv_file_path, header=False, index=False)
