import pytest
from brownie import network, accounts, config
from scripts.simple_collectible.create_and_deploy import create_and_deploy
from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_account


def test_can_create_simple_collectible():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    simple_collectible = create_and_deploy()
    assert simple_collectible.ownerOf(0) == get_account()