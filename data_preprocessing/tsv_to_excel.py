import os
import pandas as pd

# bids_DIR = './'
bids_final = 'BIDS_final_new'

subs = [i for i in os.listdir(bids_final) if i.startswith('sub')]
print(subs)


# beh 

for sub in subs:
    behdata = os.path.join(bids_final, sub, 'beh')
    for name in os.listdir(behdata):
        if 'arrangement' in name and 'tsv' in name:
            arrangedata = os.path.join(behdata, name)
            print(arrangedata)




# arrangement example
# example
