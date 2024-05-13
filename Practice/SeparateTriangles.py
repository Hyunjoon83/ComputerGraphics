import glfw
from OpenGL.GL import *
import numpy as np
from OpenGL.GLU import *

gCamAng = 0
gCamHeight = 1.

def createVertexArraySeparate():
    varr = np.array([
        (-1,  1,  1),  # v0
        ( 1, -1,  1),  # v1
        ( 1,  1,  1),  # v2
        
        (-1,  1,  1),  # v0
        (-1, -1,  1),  # v3
        ( 1, -1,  1),  # v2
        
        (-1,  1, -1),  # v4
        ( 1,  1, -1),  # v5
        ( 1, -1, -1),  # v6
        
        (-1,  1, -1),  # v4
        ( 1, -1, -1),  # v6
        (-1, -1, -1),  # v7
        
        (-1,  1,  1),  # v0
        ( 1,  1,  1),  # v1
        ( 1,  1, -1),  # v5
        
        (-1,  1,  1),  # v0
        ( 1,  1, -1),  # v5
        (-1,  1, -1),  # v4
        
        (-1, -1,  1),  # v3
        ( 1, -1, -1),  # v6
        ( 1, -1,  1),  # v2
        
        (-1, -1,  1),  # v3
        (-1, -1, -1),  # v7
        ( 1, -1, -1),  # v6
        
        ( 1,  1,  1),  # v1
        ( 1, -1,  1),  # v2
        ( 1, -1, -1),  # v6
        
        ( 1,  1,  1),  # v1
        ( 1, -1, -1),  # v6
        ( 1,  1, -1),  # v5
        
        (-1,  1,  1),  # v0
        (-1, -1, -1),  # v7
        (-1, -1,  1),  # v3
        
        (-1,  1,  1),  # v0
        (-1,  1, -1),  # v4
        (-1, -1, -1),  # v7
    ], 'float32')
    
    return varr


def render():
    global gCamAng, gCamHeight
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)
    glPolygonMode( GL_FRONT_AND_BACK, GL_LINE )
    
    glLoadIdentity()
    gluPerspective(45, 1, 1,10)
    gluLookAt(5*np.sin(gCamAng),gCamHeight,5*np.cos(gCamAng), 0,0,0, 0,1,0)
    
    drawFrame()
    glColor3ub(255, 255, 255)
    
    drawcube_glDrawArrays()
    
    
def drawcube_glDrawArrays():
    global gVertexArraySeparate
    varr = gVertexArraySeparate
    glEnableClientState(GL_VERTEX_ARRAY)
    glVertexPointer(3, GL_FLOAT, 3 * varr.itemsize, varr)
    glDrawArrays(GL_TRIANGLES, 0, int(varr.size/3))
    
    
def drawFrame():
    glBegin(GL_LINES)
    glColor3ub(255, 0, 0)
    glVertex3fv(np.array([0., 0., 0.]))
    glVertex3fv(np.array([1., 0., 0.]))
    glColor3ub(0, 255, 0)
    glVertex3fv(np.array([0., 0., 0.]))
    glVertex3fv(np.array([0., 1., 0.]))
    glColor3ub(0, 0, 255)
    glVertex3fv(np.array([0., 0., 0]))
    glVertex3fv(np.array([0., 0., 1.]))
    glEnd()
    
    
def key_callback(window, key, scancode, action, mods):
    global gCamAng, gCamHeight
    if action == glfw.PRESS or action == glfw.REPEAT:
        if key == glfw.KEY_1:
            gCamAng += np.radians(-10)
        elif key == glfw.KEY_3:
            gCamAng += np.radians(10)
        elif key == glfw.KEY_2:
            gCamHeight += .1
        elif key == glfw.KEY_W:
            gCamHeight += -.1
    
    
gVertexArraySeparate = None

def main():
    global gVertexArraySeparate
    
    if not glfw.init():
        return
    window = glfw.create_window(640,640,'Lecture10', None,None)
    if not window:
        glfw.terminate()
        return
    glfw.make_context_current(window)
    glfw.set_key_callback(window, key_callback)
    
    gVertexArraySeparate = createVertexArraySeparate()
    
    while not glfw.window_should_close(window):
        glfw.poll_events()
        render()
        glfw.swap_buffers(window)
        
    glfw.terminate()
    
if __name__ == "__main__":
    main()