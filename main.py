from fpdf import FPDF
import pandas as pd
import streamlit as st

def set_main_page(row):
    pdf.add_page("P")
    pdf.set_font("Times", style="B", size=24)
    pdf.set_text_color(200, 0, 0)
    pdf.cell(w=0, h=12, txt=f"{row['Topic']}", align="L", ln=1)
    pdf.line(10, 21, 200, 21)

def set_footer(row, is_lined = False, position = 265):
    if is_lined:
        for i in range(21, 298, 10):
            pdf.line(10, i, 200, i)
    pdf.ln(position)
    pdf.set_font("Times", style="I", size=8)
    pdf.set_text_color(210, 210, 210)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

def set_blank_pages(row, is_lined = False):
    blank_pages = row["Pages"] - 1
    for _ in range(blank_pages):
        pdf.add_page("P")
        set_footer(row, is_lined, 278)


st.set_page_config(page_title="CSV to PDF Converter")

col1, gap, col2 = st.columns([1.5, 0.5, 1.5])
with col1:
    # Get the uploaded csv file
    uploadedFile = st.file_uploader("Upload a CSV File", type=['csv'], accept_multiple_files=False, key="fileUploader")

with col2:
    st.write("Please select your options below")
    st.checkbox(key="lines_checkbox", label="Add Lines")

    # Create a downloadable example for the user
    with open("data/topics.csv") as example:
        file_bytes = example.read()
        st.download_button("Download Example", file_bytes, "example.csv")

if uploadedFile:
    # Set up PDF
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(False, 0)

    # Read in content that has been uploaded
    data_frame = pd.read_csv(uploadedFile)

    # Check if the user wants the page to be lined or not
    is_lined = st.session_state.lines_checkbox

    # Create the PDF content
    for index, row in data_frame.iterrows():
        set_main_page(row)
        set_footer(row, is_lined)
        set_blank_pages(row, is_lined)

    # Convert PDF to downloadable format
    pdf_bytes = pdf.output(dest='S').encode('latin-1')
    st.download_button("Download Converted PDF", pdf_bytes, "output.pdf")
