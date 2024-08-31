"""
    Lambert W aprroximations
    * approximate_lambertw_halleys - Approximates Lambert W function with the Halley's method
    * approximate_lambertw_newton - Approximates Lambert W function with the Halley's method
    * approximate_lambertw_iacono_boyd - Approximates Lambert W function with the Halley's method
"""

import torch

from typing import Tuple


def approximate_lambertw_halleys(z: torch.Tensor, step_tol: float = 1e-7) -> torch.Tensor:
    """
    Calculate the k=0 branch of lambert w function on each element of the Tensor separatively.
    Inverse of z*exp(z), i.e. w(z)*exp(w(z)) = z
    Iterative algorithm from https://www.quora.com/How-is-the-Lambert-W-Function-computed    

    Iteration stops when either the iteration absolute difference is maximum `step_tol` or 100 iterations.
    Shape is the same as input `z`.

    Parameters
    ----------
    z : torch.Tensor
        Input tensor of any shape.

    step_tol : float, optional
        Step tolerance of the maximum absolute difference in each step. (default is `1e-7`)

    Returns
    -------
    lambert_w : torch.Tensor
        The approximated lambert W function. The same shapes as the inputs.
    """

    max_iter = 100
    # Initial guess so the approximation is faster for values that is used in SNN-s
    w = torch.log(1 + z)
    step = w
    i = 0

    while i < max_iter and torch.max(torch.abs(step)) > step_tol:
        ew = torch.exp(w)
        numerator = w * ew - z
        denominator = ew*(w+1) - (w+2)*numerator/(2*w + 2)
        step = numerator / denominator
        w = w - step
        i += 1

    return w


def approximate_lambertw_newton(z: torch.Tensor, step_tol: float = 1e-7) -> torch.Tensor:
    """

    """


def approximate_lambertw_iacono_boyd(z: torch.Tensor, step_tol: float = 1e-7) -> torch.Tensor:
    """

    """
