class CanvasWithShapes:
    height = 10
    width = 10

    def __init__(self, shape):
        print(" 0123456789")
        for num in range(0, 10):
            print(num) 


    def add_shape(self, shape):
        print(shape)

class Shape:
    char = "*"
    fill_char = "/"

    def __init__(self, start_x, start_y, end_x, end_y):
        print("***")
        print("* *")
        print("***")
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y 
        
    def make_calculations(self):
        # line0 = " 0123456789"
        # line1 = "0          "
        # line2 = "1          "
        # line3 = "2          "
        # line4 = "3          "
        # line5 = "4          "
        # line6 = "5          "
        # line7 = "6          "
        # line8 = "7          "
        # line9 = "8          "
        # line10 = "9          "

        canvas_with_shape = [
                                "          ",
                                "          ",
                                "          ",
                                "          ",
                                "          ",
                                "          ",
                                "          ",
                                "          ",
                                "          ",
                                "          ",]

        height = self.end_y - self.start_y + 1
        width = self.end_x - self.start_x + 1

        print(canvas_with_shape[self.end_y][self.start_x:(self.end_x+1)])


        # print(canvas_with_shape)


    def translate(self, axis, num):
        # add num numbers to the values of axis axis and re-render canvas with shape.
        pass

        


