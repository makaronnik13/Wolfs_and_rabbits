__author__ = 'makar'
from math import hypot
from sympy.physics.quantum.circuitplot import np
from scipy import integrate
from numpy import *
import pylab as p

class Evaluation():
    def __init__(self, a=1., b=0.1, c=1.5, d=0.75, x0=10, y0=2):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
        self.d = float(d)
        self.x0 = float(x0)
        self.y0 = float(y0)

    def dx_dt(self, x_base, t=0):
        return array([self.a * x_base[0] - self.b * x_base[0] * x_base[1], -self.c * x_base[1] + self.d * self.b * x_base[0] * x_base[1]])

    def d2x_dt2(self, x_base, t=0):
        return array([[self.a - self.b * x_base[1], -self.b * x_base[0]], [self.b * self.d * x_base[1], -self.c + self.b * self.d * x_base[0]]])

    def create_graphs(self):
        X_f0 = array([0., 0.])
        X_f1 = array([self.c / (self.d * self.b), self.a / self.b])
        all(self.dx_dt(X_f0) == zeros(2)) and all(self.dx_dt(X_f1) == zeros(2))  # => True
        t = linspace(0, 15, 1000)
        X0 = array([self.x0, self.y0])
        X, infodict = integrate.odeint(self.dx_dt, X0, t, full_output=True)
        rabbits, foxes = X.T
        f1 = p.figure()
        p.plot(t, rabbits, 'r-', label='Rabbits')
        p.plot(t, foxes, 'b-', label='Wolfs')
        p.grid()
        p.legend(loc='best')
        p.xlabel('time')
        p.ylabel('population')
        p.title('Evolution of wolfs and rabbits population')
        f1.savefig('wolfs_and_rabbits_1.png')
        values = linspace(0.3, 0.9, 5)
        v_colors = p.cm.autumn_r(linspace(0.3, 1., 5))
        f2 = p.figure()

        for v, col in zip(values, v_colors):
            X0 = v * X_f1
            X = integrate.odeint(self.dx_dt, X0, t)
            p.plot(X[:, 0], X[:, 1], lw=3.5 * v, color=col)
        y_max = p.ylim(ymin=0)[1]
        x_max = p.xlim(xmin=0)[1]
        nb_points = 20
        x = linspace(0, x_max, nb_points)
        y = linspace(0, y_max, nb_points)
        X1, Y1 = meshgrid(x, y)
        DX1, DY1 = self.dx_dt([X1, Y1])
        M = (hypot(DX1, DY1))
        M[M == 0] = 1.
        DX1 /= M
        DY1 /= M

        p.title('Trajectories')
        p.xlabel('Number of rabbits')
        p.ylabel('Number of wolfs')
        p.legend()
        p.grid()
        p.xlim(0, x_max)
        p.ylim(0, y_max)
        f2.savefig('wolfs_and_rabbits_2.png')
