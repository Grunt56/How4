from PyQt5 import uic,QtWidgets
import mysql.connector

numero_id = 0

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="ficha_personagem"
)
def editar_dados():
    global numero_id
    tela_editar.show()
    linha = segundatela.tableWidget.currentRow()
    
    cursor = banco.cursor()
    cursor.execute("SELECT id FROM personagem")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("SELECT * FROM personagem WHERE id="+ str(valor_id))
    personagems = cursor.fetchall()

    numero_id = valor_id
    
    tela_editar.lineEdit.setText(str(personagems[0][0]))
    tela_editar.lineEdit_2.setText(str(personagems[0][1]))
    tela_editar.lineEdit_3.setText(str(personagems[0][2]))
    tela_editar.lineEdit_4.setText(str(personagems[0][3]))
    tela_editar.lineEdit_5.setText(str(personagems[0][4]))

def salvar_dados():
    global numero_id
    print(numero_id)

    nome = tela_editar.lineEdit_2.text()
    raca = tela_editar.lineEdit_3.text()
    classe = tela_editar.lineEdit_4.text()
    alinhamento = tela_editar.lineEdit_5.text()
    
    cursor = banco.cursor()
    cursor.execute("UPDATE personagem SET nome = '{}', raca = '{}', classe = '{}', alinhamento = '{}' WHERE id = {}".format(nome,raca,classe,alinhamento,numero_id))
    
    tela_editar.close()
    segundatela.close()
    chama_tela2()

def deletar_dados():
    linha = segundatela.tableWidget.currentRow()
    segundatela.tableWidget.removeRow(linha)
    
    cursor = banco.cursor()
    cursor.execute("SELECT id FROM personagem")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("DELETE FROM personagem WHERE id="+ str(valor_id))


def funcao_principal():
    linha1 = How4Crud.lineEdit.text()
    linha2 = How4Crud.lineEdit_2.text()
    linha3 = How4Crud.lineEdit_3.text()
    
    Alinhamento = ""

    if How4Crud.radioButton.isChecked() :
        print("Alinhamento Leal")
        Alinhamento ="Leal"
    elif How4Crud.radioButton_2.isChecked() :
        print("Alinhamento Neutro")
        Alinhamento ="Neutro"
    elif How4Crud.radioButton_3.isChecked() :
        print("Alinhamento Caótico")
        Alinhamento ="Caótico"


    print("Nome:",linha1)
    print("Raça:",linha2)
    print("Classe:",linha3)
    cursor = banco.cursor()
    comando_SQL = "INSERT INTO personagem (nome,raca,classe,alinhamento) VALUES (%s,%s,%s,%s)"
    dados = (str(linha1),str(linha2),str(linha3),Alinhamento)
    cursor.execute(comando_SQL,dados)
    banco.commit()
    How4Crud.lineEdit.setText("")
    How4Crud.lineEdit_2.setText("")
    How4Crud.lineEdit_3.setText("")

def chama_tela2():
    segundatela.show()

    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM personagem"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

    segundatela.tableWidget.setRowCount(len(dados_lidos))
    segundatela.tableWidget.setColumnCount(5)

    for i in range(0, len(dados_lidos)):
        for j in range(0,5):
            segundatela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


app=QtWidgets.QApplication([])
How4Crud=uic.loadUi("How4Crud.ui")
segundatela=uic.loadUi("listar_dados.ui")
tela_editar=uic.loadUi("editar_dados.ui")
How4Crud.pushButton.clicked.connect(funcao_principal)
How4Crud.pushButton_2.clicked.connect(chama_tela2)
segundatela.pushButton.clicked.connect(deletar_dados)
segundatela.pushButton_2.clicked.connect(editar_dados)
tela_editar.pushButton.clicked.connect(salvar_dados)

How4Crud.show()
app.exec()





