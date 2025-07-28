import streamlit as st
import pandas as pd
from utils.excel_loader import load_am_log, load_zsd_po_per_so, load_zstatus

def main():
    st.title("Excel File Upload and Processing")

    st.header("Upload Excel Files")
    am_log_file = st.file_uploader("Upload AM LOG Excel file", type=["xlsx"])
    zsd_po_file = st.file_uploader("Upload ZSD_PO_PER_SO Excel file", type=["xlsx"])
    zstatus_file = st.file_uploader("Upload ZSTATUS Excel file", type=["xlsx"])

    if st.button("Process Files"):
        if am_log_file and zsd_po_file and zstatus_file:
            am_log_data = load_am_log(am_log_file)
            zsd_po_data = load_zsd_po_per_so(zsd_po_file)
            zstatus_data = load_zstatus(zstatus_file)

            st.subheader("AM LOG Data")
            st.write(am_log_data)

            st.subheader("ZSD_PO_PER_SO Data")
            st.write(zsd_po_data)

            st.subheader("ZSTATUS Data")
            st.write(zstatus_data)
        else:
            st.error("Please upload all three Excel files.")

if __name__ == "__main__":
    main()