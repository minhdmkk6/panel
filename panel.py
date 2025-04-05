import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QSpinBox, QPlainTextEdit, QHBoxLayout
from PyQt5.QtCore import Qt
from threading import Thread
import time
import os
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import json
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from threading import Thread
import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QSpinBox, QPlainTextEdit, QHBoxLayout
from PyQt5.QtCore import Qt
import os
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
import os
import uuid
import hashlib
import requests
import sys
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QApplication
from PyQt5.QtCore import Qt
import os
import uuid
import hashlib
import requests
import sys
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QApplication, QPushButton
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QClipboard  
import sys
import os
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt, QTimer

class FacebookReportTool(QWidget):
    def __init__(self):
        super().__init__()
        
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Facebook Report Tool")
        self.setGeometry(100, 100, 600, 500)  # Tăng kích thước cửa sổ
        self.setStyleSheet("background-color: black; color: white;")

        self.layout = QVBoxLayout()

        # Label for FB link
        self.fb_link_label = QLabel("Nhập link Facebook:")
        self.fb_link_label.setStyleSheet("font-size: 16px color: #39FF14;")
        self.layout.addWidget(self.fb_link_label)

        # Input field for Facebook link
        self.fb_link_input = QLineEdit(self)
        self.fb_link_input.setStyleSheet("font-size: 14px; padding: 10px color: #39FF14;")
        self.layout.addWidget(self.fb_link_input)

        # Label for number of reports
        self.num_reports_label = QLabel("Nhập số lần báo cáo:")
        self.num_reports_label.setStyleSheet("font-size: 16px color: #39FF14;")
        self.layout.addWidget(self.num_reports_label)

        # Input for number of reports (SpinBox)
        self.num_reports_input = QSpinBox(self)
        self.num_reports_input.setMinimum(1)
        self.num_reports_input.setMaximum(100)
        self.num_reports_input.setStyleSheet("font-size: 14px; padding: 10px color: #39FF14;")
        self.layout.addWidget(self.num_reports_input)

        # Label for number of Chrome instances
        self.num_chrome_label = QLabel("Nhập số lượng cửa sổ Chrome:")
        self.num_chrome_label.setStyleSheet("font-size: 16px color: #39FF14;")
        self.layout.addWidget(self.num_chrome_label)

        # Input for number of Chrome instances (SpinBox)
        self.num_chrome_input = QSpinBox(self)
        self.num_chrome_input.setMinimum(1)
        self.num_chrome_input.setMaximum(10)
        self.num_chrome_input.setStyleSheet("font-size: 14px; padding: 10px color: #39FF14;")
        self.layout.addWidget(self.num_chrome_input)

        # Buttons Layout
        buttons_layout = QHBoxLayout()

        # Button to continue (show after input)
        self.continue_button = QPushButton("Tiếp tục", self)
        self.continue_button.setStyleSheet("font-size: 16px; padding: 10px color: #39FF14;")
        self.continue_button.clicked.connect(self.start_chrome_instance)
        buttons_layout.addWidget(self.continue_button)
        # Button to check (show after continue)
        self.check_button = QPushButton("Check", self)
        self.check_button.setStyleSheet("font-size: 16px; padding: 10px color: #39FF14;")
        self.check_button.clicked.connect(self.check_condition)
        self.check_button.setDisabled(True)  # Disable initially
        buttons_layout.addWidget(self.check_button)
        # Button to start reporting (show after check)
        self.start_button = QPushButton("Bắt đầu báo cáo", self)
        self.start_button.setStyleSheet("font-size: 16px; padding: 10px color: #39FF14;")
        self.start_button.clicked.connect(self.start_reporting)
        self.start_button.setDisabled(True)  # Disable initially
        buttons_layout.addWidget(self.start_button)

        self.layout.addLayout(buttons_layout)

        # Log area (for displaying logs)
        self.log_area = QPlainTextEdit(self)
        self.log_area.setReadOnly(True)
        self.log_area.setStyleSheet("font-size: 14px; padding: 10px;")
        self.layout.addWidget(self.log_area)

        self.setLayout(self.layout)

        self.driver = None  # To store the webdriver instance
        self.chrome_tabs = []  # To store opened tabs (Chrome windows)

    def start_chrome_instance(self):
        fb_link = self.fb_link_input.text()
        num_reports = self.num_reports_input.value()
        num_chrome_instances = self.num_chrome_input.value()

        # Khởi động cửa sổ Chrome
        self.log_area.appendPlainText("🔑 Đang khởi động trình duyệt Chrome...")

        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-popup-blocking")

        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

        # Mở Facebook để người dùng đăng nhập
        self.driver.get("https://www.facebook.com")
        self.log_area.appendPlainText("📝 Vui lòng đăng nhập vào Facebook trong trình duyệt Chrome và sau đó nhấn 'Check'.")

        # Sau khi người dùng đăng nhập, bấm Check để kiểm tra
        self.check_button.setEnabled(True)
        self.continue_button.setDisabled(True)  # Disable continue button after clicking

    def check_condition(self):
        fb_link = self.fb_link_input.text()
        num_reports = self.num_reports_input.value()
        num_chrome_instances = self.num_chrome_input.value()

        # Kiểm tra xem các thông tin đã hợp lệ chưa
        if fb_link and num_reports > 0 and num_chrome_instances > 0:
            self.log_area.appendPlainText("✅ Kiểm tra thành công. Có thể bắt đầu.")
            self.start_button.setEnabled(True)  # Enable start button after check
        else:
            self.log_area.appendPlainText("❌ Kiểm tra không thành công. Vui lòng kiểm tra lại các thông tin.")
            self.check_button.setEnabled(False)  # Disable check button if there's an issue

    def start_reporting(self):
        fb_link = self.fb_link_input.text()
        num_reports = self.num_reports_input.value()
        num_chrome_instances = self.num_chrome_input.value()

        # Giữ lại các tab Chrome đang mở
        self.chrome_tabs = [self.driver]  # Dùng driver đã mở trước đó
        self.driver.get(fb_link)  # Mở link Facebook muốn báo cáo
        time.sleep(10)
        # Lặp qua các tab (cửa sổ) đã mở
        for i in range(num_chrome_instances):
            for j in range(num_reports):
                self.log_area.appendPlainText(f"\n📌 Đang thực hiện báo cáo lần {j + 1}...")
                self.try_report1(self.driver, three_dot_button_xpath, report_button_xpath, reason_button_xpath, submit_button_xpath, next_button_xpath, done_button_xpath)
                self.try_report5(self.driver, three_dot_button_xpath, report_button_xpath, reason_button_xpath, submit_button_xpath, next_button_xpath, done_button_xpath)
                self.try_report2(self.driver, three_dot_button_xpath, report_button_xpath, reason_button_xpath, submit_button_xpath, next_button_xpath, done_button_xpath)
                self.try_report3(self.driver, three_dot_button_xpath, report_button_xpath, reason_button_xpath, submit_button_xpath, next_button_xpath, done_button_xpath)
                self.try_report4(self.driver, three_dot_button_xpath, report_button_xpath, reason_button_xpath, submit_button_xpath, next_button_xpath, done_button_xpath)

        self.log_area.appendPlainText("✅ Đã hoàn thành tất cả các báo cáo!")

    def try_report1(self, driver, three_dot_button_xpath, report_button_xpath, reason_button_xpath, submit_button_xpath, next_button_xpath, done_button_xpath):
        try:
            # Nhấn vào dấu 3 chấm
            try:
                three_dot_button = driver.find_element(By.XPATH, three_dot_button_xpath)
                three_dot_button.click()
                time.sleep(2)
            except Exception as e:
                pass  # Bỏ qua lỗi và tiếp tục

            # Nhấn "Report profile"
            try:
                report_button = driver.find_element(By.XPATH, report_button_xpath)
                report_button.click()
                time.sleep(3)
            except Exception as e:
                pass  # Bỏ qua lỗi và tiếp tục

            # Chọn lý do "Something about this profile"
            try:
                reason_button = driver.find_element(By.XPATH, reason_button_xpath)
                reason_button.click()
                time.sleep(3)
            except Exception as e:
                pass  # Bỏ qua lỗi và tiếp tục

            # Chọn lý do "Pretending to be someone"
            try:
                pretending_to_be_someone_button = driver.find_element(By.XPATH, "//span[text()='Pretending to be someone']")
                pretending_to_be_someone_button.click()
                time.sleep(3)
            except Exception as e:
                pass  # Bỏ qua lỗi và tiếp tục

            # Chọn "Me"
            try:
                me_button = driver.find_element(By.XPATH, "//span[text()='Me']")
                me_button.click()
                time.sleep(3)
            except Exception as e:
                pass  # Bỏ qua lỗi và tiếp tục

            # Nhấn "Submit"
            try:
                submit_button = driver.find_element(By.XPATH, submit_button_xpath)
                submit_button.click()
                time.sleep(5)
            except Exception as e:
                pass  # Bỏ qua lỗi và tiếp tục

            # Nhấn "Next"
            try:
                next_button = driver.find_element(By.XPATH, next_button_xpath)
                next_button.click()
                time.sleep(5)
            except Exception as e:
                pass  # Bỏ qua lỗi và tiếp tục

            # Nhấn "Done"
            try:
                done_button = driver.find_element(By.XPATH, done_button_xpath)
                done_button.click()
                time.sleep(2)
            except Exception as e:
                pass  # Bỏ qua lỗi và tiếp tục

            self.log_area.appendPlainText("✅ Đã báo cáo tài khoản mạo danh thành công!")

        except Exception as e:
            print(f"❌ Lỗi trong quá trình thực hiện báo cáo: {e}")
            pass  # Bỏ qua lỗi và tiếp tục



    def try_report2(self,driver, three_dot_button_xpath, report_button_xpath, reason_button_xpath, submit_button_xpath, next_button_xpath, done_button_xpath):
        try:
            # Nhấn vào dấu 3 chấm
            try:
                three_dot_button = driver.find_element(By.XPATH, three_dot_button_xpath)
                three_dot_button.click()
                time.sleep(2)
            except Exception as e:
                pass  # Bỏ qua lỗi và tiếp tục

            # Nhấn "Report profile"
            try:
                report_button = driver.find_element(By.XPATH, report_button_xpath)
                report_button.click()
                time.sleep(3)
            except Exception as e:
                pass  # Bỏ qua lỗi và tiếp tục

            # Chọn lý do "Something about this profile"
            try:
                reason_button = driver.find_element(By.XPATH, reason_button_xpath)
                reason_button.click()
                time.sleep(3)
            except Exception as e:
                pass  # Bỏ qua lỗi và tiếp tục

            # Chọn lý do "Pretending to be someone"
            try:
                pretending_to_be_someone_button = driver.find_element(By.XPATH, "//span[text()='Pretending to be someone']")
                pretending_to_be_someone_button.click()
                time.sleep(3)
            except Exception as e:
                pass  # Bỏ qua lỗi và tiếp tục

            # Chọn "Celebrity"
            try:
                me_button = driver.find_element(By.XPATH, "//span[text()='Celebrity']")
                me_button.click()
                time.sleep(3)
            except Exception as e:
                print(f"❌ Lỗi khi chọn 'Celebrity': {e}")
                pass  # Bỏ qua lỗi và tiếp tục

        # Nhập tên "Mark Zuckerberg" vào ô tìm kiếm
            try:
                search_input = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div[4]/div/div[2]/div/div/div/div/div/div/div/div/div/label/div/input")
                search_input.send_keys("Mark Zuckerberg")
                time.sleep(3)
            except Exception as e:
                pass  # Bỏ qua lỗi và tiếp tục

            # Chọn kết quả "Mark Zuckerberg"
            try:
                result = driver.find_element(By.XPATH, "//*[@id='4']/div/div[1]/div[2]/div")
                result.click()
                time.sleep(5)
            except Exception as e:
                pass  # Bỏ qua lỗi và tiếp tục
            # Nhấn "Next"
            try:
                next_button = driver.find_element(By.XPATH, next_button_xpath)
                next_button.click()
                time.sleep(5)
            except Exception as e:
                pass  # Bỏ qua lỗi và tiếp tục
            # Nhấn "Submit"
            try:
                submit_button = driver.find_element(By.XPATH, submit_button_xpath)
                submit_button.click()
                time.sleep(5)
            except Exception as e:
                pass  # Bỏ qua lỗi và tiếp tục

            # Nhấn "Next"
            try:
                next_button = driver.find_element(By.XPATH, next_button_xpath)
                next_button.click()
                time.sleep(5)
            except Exception as e:
                pass  # Bỏ qua lỗi và tiếp tục

            # Nhấn "Done"
            try:
                done_button = driver.find_element(By.XPATH, done_button_xpath)
                done_button.click()
                time.sleep(2)
            except Exception as e:
                pass  # Bỏ qua lỗi và tiếp tục

            self.log_area.appendPlainText("✅ Đã báo cáo tài khoản mạo danh Mark Zuckerburg thành công!")

        except Exception as e:
            print(f"❌ Lỗi trong quá trình thực hiện báo cáo: {e}")
            pass  # Bỏ qua lỗi và tiếp tục

    def try_report1(self, driver, three_dot_button_xpath, report_button_xpath, reason_button_xpath, submit_button_xpath, next_button_xpath, done_button_xpath):
        try:
            # Nhấn vào dấu 3 chấm
            try:
                three_dot_button = driver.find_element(By.XPATH, three_dot_button_xpath)
                three_dot_button.click()
                time.sleep(2)
            except Exception as e:
                pass  # Bỏ qua lỗi và tiếp tục

            # Nhấn "Report profile"
            try:
                report_button = driver.find_element(By.XPATH, report_button_xpath)
                report_button.click()
                time.sleep(3)
            except Exception as e:
                pass  # Bỏ qua lỗi và tiếp tục

            # Chọn lý do "Something about this profile"
            try:
                reason_button = driver.find_element(By.XPATH, reason_button_xpath)
                reason_button.click()
                time.sleep(3)
            except Exception as e:
                pass  # Bỏ qua lỗi và tiếp tục

            # Chọn lý do "Pretending to be someone"
            try:
                pretending_to_be_someone_button = driver.find_element(By.XPATH, "//span[text()='Pretending to be someone']")
                pretending_to_be_someone_button.click()
                time.sleep(3)
            except Exception as e:
                pass  # Bỏ qua lỗi và tiếp tục

            # Chọn "Me"
            try:
                me_button = driver.find_element(By.XPATH, "//span[text()='Me']")
                me_button.click()
                time.sleep(3)
            except Exception as e:
                pass  # Bỏ qua lỗi và tiếp tục

            # Nhấn "Submit"
            try:
                submit_button = driver.find_element(By.XPATH, submit_button_xpath)
                submit_button.click()
                time.sleep(5)
            except Exception as e:
                pass  # Bỏ qua lỗi và tiếp tục

            # Nhấn "Next"
            try:
                next_button = driver.find_element(By.XPATH, next_button_xpath)
                next_button.click()
                time.sleep(5)
            except Exception as e:
                pass  # Bỏ qua lỗi và tiếp tục

            # Nhấn "Done"
            try:
                done_button = driver.find_element(By.XPATH, done_button_xpath)
                done_button.click()
                time.sleep(2)
            except Exception as e:
                pass  # Bỏ qua lỗi và tiếp tục

            self.log_area.appendPlainText("✅ Đã báo cáo tài khoản mạo danh thành công!")

        except Exception as e:
            print(f"❌ Lỗi trong quá trình thực hiện báo cáo: {e}")
            pass  # Bỏ qua lỗi và tiếp tục

    def try_report3(self, driver, three_dot_button_xpath, report_button_xpath, reason_button_xpath, submit_button_xpath, next_button_xpath, done_button_xpath):
        try:
            # Nhấn vào dấu 2 chấm
            try:
                three_dot_button = driver.find_element(By.XPATH, three_dot_button_xpath)
                three_dot_button.click()
                time.sleep(2)
            except Exception as e:
                pass  # Bỏ qua lỗi và tiếp tục

            # Nhấn "Report profile"
            try:
                report_button = driver.find_element(By.XPATH, report_button_xpath)
                report_button.click()
                time.sleep(2)
            except Exception as e:
                pass  
            try:
                reason_button = driver.find_element(By.XPATH, reason_button_xpath)
                reason_button.click()
                time.sleep(2)
            except Exception as e:
                pass  
            
            # Click vào fake name mà không đợi
            fakename_button_xpath = "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div[4]/div/div[2]/div/div/div/div[3]/div/div/div/div[1]/div"
            try:
                fakename_button = driver.find_element(By.XPATH, fakename_button_xpath)
                fakename_button.click()
                time.sleep(2)
            except Exception as e:
                print(f"❌ Lỗi khi chọn fake name: {e}")
                pass  # Bỏ qua lỗi và tiếp tục
    
            # Nhấn "Done"
            try:
                done_button = driver.find_element(By.XPATH, done_button_xpath)
                done_button.click()
                time.sleep(2)
            except Exception as e:
                pass  # Bỏ qua lỗi và tiếp tục

            self.log_area.appendPlainText("✅ Đã báo cáo tài khoản mạo danh tên thành công!")

        except Exception as e:
            print(f"❌ Lỗi trong quá trình thực hiện báo cáo: {e}")
            pass  # Bỏ qua lỗi và tiếp tục

    def try_report4(self, driver, three_dot_button_xpath, report_button_xpath, reason_button_xpath, submit_button_xpath, next_button_xpath, done_button_xpath):
        try:
            # Nhấn vào dấu 2 chấm
            try:
                three_dot_button = driver.find_element(By.XPATH, three_dot_button_xpath)
                three_dot_button.click()
                time.sleep(2)
            except Exception as e:
                print(f"❌ Lỗi khi nhấn vào dấu 2 chấm: {e}")
                pass  # Bỏ qua lỗi và tiếp tục

            # Nhấn "Report profile"
            try:
                report_button = driver.find_element(By.XPATH, report_button_xpath)
                report_button.click()
                time.sleep(2)
            except Exception as e:
                print(f"❌ Lỗi khi nhấn 'Report profile': {e}")
                pass  # Bỏ qua lỗi và tiếp tục

            # Chọn lý do "Something about this profile"
            try:
                reason_button = driver.find_element(By.XPATH, reason_button_xpath)
                reason_button.click()
                time.sleep(2)
            except Exception as e:
                pass  
            
            # Click vào fake name mà không đợi
            fake_account_button_xpath = "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div[4]/div/div[2]/div/div/div/div[2]/div/div/div/div[1]/div"
            try:
                fake_account_button = driver.find_element(By.XPATH, fake_account_button_xpath)
                fake_account_button.click()
                time.sleep(2)
            except Exception as e:
                pass  # Bỏ qua lỗi và tiếp tục
        except Exception as e:
            pass  
    def try_report5(self, driver, three_dot_button_xpath, report_button_xpath, reason_button_xpath, submit_button_xpath, next_button_xpath, done_button_xpath):
        try:
            # Nhấn vào dấu 3 chấm
            try:
                three_dot_button = driver.find_element(By.XPATH, three_dot_button_xpath)
                three_dot_button.click()
                time.sleep(1)
            except Exception as e:
                pass  # Bỏ qua lỗi và tiếp tục

            # Nhấn "Report profile"
            try:
                report_button = driver.find_element(By.XPATH, report_button_xpath)
                report_button.click()
                time.sleep(1)
            except Exception as e:
                pass  # Bỏ qua lỗi và tiếp tục

            # Chọn lý do "Something about this profile"
            try:
                reason_button = driver.find_element(By.XPATH, reason_button_xpath)
                reason_button.click()
                time.sleep(1)
            except Exception as e:
                pass  # Bỏ qua lỗi và tiếp tục

            # Chọn lý do "Pretending to be someone"
            try:
                pretending_to_be_someone_button = driver.find_element(By.XPATH, "//span[text()='Pretending to be someone']")
                pretending_to_be_someone_button.click()
                time.sleep(1)
            except Exception as e:
                pass  # Bỏ qua lỗi và tiếp tục

            try:
                result = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div[4]/div/div[2]/div/div/div/div[4]/div/div/div/div[1]/div")
                result.click()
                time.sleep(2)
            except Exception as e:
                pass 

            try:
                search_input = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div[4]/div/div[2]/div/div/div/div/div/div/div/div/div/label/div/input")
                search_input.send_keys("Meta")
                time.sleep(2)
            except Exception as e:
                pass  # Bỏ qua lỗi và tiếp tục

            try:
                result = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/ul/li[1]/div/div[1]")
                result.click()
                time.sleep(2)
            except Exception as e:
                pass  # Bỏ qua lỗi và tiếp tục
            # Nhấn "Next"
            try:
                next_button = driver.find_element(By.XPATH, next_button_xpath)
                next_button.click()
                time.sleep(2)
            except Exception as e:
                pass  # Bỏ qua lỗi và tiếp tục
            # Nhấn "Submit"
            try:
                submit_button = driver.find_element(By.XPATH, submit_button_xpath)
                submit_button.click()
                time.sleep(2)
            except Exception as e:
                pass  # Bỏ qua lỗi và tiếp tục

            # Nhấn "Next"
            try:
                next_button = driver.find_element(By.XPATH, next_button_xpath)
                next_button.click()
                time.sleep(2)
            except Exception as e:
                pass  # Bỏ qua lỗi và tiếp tục

            # Nhấn "Done"
            try:
                done_button = driver.find_element(By.XPATH, done_button_xpath)
                done_button.click()
                time.sleep(1)
            except Exception as e:
                pass  # Bỏ qua lỗi và tiếp tục

            self.log_area.appendPlainText("✅ Đã báo cáo tài khoản mạo danh thành công!")


        except Exception as e:
            self.log_area.appendPlainText("Lỗi khi báo cáo tài khoản mạo danh Meta!")
            pass  # Bỏ qua lỗi và tiếp tục

# Xử lý các XPATH
three_dot_button_xpath = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[3]/div/div/div/div[2]/div/div/div"
report_button_xpath = "//span[text()='Report profile']"
reason_button_xpath = "//span[text()='Something about this profile']"
submit_button_xpath = "//span[text()='Submit']"
next_button_xpath = "//span[text()='Next']"
done_button_xpath = "//span[text()='Done']"

class CheckKEY(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🔐 Kiểm tra bản quyền")
        self.setGeometry(500, 300, 450, 200)

        self.layout = QVBoxLayout()

        self.status_label = QLabel("🔄 Đang mở tool...", self)
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setStyleSheet("font-size: 16px; color: orange;")
        self.layout.addWidget(self.status_label)

        self.setLayout(self.layout)
        self.show()

        QTimer.singleShot(1000, self.open_main_tool)

    def open_main_tool(self):
        """Mở tool chính"""
        self.close()  # 
        self.main_window = FacebookReportTool() 
        self.main_window.show() 


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CheckKEY()
    app.exec_()  

