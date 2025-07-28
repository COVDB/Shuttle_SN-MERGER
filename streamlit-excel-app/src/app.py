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

            # Zorg dat de merge kolommen strings zijn en verwijder .0 indien nodig
            filtered_am_log["Customer Reference"] = filtered_am_log["Customer Reference"].astype(str).str.strip()
            zsd_po_data["Purch.Doc."] = zsd_po_data["Purch.Doc."].apply(lambda x: str(int(x)) if pd.notnull(x) and str(x).endswith('.0') else str(x)).str.strip()

            # Merge gefilterde AM LOG met ZSD_PO_PER_SO op Customer Reference / Purch.Doc.
            merged_data = filtered_am_log.merge(
                zsd_po_data,
                left_on="Customer Reference",
                right_on="Purch.Doc.",
                how="inner"
            )

            # Selecteer gewenste kolommen uit beide datasets
            output_data = merged_data[[
                "Serial number",
                "Customer Reference",
                "Delivery Date",
                "Material",
                "Document"
            ]]

            st.subheader("Gecombineerde Output Data")
            st.dataframe(output_data)
            st.write(f"Aantal lijnen in output: {len(output_data)}")
            
            # Tweede filter: alleen gewenste Material referenties
            allowed_materials = [
                "ATL3.2_12X8N/H", "ATL3.3_12X10CM", "ATL3.3_12X12N/H", "ATL3.3_12X10C", "ATL3.3_12X10N",
                "ATL3.3_12X8C", "ATL3.3_12X8N", "ATL3.3_10X12N", "ATL3.3_12X8NM", "ATL3.3_115X100N",
                "ATL3.3_12X10NM", "ATL3.3_12X12N UL", "ATL3.3_12X10NM/H", "ATL3.3_12X8N/H", "ATL3.3_12X8N/L1",
                "ATL3.3_12X10NW", "ATL3.3_10X12N FCC", "ATL3.3_12X10N/H", "ATL3.3_12X8NM/H", "ATL3.3_12X8C/H",
                "ATL3.3_114X114N", "ATL3.3_12X12NW", "ATL3.3_114X114N/H", "ATL3.3_12X12N", "ATL3.3_10X12C FCC",
                "ATL3.3_10X12C UL", "ATL3.2_12X10N", "ATL3.2_12X10C", "ATL3.3_10X12N UL", "ATL3.3_12X10NM/L1",
                "ATL3.2_12X8C", "ATL3.3_12X10CC", "ATL3.2_12X10N/H", "ATL3.2_12X8N", "NST-ATL3.2-0000001",
                "ATL3.2_10X12N UL", "ATL3.3_116X116C", "ATL3.2_12X10NS", "ATL3.3_114X114C", "ATL3.1_12X10N",
                "ATL3.3_12X8NW UL", "ATL3.2_12X12N", "ATL3.2_116X116N", "ATL3.2_12X10NM", "ATL3.2_10X12C UL",
                "ATL3.3_12X12C", "ATL3.2_12X8NS/H", "ATL3.3_12X8NW/H", "ATL3.3_12X8CW", "ATL3.2_114X114N",
                "ATL3.2_12X8NM/H", "ATL3.2_10X12CC UL", "ATL3.2_12X12N UL", "ATL3.2_10X12N", "ATL3.2_12X10NW",
                "ATL3.2_12X8NM", "ATL3.2_115X100N", "ATL3.2_12X10NM/H", "ATL3.1_12X8N", "ATL3.2_12X12C",
                "ATL3.2_10X12C", "ATL3.2_12X8NS", "ATL3.1_12X10C", "ATL3.2_12X10C UL", "ATL3.2_12X10C/H",
                "ATL3.2_116X116NN", "ATL3.1_12X10NS", "ATL3.2_12X10CC", "ATL3.2_12X10NS/H", "ATL3.2_12X10NW/H",
                "ATL3.1_114X114N", "ATL3.2_115X100NS", "ATL3.2_114X114NS", "ATL3.1_12X8C", "ATL3.1_12X12N",
                "ATL3.1_114X114C", "ATL03_12X10N"
            ]
            output_data = output_data[output_data["Material"].isin(allowed_materials)]

            # Voeg Year en Month of construction toe
            output_data["Delivery Date"] = pd.to_datetime(output_data["Delivery Date"], errors="coerce")
            output_data["Year of construction"] = output_data["Delivery Date"].dt.year
            output_data["Month of construction"] = output_data["Delivery Date"].dt.month

            st.subheader("Gecombineerde Output Data (na Material-filter)")
            st.dataframe(output_data)
            st.write(f"Aantal lijnen in output: {len(output_data)}")

            # Merge met ZSTATUS op "Document"
            zstatus_data["Document"] = zstatus_data["Document"].astype(str).str.strip()
            output_data["Document"] = output_data["Document"].astype(str).str.strip()

            final_output = output_data.merge(
                zstatus_data[["Document", "Sold-to pt", "Ship-to", "CoSPa", "Date OKWV"]],
                on="Document",
                how="left"
            )

            # Voeg "Begin Guarantee" toe: "Date OKWV" + 2 maanden
            final_output["Date OKWV"] = pd.to_datetime(final_output["Date OKWV"], errors="coerce")
            final_output["Begin Guarantee"] = final_output["Date OKWV"] + pd.DateOffset(months=2)

            # Bereken "Warranty end date"
            # Eerst "Begin Guarantee" terug naar datetime voor berekening
            begin_guarantee_dt = pd.to_datetime(final_output["Begin Guarantee"], format="%d-%m-%Y", errors="coerce")
            final_output["Warranty end date"] = begin_guarantee_dt + pd.to_timedelta(
                final_output["CoSPa"].apply(lambda x: 2*365 if str(x).strip() == "DE" else 365), unit="D"
            )
            final_output["Warranty end date"] = final_output["Warranty end date"].dt.strftime("%d-%m-%Y")

            # Zet datumkolommen om naar DD-MM-YYYY formaat
            final_output["Delivery Date"] = final_output["Delivery Date"].dt.strftime("%d-%m-%Y")
            final_output["Date OKWV"] = final_output["Date OKWV"].dt.strftime("%d-%m-%Y")
            final_output["Begin Guarantee"] = final_output["Begin Guarantee"].dt.strftime("%d-%m-%Y")

            st.subheader("Final Output Data (met ZSTATUS info, Begin Guarantee en Warranty end date)")
            st.dataframe(final_output)
            st.write(f"Aantal lijnen in final output: {len(final_output)}")
        else:
            st.error("Please upload all three Excel files.")

if __name__ == "__main__":
    main()