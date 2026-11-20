# news-image-20261120

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/vvtwentyfive/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/vvtwentyfive/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

A one-page newspaper front page summing up the world's news of **Friday 20 November 2026** — 51 stories, first reported 19–20 November 2026, drawn entirely in code (PIL) as a 1024×1024 image.

What is on the page:

- **Lead:** Cyclone Akvan makes landfall in Odisha after ~300,000 people are evacuated.
- **16 illustrated stories** (numbered 1–16): the Shenzhen trilateral summit, the ICJ's Myanmar genocide ruling, COP31's closing day, Anthropic's record $81.3bn IPO, the Dow's 1,100-point fall, the Berlin Ukraine summit, the Crimean Bridge strike, the Houthi missile on Riyadh's tallest tower, the Hormuz tanker mines, the Senegal migrant boat, the Wellington Test, the Nvidia subpoena, the Pete Rose pardon, the Kyiv strike, and the South Florida floods.
- **34 more stories in a numbered index (17–50)** plus one more (51) — every story carries a real, dated, sourceable fact.
- **Counted region bar:** ASIA 9 · EUROPE 11 · AMERICAS 12 · MIDEAST 7 · AFRICA 3 · OCEANIA 3 · WORLD 6 = 51.
- **World map with numbered pins 1–16** matching the illustrated stories.
- **THE DAY IN UTC timeline** (6 slots) and a **6-number KPI strip** (300,000 evacuated · $81.3bn IPO · Dow −1,100 · COP31 draft 144→80 · 1,000 UK drones · 13,000 Tokyo protesters).
- **DATE CHECK footer:** a boxed list of what was deliberately left out because it happened before 19 November (Van Gogh sale, US–Venezuela deal, Iran strikes on Kuwait/Bahrain, EU €45bn loan, Vrancea quake, Gas Husky sinking) and what was not yet decided (the COP31 final deal).

All text is code-rendered with PIL; every illustration is drawn with PIL primitives. No AI-drawn text, no photographs. Sources are credited on the page (Reuters, AP, AFP, BBC, The Hindu, IMD, UN News, WSJ, CNN, ATP, PHIVOLCS, NWS). The full story list with dates, summaries and sources is in [NEWS-BRIEF.md](NEWS-BRIEF.md).

## Run it

There is no local grade of this competition: the server grades every entry. To run the program locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

It copies `entry.png` to `out/entry.png` and verifies the copy by sha256. The output is byte-identical on every run.

<sub>Entered on [make.fun](https://make.fun/?ref=073t4skd&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>
