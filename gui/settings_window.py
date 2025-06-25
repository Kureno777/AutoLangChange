from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout,
    QCheckBox, QLabel, QComboBox, QPushButton, QHBoxLayout
)

class SettingsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AutoLangChange Settings")
        self.setGeometry(100, 100, 500, 400)

        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.init_general_tab()
        self.init_app_rules_tab()
        self.init_dictionary_tab()
        self.init_instant_correction_tab()
        self.init_about_tab()

    def init_general_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()

        auto_mode = QCheckBox("Automatically learn new word")
        popup_mode = QCheckBox("Show popup notification")
        layout.addWidget(auto_mode)
        layout.addWidget(popup_mode)

        switch_input = QLabel("Switch current input key: Shift + Backspace")
        switch_selected = QLabel("Switch selected text key: Shift + Caps Lock")
        layout.addWidget(switch_input)
        layout.addWidget(switch_selected)

        ui_lang_label = QLabel("UI Language:")
        ui_lang_combo = QComboBox()
        ui_lang_combo.addItems(["English", "ไทย"])

        layout.addWidget(ui_lang_label)
        layout.addWidget(ui_lang_combo)

        tab.setLayout(layout)
        self.tabs.addTab(tab, "General")

    def init_app_rules_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Application Rules Coming Soon"))
        tab.setLayout(layout)
        self.tabs.addTab(tab, "App Rules")

    def init_dictionary_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Custom Dictionary Coming Soon"))
        tab.setLayout(layout)
        self.tabs.addTab(tab, "Dictionary")

    def init_instant_correction_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Instant Correction List Coming Soon"))
        tab.setLayout(layout)
        self.tabs.addTab(tab, "Instant Correction")

    def init_about_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("RightLang2 v0.1 Alpha"))
        layout.addWidget(QLabel("Developer: You 👨‍💻"))
        layout.addWidget(QLabel("https://github.com/..."))
        tab.setLayout(layout)
        self.tabs.addTab(tab, "About")

