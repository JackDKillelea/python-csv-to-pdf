from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")

data_frame = pd.read_csv("data/topics.csv")

for index, row in data_frame.iterrows():
    pdf.add_page("P")
    pdf.set_font("Times", style="B", size=24)
    pdf.set_text_color(200, 0, 0)
    pdf.cell(w=0, h=12, txt=f"{row['Topic']}", align="L", ln=1)
    pdf.line(10, 21, 200, 21)
    blank_pages = row["Pages"] - 1
    for _ in range(blank_pages):
        pdf.add_page("P")

pdf.output("output.pdf")
