# Python OpenGL

본 포스팅은 파이썬으로 OpenGL을 구현하고 배운 내용들을 정리한 내용입니다.

# 설치


파이썬에서 OpenGL을 설치하고 사용하는 방법을 소개하려고 합니다. 간편한 개발 환경 구성을 위해 아래 프로그램을 사용하고 있습니다.

[Anaconda](https://www.anaconda.com/products/individual)

[Visual Studio Code](https://code.visualstudio.com/)

## 아나콘다 구성

위 페이지를 통해 아나콘다를 설치하고, "Anaconda Prompt"를 실행합니다. 처음 실행하면 "base"로 표시되어 있습니다. 

```
(base) C:\Users\bum44>
```

### 1. 가상환경 생성

앞으로 OpenGL을 학습하기 위한 가상환경을 생성합니다. -n 뒤에는 생성할 가상환경의 이름을 지정할 수 있습니다.

```console
conda create -n 가상환경_이름 python=3.7 -y
```

저는 OpenGL을 학습할 것이기 때문에 opengl로 지정했습니다. 그리고 파이썬 버전은 3.7입니다.

```console
conda create -n opengl python=3.7 -y
```

### 2. 가상환경 목록 보기

생성된 가상환경의 목록을 보려면 다음 명령어를 통해 확인할 수 있습니다. 

```console
conda env list
```

그럼 방금 생성한 opengl과 base가 있습니다.

```
# conda environments:
#
base                  *  C:\Users\bum44\anaconda3
opengl                C:\Users\bum44\anaconda3\envs\opengl
```

### 3. 가상환경 활성화

다음 명령어를 통해 생성된 가상환경을 활성화 할 수 있습니다. 

```console
conda activate opengl
```

```
(opengl) C:\Users\bum44>
```

## OpenGL 설치

pip 명령어를 통해 PyOpenGL과 PyOpenGL_accelerate를 설치합니다. 자세한 내용은 [여기서](https://pypi.org/project/PyOpenGL/) 확인 할 수 있습니다.

```console
pip install PyOpenGL PyOpenGL_accelerate glfw
```


# 테스트

```python
import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy
 
 
def main():
 
    # initialize glfw
    if not glfw.init():
        return
 
    window = glfw.create_window(800, 600, "My OpenGL window", None, None)
 
    if not window:
        glfw.terminate()
        return
 
    glfw.make_context_current(window)
    #            positions        colors
    triangle = [-0.5, -0.5, 0.0, 1.0, 0.0, 0.0,
                 0.5, -0.5, 0.0, 0.0, 1.0, 0.0,
                 0.0,  0.5, 0.0, 0.0, 0.0, 1.0]
 
    triangle = numpy.array(triangle, dtype = numpy.float32)
 
    vertex_shader = """
    #version 330
    in vec3 position;
    in vec3 color;
    out vec3 newColor;
    void main()
    {
        gl_Position = vec4(position, 1.0f);
        newColor = color;
    }
    """
 
    fragment_shader = """
    #version 330
    in vec3 newColor;
    out vec4 outColor;
    void main()
    {
        outColor = vec4(newColor, 1.0f);
    }
    """
    shader = OpenGL.GL.shaders.compileProgram(OpenGL.GL.shaders.compileShader(vertex_shader, GL_VERTEX_SHADER),
                                              OpenGL.GL.shaders.compileShader(fragment_shader, GL_FRAGMENT_SHADER))
 
    VBO = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(GL_ARRAY_BUFFER, 72, triangle, GL_STATIC_DRAW)
 
    position = glGetAttribLocation(shader, "position")
    glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
    glEnableVertexAttribArray(position)
 
    color = glGetAttribLocation(shader, "color")
    glVertexAttribPointer(color, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))
    glEnableVertexAttribArray(color)
 
 
    glUseProgram(shader)
 
    glClearColor(0.2, 0.3, 0.2, 1.0)
 
    while not glfw.window_should_close(window):
        glfw.poll_events()
 
        glClear(GL_COLOR_BUFFER_BIT)
 
        glDrawArrays(GL_TRIANGLES, 0, 3)
 
        glfw.swap_buffers(window)
 
    glfw.terminate()
 
if __name__ == "__main__":
    main()
```