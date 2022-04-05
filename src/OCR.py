import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
from doctr.io import DocumentFile
from doctr.models import ocr_predictor

import json
import matplotlib.pyplot as plt

def syn(result):
    synthetic_pages = result.synthesize()
    plt.imshow(synthetic_pages[0]); plt.axis('off'); plt.show()
def OCR(image):
    # Use a breakpoint in the code line below to debug your script.
    ssl._create_default_https_context = ssl._create_unverified_context
    model = ocr_predictor(pretrained=True)
    # PDF
    doc = DocumentFile.from_images(image)
    # Analyze
    result = model(doc)
    #result.show(doc)  # Press ⌘F8 to toggle the breakpoint.
    json_output = result.export()
    return json_output
    #print(json_output)
    #with open('res.json','w') as f:
    #    json.dump(json_output,f)
    #syn(result)
