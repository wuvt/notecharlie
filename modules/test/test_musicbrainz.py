# coding=utf-8
"""
test_musicbrainz.py - tests for the mb module
author: paulwalko <paulsw.pw@gmail.com>
"""

import unittest
from mock import MagicMock, Mock
from modules.musicbrainz import mb


class TestMusicBrainz(unittest.TestCase):
    def setUp(self):
        self.phenny = MagicMock()

    def test_mb_area(self):
        input = Mock(group=lambda x: "area Los Angeles")
        mb(self.phenny, input)

        self.phenny.say.assert_called_once_with("Los Angeles, City: https://musicbrainz.org/area/1f40c6e1-47ba-4e35-996f-fe6ee5840e62")

    def test_mb_artist(self):
        input = Mock(group=lambda x: "artist Queen")
        mb(self.phenny, input)

        self.phenny.say.assert_called_once_with("Queen, Group (UK rock group) : https://musicbrainz.org/artist/0383dadf-2a4e-4d10-a46a-e9e041da8eb3")

    def test_mb_release(self):
        input = Mock(group=lambda x: "release CavDeacon")
        mb(self.phenny, input)

        self.phenny.say.assert_called_once_with("CavDeacon: https://musicbrainz.org/release/27c85e13-7e8f-42be-803f-f577fb2e3897")

    def test_mb_release_group(self):
        input = Mock(group=lambda x: "release-group 808s & Heartbreak")
        mb(self.phenny, input)

        self.phenny.say.assert_called_once_with("808s & Heartbreak, Album: https://musicbrainz.org/release-group/1c1b50ec-828b-3d7c-9b1b-54cb1fe97d55")

    def test_mb_work(self):
        input = Mock(group=lambda x: "work The Girl from Ipanema")
        mb(self.phenny, input)

        self.phenny.say.assert_called_once_with("The Girl From Ipanema, Song: https://musicbrainz.org/work/69f81329-a815-3ec2-aaee-1f781a1e026d")

    def text_mb_recording(self):
        input = Mock(group=lambda x: "recording Never Gonna Give You Up")
        mb(self.phenny, input)

        self.phenny.say.assert_called_once_with("Never Gonna Give You Up: https://musicbrainz.org/recording/df345c38-5951-4c8d-9d84-90727304ec48")
