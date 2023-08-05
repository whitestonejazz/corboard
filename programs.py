from corboard import Sentence, Polynomial


# The Lorenz system (S=10, R=28, B=8/3)
# dx/dt = S*(y - x)
# dy/dt = x*(R - z) - y
# dz/dt = x*y - B*z
lorenz_corboard = [
    Polynomial('dx', '+sigma$lorenz*ypos -sigma$lorenz*xpos'),
    Polynomial('dy', '+xpos*rho$lorenz -xpos*zpos -ypos'),
    Polynomial('dz', '+xpos*ypos -beta$lorenz*zpos'),
    [Sentence('dx', '*=', 'dt$global'), Sentence('dy', '*=', 'dt$global'), Sentence('dz', '*=', 'dt$global')],
    [Sentence('xpos', '+=', 'dx'), Sentence('ypos', '+=', 'dy'), Sentence('zpos', '+=', 'dz')]
]


# Halvorsen system (A=1.4, B=4)
# dx/dt = -A*x - B*y - B*z - y*y
# dy/dt = -A*y - B*z - B*x - z*z
# dz/dt = -A*z - B*x - B*y - x*x
halvorsen_corboard = [
    Polynomial('dx', '-A$halvorsen*xpos -B$halvorsen*ypos -B$halvorsen*zpos -ypos*ypos'),
    Polynomial('dy', '-B$halvorsen*xpos -A$halvorsen*ypos -B$halvorsen*zpos -zpos*zpos'),
    Polynomial('dz', '-B$halvorsen*xpos -B$halvorsen*ypos -A$halvorsen*zpos -xpos*xpos'),
    [Sentence('dx', '*=', 'dt$global'), Sentence('dy', '*=', 'dt$global'), Sentence('dz', '*=', 'dt$global')],
    [Sentence('xpos', '+=', 'dx'), Sentence('ypos', '+=', 'dy'), Sentence('zpos', '+=', 'dz')]
]


# Arneodo system (A=-5.5, B=3.5)
# dx/dt = y
# dy/dt = z
# dz/dt = -A*x - B*y - z - x*x*x
arneodo_corboard = [
    Polynomial('dx', '+ypos'),
    Polynomial('dy', '+zpos'),
    Polynomial('dz', '-$A$arneodo*xpos -B$arneodo*ypos -zpos -xpos*xpos*xpos'),
    [Sentence('dx', '*=', 'dt$global'), Sentence('dy', '*=', 'dt$global'), Sentence('dz', '*=', 'dt$global')],
    [Sentence('xpos', '+=', 'dx'), Sentence('ypos', '+=', 'dy'), Sentence('zpos', '+=', 'dz')]
]


# Bouali system (A=0.3, B=4, C=1.5, D=0.005)
# dx/dt = x*(B - y) + A*z
# dy/dt = -y*(1 - x*x)
# dz/dt = -x*(C - z) - D*z
bouali_corboard = [
    Polynomial('dx', '+xpos*B$bouali -xpos*ypos +A$bouali*zpos'),
    Polynomial('dy', '-ypos +ypos*xpos*xpos'),
    Polynomial('dz', '-xpos*C$bouali +xpos*zpos -D$bouali*zpos'),
    [Sentence('dx', '*=', 'dt$global'), Sentence('dy', '*=', 'dt$global'), Sentence('dz', '*=', 'dt$global')],
    [Sentence('xpos', '+=', 'dx'), Sentence('ypos', '+=', 'dy'), Sentence('zpos', '+=', 'dz')]
]


# Chencel system (A=36, B=3, C=20)
# dx/dt = A*(y - x)
# dy/dt = -x*z + C*y
# dz/dt = x*y - B*z
chencel_chapter = [
    Polynomial('dx', '+A$chencel*ypos -A$chencel*xpos'),
    Polynomial('dy', '-xpos*zpos +C$chencel*ypos'),
    Polynomial('dz', '+xpos*ypos -B$chencel*zpos'),
    [Sentence('dx', '*=', 'dt$global'), Sentence('dy', '*=', 'dt$global'), Sentence('dz', '*=', 'dt$global')],
    [Sentence('xpos', '+=', 'dx'), Sentence('ypos', '+=', 'dy'), Sentence('zpos', '+=', 'dz')]
]


# TODO: Not included; too large for the fake floating-point scoreboard multiplication.
# Chenlee system (A=5, B=-10, C=-0.38, D=1/3)
# dx/dt = A*x - y*z
# dy/dt = B*y + x*z
# dz/dt = C*z + D*x*y
chenlee_chapter = [
    Polynomial('dx', '+A$chenlee*xpos -ypos*zpos'),
    Polynomial('dy', '+B$chenlee*ypos +xpos*zpos'),
    Polynomial('dz', '+C$chenlee*zpos +D$chenlee*xpos*ypos'),
    [Sentence('dx', '*=', 'dt$global'), Sentence('dy', '*=', 'dt$global'), Sentence('dz', '*=', 'dt$global')],
    [Sentence('xpos', '+=', 'dx'), Sentence('ypos', '+=', 'dy'), Sentence('zpos', '+=', 'dz')]
]


# TODO: Not included; too large for the fake floating-point scoreboard multiplication.
# Dequanli system (A=40, C=1.833, D=0.16, E=0.65, K=55, F=20)
# dx/dt = A*(y-x) + D*x*z
# dy/dt = K*x + F*y - x*z
# dz/dt = C*z + x*y - E*x*x
dequanli_chapter = [
    Polynomial('dx', '+A$dequanli*ypos -A$dequanli*xpos +D$dequanli*xpos*zpos'),
    Polynomial('dy', '+K$dequanli*xpos +F$dequanli*ypos -xpos*zpos'),
    Polynomial('dz', '+C$dequanli*zpos +xpos*ypos -E$dequanli*xpos*xpos'),
    [Sentence('dx', '*=', 'dt$global'), Sentence('dy', '*=', 'dt$global'), Sentence('dz', '*=', 'dt$global')],
    [Sentence('xpos', '+=', 'dx'), Sentence('ypos', '+=', 'dy'), Sentence('zpos', '+=', 'dz')]
]


# Rossler system (A=0.2, C=5.7)
# dx/dt = -y - z
# dy/dt = x + A*y
# dz/dt = A + z*(x - C)
rossler_chapter = [
    Polynomial('dx', '-ypos -zpos'),
    Polynomial('dy', '+xpos +A$rossler*ypos'),
    Polynomial('dz', '+A$rossler +zpos*xpos -zpos*C$rossler'),
    [Sentence('dx', '*=', 'dt$global'), Sentence('dy', '*=', 'dt$global'), Sentence('dz', '*=', 'dt$global')],
    [Sentence('xpos', '+=', 'dx'), Sentence('ypos', '+=', 'dy'), Sentence('zpos', '+=', 'dz')]
]


### BLANK ATTRACTOR SYSTEM TEMPLATE ###
# NAME system (CONSTANTS)
# dx/dt =
# dy/dt =
# dz/dt =
NAME_chapter = [
    Polynomial('dx', ''),
    Polynomial('dy', ''),
    Polynomial('dz', ''),
    [Sentence('dx', '*=', 'dt$global'), Sentence('dy', '*=', 'dt$global'), Sentence('dz', '*=', 'dt$global')],
    [Sentence('xpos', '+=', 'dx'), Sentence('ypos', '+=', 'dy'), Sentence('zpos', '+=', 'dz')]
]
