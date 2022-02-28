import glfw
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import numpy as np

vertex_src ='''
# version 330 
in vec3 a_position; 
void main(){
    gl_Position = vec4(a_position, 1.0);
}'''

fragment_src ='''
# version 330 
out vec4 out_color; 
void main(){
    out_color = vec4(1.0, 0.0, 0.0, 1.0);
}'''

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

        shader = compileProgram(compileShader(vertex_src, GL_VERTEX_SHADER), 
                                compileShader(fragment_src, GL_FRAGMENT_SHADER))

        # VBO : Vertex Buffer Object
        VBO = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, VBO)
        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL_STATIC_DRAW)

        position = glGetAttribLocation(shader, "a_position")
        glEnableVertexAttribArray(position)
        glVertexAttribPointer(position,3,GL_FLOAT,GL_FALSE, 0, ctypes.c_void_p(0))

        glUseProgram(shader)


    def main_loop(self):

        self.start()

        while not glfw.window_should_close(self.window):
            glfw.poll_events()

            # to do

            glfw.swap_buffers(self.window)
        
        glfw.terminate()


if __name__ =="__main__":
    window = Window(1280,720, "Opengl Window")
    window.main_loop()