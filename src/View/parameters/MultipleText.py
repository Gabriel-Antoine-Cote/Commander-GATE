from PyQt6.QtWidgets import QWidget, QPushButton, QListView, QVBoxLayout, QHBoxLayout, QLineEdit, QSizePolicy, QLabel, QComboBox
from PyQt6.QtGui import QStandardItemModel, QStandardItem, QRegularExpressionValidator
from PyQt6.QtCore import Qt, QRegularExpression, pyqtSignal
from src.Control.ControlAPI import ControlAPI
from src.View.parameters.BigPopupCombo import BigPopupCombo

class MultipleText(QWidget):

    dataChanged = pyqtSignal()

    def __init__(self, units: list[str], parent=None):
        super().__init__(parent)
        
        self.lineEdit = QLineEdit(self)
        if len(units) > 0:
            self.unitDropdown = QComboBox(self)
        self.addButton = QPushButton(self)
        self.widgetLayout = QVBoxLayout()
        self.widgetLayout.setSpacing(0)
        self.widgetLayout.setContentsMargins(0,0,0,0)
        self.units = units

        self._build_ui()

        self.setLayout(self.widgetLayout)

        

    def _build_ui(self):
        rowWidget = QWidget()
        lineEditlayout = QHBoxLayout()
        rowWidget.setLayout(lineEditlayout)

        lineEditlayout.addStretch()

        ### Build the line edit
        self.lineEdit.setText("0")
        self.lineEdit.setStyleSheet("QLineEdit : { border: 1px solid black }")
        regex = QRegularExpression("-?[0-9]+(.[0-9]+)?")
        validator = QRegularExpressionValidator(regex)
        self.lineEdit.setValidator(validator)
        self.lineEdit.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.lineEdit._edited = False
        lineEditlayout.addWidget(self.lineEdit, alignment=Qt.AlignmentFlag.AlignVCenter)

        # Build the unit dropdown
        if len(self.units) > 0:
            self.unitDropdown.addItems(self.units)
            self.unitDropdown.setStyleSheet("QComboBox : { border: 1px solid black }")
            lineEditlayout.addWidget(self.unitDropdown, alignment=Qt.AlignmentFlag.AlignVCenter)

        # Build the button to add
        self.addButton.setText("Add")
        self.addButton.setStyleSheet("QPushButton : { border: 1px solid black }")
        self.addButton.clicked.connect(lambda: self.addTextLine(self.lineEdit.text()))
        lineEditlayout.addWidget(self.addButton, alignment=Qt.AlignmentFlag.AlignVCenter)

        self.widgetLayout.addWidget(rowWidget)
        ### Build the list view


    def addTextLine(self, text: str):
        """
        Add a line in the layout

        Args:
            text: text to add to the listView
        """
        rowWidget = QWidget()
        lineLabelLayout = QHBoxLayout()
        text = str(text)

        rowWidget.setLayout(lineLabelLayout)

        # Remove button
        removeButton = QPushButton(self)
        removeButton.setText("X")
        removeButton.setStyleSheet("QPushButton : { border: 1px solid black }")
        removeButton.clicked.connect(lambda : self.removeTextLine(text))
        lineLabelLayout.addWidget(removeButton, alignment=Qt.AlignmentFlag.AlignVCenter)

        lineLabelLayout.addStretch()

        # Label of the text
        label = QLabel(self)
        label.setText(text)
        label.setStyleSheet("QLabel : { border: 1px solid black }")
        lineLabelLayout.addWidget(label, alignment=Qt.AlignmentFlag.AlignVCenter)

        self.widgetLayout.addWidget(rowWidget)

        self.dataChanged.emit()

    def addValues(self, values: list[str]):
        for value in values:
            self.addTextLine(value)

    def removeTextLine(self, text: str):
        for itemIndex in range(1, self.widgetLayout.count()):
            labelText: QLabel = self.widgetLayout.itemAt(itemIndex).widget().layout().itemAt(2).widget()
            if labelText.text() == text:
                widgetToRemove: QWidget = self.widgetLayout.takeAt(itemIndex).widget()
                while (widgetToRemove.layout().count() > 0):
                    subWidget = widgetToRemove.layout().takeAt(0).widget()
                    if subWidget:
                        subWidget.deleteLater()
                widgetToRemove.deleteLater()
                break
        
        self.dataChanged.emit()