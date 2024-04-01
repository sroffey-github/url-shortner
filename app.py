from flask import Flask, render_template, request, flash
import shortner

app = Flask(__name__)
app.secret_key = 'roffey'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        long_url = request.form['long_url']
        if len(long_url) > 0:
            short_url = shortner.shorten_url(long_url)
            if short_url == False:
                flash('Error creating short Url')
                return render_template('index.html')
            else:
                return render_template('index.html', short_url=short_url)
        else:
            flash('Error, Invalid Url')
            return render_template('index.html')
    else:
        return render_template('index.html')
    
if __name__ == '__main__':
    app.run(debug=True)