import pandas as pd

def load_am_log(file_path):
    return pd.read_excel(file_path)

def load_zsd_po_per_so(file_path):
    return pd.read_excel(file_path)

def load_zstatus(file_path):
    return pd.read_excel(file_path)