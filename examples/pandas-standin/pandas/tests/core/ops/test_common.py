"""Tests for pandas.core.ops.common."""

import numpy as np
import pytest

from pandas.core.ops.common import normalize_values, safe_divide


class TestNormalizeValues:
  def test_happy_path_unit_vector(self):
    result = normalize_values(np.array([3.0, 4.0]))
    np.testing.assert_allclose(result, np.array([0.6, 0.8]))

  def test_edge_case_zero_vector(self):
    result = normalize_values(np.array([0.0, 0.0]))
    np.testing.assert_array_equal(result, np.array([0.0, 0.0]))

  def test_error_case_non_numeric_raises(self):
    with pytest.raises(TypeError):
      normalize_values(np.array(["a", "b"], dtype=object))


class TestSafeDivide:
  def test_happy_path(self):
    result = safe_divide(np.array([4.0, 6.0]), np.array([2.0, 3.0]))
    np.testing.assert_array_equal(result, np.array([2.0, 2.0]))

  def test_edge_case_zero_denominator(self):
    result = safe_divide(np.array([1.0, 2.0]), np.array([0.0, 4.0]))
    np.testing.assert_array_equal(result, np.array([0.0, 0.5]))

  def test_error_case_non_numeric_raises(self):
    with pytest.raises((TypeError, ValueError)):
      safe_divide(np.array(["a"]), np.array([1]))
