# PendulumModels
Fun with pendulums. Modeling pendulum mechanics for various systems 
Equations of motion are first derived. The system is then evolved from initial conditions using an ODE solver.

## Double Pendulums
![DoublePendStill](https://user-images.githubusercontent.com/49063400/132660503-1334445c-ce7c-40d8-87b9-513bad76081d.png)
A classic example of chaos theory. Tiny perturbations to initial conditions here can cause completely different behaviour after a short time. For a derivation of the equations that govern the motion of these systems see [Double Pendulum Equations of Motion Derivation](/DoublePendulumEquationsOfMotionDerivation.md).  
We can see that when the system has relatively low energy it behaves in a way that is intuitive. At higher energy levels the motion becomes more volitile. While mathematically predictable, it is not always easy intuitivly to tell what will happen next.
|Low energy             |  High energy|
|-------------------------|-------------------------|
|![](https://user-images.githubusercontent.com/49063400/132666825-342e70e8-149c-4793-9dca-6f49fe836d55.gif)  |  ![](https://user-images.githubusercontent.com/49063400/132665907-0bc6926a-2412-49e9-b1bc-c1afd44acf92.gif)|  
  
The below animation shows two identical double pendulums. The only difference between the two is that one has an initial <img src="https://render.githubusercontent.com/render/math?math=\theta_2"> value that differs from the other by only <img src="https://render.githubusercontent.com/render/math?math=10^{-6}"> radians, or 0.00057 degrees. In the begining their paths are very similar. Once they begin to diverge from eachother however, their trajectories quickly become incomparable. This shows that the system is chaotic.  

![DoublePendulumComparison](https://user-images.githubusercontent.com/49063400/132736365-96950591-cb6e-4c59-bac8-0d7804d9bd5f.gif)
  
> Chaos: When the present determines the future, but the approximate present does not approximately determine the future  

-Edward Lorenz


