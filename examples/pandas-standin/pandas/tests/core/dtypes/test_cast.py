"""Tests for pandas.core.dtypes.cast."""

import numpy as np
import pytest

from pandas.core.dtypes.cast import can_cast_safely, coerce_to_float64


class TestCoerceToFloat64:
  def test_happy_path_integers(self):
    result = coerce_to_float64(np.array([1, 2, 3], dtype=np.int32))
    assert result.dtype == np.float64

  def test_edge_case_already_float64(self):
    source = np.array([1.5], dtype=np.float64)
    result = coerce_to_float64(source)
    np.testing.assert_array_equal(result, source)

  def test_error_case_object_dtype(self):
    with pytest.raises((ValueError, TypeError)):
      coerce_to_float64(np.array(["x"], dtype=object))


class TestCanCastSafely:
  def test_happy_path_widening_int(self):
    assert can_cast_safely(np.dtype("int8"), np.dtype("int64"))

  def test_edge_case_float_target(self):
    assert can_cast_safely(np.dtype("int32"), np.dtype("float64"))

  def test_error_case_narrowing_int(self):
    assert not can_cast_safely(np.dtype("int64"), np.dtype("int8"))
