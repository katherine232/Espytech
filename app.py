from flask import Flask, render_template, request
from data import Articles
import main


app = Flask(__name__)

Articles = Articles()


Budget = ""
Mobility =""
Use = ""

@app.route('/')
def start():
	return render_template('start.html')

@app.route('/home')
def home():
	return render_template('home.html')


@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/device')
def device():
	return render_template('device.html')

@app.route('/builds')
def builds():
    return render_template('builds.html')


@app.route('/', methods=['POST'])
def getValue():
	
	Budget = request.form['Range']

	Mobility = request.form['Mobility']

	Use = request.form['Use']

	main.main(Budget,Mobility,Use)
	
	return render_template('builds.html',Budget=Budget,Mobility=Mobility,Use=Use)


@app.route('/articles')
def articles():

	return render_template('articles.html', articles = Articles )


@app.route('/article/<string:id>/')
def article(id):
	return render_template('article.html', id=id)





if __name__ == '__main__':
	app.run(debug=True)
