from app import app
from flask import render_template, redirect, url_for, request, session
from .forms import RuleForm
import urllib

@app.route('/')
@app.route('/index')
def index():
    form = RuleForm()
    if form.validate_on_submit():
        return redirect('/rules')
    return render_template('index.html',
                            form=form)

@app.route('/rules')
def rules():
	form = RuleForm()
	source = request.args.get('source')
	destination = request.args.get('destination')
	port = request.args.get('port')
	source1 = request.args.get('source1')
	destination1 = request.args.get('destination1')
	port1 = request.args.get('port1')
	source2 = request.args.get('source2')
	destination2 = request.args.get('destination2')
	port2 = request.args.get('port2')
	source3 = request.args.get('source3')
	destination3 = request.args.get('destination3')
	port3 = request.args.get('port3')
	source4 = request.args.get('source4')
	destination4 = request.args.get('destination4')
	port4 = request.args.get('port4')
	source5 = request.args.get('source5')
	destination5 = request.args.get('destination5')
	port5 = request.args.get('port5')
	source6 = request.args.get('source6')
	destination6 = request.args.get('destination6')
	port6 = request.args.get('port6')
	sourced = [source,source1,source2,source3,source4,source5,source6]
	destd = [destination,destination1,destination2,destination3,destination4,destination5,destination6]
	portd = [port,port1,port2,port3,port4,port5,port6]
	sources =[]
	dests=[]
	ports=[]
	for source in sourced:
		if source != None:
			count = len(source)
			while count < 15:
				source = source + " "
				count += 1
			sources.append(source)
		else:
			source = ""
			sources.append(source)
	for dest in destd:
		if dest != None:
			count = len(dest)
			while count < 15:
				dest = dest + " "
				count += 1
			dests.append(dest)
		else:
			dest = ""
			dests.append(dest)
	for port in portd:
		if port != None:
			ports.append(port)
		else:
			port = ""
			ports.append(port)
    #file2open = destination + ".txt"
    #f = open(file2open, "r")
    #text =[]
    #while 1:
    #    line = f.readline()
    #    if not line:break
    #    text.append(line)
    #f.close()
	return render_template('rules.html',
							form=form,
							sources=sources,
							dests=dests,
							ports=ports)
