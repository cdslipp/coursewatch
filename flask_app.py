from flask import Flask, render_template, request
import instuff

app = Flask(__name__)
app.debug = True

@app.route('/')
def main():
    return render_template('index.html')
@app.route('/send', methods=['GET','POST'])
def send():
    if request.method == 'POST':
        courCode = request.form['courCode']
        courNum = request.form['courNum']
        section = request.form['section']
        emailAddr = request.form['email']
        dbSetter.saveForm(courCode,courNum,section,emailAddr)
        return render_template('thanks.html',email=emailAddr)
    else:
        return render_template('index.html')

@app.route('/email')
def email():
    return render_template('email.html')

@app.route('/text')
def text():
    return render_template('text.html')

@app.route('/email/send', methods=['GET','POST'])
def send():
    if request.method == 'POST':
        courCode = request.form['courCode']
        courNum = request.form['courNum']
        section = request.form['section']
        emailAddr = request.form['email']
        dbSetter.saveForm(courCode,courNum,section,emailAddr)
        return render_template('thanks.html',email=emailAddr)
    else:
        return render_template('index.html')

@app.route('/thanks')
def thanks():
    return render_template('thanks.html')

@app.route('/stop')
def stop():
    return render_template('stop.html')

if __name__ == '__main__':
    app.run()
