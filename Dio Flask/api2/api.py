from os import execv
from flask import Flask, jsonify, request
import json

app = Flask(__name__)

lista_tarefa= [{
    'id':'0',
    'responsavel':'Pedro',
    'tarefa':'Lista da dio',
    'status':'Em andamento',
    },
    {
    'id':'1',
    'responsavel':'Pedro Lucas',
    'tarefa':'Lista de flask',
    'status':'Concluido'
    }
    ]

#********************************************************************#
@app.route('/', methods=['GET'])
def listar_tudo():
    if request.method=='GET':
        return jsonify(lista_tarefa)

#********************************************************************#
@app.route('/dev/<int:id>', methods=['GET','PUT'])
def consulta_por_id(id):
    if request.method == 'GET':
        try:
            consulta = lista_tarefa[id]
        except IndexError:
            mensagem = ('O id {} nao existe'.format(id))
            consulta = {'status':'erro', 'mensagem':mensagem}    
        except Exception:
            mensagem = ('Erro nao especificado, contate o administrador da API')
            consulta = {'status':'erro', 'mensagem':mensagem}
        return jsonify(consulta)

    elif request.method == 'PUT':    
        try:    
            dados= json.loads(request.data)
            lista_tarefa[id] = dados
            return jsonify(dados)
        except Exception:
            print("Deu ruim")
        finally:
            print("Nao desanime") 
#********************************************************************#

if __name__ == ('__main__'):
    app.run(debug=True)