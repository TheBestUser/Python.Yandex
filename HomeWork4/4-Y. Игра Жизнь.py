import sys
import functools
from PyQt5.QtCore import Qt, QTimer, QRect
from PyQt5.QtGui import QImage, QColor, QPainter, QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QActionGroup, QWidget, QVBoxLayout, QScrollArea, \
    QFileDialog, QMessageBox, QToolBar

M = 200
N = 200


class Model:
    def __init__(self, m, n):
        self.m, self.n = m, n
        self.cell_size = 15
        self.cells = []
        for i in range(self.m):
            self.cells.append([])
            for _ in range(self.n):
                self.cells[i].append([0, 0])

    def step(self):
        for x in range(self.m):
            for y in range(self.n):
                k = 0
                for xx in range(-1, 2):
                    for yy in range(-1, 2):
                        try:
                            if x + xx < 0 or y + yy < 0:
                                continue
                            if (xx != 0 or yy != 0) and self.cells[x + xx][y + yy][0] == 1:
                                k += 1
                        except IndexError:
                            pass

                if k == 3:
                    self.cells[x][y][1] = 1
                elif k <= 1 or k >= 4:
                    self.cells[x][y][1] = 0
                elif k == 2 and self.cells[x][y][0] == 1:
                    self.cells[x][y][1] = 1

        for rows in self.cells:
            for cell in rows:
                cell[0] = cell[1]

    def clear(self):
        for rows in self.cells:
            for cell in rows:
                cell[0] = 0

    def setLive(self, x, y):
        self.cells[x][y][0] = 1

    def setDead(self, x, y):
        self.cells[x][y][0] = 0

    def cellIsLive(self, x, y):
        return self.cells[x][y][0] == 1


