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
	theSources = request.args.getlist('source')
	theDestinations = request.args.getlist('destination')
	thePorts = request.args.getlist('port')
	sources = addSpaces(theSources)
	dests = addSpaces(theDestinations)
	ports = addSpaces(thePorts)
	output = formatValues(sources,dests,ports)
		
	return render_template('rules.html',
                            form=form,
							output=output)
							
def addSpaces(array):
	result=[]
	for a in array:
		if a != None:
			count = len(a)
			while count < 17:
				a += " "
				count += 1
			result.append(a)
		else:
			a = ""
			result.append(a)
	return result
	
def formatValues(mySources, myDests, myPorts):
	result =[]
	for i,source in enumerate(mySources):
		line = mySources[i] + myDests[i] + myPorts[i]
		result.append(line)
	return result