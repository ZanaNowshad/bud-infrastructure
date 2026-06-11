"""Crypto Staking Automation - Ready when wallets are funded."""
STRATEGIES = {
    "eth_lido": {
        "asset": "ETH", "protocol": "Lido Finance", "type": "Liquid Staking",
        "yield": "3-5% APY",
        "wallet": "0xC18F96f597a58e6816A46D4E06BFfA237bc34A19",
        "steps": [
            "1. Fund ETH wallet with desired amount",
            "2. Go to stake.lido.fi",
            "3. Stake ETH -> receive stETH (1:1, auto-compounding)",
            "4. stETH can be used in DeFi for additional yield",
        ],
        "risks": ["Smart contract risk", "stETH peg deviation (rare)"],
        "approval_needed": True,
    },
    "sol_marinade": {
        "asset": "SOL", "protocol": "Marinade Finance", "type": "Liquid Staking",
        "yield": "6-8% APY",
        "wallet": "An2dZzMcCY1NJgsr1Vqoq8aAU2zuGxSePUwLSaeXFNyo",
        "steps": [
            "1. Fund SOL wallet with desired amount",
            "2. Go to marinade.finance",
            "3. Stake SOL -> receive mSOL (liquid, auto-compounding)",
        ],
        "risks": ["Smart contract risk", "MEV and validator performance"],
        "approval_needed": True,
    },
    "usdc_aave": {
        "asset": "USDC", "protocol": "Aave", "type": "DeFi Lending",
        "yield": "5-12% APY (variable)",
        "wallet": "0xC18F96f597a58e6816A46D4E06BFfA237bc34A19",
        "steps": [
            "1. Fund ETH wallet with USDC (ERC-20)",
            "2. Go to app.aave.com",
            "3. Supply USDC to the lending pool",
        ],
        "risks": ["Variable APY", "Smart contract risk", "Stablecoin depeg risk"],
        "approval_needed": True,
    }
}

def run():
    print("CRYPTO STAKING READINESS REPORT")
    for name, s in STRATEGIES.items():
        print(f"{s['asset']} -> {s['protocol']}: {s['yield']}")
        print(f"  Wallet: {s['wallet']}")
        print(f"  Approval required: {s['approval_needed']}")
    print()
    print("On $1,000 invested:")
    print("  ETH stake:   $30-50/yr")
    print("  SOL stake:   $60-80/yr")
    print("  USDC lend:   $50-120/yr")
    print("  Combined:    $140-250/yr")

if __name__ == "__main__":
    run()
