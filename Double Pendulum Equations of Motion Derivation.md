# Double Pendulum Equations of Motion Derivation
Consider two pendulums of length <img src="https://render.githubusercontent.com/render/math?math=l_1"> and <img src="https://render.githubusercontent.com/render/math?math=l_2">. Pendulum 1 has one end fixed at the origin. Pendulum 2 has one end fixed to the free end of pendulum 1. Point masses <img src="https://render.githubusercontent.com/render/math?math=m_1"> and <img src="https://render.githubusercontent.com/render/math?math=m_2"> are attached to the free end of each pendulum respectively.  

![DoublePendDiagram](https://user-images.githubusercontent.com/49063400/132529406-b60941ae-8abc-4301-9896-0b0a9d7f14d6.png)  
Let the following vectors denote the positions of point mass at the end of each pendulum in cartesian coordinates.  
<img src="https://render.githubusercontent.com/render/math?math=\X_i = (x_i, y_i)"> for i=1,2  
  
Therefore  
<img src="https://render.githubusercontent.com/render/math?math=x_1 = l_1 sin \theta_1">  
<img src="https://render.githubusercontent.com/render/math?math=y_1 = -l_1 cos \theta_1">  
<img src="https://render.githubusercontent.com/render/math?math=x_2 = l_1 sin \theta_1 %2B l_2 sin \theta_2">  
<img src="https://render.githubusercontent.com/render/math?math=y_2 = -l_1 cos \theta_1 - l_2 cos \theta_2">
  
And taking the first derivative w.r.t. theta  
<img src="https://render.githubusercontent.com/render/math?math=\dot{x_1} = \dot{\theta_1} l_1 cos \theta_1">  
<img src="https://render.githubusercontent.com/render/math?math=\dot{y_1} = \dot{\theta_1} l_1 sin \theta_1">  
<img src="https://render.githubusercontent.com/render/math?math=\dot{x_2} = \dot{\theta_1} l_1 cos \theta_1 %2B \dot{\theta_2} l_2 cos \theta_2">  
<img src="https://render.githubusercontent.com/render/math?math=\dot{y_2} = \dot{\theta_1} l_1 sin \theta_1 %2B \dot{\theta_2} l_2 sin \theta_2">  
  
So the potential energy of the system  
<img src="https://render.githubusercontent.com/render/math?math=P_E = m_1 g h_1 %2B m_2 g h_2">  
<img src="https://render.githubusercontent.com/render/math?math=P_E = m_1 g y_1 %2B m_2 g y_2">  
<img src="https://render.githubusercontent.com/render/math?math=P_E = m_1 g (-l_1 cos \theta_1) %2B m_2 g (-l_1 cos \theta_1 - l_2 cos \theta_2)">  
<img src="https://render.githubusercontent.com/render/math?math=P_E = -(m_1 %2B m_2) g l_1 cos \theta_1 - m_2 g (l_2 cos \theta_2)">  
  
And kinetic energy  
<img src="https://render.githubusercontent.com/render/math?math=K_E = \frac{1}{2} m_1 v_1^2 %2B \frac{1}{2} m_2 v_2^2">  
<img src="https://render.githubusercontent.com/render/math?math=K_E = \frac{1}{2} m_1 (\dot{x_1}^2 %2B \dot{y_1}^2)  %2B \frac{1}{2} m_2 (\dot{x_2}^2 %2B \dot{y_2}^2)">  
...  
<img src="https://render.githubusercontent.com/render/math?math=K_E = \frac{1}{2} (m_1 %2B m_2) \dot{\theta_1}^2 {l_1}^2 %2B \frac{1}{2} m_2 {l_2}^2 \dot{\theta_2}^2  %2B m_2 l_1 l_2 \dot{\theta_1} \dot{\theta_2} cos(\theta_1 - \theta_2)">  
  
The lagrangian  
<img src="https://render.githubusercontent.com/render/math?math=\L = K_E-P_E">  
<img src="https://render.githubusercontent.com/render/math?math=\L = \frac{1}{2} (m_1 %2B m_2) \dot{\theta_1}^2 {l_1}^2 %2B \frac{1}{2} m_2 {l_2}^2 \dot{\theta_2}^2  %2B m_2 l_1 l_2 \dot{\theta_1} \dot{\theta_2} cos(\theta_1 - \theta_2) %2B (m_1 %2B m_2) g l_1 cos \theta_1 %2B m_2 g (l_2 cos \theta_2)">  
  
Using
<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{dt} \frac{\partial \L}{\partial \dot{\theta_i}} = \frac{\partial \L}{\partial \theta_i}">  
We can derive the equations of motion  
<img src="https://render.githubusercontent.com/render/math?math=(m_1 %2B m_2) l_1 \ddot{\theta}_1 %2B m_2 l_2 \ddot{\theta_2} cos (\theta_1 - \theta_2) %2B m_2 l_2 \dot{\theta}^2 sin(\theta_1 - \theta_2) %2B (m_1 %2B m_2) g sin \theta_1 = 0"> (1)  
<img src="https://render.githubusercontent.com/render/math?math=l_2 \ddot{\theta_2} %2B l_1 \ddot{\theta_1} cos(\theta_1 - \theta_2) - l_1 \dot{\theta_1}^2 sin (\theta_1 - \theta_2) %2B g sin \theta_2 = 0"> (2)  
  
  
Let <img src="https://render.githubusercontent.com/render/math?math=U(t) = [\theta_1, \alpha_1,  \theta_2, \alpha_2]"> where <img src="https://render.githubusercontent.com/render/math?math=\alpha_i = \dot{\theta_i}"> describe the system at any given time. This is what we need to evolve. To see how it changes we look at     
<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{dt} U = [\alpha_1, \dot{\alpha_1},  \alpha_2, \dot{\alpha_2}]">  
  
So in order to evolve the system we need explicit expressions for <img src="https://render.githubusercontent.com/render/math?math=\dot{\alpha_1}"> and <img src="https://render.githubusercontent.com/render/math?math=\dot{\alpha_2}"> from the equations of motion we take <img src="https://render.githubusercontent.com/render/math?math=(1)-m_2cos(\theta_1-\theta_2)(2)"> to get  
<img src="https://render.githubusercontent.com/render/math?math=\dot{\alpha_1} = \frac{m_2 g cos(\theta_1-\theta_2)sin\theta_2 - m_2 l_2 {\alpha_2}^2 sin (\theta_1 - \theta_2) - \frac{1}{2} m_2 l_1 {\alpha_1}^2 sin(2\theta_1 - 2\theta_2) - (m_1 %2B m_2) g sin\theta_1}{l_1(m_1 %2B m_2 - m_2 cos^2 (\theta_1 - \theta_2)))}">  
  
And taking <img src="https://render.githubusercontent.com/render/math?math=cos(\theta_1 - \theta_2)(1)-(m_1%2Bm_2)(2)"> we get   
<img src="https://render.githubusercontent.com/render/math?math=\dot{\alpha_2} = \frac{(m_1 %2B m_2) (g sin \theta_2 - l_1 {\alpha_1}^2 sin(\theta_1-\theta_2) -g cos(\theta_1-\theta_2)sin\theta_1) - \frac{1}{2} m_2 l_2 {\alpha_2}^2 sin (2\theta_1 - 2\theta_2)}{l_2(m_2 cos^2 (\theta_1-\theta_2) -m_1-m_2)}">  
  
We can now use these equations with an ODE solver to evolve U and model the movement of the system.
