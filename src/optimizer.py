import numpy as np

def optimize_momentum(func, grad_func, dim=2, max_iter=5000, alpha=0.01, beta=0.9):
    """
    Momentum-based gradient descent optimizer.

    Parameters:
        func: Callable – objective function f(x)
        grad_func: Callable – gradient of f
        dim: int – number of dimensions
        max_iter: int – max iterations
        alpha: float – learning rate
        beta: float – momentum factor

    Returns:
        best_x: np.ndarray – best position found
        history: list – history of x positions
    """
    x = np.random.uniform(-5, 5, dim)
    v = np.zeros(dim)
    history = [x.copy()]

    for i in range(max_iter):
        # TODO: Compute gradient
        grad = grad_func(x)
        # TODO: Update momentum vector
        v = beta * v - alpha * grad
        # TODO: Update x using momentum
        x = x + v
        # TODO: Log x to history
        history.append(x.copy())

    return x, history

def optimize_exploration(func, dim=2, max_iter=500, exploration_scale=0.1):
    """
    Stochastic exploration-based optimizer (no gradient).

    Parameters:
        func: Callable – objective function f(x)
        dim: int – number of dimensions
        max_iter: int – max iterations
        exploration_scale: float – standard deviation of noise

    Returns:
        best_x: np.ndarray – best position found
        history: list – history of x positions
    """
    x = np.random.uniform(-5, 5, dim)
    best_val = func(x)
    history = [x.copy()]

    for i in range(max_iter):
        # TODO: Generate random step
        # TODO: Evaluate new candidate
        # TODO: Accept or reject move
        # TODO: Log x to history
        pass

    return x, history
    