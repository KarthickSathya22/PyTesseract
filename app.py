# Importing Libraries:
import pytesseract
from PIL import Image
# Path of the tesseract Engine:
pytesseract.pytesseract.tesseract_cmd = '/app/.apt/usr/bin/tesseract'
from flask import Flask,request,render_template,jsonify

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For rendering results on HTML GUI
    '''        
    #Uploading file:
    image1 = request.files['image1']
    
    # Recognize the text as string in image using pytesserct 
    text = str(((pytesseract.image_to_string(Image.open(image1))))) 
  
    # The recognized text is stored in variable text 
    # Any string processing may be applied on text 
    # Here, basic formatting has been done: 
    # In many PDFs, at line ending, if a word can't 
    # be written fully, a 'hyphen' is added. 
    # The rest of the word is written in the next line 
    # Eg: This is a sample text this word here GeeksF- 
    # orGeeks is half on first line, remaining on next. 
    # To remove this, we replace every '-\n' to ''. 
    text = text.replace('-\n', '')     
    
    return jsonify(prediction_text = text)

if __name__ == "__main__":
    app.run(debug=True)
