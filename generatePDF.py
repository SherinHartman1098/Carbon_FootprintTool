
import datetime
import pdfkit
def save_html_as_pdf(html_file_path, output_pdf_path):
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    unique_filename = f"{output_pdf_path}_{timestamp}.pdf"

    
    options = {
    'page-size': 'A3',
    'viewport-size': '1920x1080',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': 'UTF-8',
    'no-outline': None,
    'enable-local-file-access': None,
    'orientation': 'Portrait'   
}

    try:
       
       
        pdfkit.from_file(html_file_path, unique_filename, options=options)
        print("PDF is downloaded successfully.")
    except Exception as e:
        print(f"Error occurred while downloading PDF: {e}")


