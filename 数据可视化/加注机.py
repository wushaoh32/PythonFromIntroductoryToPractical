import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QPushButton, QTabWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Excel数据可视化')
        self.setGeometry(100, 100, 800, 600)

        # 读取Excel数据
        self.df = pd.read_excel('制动.xlsx')

        # 创建布局
        layout = QVBoxLayout()

        # 创建车型号筛选按钮
        self.combo_box = QComboBox()
        self.combo_box.addItems(self.df['车型'].unique())
        self.combo_box.currentIndexChanged.connect(self.update_plots)

        # 创建更新按钮
        update_button = QPushButton('更新数据')
        update_button.clicked.connect(self.update_data)

        # 创建选项卡
        self.tab_widget = QTabWidget()

        # 创建四个折线图
        self.figures = [Figure(figsize=(6, 4), dpi=100) for _ in range(4)]
        self.canvas = [FigureCanvas(fig) for fig in self.figures]

        self.axs = [fig.add_subplot(111) for fig in self.figures]

        for i, canvas in enumerate(self.canvas):
            self.tab_widget.addTab(canvas, ['真空度', '加注压力', '加注量', '保压'][i])

        # 将组件添加到布局中
        layout.addWidget(self.combo_box)
        layout.addWidget(update_button)
        layout.addWidget(self.tab_widget)

        self.setLayout(layout)

        # 初始化折线图
        self.update_plots()

    def update_plots(self):
        selected_model = self.combo_box.currentText()
        filtered_df = self.df[self.df['车型号'] == selected_model]

        for ax, y_label in zip(self.axs, ['真空度', '加注压力', '加注量', '保压']):
            ax.clear()
            ax.plot(filtered_df['id'], filtered_df[y_label])

            # 设置最高值和最低值的预警
            max_value = filtered_df[y_label].max()
            min_value = filtered_df[y_label].min()
            ax.axhline(y=max_value, color='r', linestyle='--', label=f'最大值: {max_value}')
            ax.axhline(y=min_value, color='g', linestyle='--', label=f'最小值: {min_value}')

            ax.set_xlabel('id')
            ax.set_ylabel(y_label)
            ax.legend()

        for canvas in self.canvas:
            canvas.draw()

    def update_data(self):
        self.df = pd.read_excel('your_excel_file.xlsx')
        self.update_plots()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())