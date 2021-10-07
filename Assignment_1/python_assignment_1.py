#!/usr/bin/env python
# coding: utf-8


import numpy as np
import matplotlib.pyplot as plt


# Q6. Prove that the points (2, 4), (3, 2), (8, 4) and (7, 6) are the vertices of a parallelogram.

A = np.array([2,4])
B = np.array([3,2])
C = np.array([8,4])
D = np.array([7,6])
print(f'A={A}\nB={B}\nC={C}\nD={D}')

# Now we need to check if the opposite sides are parallel by checking if A−B=k1(D−C) and A−D=k2(B−C)
AB = A - B
DC = D - C
print(f'AB = {AB} and DC = {DC}')

AD = A - D
BC = B - C
print(f'AC = {AD} and BC = {BC}')

if np.all((AB == DC) & (AD == BC)) :
    print('Opposite sides AB‖CD and AD‖BC \nThus, ABCD is a parallelogram.')
else:
    print('Here Opposite sides  are not parallel  \n Thus, ABCD does not form a parallelogram.')


#Generate line points
def line_gen(A,B):
    len =10
    dim = A.shape[0]
    x_AB = np.zeros((dim,len))
    lam_1 = np.linspace(0,1,len)
    for i in range(len):
        temp1 = A + lam_1[i]*(B-A)
        x_AB[:,i]= temp1.T
    return x_AB


# Generating all lines

x_AB = line_gen(A, B)
x_BC = line_gen(B, C)
x_CD = line_gen(C, D)
x_DA = line_gen(D, A)


plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CD[0,:],x_CD[1,:],label='$CD$')
plt.plot(x_DA[0,:],x_DA[1,:],label='$DA$')

plt.legend()
plt.annotate("A", (2,4))
plt.annotate("B", (3,2))
plt.annotate("C", (8,4))
plt.annotate("D", (7,6))

plt.ylabel('$y-axis$')
plt.xlabel('$x-axis$')
plt.grid() 
plt.savefig('parallelogram.jpg', dpi=200)
plt.show()

