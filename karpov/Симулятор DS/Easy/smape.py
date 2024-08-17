import unittest

import numpy as np


def __smape(y_true: np.array, y_pred: np.array) -> float:
    denominator = np.abs(y_true) + np.abs(y_pred)
    denominator = np.where(denominator == 0, 1e-10, denominator)
    smape_values = 2 * np.abs(y_true - y_pred) / denominator
    return np.mean(smape_values)


def smape(y_true: np.array, y_pred: np.array) -> float:
    """Return fixed sMAPE"""
    nom = np.abs(y_true - y_pred)
    den = (np.abs(y_true) + np.abs(y_pred)) / 2
    ratio = nom / np.where(den != 0, den, 1.0)
    return np.mean(ratio)


class TestSMAPE(unittest.TestCase):

    def test_regular_values(self):
        y_true = np.array([100, 200, 300])
        y_pred = np.array([90, 210, 310])
        result = smape(y_true, y_pred)
        expected = np.mean([
            2 * np.abs(100 - 90) / (np.abs(100) + np.abs(90)),
            2 * np.abs(200 - 210) / (np.abs(200) + np.abs(210)),
            2 * np.abs(300 - 310) / (np.abs(300) + np.abs(310))
        ])
        self.assertAlmostEqual(result, expected, places=5)

    def test_equal_values(self):
        y_true = np.array([100, 200, 300])
        y_pred = np.array([100, 200, 300])
        result = smape(y_true, y_pred)
        expected = 0.0  # sMAPE должен быть 0, когда значения совпадают
        self.assertAlmostEqual(result, expected, places=5)

    def test_zeros(self):
        y_true = np.array([0, 0, 0])
        y_pred = np.array([0, 0, 0])
        result = smape(y_true, y_pred)
        expected = 0.0  # sMAPE должен быть 0, когда все значения равны нулю
        self.assertAlmostEqual(result, expected, places=5)

    def test_mixed_values(self):
        y_true = np.array([0, 100, 200])
        y_pred = np.array([0, 110, 190])
        result = smape(y_true, y_pred)
        expected = np.mean([
            0,  # когда оба равны 0
            2 * np.abs(100 - 110) / (np.abs(100) + np.abs(110)),
            2 * np.abs(200 - 190) / (np.abs(200) + np.abs(190))
        ])
        self.assertAlmostEqual(result, expected, places=5)

    def test_large_values(self):
        y_true = np.array([1e10, 2e10, 3e10])
        y_pred = np.array([0.9e10, 2.1e10, 3.1e10])
        result = smape(y_true, y_pred)
        expected = np.mean([
            2 * np.abs(1e10 - 0.9e10) / (np.abs(1e10) + np.abs(0.9e10)),
            2 * np.abs(2e10 - 2.1e10) / (np.abs(2e10) + np.abs(2.1e10)),
            2 * np.abs(3e10 - 3.1e10) / (np.abs(3e10) + np.abs(3.1e10))
        ])
        self.assertAlmostEqual(result, expected, places=5)


if __name__ == '__main__':
    unittest.main()
