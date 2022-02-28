import glfw

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

    def main_loop(self):
        # 6. the main application loop
        while not glfw.window_should_close(self.window):
            glfw.poll_events()

            # use double buffering
            glfw.swap_buffers(self.window)
        
        # 7. terminate glfw
        glfw.terminate()
    
if __name__ =="__main__":
    window = Window(1280,720, "Opengl Window")
    window.main_loop()