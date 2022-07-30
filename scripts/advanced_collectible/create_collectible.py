from brownie import AdvancedCollectible
from scripts.helpful_scripts import get_account, fund_with_link

def main():
    account = get_account()
    advanced_collectible = AdvancedCollectible[-1]
    fund_with_link(advanced_collectible.address, amount = 10**18)
    creation_tx = advanced_collectible.createCollectible({"from": account})
    creation_tx.wait(1)