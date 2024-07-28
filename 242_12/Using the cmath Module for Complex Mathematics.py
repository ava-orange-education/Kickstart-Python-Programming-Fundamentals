import cmath

z = 1 + 2j

sqrt_z = cmath.sqrt(z)
exp_z = cmath.exp(z)
log_z = cmath.log(z)
sin_z = cmath.sin(z)
cos_z = cmath.cos(z)
sinh_z = cmath.sinh(z)

print(f"Square root of {z}: {sqrt_z}")  # Output: (1.272019649514069+0.7861513777574233j)
print(f"Exponential of {z}: {exp_z}")  # Output: (-1.1312043837568135+2.4717266720048188j)
print(f"Natural logarithm of {z}: {log_z}")  # Output: (0.8047189562170503+1.1071487177940904j)
print(f"Sine of {z}: {sin_z}")  # Output: (3.165778513216168+1.9596010414216063j)
print(f"Cosine of {z}: {cos_z}")  # Output: (2.0327230070196656-3.0518977991517997j)
print(f"Hyperbolic sine of {z}: {sinh_z}")  # Output: (1.9596010414216063+3.165778513216168j)
