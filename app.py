import csv
from flask import Flask
from flask import abort
from flask import render_template
app = Flask(__name__)


def get_csv():
	csv_path = './static/la-riots-deaths.csv' #find the file
	csv_file = open(csv_path,'r') #open the file
		#Windows - "rb" for "read binary"
		#Mac -"r" for "read"

	csv_obj = csv.DictReader(csv_file) #parse the file
	csv_list = list(csv_obj) #return a list that won't disappear
	return csv_list

@app.route("/") #sets path to root (index.html)
def index():
	template = 'index.html'
	object_list = get_csv()
	return render_template(template,object_list=object_list)


@app.route('/<row_id>/')
def detail(row_id):
	template = 'detail.html'
	object_list = get_csv()
	for row in object_list: #loop through csv to find record matching row_id passed into URL
		if row['id'] == row_id: #pass out this row's data into detail.html's template
			return render_template(template, object=row)
	abort(404)		

#all functions must be run before these lines
if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)