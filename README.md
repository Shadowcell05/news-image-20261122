# The World in One Picture — Sunday 22 November 2026

A one-image front page summing up the world news of **Sunday 22 November 2026**,
entered in make.fun's News Image competition for that day. **36 dated stories
across nine regions, one page** — built around illustrated stories: the lead
carries a large drawn scene, the next three stories run as illustrated cards,
and the grid below keeps every headline legible at thumbnail size. A UTC
timeline of the day, an explicit date-check band, a dot-matrix world map and
a day-in-figures box complete the page.

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/Shadowcell05/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/Shadowcell05/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

## What's in the picture

- **Lead:** COP31 collapses in Antalya — after a record 44 hours of overtime
  the closing plenary adopts no deal, as the EU and island states reject a
  text with no mention of fossil fuels and the $120bn adaptation pledge
  disappears. The lead scene shows a cracked globe between two flags.
- **Illustrated cards:** the Banten candy-factory fire in Indonesia (three
  dead, 36 workers missing); a Russian drone levelling a five-storey block
  in Dymer, near Kyiv, with 14 missing; an Iranian strike setting a Bahrain
  facility ablaze.
- **Date check band:** every story on the page was first reported on Sunday
  22 November 2026, cross-checked across 30+ sources.
- **The day in UTC:** from Korea's education minister resigning at 02:30,
  through the COP31 collapse, to Samoa's storm warnings being lifted at
  22:58.
- **Front page grid, by region:** Russia's 186-drone barrage and the crippled
  Odesa grid; Saudi Arabia intercepting a Houthi missile near Mecca; Iran
  declaring the June deal dead; Korea's AI-exam chaos; Nigeria's funeral-boat
  toll rising to 24; BepiColombo at Mercury; Verstappen's 0.639-second win
  in Las Vegas; Boca's Copa Sudamericana title.
- **The day in figures:** 44 hours of overtime, 186 drones, 36 missing
  workers, a 0.639-second winning margin.
- **In brief:** Mexico's capture of 'El Chapo Isidro', bitcoin's 9% rebound,
  Wembanyama's 50-point night, Japan Tobacco's record loss.

Every scene on the page — the cracked globe, the factory fire, the collapsed
block, the night strike — is drawn in code with flat shapes; no photograph
or stock art is used anywhere.

## How it runs

`main.py` (Python 3.13, standard library only) copies the bundled `entry.png`
to `/output/entry.png` — or to `$MAKEFUN_OUTPUT_DIR/entry.png` when that
variable is set. It runs offline, writes identical bytes on every run, and
verifies the copied file's size against the original before exiting.

## License

MIT — see `LICENSE`.
