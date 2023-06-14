import tabula
import PyPDF2
import pandas as pd

def find_keyword_page(pdf_path, keyword):
    with open(pdf_path, 'rb') as f:
        reader = PyPDF2.PdfFileReader(f)
        num_pages = reader.numPages
        
        for page in range(num_pages):
            text = reader.getPage(page).extractText()
            if keyword in text:
                return page + 1
    return None

def extract_tables_from_pdf(pdf_path, page, output_format="dataframe"):
    tables = tabula.read_pdf(pdf_path, pages=page, multiple_tables=True, output_format=output_format)
    return tables

def save_tables_to_csv(tables, output_prefix):
    for i, table in enumerate(tables):
        output_path = f"{output_prefix}_table_{i + 1}.csv"
        table.to_csv(output_path, index=False)

pdf_path = "asset/pdf/abl여30세.pdf"
keyword = "해약환급금 예시표"
page_with_keyword = find_keyword_page(pdf_path, keyword)

if page_with_keyword is not None:
    tables = extract_tables_from_pdf(pdf_path, page_with_keyword)
    save_tables_to_csv(tables, "extracted_table")
    print("Tables have been saved as CSV files.")
else:
    print(f"Keyword '{keyword}' not found in the PDF.")
