import os
import urllib.request
import cv2
import pytesseract
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

UPLOAD_FOLDER = 'static/uploads/'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

def main(path):
    img = cv2.imread(path)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    '''
    Each individual character selected
    text = pytesseract.image_to_boxes(img, config = cong)
    imgh,imgw,_ = img.shape
    for b in text.splitlines():
        b = b.split(' ')
        x,y,w,h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
        cv2.rectangle(img, (x,imgh - y), (w, imgh-h), (0, 255, 0), 1)
    '''

    imgh,imgw,_ = img.shape
    box = pytesseract.image_to_data(img)
    text = pytesseract.image_to_string(img)




    room_numbers = []
    for i in text:
        if(i == "0" or i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9"):
            room_numbers += i



    print(room_numbers[1:49])
    for i, b in enumerate(box.splitlines()):
        if i!= 0:
            b = b.split()
            if len(b) == 12:
                x,y,w,h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                cv2.circle(img, (x+w,y+h), 2, (0, 0, 255), 5)


    cv2.imwrite('static/uploads/tracked.jpg', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()





@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        f = request.files['school-img']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        full_filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        main(full_filename)
        return render_template("index.html", school_img = 'static/uploads/tracked.jpg')
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
