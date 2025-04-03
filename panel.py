from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QFileDialog, 
    QTabWidget, QHBoxLayout, QCheckBox, QSlider
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
import sys

class BeoBeoCrypter(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("BeoBeo Crypter")
        self.setGeometry(100, 100, 900, 600)
        self.setStyleSheet("background-color: black;")

        self.tabs = QTabWidget(self)
        self.tabs.setStyleSheet("color: #00FF00; font-size: 42px; background-color: black;")
        
        self.encoder_tab = QWidget()
        self.features_tab = QWidget()
        self.build_tab = QWidget()
        self.status_tab = QWidget()
        
        self.tabs.addTab(self.encoder_tab, "Encoder")
        self.tabs.addTab(self.features_tab, "Features")
        self.tabs.addTab(self.build_tab, "Build")
        self.tabs.addTab(self.status_tab, "Status")

        self.initEncoderTab()
        self.initFeaturesTab()
        self.initBuildTab()
        self.initStatusTab()
        
        layout = QVBoxLayout()
        layout.addWidget(self.tabs)
        self.setLayout(layout)
    
    def initEncoderTab(self):
        layout = QVBoxLayout()

        self.title = QLabel("BeoBeo Crypter", self)
        self.title.setFont(QFont("Arial", 32, QFont.Bold))
        self.title.setStyleSheet("color: #00FF00; text-shadow: 0px 0px 10px #00FF00;")
        self.title.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.title)

        self.btn_select = QPushButton("🔍 Select File", self)
        self.btn_select.setFont(QFont("Arial", 14))
        self.btn_select.setStyleSheet("background-color: #00FF00; color: black; border-radius: 10px; padding: 10px;")
        self.btn_select.clicked.connect(self.select_file)
        layout.addWidget(self.btn_select, alignment=Qt.AlignCenter)

        self.status_label = QLabel("Chưa chọn tệp nào...", self)
        self.status_label.setFont(QFont("Arial", 12))
        self.status_label.setStyleSheet("color: #00FF00; text-shadow: 0px 0px 10px #00FF00;")
        self.status_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.status_label)

        self.video_widget = QVideoWidget()
        self.video_widget.setStyleSheet("border: 2px solid #00FF00; border-radius: 10px;")
        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.video_widget)
        video_path = "IMG_5263.MP4"
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(video_path)))
        self.player.play()
        self.player.mediaStatusChanged.connect(self.loop_video)

        layout.addWidget(self.video_widget, alignment=Qt.AlignCenter)
        self.encoder_tab.setLayout(layout)

    def loop_video(self, status):
        if status == QMediaPlayer.EndOfMedia:
            self.player.setPosition(0)
            self.player.play()

    def initFeaturesTab(self):
        layout = QVBoxLayout()
        features = [
            "🕵️‍♂️ Chế độ tàng hình", "🔐 Mật mã không bị phát hiện", "🛡️ Tính năng kiên trì", "🐞 Chống gỡ lỗi",
            "🔬 Tiêm rootkit", "⚙️ Rootkit cấp độ hạt nhân", "📌 Tính kiên trì nâng cao", "🗑️ Quá trình làm rỗng",
            "🦠 Trốn tránh virus", "💉 Tiêm bộ nhớ"
        ]
        for feature in features:
            checkbox = QCheckBox(feature, self)
            checkbox.setFont(QFont("Arial", 12, QFont.Bold))
            checkbox.setStyleSheet("color: #00FF00; padding: 5px; text-shadow: 0px 0px 5px #00FF00;")
            layout.addWidget(checkbox)
        self.features_tab.setLayout(layout)
    
    def initBuildTab(self):
        layout = QVBoxLayout()
        label = QLabel("🚀 Build File", self)
        label.setFont(QFont("Arial", 16, QFont.Bold))
        label.setStyleSheet("color: #00FF00; text-shadow: 0px 0px 10px #00FF00;")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        btn_build = QPushButton("🔨 Build Crypter", self)
        btn_build.setFont(QFont("Arial", 14))
        btn_build.setStyleSheet("background-color: #00FF00; color: black; border-radius: 10px; padding: 10px;")
        layout.addWidget(btn_build, alignment=Qt.AlignCenter)
        
        self.build_tab.setLayout(layout)
    
    def initStatusTab(self):
        layout = QVBoxLayout()
        label = QLabel("📢 Thông Tin Tool", self)
        label.setFont(QFont("Arial", 12))
        label.setStyleSheet("color: #00FF00; text-shadow: 0px 0px 10px #00FF00;")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        label_info = QLabel("Crypter: Tiendev Crypter\n"
                            "CopyRight By: TienDev\n"
                            "Owner Tool: @tiendevt\n"
                            "Design Crypter: @tiendev\n"
                            "🔗 Contact: T.me/skibidi_botnet", self)
        label_info.setFont(QFont("Arial", 33))
        label_info.setStyleSheet("color: #00FF00; text-shadow: 0px 0px 10px #00FF00;")
        label_info.setAlignment(Qt.AlignCenter)
        layout.addWidget(label_info)
        self.status_tab.setLayout(layout)
    
    def select_file(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Chọn Tệp Tin")
        if file_path:
            self.status_label.setText(f"📂 Đã chọn: {file_path}")
        else:
            self.status_label.setText("⚠️ Không có tệp nào được chọn.")

if __name__ == "__main__":
    app = QApplication(sys.argv)  
    window = BeoBeoCrypter()
    window.show()
    sys.exit(app.exec_())
