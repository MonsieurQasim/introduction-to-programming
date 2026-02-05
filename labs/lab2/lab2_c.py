# FOR THIS ASSIGNMENT I USED COPILOT,
# THE PTOMPT I USED IS THE FOLLOWING:
# instructions:
#using the ellipse equation and the line equation, to solve the quadratic equation Ax^2 + Bx + C = 0, substitute x values back into the line equation to find y values.
#interaction cases:
#2 points: the Discriminant D=B^2-4AC>0
#1 point: the Discriminant D=B^2-4AC=0
#No interactions: the Discriminant D=B^2-4AC>0
# I want it to:
#it drwas the ellipse and line (I already installed pip install matplotlib, pip install numpy).
#program asks the user to input line and ellipse parameters.
#given parameters are casted to numbers.
#line and ellipse are drawn.
#print information if there are no intersection points.
#print intersection point(s) coordinates if there are any.





import sys
import math
import numpy as np
import matplotlib.pyplot as plt


def prompt_float(prompt):
    try:
        return float(input(prompt))
    except Exception:
        print("Invalid number entered. Exiting.")
        sys.exit(1)


def main():
    print("Ellipse: ((x-h)^2)/a^2 + ((y-k)^2)/b^2 = 1")
    h = prompt_float("Enter ellipse center h (x-coordinate): ")
    k = prompt_float("Enter ellipse center k (y-coordinate): ")
    a = prompt_float("Enter ellipse semi-axis a (along x): ")
    b = prompt_float("Enter ellipse semi-axis b (along y): ")
    if a <= 0 or b <= 0:
        print("Semi-axes must be positive. Exiting.")
        sys.exit(1)

    print("\nLine (slope-intercept form): y = m*x + c")
    m = prompt_float("Enter slope m: ")
    c = prompt_float("Enter intercept c: ")

    # Compute intersections
    # Compute intersections: substitute y = m*x + c into ellipse
    intersections = []
    A = (1.0 / (a * a)) + (m * m) / (b * b)
    B = (-2.0 * h) / (a * a) + (2.0 * m * (c - k)) / (b * b)
    C = (h * h) / (a * a) + ((c - k) * (c - k)) / (b * b) - 1.0

    D = B * B - 4 * A * C
    if D < 0:
        discriminant_case = -1
    elif abs(D) < 1e-12:
        discriminant_case = 0
        x = -B / (2 * A)
        y = m * x + c
        intersections.append((x, y))
    else:
        discriminant_case = 2
        sqrtD = math.sqrt(D)
        x1 = (-B + sqrtD) / (2 * A)
        x2 = (-B - sqrtD) / (2 * A)
        y1 = m * x1 + c
        y2 = m * x2 + c
        intersections.append((x1, y1))
        intersections.append((x2, y2))

    # Print results
    if discriminant_case == -1:
        print("\nNo intersection points between the line and the ellipse.")
    elif discriminant_case == 0:
        print("\nTangent: exactly 1 intersection point:")
        for pt in intersections:
            print(f"(x, y) = ({pt[0]:.6f}, {pt[1]:.6f})")
    else:
        print("\nTwo intersection points:")
        for pt in intersections:
            print(f"(x, y) = ({pt[0]:.6f}, {pt[1]:.6f})")

    # Plotting
    theta = np.linspace(0, 2 * np.pi, 400)
    xe = h + a * np.cos(theta)
    ye = k + b * np.sin(theta)

    fig, ax = plt.subplots()
    ax.plot(xe, ye, label='Ellipse')

    # Plot line (y = m*x + c)
    xmin = h - a - 1
    xmax = h + a + 1
    xs = np.linspace(xmin, xmax, 400)
    ys = m * xs + c
    ax.plot(xs, ys, 'r', label=f'y = {m}x + {c}')

    # Mark intersection points
    if intersections:
        xs = [p[0] for p in intersections]
        ys = [p[1] for p in intersections]
        ax.scatter(xs, ys, color='magenta', zorder=5, label='Intersection(s)')

    ax.set_aspect('equal', adjustable='box')
    ax.grid(True)
    ax.legend()
    ax.set_title('Ellipse and Line Intersection')
    plt.show()


if __name__ == '__main__':
    main()
