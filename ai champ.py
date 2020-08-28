import pandas as pd
import numpy as np
import pdfplumber
import os


directory="/home/kite/Desktop/aichamp"
with pdfplumber.open(pdf_file) as pdf:
    for filename in os.listdir(directory):
        if filename.endswith(".pdf") :
            first_page = pdf.pages[0]
            data = first_page.extract_text()
data.pivot.to_csv('test.csv')
with open('test.csv') as f:
    print(f.read())
