# type: ignore
# flake8: noqa
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
import numpy as np
import matplotlib.pyplot as plt
from qutip import Bloch, basis, sigmax, sigmay, sigmaz

def plot_bloch_sphere(states, labels):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    b = Bloch(axes=ax)
    b.point_color = ['r', 'g', 'b', 'y']
    
    for state, label in zip(states, labels):
        b.add_states(state)
        b.add_annotation(state, label)
    
    b.render()
    return fig

# some example states
psi1 = basis(2, 0)  # |0⟩ i.e. classical 0
psi2 = basis(2, 1)  # |1⟩ i.e. classical 1
psi3 = (basis(2, 0) + basis(2, 1)).unit()  # (|0⟩ + |1⟩)/√2 i.e. equal superposition
psi4 = (basis(2, 0) + 1j*basis(2, 1)).unit()  # (|0⟩ + i|1⟩)/√2 i.e. superposition with a phase difference

states = [psi1, psi2, psi3, psi4]
labels = ["|0⟩", "|1⟩", "|+⟩", "|+i⟩"]

fig = plot_bloch_sphere(states, labels)

plt.tight_layout()
plt.savefig('bloch_sphere_example.png', dpi=150, bbox_inches='tight')
plt.close(fig)
```
#
#
#
#
#
#
#
#
#
#
#
#
import numpy as np
import matplotlib.pyplot as plt
from qutip import Bloch, basis, qeye, sigmax, sigmay, sigmaz
from matplotlib.animation import FuncAnimation
import imageio

def plot_bloch_sphere(states, filename='bloch_sphere_evolution.gif', duration=0.1):
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    b = Bloch(axes=ax)

    def update(frame):
        ax.cla()
        b = Bloch(axes=ax)
        b.add_states(states[frame])
        b.add_states([states[0], states[-1]], 'point')
        b.render()
        ax.set_title(f'Frame {frame + 1}/{len(states)}')

    anim = FuncAnimation(fig, update, frames=len(states), repeat=True)

    frames = []
    for i in range(len(states)):
        update(i)
        fig.canvas.draw()
        image = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8')
        image = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))
        frames.append(image)

    imageio.mimsave(filename, frames, duration=duration)
    plt.close(fig)

def state_evolution(initial_state, operation, steps=50):
    states = [initial_state]
    for i in range(1, steps+1):
        states.append(operation(initial_state, i/steps))
    return states

def hadamard_like_transform(state, t):
    H = np.sqrt(1 - t) * sigmaz() + np.sqrt(t) * sigmax()
    return (1 - t) * state + t * H * state

psi0 = basis(2, 0) # initial state |0⟩

states = state_evolution(psi0, hadamard_like_transform, steps=50)

plot_bloch_sphere(states, 'bloch_sphere_evolution.gif', duration=0.1)
```
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
