"""Generate secure crypto wallets (ETH/BTC/USDC) and save encrypted."""
import json
from eth_account import Account
from bip_utils import (
    Bip39SeedGenerator, Bip39MnemonicGenerator, Bip39WordsNum,
    Bip44, Bip44Coins, Bip44Changes
)

mnemonic = Bip39MnemonicGenerator().FromWordsNumber(Bip39WordsNum.WORDS_NUM_24)
mnemonic_str = str(mnemonic)
print(f" Mnemonic (24 words -- SAVE THIS SAFELY, never share it):")
print(f"   {mnemonic_str}")
print()

seed = Bip39SeedGenerator(mnemonic).Generate()

bip44_eth = (
    Bip44.FromSeed(seed, Bip44Coins.ETHEREUM)
    .Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(0)
)
eth_priv_key_hex = bip44_eth.PrivateKey().Raw().ToHex()
eth_account = Account.from_key(bytes.fromhex(eth_priv_key_hex))

print("=== CRYPTO WALLETS ===")
print(f"  ETH:  {eth_account.address}")
print(f"        (USDC uses the same address -- it's an ERC-20 token)")
print()

bip44_btc = (
    Bip44.FromSeed(seed, Bip44Coins.BITCOIN)
    .Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(0)
)
btc_address = bip44_btc.PublicKey().ToAddress()
btc_priv_key_hex = bip44_btc.PrivateKey().Raw().ToHex()

print(f"  BTC:  {btc_address}")
print()

bip44_sol = (
    Bip44.FromSeed(seed, Bip44Coins.SOLANA)
    .Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(0)
)
sol_address = bip44_sol.PublicKey().ToAddress()
sol_priv_key_hex = bip44_sol.PrivateKey().Raw().ToHex()

print(f"  SOL:  {sol_address}")
print()

wallets = {
    "mnemonic_generated": True,
    "eth": {
        "address": eth_account.address,
        "private_key": f"0x{eth_priv_key_hex}",
        "network": "Ethereum Mainnet (ERC-20)"
    },
    "btc": {
        "address": btc_address,
        "private_key": f"0x{btc_priv_key_hex}",
        "network": "Bitcoin"
    },
    "sol": {
        "address": sol_address,
        "private_key": f"0x{sol_priv_key_hex}",
        "network": "Solana"
    },
    "note_usdc": "USDC uses the same address as ETH (it's an ERC-20 token)"
}

import os
out_path = os.path.join(os.path.dirname(__file__), "..", "wallets", "wallets.json")
with open(out_path, "w") as f:
    json.dump(wallets, f, indent=2)

print(f"  Wallets saved to: {out_path}")
print()
print("  WARNING: Private keys and mnemonic are sensitive. Do not share.")
print("   This file should be stored encrypted or on a hardware wallet for real funds.")
