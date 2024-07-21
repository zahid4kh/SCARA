import numpy as np

# INPUTS
th1 = np.radians(0.0)
th2 = np.radians(0.0)
th4 = np.radians(0.0)
stroke = 0.0

# CONSTANTS
a1 = 398.5  # height from frame 0 to frame 1
a2 = 320.6  # distance from frame 0 to frame 1 in X0 direction
a3 = 320.0    # distance from frame 1 to frame 2 in X1 direction
a4 = 173.0    # height from frame 1 to frame 2
a5 = 294.0    # height from frame 2 to frame 3

# DEPENDING ON TOOL LENGTH a5 MIGHT DIFFER

# DH PARAMETERS
zero = np.radians(0)
alpha = [np.radians(0), np.radians(180), np.radians(0), np.radians(0)]
r = [a2, a3, 0, 0]
d = [a1, a4, a5 + stroke, 0]

H0_1 = np.array([[np.cos(th1), -np.sin(th1)*np.cos(alpha[0]), np.sin(th1)*np.sin(alpha[0]), r[0]*np.cos(th1)],
                [np.sin(th1), np.cos(th1)*np.cos(alpha[0]), -np.cos(th1)*np.sin(alpha[0]), r[0]*np.sin(th1)],
                [0, np.sin(alpha[0]), np.cos(alpha[0]), d[0]],
                [0, 0, 0, 1]])
H1_2 = np.array([[np.cos(th2), -np.sin(th2)*np.cos(alpha[1]), np.sin(th2)*np.sin(alpha[1]), r[1]*np.cos(th2)],
                [np.sin(th2), np.cos(th2)*np.cos(alpha[1]), -np.cos(th2)*np.sin(alpha[1]), r[1]*np.sin(th2)],
                [0, np.sin(alpha[1]), np.cos(alpha[1]), d[1]],
                [0, 0, 0, 1]])
H2_3 = np.array([[np.cos(zero), -np.sin(zero)*np.cos(alpha[2]), np.sin(zero)*np.sin(alpha[2]), r[2]*np.cos(zero)],
                [np.sin(zero), np.cos(zero)*np.cos(alpha[2]), -np.cos(zero)*np.sin(alpha[2]), r[2]*np.sin(zero)],
                [0, np.sin(alpha[2]), np.cos(alpha[2]), d[2]],
                [0, 0, 0, 1]])
H3_4 = np.array([[np.cos(th3), -np.sin(th3)*np.cos(alpha[3]), np.sin(th3)*np.sin(alpha[3]), r[3]*np.cos(th3)],
                [np.sin(th3), np.cos(th3)*np.cos(alpha[3]), -np.cos(th3)*np.sin(alpha[3]), r[3]*np.sin(th3)],
                [0, np.sin(alpha[3]), np.cos(alpha[3]), d[3]],
                [0, 0, 0, 1]])

H0_2 = np.dot(H0_1, H1_2)
H2_4 = np.dot(H2_3, H3_4)
H0_4 = np.dot(H0_2, H2_4)
print(np.round(H0_4, 3))
