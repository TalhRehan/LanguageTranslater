from flask import Flask,request,render_template
from langdetect import detect
from googletrans import  Translator,LANGUAGES


app = Flask(__name__)

def detect_and_translate(text,target_lang):
    result_lang = detect(text)
    translator = Translator()
    translate_text = translator.translate(text,dest=target_lang).text
    return result_lang,translate_text

@app.route('/')
def index():
    return render_template('index.html',languages = LANGUAGES)

@app.route('/trans',methods=['GET','POST'])
def trans():
    translation = ""
    detect_lang = ""
    if request.method == "POST":
        text = request.form['text']
        target_lang = request.form['target_lang']
        detect_and_translate(text,target_lang)
        detect_lang,translation = detect_and_translate(text,target_lang)
        return render_template('index.html', translation=translation,detect_lang=detect_lang,languages=LANGUAGES)






if __name__ == "__main__":
    app.run(debug=True, port=5001)
