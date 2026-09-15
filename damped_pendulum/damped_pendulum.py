"""Damped pendulum simulator (script / importable version).

Mirrors ``damped_pendulum.ipynb`` so the same model can be used without a
Jupyter kernel: import :func:`pendulum_angle` from Python, or run this file
from the command line to render one plot.

Model (small-angle, closed-form):

    theta(t) = theta0 * exp(-damping * t) * cos(omega * t),   omega = sqrt(g / L)

Examples
--------
    python damped_pendulum.py                       # defaults, opens a window
    python damped_pendulum.py --length 2 --damping 0.3 --angle0 45 --save out.png
"""

from __future__ import annotations

import argparse

import matplotlib.pyplot as plt
import numpy as np

G = 9.81  # gravitational acceleration, m/s^2


def pendulum_angle(t, length=1.0, damping=0.1, angle0=30):
    """Return the pendulum angle in degrees at the times ``t`` (seconds)."""
    t = np.asarray(t, dtype=float)
    omega = np.sqrt(G / length)
    theta = np.radians(angle0) * np.exp(-damping * t) * np.cos(omega * t)
    return np.degrees(theta)


def pendulum(length=1.0, damping=0.1, angle0=30, ax=None):
    """Plot angle vs. time over 10 s and return the matplotlib Axes."""
    t = np.linspace(0, 10, 500)
    if ax is None:
        _, ax = plt.subplots(figsize=(6, 3))
    ax.plot(t, pendulum_angle(t, length, damping, angle0))
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Angle (deg)")
    ax.set_title(f"Pendulum: L={length}m, damping={damping}")
    ax.grid(True)
    return ax


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Plot a damped pendulum's angle over time."
    )
    parser.add_argument(
        "--length", type=float, default=1.0,
        help="pendulum length in metres (default 1.0)",
    )
    parser.add_argument(
        "--damping", type=float, default=0.1,
        help="damping coefficient in 1/s (default 0.1)",
    )
    parser.add_argument(
        "--angle0", type=float, default=30,
        help="initial angle in degrees (default 30)",
    )
    parser.add_argument(
        "--save", metavar="PATH",
        help="write the plot to PATH instead of opening a window",
    )
    args = parser.parse_args(argv)
    if args.length <= 0:
        parser.error("--length must be positive")

    ax = pendulum(args.length, args.damping, args.angle0)
    if args.save:
        ax.figure.savefig(args.save, dpi=150, bbox_inches="tight")
        print(f"saved {args.save}")
    else:
        plt.show()


if __name__ == "__main__":
    main()
