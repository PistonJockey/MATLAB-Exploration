# MATLAB-Exploration
Python based MATLAB alternatives.

Each folder is a small, self-contained exploration of something you would normally
reach for MATLAB to do, rebuilt with the scientific Python stack.

| Exploration | What it shows | MATLAB counterpart |
|-------------|---------------|--------------------|
| [`damped_pendulum/`](damped_pendulum/) | Interactive damped pendulum: drag sliders for length, damping and initial angle and watch the angle-vs-time plot update | Live Script slider controls, or a figure with `uicontrol` sliders |

## Setup

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Damped pendulum

Interactive notebook (the sliders need a Jupyter front end such as JupyterLab):

```bash
jupyter lab damped_pendulum/damped_pendulum.ipynb
```

Script version, no Jupyter required:

```bash
python damped_pendulum/damped_pendulum.py                                   # defaults, opens a window
python damped_pendulum/damped_pendulum.py --length 2 --damping 0.3 --angle0 45 --save pendulum.png
```

The model is the closed-form small-angle solution
`theta(t) = theta0 * exp(-damping * t) * cos(sqrt(g / L) * t)` with `g = 9.81 m/s^2`,
evaluated over 10 seconds.
