from fpdf import FPDF
import pandas as pd

def set_main_page(row):
    pdf.add_page("P")
    pdf.set_font("Times", style="B", size=24)
    pdf.set_text_color(200, 0, 0)
    pdf.cell(w=0, h=12, txt=f"{row['Topic']}", align="L", ln=1)
    pdf.line(10, 21, 200, 21)

def set_footer(row, is_lined, line_height = 0, position = 265):
    if is_lined == "y":
        for i in range(21, 298, line_height):
            pdf.line(10, i, 200, i)
    pdf.ln(position)
    pdf.set_font("Times", style="I", size=8)
    pdf.set_text_color(210, 210, 210)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

def set_blank_pages(row, is_lined, line_height = 0):
    blank_pages = row["Pages"] - 1
    for _ in range(blank_pages):
        pdf.add_page("P")
        set_footer(row, is_lined, line_height, 275)

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(False, 0)

data_frame = pd.read_csv("data/topics.csv")

is_lined = input("Do you want a lined PDF? (y/n) ").lower()
if is_lined == "y":
    line_height = input("Enter your line height: ")
else:
    line_height = 0

try:
    for index, row in data_frame.iterrows():
        set_main_page(row)
        set_footer(row, is_lined, int(line_height))
        set_blank_pages(row, is_lined, int(line_height))
except ValueError:
    print("Please enter valid inputs.")

pdf.output("output.pdf")
