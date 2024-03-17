from flask import Flask, render_template, jsonify
import main
import webview

app = Flask(__name__)

subj1 = ""
ab1 = ""
subj2 = ""
ab2 = ""

@app.route('/')
def index():
    initial_text = "Initial Text"
    return render_template('index.html', initial_text=initial_text)

@app.route('/change_text')
def change_text():
    global subj1
    global ab1
    global subj2
    global ab2
    subj1 = main.getFighter()
    ab1 = main.getPower()
    subj2 = main.getFighter()
    ab2 = main.getPower()


    return jsonify(text1=subj1, text2=ab1, text3=subj2, text4=ab2)



@app.route('/gen_image')
def gen_image():
    url = main.GenerateImage(subj1, subj2, ab1, ab2)
    return jsonify(url=url)


if __name__ == '__main__':
    #app.run(debug=True)
    webview.create_window("MEGA BATTLE", app, width=1920, height=1080, resizable=False)
    webview.start()
