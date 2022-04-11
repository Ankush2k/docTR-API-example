import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
from doctr.io import DocumentFile
from doctr.models import ocr_predictor

import json
import matplotlib.pyplot as plt

'''
Plotting the result
def syn(result):
    synthetic_pages = result.synthesize()
    plt.imshow(synthetic_pages[0]); plt.axis('off'); plt.show()
'''
def check_file_type(name):
    try:
        lower_name = name.lower()
        if lower_name.__contains__('.pdf'):
            type='PDF'
        else:
            type = 'images'
        return type
    except Exception as e:
        return 'Error while detecting file type'

def OCR(file,type):
    try:
        ssl._create_default_https_context = ssl._create_unverified_context
        model = ocr_predictor(pretrained=True)
        # PDF
        if type == 'PDF':
            doc = DocumentFile.from_pdf(file)
        else:
            doc = DocumentFile.from_images(file)
        # Analyze
        result = model(doc)
        #result.show(doc)
        json_output = result.export()
        return json_output
    except Exception as e:
        return {'Error while executing OCR prediction, Check file type passed as images and pdf can be read by the model'}