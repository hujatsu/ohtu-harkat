import unittest
from unittest.mock import Mock, ANY
from kassapaate import Kassapaate, HINTA
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()

    def test_kortilta_velotetaan_hinta_jos_rahaa_on(self):
        maksukortti_mock = Mock()
        maksukortti_mock.saldo = 10

        self.kassa.osta_lounas(maksukortti_mock)

        maksukortti_mock.osta.assert_called_with(HINTA)

    def test_kortilta_ei_veloteta_jos_raha_ei_riita(self):
        maksukortti_mock = Mock()
        maksukortti_mock.saldo = 4

        self.kassa.osta_lounas(maksukortti_mock)

        maksukortti_mock.osta.assert_not_called()

    def test_kortti_ladataan_positiivisella_summalla(self):
        """Testaa, että maksukortin latausmetodia kutsutaan positiivisella
        summalla."""
        maksukortti_mock = Mock()
        SUMMA = 1

        self.kassa.lataa(maksukortti_mock, SUMMA)

        maksukortti_mock.lataa.assert_called_with(SUMMA)

    def test_korttia_ei_ladata_nolla_summalla(self):
        """Tehtävä ei spesifioinut, ladataanko korttia nollasummalla vai ei.
        Päätin, ettei ladata."""
        maksukortti_mock = Mock()
        SUMMA = 0

        self.kassa.lataa(maksukortti_mock, SUMMA)

        maksukortti_mock.lataa.assert_not_called()

    def test_korttia_ei_ladata_negatiivisella_summalla(self):
        """Testaa, ettei maksukortin latausmetodia kutsuta lainkaan, jos summa
        on negativiinen."""
        maksukortti_mock = Mock()
        SUMMA = -1

        self.kassa.lataa(maksukortti_mock, SUMMA)

        maksukortti_mock.lataa.assert_not_called()
