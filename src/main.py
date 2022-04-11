# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import uvicorn
from fastapi import FastAPI,File,UploadFile
import OCR

app = FastAPI()

@app.post('/ocr')
async def get_file(file: UploadFile=File(...)):
    doc_name = file.filename
    file_type = OCR.check_file_type(doc_name)
    content = await file.read()
    result = OCR.OCR(content,file_type)
    return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    uvicorn.run(app)

# uvicorn main:app --reload
