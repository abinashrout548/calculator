#import operation as operation
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST']) # To render Homepage
def home_page():
    return render_template('index.html')

@app.route('/math', methods=['POST'])  # This will be called from UI
def math_operation():
    if (request.method == 'POST'):
        operation = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])

    if(operation=='add'):
        r=num1+num2
        #result=num1+num2+num3
        result= 'the sum of '+str(num1)+' and '+str(num2) + 'is '+str(r)
    if (operation == 'subtract'):
        r = num1 - num2
        result = 'the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
    if (operation == 'multiply'):
        r = num1 * num2
        result = 'the product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
    if (operation == 'divide'):
        r = num1 / num2
        result = 'the quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
    return render_template('results.html',result=result)


@app.route('/abinash', methods=['POST'])  # for calling the API from Postman/SOAPUI
def math_operation_abinash():
    if (request.method == 'POST'):
        # operation=request.json['operation']
        num0 = request.json['num0']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])
        num3 = int(request.json['num3'])
        if (operation == 'add'):
            r = num1 + num2
            result = 'the sum of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'subtract'):
            r = num1 - num2
            result = 'the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'multiply'):
            r = num1 * num2
            result = 'the product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'divide'):
            r = num1 / num2
            result = num1 * num2 + num0
            #result = 'the quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
        return render_template('results.html', result=result)
        result = num1 * num2 + num0
       # return render_template('results.html', result=result)




@app.route('/abinash2', methods=['POST'])
def math_abinash2():
    if (request.method == 'POST'):
        name = request.json['name']
        email = request.json['email']
        ph_no = request.json['ph_no']
        return jsonify(name + email + str(ph_no))


@app.route('/abinash3', methods=['POST'])
def math_abinash3():
    if (request.method == 'POST'):
        num0 = int(request.json['num0'])
        num2 = int(request.json['num2'])
        num1 = int(request.json['num1'])

        return jsonify(num0 + num2 + num1)


@app.route('/abinash4')
def url_test():
    test1 = request.args.get('val1')
    test2 = request.args.get('val2')
    test3 = test1 + test2

    return '''<h1>my result is : {}</h1>'''.format(test3)


@app.route('/url_function')
def url_function():
    test1 = request.args.get('val1')
    test2 = request.args.get('val2')
    test3 = int(test1) + int(test2)

    return '''result {} '''.format(test3)


if __name__ == '__main__':
    app.run()

