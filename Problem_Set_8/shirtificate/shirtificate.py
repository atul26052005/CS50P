from fpdf import FPDF

class Shirtificate(FPDF):
    def header(self):
        """Add a header with the title 'CS50 Shirtificate'"""
        self.set_font("Arial", "B", 24)
        self.cell(0, 20, "CS50 Shirtificate", ln=True, align="C")

def main():
    name = input("Name: ").strip()
    generate_shirtificate(name)

def generate_shirtificate(name):
    pdf = Shirtificate()
    pdf.set_auto_page_break(auto=False)
    pdf.add_page()

    # Add shirt image
    pdf.image("shirtificate.png", x=40, y=70, w=130)

    # Add name on top of the shirt
    pdf.set_font("Arial", "B", 22)
    pdf.set_text_color(255, 255, 255)  # White text
    pdf.text(70, 140, f"{name} took CS50")

    # Save PDF
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
