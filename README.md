# CAP-Dataset-CSV-Converter
Convert CAP Dataset from EDF to CSV and reduce its size to 10% of original data

Steps:

1. Download dataset from https://physionet.org/content/capslpdb/1.0.0/ ( ~ 40.1 GB ) .
2. Extract ZIP
3. Put `minifier.py`, `files.py` and `requirements.txt` in dataset folder (inside `/cap-sleep-dataset-1.0.0/`)
4. Install requirements ( `pip install -r requirements.txt` )
5. Run `minifier.py`
6. Wait for 1000 years.

Notes:

1. Make sure your free diskspace is more than 100GB
2. Edit `files.py` if you want to work with only part of dataset. By default it will convert all edf files
3. It will take looong time to process. So if you decide to leave computer running, make sure your computer don't go to sleep automatically after some time.
