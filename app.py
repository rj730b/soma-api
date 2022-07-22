from flask import Flask, jsonify, request


"""
The variable __name__ is passed as first argument when
 creating an instance of the Flask object (a Python Flask application).
 In this case __name__ represents the name of the application package and 
 it’s used by Flask to identify resources like templates, static assets and the instance folder.
"""
app = Flask(__name__)
app.config.from_object(__name__)

# Sobre decorator @
# https://jucacrispim.wordpress.com/2013/12/22/python-escrevendo-decorators/
@app.route('/soma', methods=['POST']) # Rota soma que aceita o método Post
def soma(): # Função que soma dois números,  x e y
    try:
        postedData = request.get_json() # O request.get_json() converte o objeto JSON para dados do Python.
        x = int(postedData["x"])
        y = int(postedData["y"])

        response = x + y

        JSON_response = {
        'Message' : response,
        'Status Code ' : 200
        }
        return jsonify(JSON_response)

    except:
        JSON_response = {
        'Message' : "Não foi possível processar",
        'Status Code ' : 500
        }
        return jsonify(JSON_response)        
        """
        jsonify is a function in Flask's flask.json module. 
        jsonify serializes data to JavaScript Object Notation (JSON) format,
         wraps it in a Response object with the application/json mimetype.
        """

if __name__ == '__main__': 
    # Para compreender o que if __name__ == '__main__' faz.
    # http://devfuria.com.br/python/entenda-__name__-__main__/
    # https://pythonhelp.wordpress.com/2012/06/15/por-que-__name__-__main__/
    app.run()