"""Dtype casting utilities (pandas stand-in)."""

from __future__ import annotations

import numpy as np


def coerce_to_float64(values: np.ndarray) -> np.ndarray:
  """Coerce array values to float64 dtype.

  Parameters
  ----------
  values : np.ndarray
      Input array.

  Returns
  -------
  np.ndarray
      Array cast to ``float64``.

  Examples
  --------
  >>> import numpy as np
  >>> coerce_to_float64(np.array([1, 2], dtype=np.int32)).dtype
  dtype('float64')
  """
  return np.asarray(values, dtype=np.float64)


def can_cast_safely(source: np.dtype, target: np.dtype) -> bool:
  """Return whether values can be cast without loss for integer dtypes.

  Parameters
  ----------
  source : np.dtype
      Source dtype.
  target : np.dtype
      Target dtype.

  Returns
  -------
  bool
      True when cast is considered safe for demo purposes.
  """
  if np.issubdtype(source, np.floating) or np.issubdtype(target, np.floating):
    return True
  return np.dtype(source).itemsize <= np.dtype(target).itemsize
