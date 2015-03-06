import csv
from flask import Flask
from flask import render_template
app = Flask(__name__)


def get_csv():
	csv_path = './static/la-riots-deaths.csv' ##find the file
	csv_file = open(csv_path,'rb') ##open the file
		##Windows - "rb" for "read binary"
		##Mac -"r" for "read"

	csv_obj = csv.DictReader(csv_file) ##parse the file
	csv_list = list(csv_obj) ##return a list that won't disappear
	return csv_list

@app.route("/")
def index():
	template = 'index.html'
	##return render_template(template)
	object_list = get_csv()
	return render_template(template,object_list=object_list)


if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)