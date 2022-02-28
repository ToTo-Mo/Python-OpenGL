import glfw
from OpenGL.GL import *
import numpy as np

class Window():
    def __init__(self, width:int, height:int, title:str) -> None:
        if not glfw.init():
            raise Exception("glfw can not be initialized")

        self.width, self.height = width, height
        self.title = title
        self.window = glfw.create_window(width, height, title, None, None)

        if not self.window:
            glfw.terminate()
            raise Exception("glfw window can not be created")
    
        glfw.set_window_pos(self.window,xpos=0,ypos=0)
        glfw.make_context_current(self.window)

    def start(self):
        glClearColor(0, 0.2, 0.1,1)

        vertices = [-0.5, -0.5 , 0.0,
                         0.5, -0.5, 0.0,
                         0.0, 0.5, 0.0]
        
        colors = [1.0, 0.0, 0.0,
                        0.0,1.0,0.0,
                        0.0,0.0,1.0]
        
        self.vertices = np.array(vertices, dtype=np.float32)
        self.colors = np.array(colors, dtype=np.float32)

        glEnableClientState(GL_VERTEX_ARRAY)
        glVertexPointer(3, GL_FLOAT, 0, vertices)

        glEnableClientState(GL_COLOR_ARRAY)
        glColorPointer(3, GL_FLOAT, 0, colors)

    def main_loop(self):

        self.start()

        while not glfw.window_should_close(self.window):
            glfw.poll_events()

            # to do
            draw_triangle()

            glfw.swap_buffers(self.window)
        
        glfw.terminate()

def draw_triangle():
    glClear(GL_COLOR_BUFFER_BIT)
    glDrawArrays(GL_TRIANGLES, 0,3)

def rotate_triangle():
    glClear(GL_COLOR_BUFFER_BIT)
    glRotatef(10,0,1,0)
    glDrawArrays(GL_TRIANGLES, 0,3)


if __name__ =="__main__":
    window = Window(1280,720, "Opengl Window")
    window.main_loop()