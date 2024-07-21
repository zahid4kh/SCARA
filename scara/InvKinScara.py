import numpy as np

a1 = 320.6  #float(input("Length of link 1 = "))
a2 = 320.0  #float(input("Length of link 2 = "))


def angles(px, py, pz): # PX, PY, PZ --->>> desired coordinates
    tool_angle = np.radians(0.0)  # float(input("Gripper angle with respect to the WCS = "))
    tcp = 277.5

    l = np.sqrt(px ** 2 + py ** 2)
    alpha_1 = np.atan2(py, px)

    cos_beta1 = (a1 ** 2 + l ** 2 - a2 ** 2) / (2 * a1 * l)
    sin_beta1 = np.sqrt(1 - cos_beta1 ** 2)
    beta1 = np.arctan2(sin_beta1, cos_beta1)

    cos_fi = (a1 ** 2 + a2 ** 2 - l ** 2) / (2 * a1 * a2)
    sin_fi = np.sqrt(1 - cos_fi ** 2)
    fi = np.arctan2(sin_fi, cos_fi)

    theta1_1 = alpha_1 - beta1
    theta2_1 = np.radians(180) - fi

    theta1_2 = alpha_1 + beta1
    theta2_2 = -(np.radians(180) - fi)

    theta4_1 = (theta1_1 + theta2_1) - tool_angle
    theta4_2 = (theta1_2 + theta2_2) - tool_angle

    d = tcp - pz

    print(f"Set 1:\n"
          f"Theta 1 = {np.degrees(theta1_1)}\n"
          f"Theta 2 = {np.degrees(theta2_1)}\n"
          f"Theta 4 = {np.degrees(theta4_1)}\n"
          f"Z stroke = {d}")

    print(f"Set 2:\n"
          f"Theta 1 = {np.degrees(theta1_2)}\n"
          f"Theta 2 = {np.degrees(theta2_2)}\n"
          f"Theta 4 = {np.degrees(theta4_2)}\n"
          f"Z stroke = {d}")


angles(-100, 250, 157.5)
