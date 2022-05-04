from turtle import position
from flask import Flask, jsonify, request
import json
app = Flask(__name__)

desenvolvedores = [ {'id':'0','nome':'Pedro',
                     'habilidades':['Python','Flask']}
                   , {'id':'1','nome':'Lucas',
                      'habilidades':['SQL','Oracle']} ]


#devolve um desenvolvedor pelo ID, tambem altera e deleta um desenvolvedor
@app.route('/dev/<int:id>',methods=['GET','PUT','DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':    
        try:
            response = desenvolvedores[id]
            print(response)
        except IndexError:
            mensagem = ('Desenvolvedor com id {} nao encontrado'.format(id))
            response = {'status':'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido'
            response = {'status':'erro', 'mensagem': mensagem}
        return jsonify(response)
    
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    
    
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
    return jsonify({'status':'sucesso'})




#lista todos os desenvolvedorese permite registrar e incluir um novo desenvolvedor 
@app.route('/dev/', methods=['POST','GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify({'status':'sucesso','Mensagem':'Registro incluido'},desenvolvedores[posicao])
    elif request.method == 'GET':
        return jsonify(desenvolvedores)

if __name__ == '__main__':
    app.run(debug=True)