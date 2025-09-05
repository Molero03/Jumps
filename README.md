# Jumps Detection in Glassy Systems (Based on Pigolotti and Roldán-Vargas, 2024)

The project consists of a Python implementation of the synthetic model described in the paper [Inspection paradox and jump detection in glassy systems](https://arxiv.org/abs/2407.19873) by Simone Pigolotti and Sándalo Roldán-Vargas. <br />

The program simulates particle dynamics as a combination of vibrational motion, which is constant in time, and occasional jumps, which occur over short time spans. From the simulated trajectory, the program then applies the same statistical analysis as in the paper to extract the characteristic length (Δr) and characteristic time (Δt) of the system. At the end of the process, two plots are displayed:

- α(Δr, Δt): The ratio between the average time an observer must wait to see the first jump and the average time between consecutive jumps, shown as a function of Δr and Δt (the parameters that define a jump).
- N/Nr: The ratio between the number of detected jumps and the actual number of jumps (from the simulation), plotted as a function of Δr and Δt.

The characteristic length and time of the system correspond to the pair of values (Δr, Δt) that maximize α. 

![jumps](https://github.com/Molero03/Jumps/blob/main/jumps.png)


For more details, please refer to the complete paper.

# # Reference
S. Pigolotti and S. Roldán-Vargas. Inspection paradox and jump detection in glassy systems. arXiv:2407.19873, 2024.


