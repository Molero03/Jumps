# Jumps Detection in Glassy Systems (Based on Pigolotti and Roldán-Vargas, 2024)

The project consists of a Python implementation of the synthetic model described in the [Inspection paradox and jump detection in glassy systems](https://arxiv.org/abs/2407.19873) paper by Simone Pigolotti and Sándalo Roldán-Vargas. <br />

The program simulates particle dynamics as a combination of a vibrational motion, which is constant in time, and occasional jumps that occurs in a short time span. Then, from the simulated trajectory, the program applies the same statistical analysis as in the paper to extract the characteristic length (Δr) and characteristic time (Δt) of the system. At the end of the process, two plots are displayed. The first plot shows α, which is the ratio between the average time an observer have to wait to see the first jump and the average time between jumps, as a function of Δr and Δt (length and time that defines the jump). The second plot just shows the ratio between the observed jumps and the real jumps (obtained from the first simulation) as a function of Δr and Δt. The characteristic length is then the pair of values, Δr and Δt, that maximize α. 

![jumps](https://github.com/Molero03/Jumps/blob/main/jumps.png)


For more details, you can read the complete paper.

# # Reference
S. Pigolotti and S. Roldán-Vargas. Inspection paradox and jump detection in glassy systems. arXiv:2407.19873, 2024.


