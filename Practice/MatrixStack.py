import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

gCamAng = 0

def render(camAng):
    # enable depth test (we'll see details later)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)
    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    
    # projection transformation
    glOrtho(-1, 1, -1, 1, -1, 1)
    
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    # viewing transformation
    gluLookAt(.1*np.sin(camAng), .1, .1*np.cos(camAng), 0,0,0, 0,1,0)
    
    drawFrame()
    
    t = glfw.get_time()
    # modeling transformation
    
    # blue base transformation
    glPushMatrix()
    glTranslatef(np.sin(t), 0, 0)
    
    # blue base drawing
    glPushMatrix()
    glScalef(.2, .2, .2)
    glColor3ub(0, 0, 255)
    drawBox()
    glPopMatrix()

    # red arm transformation
    glPushMatrix()
    glRotatef(t*(180/np.pi), 0, 0, 1)
    glTranslatef(.5, 0, .01)
    
    # red arm drawing
    glPushMatrix()
    glScalef(.5, .1, .1)
    glColor3ub(255, 0, 0)
    drawBox()
    glPopMatrix()
    
    glPopMatrix()
    glPopMatrix()
    
    
def drawBox():
    glBegin(GL_QUADS)
    glVertex3fv(np.array([1, 1, 0.]))
    glVertex3fv(np.array([-1, 1, 0.]))
    glVertex3fv(np.array([-1, -1, 0.]))
    glVertex3fv(np.array([1, -1, 0.]))
    glEnd()


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
    global gCamAng
    if action == glfw.PRESS or action == glfw.REPEAT:
        if key == glfw.KEY_1:
            gCamAng += np.radians(-10)
        elif key == glfw.KEY_3:
            gCamAng += np.radians(10)


def main():
    if not glfw.init():
        return
    window = glfw.create_window(640, 640, 'Hierarchy', None, None)
    if not window:
        glfw.terminate()
        return
    glfw.make_context_current(window)
    glfw.swap_interval(1)

    while not glfw.window_should_close(window):
        glfw.poll_events()
        render(gCamAng)
        glfw.swap_buffers(window)

    glfw.terminate()

if __name__ == '__main__':
    main()