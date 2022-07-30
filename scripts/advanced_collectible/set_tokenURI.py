from brownie import AdvancedCollectible, network
from scripts.helpful_scripts import OPENSEA_URL, get_account, get_breed

dog_metadata_dict = {
    "PUG": "https://ipfs.io/ipfs/QmSsYRx3LpDAb1GZQm7zZ1AuHZjfbPkD6J7s9r41xu1mf8?filename=pug.png",
    "SHIBA_INU": "https://ipfs.io/ipfs/QmYx6GsYAKnNzZ9A6NvEKV9nf1VaDzJrqDR23Y8YSkebLU?filename=shiba-inu.png",
    "ST_BERNARD": "https://ipfs.io/ipfs/QmUPjADFGEKmfohdTaNcWhp7VGk26h5jXDA7v3VtTnTLcW?filename=st-bernard.png",
}

def main():
    print(f"Working on {network.show_active()}")
    advanced_collectible = AdvancedCollectible[-1]
    number_of_collectible = advanced_collectible.tokenCounter()
    print(f"You have {number_of_collectible} collectibles")
    for tokenId in range(number_of_collectible):
        breed = get_breed(advanced_collectible.tokenIdToBreed(tokenId))
        if not advanced_collectible.tokenURI(tokenId).startswith("https://"):
            print(f"Setting tokenURI of {tokenId}")
            set_tokenURI(tokenId, advanced_collectible, dog_metadata_dict[breed] )

def set_tokenURI(token_id, nft_contract, tokenURI):
    account = get_account()
    tx = nft_contract.setTokenURI(token_id, tokenURI, {"from": account})
    tx.wait(1)
    print(f"Awesome, you can view your nft at {OPENSEA_URL.format(nft_contract.address, token_id)}")
    print("Just wait for 20 mins and hit the refress metadata button !")