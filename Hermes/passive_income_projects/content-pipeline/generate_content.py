"""Content Generation Pipeline - produces affiliate-ready articles for publication."""
import os
from datetime import datetime

ARTICLES = [
    {
        "title": "Best Crypto Wallets for June 2026: Self-Custody Guide",
        "niche": "crypto",
        "outline": ["Why self-custody matters in 2026", "Top 5 hardware wallets compared", "Best software wallets for daily use", "How to set up your first wallet safely", "Security best practices"],
        "affiliate_opportunities": ["Hardware wallet affiliate programs", "Exchange referral links"],
        "target_platforms": ["Medium", "Substack", "Dev.to"],
        "word_count": 2000,
    },
    {
        "title": "How I Built an Automated Crypto Portfolio Tracker in Python",
        "niche": "crypto + coding",
        "outline": ["Why you need a portfolio tracker", "Setting up free blockchain APIs", "Building the monitoring script", "Adding email alerts with AgentMail", "Deploying a dashboard with FastAPI"],
        "affiliate_opportunities": ["Hosting referral (Railway/Render)", "API service referrals"],
        "target_platforms": ["Medium", "Dev.to", "HackerNoon"],
        "word_count": 2500,
    },
    {
        "title": "Solana Staking in 2026: Earn 6-8% APY Passive Income Guide",
        "niche": "crypto",
        "outline": ["Why Solana staking is attractive in 2026", "Native vs liquid staking (Marinade)", "Step-by-step staking guide", "Risk assessment", "Compounding strategies"],
        "affiliate_opportunities": ["Exchange referrals (Coinbase, Kraken)", "DeFi platform referrals"],
        "target_platforms": ["Medium", "Substack"],
        "word_count": 2200,
    },
    {
        "title": "10 AI Tools That Actually Save You Hours Every Week",
        "niche": "AI + productivity",
        "outline": ["The AI landscape in mid-2026", "AI writing assistants compared", "Automation and workflow tools", "AI for developers", "AI for creators", "Cost analysis: free vs paid"],
        "affiliate_opportunities": ["SaaS tool affiliate programs", "AI tool referral links"],
        "target_platforms": ["Medium", "Substack", "LinkedIn"],
        "word_count": 3000,
    },
    {
        "title": "USDC Yield Farming: Earn 5-12% on Your Stablecoins",
        "niche": "crypto + DeFi",
        "outline": ["Why stablecoin yields still exist", "Aave vs Compound vs Curve", "Risk comparison", "How to supply USDC", "Strategies for maximizing yield"],
        "affiliate_opportunities": ["DeFi platform referrals", "Exchange referrals"],
        "target_platforms": ["Medium", "Substack"],
        "word_count": 2000,
    },
    {
        "title": "Building a Micro-SaaS as a Solo Developer: Complete Blueprint",
        "niche": "coding + business",
        "outline": ["Why micro-SaaS is the best solo business model", "Finding the right problem", "Tech stack decisions", "From MVP to first paying customer", "Marketing without a budget", "Pricing strategies"],
        "affiliate_opportunities": ["Hosting affiliate", "Domain registrar", "API referrals"],
        "target_platforms": ["Medium", "IndieHackers", "Dev.to"],
        "word_count": 3000,
    },
]

def generate_all():
    output_dir = "outlines"
    os.makedirs(output_dir, exist_ok=True)
    print(f"Generating {len(ARTICLES)} content outlines...")
    for article in ARTICLES:
        slug = article["title"].lower().replace(" ", "-").replace(":", "").replace("'", "").replace(",", "")
        filename = f"{slug}.md"
        content = f"""# {article["title"]}

Niche: {article["niche"]}
Platforms: {', '.join(article["target_platforms"])}
Words: ~{article["word_count"]}
Status: DRAFT

## Outline
"""
        for i, s in enumerate(article["outline"], 1):
            content += f"{i}. {s}\n"
        content += "\n## Affiliate Opportunities\n"
        for a in article["affiliate_opportunities"]:
            content += f"- [ ] {a}\n"
        content += "\n---\n*Contains affiliate links.*\n"
        path = os.path.join(output_dir, filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  [OK] {filename}")
    print(f"\n{len(ARTICLES)} outlines ready in {os.path.abspath(output_dir)}/")

if __name__ == "__main__":
    generate_all()
