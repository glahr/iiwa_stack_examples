#!/usr/bin/env python

from robot import Robot

if __name__ == '__main__':
    robot = Robot()

    x_square = 0.2
    y_square = 0.1
    z_square = 0.0


    print("pt 1")
    robot.move(x_lin = x_square, y_lin = -y_square, z_lin = 1+z_square, w_ori = 1)
    print("pt 2")
    robot.move(x_lin = x_square, y_lin = y_square, z_lin = 1-z_square, w_ori = 1)
    print("pt 3")
    robot.move(x_lin = -x_square, y_lin = y_square, z_lin = 1-z_square, w_ori = 1)
    print("pt 4")
    robot.move(x_lin = -x_square, y_lin = -y_square, z_lin = 1+z_square, w_ori = 1)
    print("pt 5")
    robot.move(x_lin = x_square, y_lin = -y_square, z_lin = 1+z_square, w_ori = 1)
    print("DONE!")
