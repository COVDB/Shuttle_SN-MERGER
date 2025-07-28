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

            # Filter AM LOG data
            material_numbers = [
                "000000000001001917", "000000000001001808", "000000000001001749", "000000000001001776",
                "000000000001001911", "000000000001001755", "000000000001001760", "000000000001001809",
                "000000000001001747", "000000000001001711", "000000000001001757", "000000000001001708",
                "000000000001001770", "000000000001001710", "000000000001001771", "000000000001001758",
                "000000000001007905", "000000000001001753", "000000000001001752", "000000000001008374",
                "000000000001001805", "000000000001001709", "000000000001008561", "000000000001008560",
                "000000000001001765", "000000000001001775", "000000000001009105", "000000000001001777",
                "000000000001001742", "000000000001001813", "000000000001009719"
            ]
            filtered_am_log = am_log_data[am_log_data["Material Number"].isin(material_numbers)][
                ["Serial number", "Customer Reference", "Delivery Date"]
            ]

            st.subheader("Gefilterde AM LOG Data")
            st.dataframe(filtered_am_log)
            st.write(f"Aantal overgebleven lijnen na filtering: {len(filtered_am_log)}")
        else:
            st.error("Please upload all three Excel files.")

if __name__ == "__main__":
    main()