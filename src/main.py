import json
from src.invoice_generator import generate_invoice_content
from src.utils import output_invoice

if __name__ == "__main__":
    invoice_content = generate_invoice_content()
    output_invoice(invoice_content)
