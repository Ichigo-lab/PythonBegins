from abc import ABC, abstractmethod


class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("TextBox")


class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")


# def draw(control):
#     control.draw()


# ddl = DropDownList()
# tb = TextBox()
# draw(ddl)
# draw(tb)


def draw(controls):
    for control in controls:
        control.draw()


ddl = DropDownList()
tb = TextBox()
draw([ddl, tb])


# Duck Typing

# class TextBox(UIControl):
#     def draw(self):
#         print("TextBox")


# class DropDownList(UIControl):
#     def draw(self):
#         print("DropDownList")


# def draw(controls):
#     for control in controls:
#         control.draw()

# Long as work is being done doesnt mattter
