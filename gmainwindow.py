from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QMainWindow

app = QApplication([])  # Menambahkan tanda '='

window = QMainWindow()

# Membuat label dan menambahkan teks serta posisi
label = QLabel(window)
label.setText("Label")
label.move(200, 0)

# Membuat tombol dan menambahkan teks
button = QPushButton(window)
button.setText("Button1")

window.show()

app.exec_()  # Menambahkan tanda '()' di exec_
