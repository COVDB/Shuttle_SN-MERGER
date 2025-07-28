## Shuttle_SN-MERGER Streamlit Excel App

Deze Streamlit-app verwerkt drie Excel-bestanden (AM LOG, ZSD_PO_PER_SO, ZSTATUS) en genereert een downloadbaar bestand met gefilterde en gemergede data voor aftersales doeleinden.

## Functionaliteit

- Upload drie Excel-bestanden via de sidebar.
- Kies het gewenste output-formaat: **CSV**, **XLSX** of **tabulator TXT**.
- Bekijk previews van de ingelezen data en van de gefilterde/mergede data.
- Preview van het uiteindelijke downloadbare document.
- Download het finale bestand met de juiste kolomnamen en data.

## Kolommen in de finale output

| Kolomnaam | Omschrijving |
|-----------|--------------|
| Equipment Number | Leeg veld |
| Date valid from | Datum van aanmaak bestand |
| Equipment category | Altijd "S" |
| Description | Uit ZSD-bestand, gefilterd |
| Sold to partner | Uit ZSTATUS-bestand |
| Ship to partner | Uit ZSTATUS-bestand |
| Material Number | Uit gefilterde data |
| Serial number | Uit gefilterde data |
| Begin Guarantee | Berekend: "Date OKWV" + 2 maanden |
| Warranty end date | Berekend: afhankelijk van "CoSPa" |
| Indicator, Whether Technical Object Should Inherit Warranty | Altijd "X" |
| Indicator: Pass on Warranty | Altijd "X" |
| Construction year | Jaar van levering |
| Construction month | Maand van levering |

## Gebruik

1. Start de app vanuit de hoofdmap:
    ```
    streamlit run src/app.py
    ```
2. Upload de drie Excel-bestanden via de sidebar.
3. Kies het gewenste output-formaat.
4. Klik op **Process Files**.
5. Controleer de previews.
6. Download het finale bestand.

## Dependencies

- `streamlit`
- `pandas`
- `xlsxwriter` (voor XLSX-export, toegevoegd aan `requirements.txt`)

## Opmerkingen

- Zorg dat je de app start vanuit de hoofdmap van het project zodat alle paden kloppen.
- Alle kolomnamen in de download zijn exact zoals hierboven beschreven.


