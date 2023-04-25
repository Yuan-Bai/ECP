from app.settings import MAX_WINDOW_NUMS


class Switch:
    def __init__(self, parent_window):
        self.parent_window = parent_window
        self.parent_layout = parent_window.layout()
        self.children_index = len(self.parent_window.children())-1
        self.children_type = []
        for ele in self.parent_window.children():
            self.children_type.append(type(ele))

    def switch_windows(self, window_class, *args, insert_index=0):
        if self.children_type.__contains__(window_class):
            self.parent_window.children()[self.children_index].hide()
            self.children_index = self.children_type.index(window_class)
            self.parent_window.children()[self.children_index].show()
        else:
            self.children_index = len(self.parent_window.children())-1
            if len(self.parent_window.children()) != 1:
                self.parent_window.children()[self.children_index].hide()
            window = window_class(*args, parent=self.parent_window)
            self.parent_layout.insertWidget(insert_index, window)
            self.children_type.append(window_class)
            self.pop_if_max()
            self.children_index = len(self.children_type)-1

    def pop_if_max(self):
        sup = len(self.parent_window.children())-MAX_WINDOW_NUMS
        if sup > 0:
            for index in range(sup):
                self.parent_window.children()[index+1].deleteLater()
                self.children_type.pop(index+1)

    def exchange_ele(self, index):
        self.parent_window.children()[index], self.parent_window.children()[-1] =\
            self.parent_window.children()[-1], self.parent_window.children()[index]
        self.children_type[index], self.children_type[-1] = self.children_type[-1], self.children_type[index]
