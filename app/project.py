from flask import Flask,render_template


app=Flask(__name__)

@app.route('/')
def index():
	return render_template('basic.html')

@app.route('/find')
def find():
	return render_template('find.html')

@app.route('/delete')
def delete():
	return render_template('basic.html')

if __name__=='__main__':
	app.run(debug=True)