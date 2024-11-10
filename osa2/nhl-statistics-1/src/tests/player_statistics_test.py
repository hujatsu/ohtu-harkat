import unittest
from statistics_service import StatisticsService
from player import Player


# Luodaan erillinen pelaajalista, jotta testeissä
# vertaillaan samoja olioita (muistissa)
player_list = [
    Player("Semenko", "EDM", 4, 12),  # 16 pistettä
    Player("Lemieux", "PIT", 45, 54),  # 99 pistettä
    Player("Kurri",   "EDM", 37, 53),  # 90 pistettä
    Player("Yzerman", "DET", 42, 56),  # 98 pistettä
    Player("Gretzky", "EDM", 35, 89)  # 124 pistettä
]


class PlayerReaderStub:
    def get_players(self):
        return player_list


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()  # type: ignore
        )

    def test_search_not_found(self):
        # Koivu nimistä pelaajaa ei pitäisi löytyä
        self.assertIsNone(self.stats.search('Koivu'))

    def test_search_found(self):
        # Palvelun pitäisi palauttaa Kurri-hakusanalla
        # player listin kolmas olio
        found = self.stats.search("Kurri")
        expected = player_list[2]
        self.assertEqual(found, expected)

    def test_team_filters_correct_players(self):
        FILTER = "EDM"
        result = self.stats.team(FILTER)
        expected = [player_list[0], player_list[2], player_list[4]]

        self.assertCountEqual(result, expected)

    def test_top_result_count(self):
        # top metodi palauttaa oikean määrän pelaajia
        self.assertEqual(len(self.stats.top(3)), 4)

    def test_top_sort_order(self):
        result = self.stats.top(4)
        expected = [player_list[4], player_list[3],
                    player_list[1], player_list[2], player_list[0]]
        self.assertCountEqual(result, expected)
