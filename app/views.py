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
    source = request.args['source']
    destination = request.args['destination']
    port = request.args['port']
    source2 = request.args['source2']
    destination2 = request.args['destination2']
    port2 = request.args['port2']
    source3 = request.args['source3']
    destination3 = request.args['destination3']
    port3 = request.args['port3']
    source4 = request.args['source4']
    destination4 = request.args['destination4']
    port4 = request.args['port4']
    source5 = request.args['source5']
    destination5 = request.args['destination5']
    port5 = request.args['port5']
    sourced = [source,source2,source3,source4,source5]
    destd = [destination,destination2,destination3,destination4,destination5]
    ports = [port,port2,port3,port4,port5]
    sources =[]
    dests=[]
    for source in sourced:
        count = len(source)
        while count < 15:
            source = source + " "
            count += 1
        sources.append(source)
    for dest in destd:
        count = len(dest)
        while count < 15:
            dest = dest + " "
            count += 1
        dests.append(dest)
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
