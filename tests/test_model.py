from unittest import TestCase
from src.model import TEAM35Model
from math import pi


class TestPowerTransformerExample(TestCase):

    def test_init_transformer_model(self):
        self.init_transformer_model()

        self.assertEqual(self.pt.design_parameters['ff_in'], 60)
        self.assertEqual(self.pt.design_parameters['ff_ou'], 60)
        self.assertEqual(self.pt.design_parameters['end_ins'], 180)
        self.assertEqual(self.pt.design_parameters['alpha'], 1.0)
        self.assertEqual(self.pt.design_parameters['core_ins'], 20)

        self.assertEqual(self.pt.design_variables['core_diam'], 420)
        self.assertEqual(self.pt.design_variables['gap'], 50)
        self.assertEqual(self.pt.design_variables['jin'], 2.6)
        self.assertEqual(self.pt.design_variables['jou'], 2.26)

