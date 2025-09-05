import time
from math import sin, cos, pi

phi_step = 0.02
theta_step = 0.07
a_spacing = 0.1
b_spacing = 0.1

screen_w = 25
screen_h = 25

r1, r2 = 1, 2
k2 = 5

k1 = (screen_w * k2 * 3) / ((r1+r2)*8)



def render_frame(A:float, B:float):
    output = [[' ' for _ in range(screen_w)] for _ in range(screen_h)]
    z_buffer = [[0 for _ in range(screen_w)] for _ in range(screen_h)]
    cosA = cos(A)
    sinA = sin(A)
    cosB = cos(B)
    sinB = sin(B)

    # Step 1 calculate coordinate of point of donut in 3d space
    # step 2 calucate its pixcel position in 2d screen 
    # step 3 calculate z buffer
    # step 4 calculate lumin
    # step 5 assign char for final output 

    theta = 0.0
    while theta < 2*pi:
        sintheta = sin(theta)
        costheta = cos(theta)

        circlex = r2 + r1 * costheta
        circley = r1 * sintheta

        phi = 0.0
        while phi < 2 * pi:
            cosphi = cos(phi)
            sinphi = sin(phi)

            x = circlex*(cosB*cosphi + sinA*sinB*sinphi)- circley*cosA*sinB
            y = circlex*(sinB*cosphi - sinA*cosB*sinphi)+ circley*cosA*cosB

            z = k2 + cosA*circlex*sinphi + circley*sinA

            ooz = 1/z # z-bufer value

            x_px = int(screen_w // 2 + x*k1*ooz)
            y_px = int(screen_h // 2 - y * k1 * ooz )  # Scale y by 0.5 to adjust for terminal aspect ratio

            L = cosphi*costheta*sinB - cosA*costheta*sinphi - sinA*sintheta + cosB*(cosA*sintheta - costheta*sinA*sinphi)

            if L > 0:

                if (0 <= x_px < screen_w and 0 <= y_px < screen_h) and ooz > z_buffer[y_px][x_px]:
                    z_buffer[y_px][x_px] = ooz
                    l_idx = int(L*8)
                    output[y_px][x_px] = ".,-~:;=!*#$@"[l_idx]
            phi += phi_step
        theta += theta_step
    
    return output





    

def print_frame(mat):
    print()
    for row in mat:
        print("".join(row))

a = 0.0
b = 0.0

while True:
    a = (a+a_spacing) % (2*pi)
    b = (b+a_spacing) % (2*pi)

    mat = render_frame(a,b)
    print_frame(mat)
    time.sleep(0.01)
    print("\x1b[27A")
