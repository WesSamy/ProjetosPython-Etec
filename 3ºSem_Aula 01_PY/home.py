from PyQt5 import uic, QtWidgets

def main():
    campoId = bloco.id.text()
    print("Id: ", campoId)
    campoNome = bloco.nome.text()
    print("Nome: ", campoNome)
    campoEmail = bloco.email.text()
    print("Email: ", campoEmail)
    campoTelefone = bloco.telefone.text()
    print("Telefone: ", campoTelefone)
    
tipoTelefone = ""


    
app=QtWidgets.QApplication([])

bloco=uic.loadUi("bloco_de_notas.ui")

bloco.enviacao.clicked.connect(main)

# Fazer o programa funcionar
bloco.show()
app.exec()