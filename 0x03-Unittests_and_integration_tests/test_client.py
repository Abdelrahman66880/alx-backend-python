# !/usr/bin/env python3
""" Module for testing client """
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
import json
import unittest
from unittest.mock import patch, PropertyMock, Mock


class TestGithubOrgClient(unittest.TestCase):
    """ Class for Testing GithubOrgClient """

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    def test_org(self, input, mock):
        """ Test org method of GithubOrgClient """
        client = GithubOrgClient(input)
        client.org()
        mock.assert_called_once_with(f"https://api.github.com/orgs/{input}")

