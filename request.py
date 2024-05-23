import os
import requests

url = "http://127.0.0.1:5000/convert"
input_pdf_file = 'exemple.pdf'

with open(input_pdf_file, 'rb') as pdf_file:
    files = {'file': pdf_file}
    response = requests.post(url, files=files)

if response.status_code == 200:

    pdf_filename = os.path.basename(input_pdf_file)

    output_svg_file = pdf_filename.replace('.pdf', '.svg')

    with open(output_svg_file, 'wb') as f:
        f.write(response.content)
    print("Arquivo SVG salvo com sucesso como:", output_svg_file)
else:
    print("Falha ao converter o arquivo PDF para SVG:", response.text)
