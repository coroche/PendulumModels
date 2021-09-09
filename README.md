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

