from flask import Flask, request , render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__, template_folder ="UI")
bootstrap = Bootstrap(app)
users_list = [ ]

@app.route('/' ,methods=['GET'])
def index_page():
	return render_template('Index.html')



if __name__ == '__main__':
	app.run(debug=True)