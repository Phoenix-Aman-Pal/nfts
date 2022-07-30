import time
import pytest
from brownie import network
from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from scripts.advanced_collectible.create_and_deploy import create_and_deploy


def test_can_create_collectible_integration():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.show()
    advanced_collectible = create_and_deploy()
    time.sleep(60)
    assert advanced_collectible.tokenCounter() == 1
