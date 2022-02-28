import glfw

def main():
    # 1. initialize glfw library
    if not glfw.init():
        raise Exception("glfw can not be initialized")

    # 2. create window
    window = glfw.create_window(1280, 720, "OpenGL Window", None, None)

    # 3. check if window was created
    if not window:
        glfw.terminate()
        raise Exception("glfw window can not be created")
    
    # 4. set window's position
    glfw.set_window_pos(window,xpos=400,ypos=200)

    # 5. make the context current
    glfw.make_context_current(window)

    # 6. the main application loop
    while not glfw.window_should_close(window):
        glfw.poll_events()

        # use double buffering
        glfw.swap_buffers(window)
    
    # 7. terminate glfw
    glfw.terminate()

if __name__=="__main__":
    main()
