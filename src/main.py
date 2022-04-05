# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import uvicorn
from fastapi import FastAPI,File,UploadFile
import OCR

app = FastAPI()

@app.post('/')
async def get_file(file: UploadFile=File(...)):
    content = await file.read()
    result = OCR.OCR(content)
    return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1',port=8000)

# uvicorn main:app --reload