class DrawPanel(QWidget):
    def __init__(self):
        super().__init__()

        self.life = Model(M, N)
        self._timer = QTimer()

        self._speed = 1
        self._live_color = QColor(0, 255, 0)
        self._dead_color = QColor(0, 0, 0)
        self._timer.timeout.connect(self._timerAction)

        self._im = QImage(self.life.m * self.life.cell_size, self.life.n * self.life.cell_size, QImage.Format_ARGB32)
        self._im_dead = QImage(self.life.m * self.life.cell_size, self.life.n * self.life.cell_size,
                               QImage.Format_ARGB32)
        self.setGeometry(QRect(0, 0, self.life.m * self.life.cell_size, self.life.n * self.life.cell_size))
        self._im_dead.fill(QColor(105, 105, 105))

        self._drawBackground()
        self._drawCells()

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.drawImage(0, 0, self._im_dead)
        painter.drawImage(0, 0, self._im)

    def _drawBackground(self):
        qp = QPainter(self._im_dead)
        cs = self.life.cell_size
        qp.setBrush(self._dead_color)
        for x in range(self.life.m):
            for y in range(self.life.n):
                qp.drawRect(x * cs, y * cs, cs - 2, cs - 2)

    def _drawCells(self):
        self._im = QImage(self.life.m * self.life.cell_size, self.life.n * self.life.cell_size, QImage.Format_ARGB32)
        qp = QPainter(self._im)
        cs = self.life.cell_size
        qp.setBrush(self._live_color)
        for x in range(self.life.m):
            for y in range(self.life.n):
                if self.life.cellIsLive(x, y):
                    qp.drawRect(x * cs, y * cs, cs - 2, cs - 2)

    def _drawCell(self, x, y):
        qp = QPainter(self._im)
        cs = self.life.cell_size
        if self.life.cellIsLive(x, y):
            qp.setBrush(self._live_color)
        else:
            qp.setBrush(self._dead_color)
        qp.drawRect(x * cs, y * cs, cs - 2, cs - 2)

    def mouseMoveEvent(self, e):
        try:
            self.mousePressEvent(e)
        except BaseException:
            print("pass")

    def mousePressEvent(self, e):
        if self._timer.isActive():
            return

        xx = int(e.x() / self.life.cell_size)
        yy = int(e.y() / self.life.cell_size)

        if e.buttons() == Qt.LeftButton:
            self.life.setLive(xx, yy)
        elif e.buttons() == Qt.RightButton:
            self.life.setDead(xx, yy)
        self._drawCell(xx, yy)
        self.repaint()

    def buttonStep(self):
        if self._timer.isActive():
            return
        self.life.step()
        self._drawCells()
        self.repaint()

    def buttonClear(self):
        if self._timer.isActive():
            return
        self.life.clear()
        self._drawCells()
        self.repaint()

    def toggle_timer(self):
        if self._timer.isActive():
            self._timer.stop()
        else:
            self._timer.start(1000 / self._speed)

    def setSpeed(self, n):
        self._speed = n
        self._timer.setInterval(1000 / self._speed)

    def setLife(self, new_life):
        self.life = new_life
        self._im = QImage(self.life.m * self.life.cell_size, self.life.n * self.life.cell_size, QImage.Format_ARGB32)
        self._im_dead = QImage(self.life.m * self.life.cell_size, self.life.n * self.life.cell_size,
                               QImage.Format_ARGB32)
        self.setGeometry(QRect(0, 0, self.life.m * self.life.cell_size, self.life.n * self.life.cell_size))
        self._im_dead.fill(QColor(105, 105, 105))

        self._drawBackground()
        self._drawCells()

    def _timerAction(self):
        self.life.step()
        self._drawCells()
        self.repaint()


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.central_widget = QWidget()
        self._scroll_area = QScrollArea(self)
        self._scroll_w = DrawPanel()

        self.initUI()

    def initUI(self):
        self.addToolBar(self._createToolBar())

        layout = QVBoxLayout(self.central_widget)
        layout.addWidget(self._scroll_area)

        self._scroll_area.setWidget(self._scroll_w)

        self.setCentralWidget(self.central_widget)
        self.setGeometry(200, 200, 620, 493)
        self.setWindowTitle("Игра Жизнь")
        # self.setWindowIcon(QIcon("LifeIcon.jpg"))

        self.show()

    def _createToolBar(self):
        tool_bar = QToolBar()

        open_action = QAction('Open', self, triggered=self._openFile)
        save_action = QAction('Save', self, triggered=self._saveFile)
        start_action = QAction('Run', self, checkable=True, triggered=self._scroll_w.toggle_timer)
        step_action = QAction('Step', self, triggered=self._scroll_w.buttonStep)
        clear_action = QAction('Clear', self, triggered=self._scroll_w.buttonClear)

        ag = QActionGroup(self, exclusive=True)
        x1 = ag.addAction(
            QAction('x1', self, checkable=True, checked=True, triggered=functools.partial(self._scroll_w.setSpeed, 1)))
        x2 = ag.addAction(QAction('x2', self, checkable=True, triggered=functools.partial(self._scroll_w.setSpeed, 2)))
        x4 = ag.addAction(QAction('x4', self, checkable=True, triggered=functools.partial(self._scroll_w.setSpeed, 4)))
        x8 = ag.addAction(QAction('x8', self, checkable=True, triggered=functools.partial(self._scroll_w.setSpeed, 8)))
        x16 = ag.addAction(QAction('x12', self, checkable=True, triggered=functools.partial(self._scroll_w.setSpeed, 12)))

        tool_bar.addAction(open_action)
        tool_bar.addAction(save_action)
        tool_bar.addSeparator()
        tool_bar.addAction(start_action)
        tool_bar.addAction(step_action)
        tool_bar.addAction(clear_action)
        tool_bar.addSeparator()
        tool_bar.addAction(x1)
        tool_bar.addAction(x2)
        tool_bar.addAction(x4)
        tool_bar.addAction(x8)
        tool_bar.addAction(x16)
        tool_bar.addSeparator()

        return tool_bar

    def _openFile(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open file', '', 'TXT Files (*.txt)')[0]
        if file_name is "":
            return

        with open(file_name, 'r') as f:
            try:
                data = f.readline()
                m, n = map(int, data.split())
                if m <= 0 or n <= 0:
                    raise ValueError

                life = Model(m, n)
                for line in f:
                    x, y = map(int, line.split())
                    life.setLive(x, y)

                self._scroll_w.setLife(life)
            except ValueError:
                QMessageBox.information(self, "Error!", "The file \"" + file_name + "\" is incorrect")
                return

    def _saveFile(self):
        file_name = QFileDialog.getSaveFileName(self, 'Save file', '', 'TXT Files (*.txt)')[0]
        if file_name is "":
            return

        with open(file_name, 'w') as f:
            life = self._scroll_w.life
            print(life.m, life.n, file=f)
            i = 0
            for cell in life.cells:
                if cell[0] == 1:
                    print(i % life.m, int(i / life.m), file=f)
                i += 1
        return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
