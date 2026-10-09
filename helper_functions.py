import numpy as np
from scipy.optimize import curve_fit


def bass_F(t, p, q):
    """Cumulative share of the market potential that has adopted by time t."""
    e = np.exp(-(p + q) * t)
    return (1 - e) / (1 + (q / p) * e)


def bass_f(t, p, q):
    """Adoption rate at time t (share of the market potential per period)."""
    e = np.exp(-(p + q) * t)
    return ((p + q) ** 2 / p) * e / (1 + (q / p) * e) ** 2


def bass_cumulative(t, p, q, m):
    """Cumulative adopters at time t, for a market potential m."""
    return m * bass_F(t, p, q)


def fit_bass(t, cumulative, m_upper):
    """Estimate p, q and m by non-linear least squares on cumulative adoption.

    t          : time periods since launch (1, 2, 3, ...)
    cumulative : observed cumulative adoption in the same units as m
    m_upper    : the largest value m is allowed to take
    """
    m_lower = float(np.max(cumulative))
    initial_guess = [0.01, 0.4, (m_lower + m_upper) / 2]
    bounds = ([1e-6, 1e-6, m_lower], [1.0, 2.0, m_upper])
    params, _ = curve_fit(bass_cumulative, t, cumulative,
                          p0=initial_guess, bounds=bounds, maxfev=20000)
    return params


def r_squared(actual, predicted):
    """Share of the variance in the actual data explained by the model."""
    actual = np.asarray(actual)
    predicted = np.asarray(predicted)
    ss_res = np.sum((actual - predicted) ** 2)
    ss_tot = np.sum((actual - actual.mean()) ** 2)
    return 1 - ss_res / ss_tot


def peak_time(p, q):
    """Time period in which yearly adoption reaches its maximum."""
    return np.log(q / p) / (p + q)