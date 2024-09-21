import sys
from PyQt5.QtWidgets import QApplication
from src.vista.InterfazEPorra import App_EPorra
from src.logica.Fachada_EPorra import Fachada_EPorra
from PyQt5.QtGui import QFont

if __name__ == '__main__':
    # Punto inicial de la aplicación

    logica = Fachada_EPorra()

    app = App_EPorra(sys.argv, logica)
    font = QFont("Arial")
    app.setFont(font)
    sys.exit(app.exec_())

    