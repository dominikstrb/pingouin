import numpy as np
from unittest import TestCase
from pingouin.parametric import ttest
from pingouin.bayesian import bayesfactor_ttest, bayesfactor_pearson

np.random.seed(1234)
x = np.random.normal(size=100)
y = np.random.normal(size=100)
z = np.random.normal(loc=.5, size=100)


class TestBayesian(TestCase):
    """Test bayesian.py."""

    def test_bayesfactor_ttest(self):
        """Test function bayesfactor_ttest."""
        bf = bayesfactor_ttest(3.5, 20, 20)
        assert float(bf) == 26.743
        assert float(bayesfactor_ttest(3.5, 20)) == 17.185
        assert float(bayesfactor_ttest(3.5, 20, 1)) == 17.185
        # Compare against BayesFactor::testBF
        # >>> ttestBF(df$x, df$y, paired = FALSE, rscale = "medium")
        assert ttest(x, y).at['T-test', 'BF10'] == '0.183'
        assert ttest(x, y, paired=True).at['T-test', 'BF10'] == '0.135'
        assert int(float(ttest(x, z).at['T-test', 'BF10'])) == 1290
        assert int(float(ttest(x, z, paired=True).at['T-test', 'BF10'])) == 420

    def test_bayesfactor_pearson(self):
        """Test function bayesfactor_pearson."""
        assert float(bayesfactor_pearson(0.6, 20)) == 8.221
        assert float(bayesfactor_pearson(-0.6, 20)) == 8.221
        assert float(bayesfactor_pearson(0.6, 10)) == 1.278
