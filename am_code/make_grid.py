import numpy as np

weather = [5, 25, 50, 75, 95]

am_base = np.genfromtxt("output/MaunaKea_30_1000_10_0_1_annual_05.out")

am_tau = am_base[:, 0]
am_T = am_base[:, 0]


for pwv in weather:
    am = np.genfromtxt(f"output/MaunaKea_30_1000_10_0_1_annual_{pwv:02d}.out")
    am_tau = np.column_stack((am_tau, am[:, 1]))
    am_T = np.column_stack((am_T, am[:, 2]))

np.savetxt("am_MK_tau_annual.txt", am_tau)
np.savetxt("am_MK_T_annual.txt", am_T)
