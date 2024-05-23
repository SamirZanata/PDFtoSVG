from flask import Flask, request, send_file
import os
import fitz  

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
@app.route('/', methods=['GET'])
def index():
    return "Welcome to the PDF to SVG Converter"
@app.route('/convert', methods=['POST'])
def convert_pdf_to_svg():
    if 'file' not in request.files:
        return "No file part in the request", 400
    
    file = request.files['file']
    
    if file.filename == '':
        return "No selected file", 400
    
    if file:
        pdf_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(pdf_path)
        
        svg_file_name = pdf_path.replace('.pdf', '.svg')
        
        pdf_document = fitz.open(pdf_path)
        page = pdf_document.load_page(0)  
        svg_content = page.get_svg_image()

        with open(svg_file_name, "w") as svg_file:
            svg_file.write(svg_content)
        
        return send_file(svg_file_name, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
