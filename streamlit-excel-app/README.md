# Streamlit Excel App

This project is a Streamlit application designed to upload and process three specific Excel files: AM LOG, ZSD_PO_PER_SO, and ZSTATUS. The application provides a user-friendly interface for users to interact with the data contained in these files.

## Project Structure

```
streamlit-excel-app
├── src
│   ├── app.py                # Main entry point of the Streamlit application
│   ├── utils
│   │   └── excel_loader.py   # Utility functions for loading and processing Excel files
│   └── types
│       └── __init__.py       # Custom types or data structures for the application
├── requirements.txt          # List of dependencies for the project
└── README.md                 # Documentation for the project
```

## Installation

To set up the project, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd streamlit-excel-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the Streamlit application, execute the following command in your terminal:
```
streamlit run src/app.py
```

Once the application is running, you can upload the three Excel files (AM LOG, ZSD_PO_PER_SO, ZSTATUS) through the provided interface. The application will process the data and display the results accordingly.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.