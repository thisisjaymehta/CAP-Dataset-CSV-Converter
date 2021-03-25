import numpy as np
import pandas as pd
import os

import mne

from files import files

print("Total {0} edf files".format(len(files)))

for i in files:

    print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
    print("[ACTION] Converting {0}.edf to {0}.csv".format(i))
    print()

    edf_name = i+".edf"
    csv_name = i+".csv"
    csv_min_name = i+"_min.csv"

    edf = mne.io.read_raw_edf(edf_name)
    header = ','.join(edf.ch_names)
    np.savetxt(csv_name, edf.get_data().T, delimiter=',', header=header)

    print()
    print("[STATUS] EDF converted to CSV")
    print()

    print()
    print("[ACTION] Minimizing {0}.csv to {0}_min.csv".format(i))
    print()

    df = pd.read_csv(csv_name)
    length = len(df)//10
    df = df[:length]
    df.to_csv(csv_min_name)

    print()
    print("[STATUS] CSV Minimized")
    print()

    print()
    print("[ACTION] Deleting original {0}.csv".format(i))
    print()

    os.remove(csv_name)

    print()
    print("[STATUS] Original CSV Deleted")
    print()
