import collections
import os
import csv

data_dir = "~/Downloads/wpc"
# data_dir = "/Users/yuhuilin/Downloads/wpc"
ukwa_file = "classification.tsv"
ukwa_path = os.path.join(os.path.expanduser(data_dir), ukwa_file)

with open(ukwa_path) as tsvin:
    tsvin = csv.reader(tsvin, delimiter='\t')

    p_cats = []
    for row in tsvin:
        p_cats.append(row[0])
    cnt = collections.Counter(p_cats)
    print (cnt)
    print("length: {}".format(len(cnt.items())))
    for cat, num in cnt.most_common(10):
        print(cat)
