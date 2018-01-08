from flask import Flask, request, send_from_directory, render_template
app = Flask(__name__, static_url_path='', \
	static_folder='frontend/dist', \
	template_folder='frontend/dist')

@app.route('/')
def hello_world():
	# return app.send_static_file('index.html')
	return render_template('index.html')
	# return "Hello world"

if __name__ == '__main__':
	app.jinja_env.auto_reload = True
	app.config['TEMPLATES_AUTO_RELOAD']=True
	app.run(host='0.0.0.0',use_reloader=True)