"""Common operations utilities (pandas stand-in)."""

from __future__ import annotations

from typing import Any

import numpy as np


def normalize_values(values: np.ndarray, axis: int | None = None) -> np.ndarray:
  """Normalize array values to unit norm along an axis.

  Parameters
  ----------
  values : np.ndarray
      Input array to normalize.
  axis : int or None, optional
      Axis along which to compute norms. None normalizes the full array.

  Returns
  -------
  np.ndarray
      Normalized array with the same shape as ``values``.

  Examples
  --------
  >>> import numpy as np
  >>> normalize_values(np.array([3.0, 4.0]))
  array([0.6, 0.8])
  """
  norms = np.linalg.norm(values, axis=axis, keepdims=True)
  norms = np.where(norms == 0, 1, norms)
  return values / norms


def legacy_normalize(values: np.ndarray) -> np.ndarray:
  """Deprecated: use ``normalize_values`` instead."""
  return normalize_values(values)


def safe_divide(numerator: np.ndarray, denominator: np.ndarray) -> np.ndarray:
  """Divide arrays, returning 0 where denominator is zero.

  Parameters
  ----------
  numerator : np.ndarray
      Dividend array.
  denominator : np.ndarray
      Divisor array.

  Returns
  -------
  np.ndarray
      Element-wise division with zero-safe behavior.

  Examples
  --------
  >>> import numpy as np
  >>> safe_divide(np.array([1.0, 2.0]), np.array([2.0, 0.0]))
  array([0.5, 0. ])
  """
  with np.errstate(divide="ignore", invalid="ignore"):
    result = np.true_divide(numerator, denominator)
  return np.where(denominator == 0, 0.0, result)
