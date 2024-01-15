import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QGraphicsScene, QGraphicsView, QGraphicsRectItem
from PyQt6.QtGui import QPixmap, QFontDatabase, QFont, QColor, QPainter
from PyQt6.QtCore import Qt
from mnk_projekt import Game, Player, Bot_random, Bot_simple, Bot_complex


class ChalkboardButton(QPushButton):
    def __init__(self, text, value):
        super(ChalkboardButton, self).__init__(text)
        self.value = value
        self.setStyleSheet("color: white; font: bold 16px;")
        

class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load chalk font
        font_path = "EraserRegular.ttf"  # path
        chalk_font = QFontDatabase.addApplicationFont(font_path)
        chalk_font = QFont("Eraser", 20)
        
        # # check if font is loaded
        if chalk_font == -1:
            print(f"Error loading font from path: {font_path}")
        else:
            print(f"Font loaded successfully!")

        # Set up background
        chalkboard_image_path = "chalkboard4.jpg" 
        chalkboard_image = QPixmap(chalkboard_image_path).scaled(self.size())

        self.setStyleSheet(f"background-image: url({chalkboard_image_path});")

        # Set up central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Set up main layout
        main_layout = QVBoxLayout(central_widget)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        #headline
        headline_label = QLabel("Main Menu", self)
        headline_label.setFont(QFont("Eraser", 40, QFont.Weight.Bold))  # Set a larger font size and bold style
        headline_label.setStyleSheet("color: white;")  # Set font color to white
        main_layout.addWidget(headline_label)
        
        # Create input boxes for m, n, k
        input_layout = QHBoxLayout()
        
        input_mnk_label = QLabel("Enter gameboard parameters:", self)
        input_mnk_label.setFont(chalk_font)
        input_mnk_label.setStyleSheet("color: white;")

        m_input = QLineEdit(self)
        m_input.setPlaceholderText("height")
        m_input.setFont(chalk_font)
        m_input.setStyleSheet("color: white; margin-bottom: 0px;")
        input_layout.addWidget(m_input)

        n_input = QLineEdit(self)
        n_input.setPlaceholderText("width")
        n_input.setFont(chalk_font)
        n_input.setStyleSheet("color: white; margin-bottom: 5px;")
        input_layout.addWidget(n_input)

        k_input = QLineEdit(self)
        k_input.setPlaceholderText("winning length")
        k_input.setFont(chalk_font)
        k_input.setStyleSheet("color: white; margin-bottom: 5px;")
        input_layout.addWidget(k_input)
        
        
        
        #Player 1

        # Create labels and buttons
        player1_label = QLabel("Player 1", self)
        player1_label.setFont(chalk_font)
        player1_label.setStyleSheet("color: white;")  # Set font color to white

        # Create a horizontal layout for "Enter player name" label and text box
        player1_name_layout = QHBoxLayout()  
        player1_name_label = QLabel("Enter player name:", self)
        player1_name_label.setFont(chalk_font)
        player1_name_label.setStyleSheet("color: white;")  # Set font color to white
        
        self.player1_name_input = QLineEdit(self)
        self.player1_name_input.setStyleSheet("color: white; margin-bottom: 0px;")
        self.player1_name_input.setFont(chalk_font)
        player1_name_layout.addWidget(player1_name_label)
        player1_name_layout.addWidget(self.player1_name_input)

        
       #  Buttons
        player1_type_label = QLabel("Select your player type", self)
        player1_type_label.setFont(chalk_font)
        player1_type_label.setStyleSheet("color: white;")
        player1_buttons_layout = QHBoxLayout()

        self.player1_buttons = [
            ChalkboardButton("Player", 1),
            ChalkboardButton("Bot Random", 2),
            ChalkboardButton("Bot Simple", 3),
            ChalkboardButton("Bot Complex", 4),
        ]
        

        # Player 2
       
        # Create labels and buttons
        player2_label = QLabel("Player 2", self)
        player2_label.setFont(chalk_font)
        player2_label.setStyleSheet("color: white;")  # Set font color to white

        # Create a horizontal layout for "Enter player name" label and text box
        player2_name_layout = QHBoxLayout()  
        player2_name_label = QLabel("Enter player name:", self)
        player2_name_label.setFont(chalk_font)
        player2_name_label.setStyleSheet("color: white;")  # Set font color to white
        
        self.player2_name_input = QLineEdit(self)
        self.player2_name_input.setStyleSheet("color: white; margin-bottom: 0px;")
        self.player2_name_input.setFont(chalk_font)
        player2_name_layout.addWidget(player2_name_label)
        player2_name_layout.addWidget(self.player2_name_input)

        
       #  #Buttons
       
        player2_type_label = QLabel("Select your player type", self)
        player2_type_label.setFont(chalk_font)
        player2_type_label.setStyleSheet("color: white;")
        player2_buttons_layout = QHBoxLayout()
        
        self.player2_buttons = [
            ChalkboardButton("Player", 1),
            ChalkboardButton("Bot Random", 2),
            ChalkboardButton("Bot Simple", 3),
            ChalkboardButton("Bot Complex", 4),
        ]
        


        
        # Add widgets to layout
        #m,n,k
        main_layout.addWidget(input_mnk_label)
        main_layout.addLayout(input_layout)
        
        # Player 1
        main_layout.addWidget(player1_label)
        main_layout.addLayout(player1_name_layout)
        main_layout.addWidget(player1_type_label)
        # Add player type buttons to layout
        for button in self.player1_buttons:
            button.setFont(chalk_font)
            player1_buttons_layout.addWidget(button)
            button.clicked.connect(self.on_player1_button_click)
        main_layout.addLayout(player1_buttons_layout)
        
        # Create start game button
        start_button = ChalkboardButton("Start Game", 0)
        start_button.setFont(chalk_font)
        start_button.setStyleSheet("color: white;")
        start_button.clicked.connect(self.on_start_button_click)
        
        # Player 2
        main_layout.addWidget(player2_label)
        main_layout.addLayout(player2_name_layout)  # Use the corrected layout here
        main_layout.addWidget(player2_type_label)
        # Add player type buttons to layout
        for button in self.player2_buttons:
            player2_buttons_layout.addWidget(button)
            button.clicked.connect(self.on_player2_button_click)
        main_layout.addLayout(player2_buttons_layout)

        main_layout.addWidget(start_button)


        # Store input boxes
        self.m_input = m_input
        self.n_input = n_input
        self.k_input = k_input

        self.setWindowTitle("Main Menu")
        self.setGeometry(100, 100, 800, 600)  # Set your preferred window size
        
        
        
    def on_player1_button_click(self):
        self.handle_player_button_click(self.player1_buttons) 
        
    def on_player2_button_click(self):
        self.handle_player_button_click(self.player2_buttons)
        
    def handle_player_button_click(self, buttons):
        
        font_path = "EraserRegular.ttf"  # path
        chalk_font = QFontDatabase.addApplicationFont(font_path)
        chalk_font = QFont("Eraser", 20)
        
        # Clear any previous selection
        for button in buttons:
            button.setFont(chalk_font)
            button.setStyleSheet("background-color: transparent; color: white;")

        # Highlight the clicked button
        sender_button = self.sender()
        sender_button.setFont(chalk_font)
        sender_button.setStyleSheet("background-color: blue; color: white;")
        
    def get_selected_button_value(self, buttons):
        for button in buttons:
            if "background-color: blue;" in button.styleSheet():
                return button.value
        return None
        
    def on_start_button_click(self):
            # Get the chosen options
        m = int(self.m_input.text())
        n = int(self.n_input.text())
        k = int(self.k_input.text())


        # Get name 
        player1_name = self.player1_name_input.text()
        player2_name = self.player2_name_input.text()
        # Get the selected player types
        player1_type = self.get_selected_button_value(self.player1_buttons)
        player2_type = self.get_selected_button_value(self.player2_buttons)
        # print(player1_type)
        # print(player2_type)

        # Create MNK game instance and start the game with the chosen options
        current_game = Game(m, n, k)
        player1 = current_game.choose_player(1, player1_name, player1_type)
        player2 = current_game.choose_player(2, player2_name, player2_type)
        current_game.start(player1, player2)
        current_game.game_loop()
        
        # Show the game board window
        game_board_window = GameBoardWindow(m, n)
        game_board_window.show()
        self.hide()
        
        
class GameBoardWindow(QMainWindow):
    def __init__(self, m, n):
        super().__init__()

        # Load chalk font
        chalk_font = QFont("Eraser", 20)

        # Set up background
        chalkboard_image_path = "chalkboard4.jpg"
        chalkboard_image = QPixmap(chalkboard_image_path).scaled(self.size())
        self.setStyleSheet(f"background-image: url({chalkboard_image_path});")

        # Set up central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Set up main layout
        main_layout = QVBoxLayout(central_widget)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Create QGraphicsScene and QGraphicsView for the game board
        scene = QGraphicsScene(self)
        view = QGraphicsView(scene)
        main_layout.addWidget(view)

        # Draw m x n scratchboard
        cell_size = 50
        for row in range(m):
            for col in range(n):
                rect_item = QGraphicsRectItem(col * cell_size, row * cell_size, cell_size, cell_size)
                rect_item.setPen(QColor("white"))
                scene.addItem(rect_item)

        self.setWindowTitle("Game Board")
        self.setGeometry(100, 100, n * cell_size, m * cell_size)  # Adj

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_menu = MainMenu()
    main_menu.show()
    sys.exit(app.exec())