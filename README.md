# The World in One Day — 18 November 2026

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/theyschool/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/theyschool/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

A one-image summary of the world's news of **Wednesday 18 November 2026**,
for make.fun's [news-image-20261118](https://make.fun/bounty/news-image-20261118)
bounty. A newspaper front page: a masthead naming the day, and the five
stories that defined it — the Gulf on alert, Trump meeting Marcos, Nvidia's
earnings, Cyclone Akvan, and APEC opening in Shenzhen. Every story is an
18 November event: the Crimea bridge collapse (overnight 16–17 November,
reported Tuesday) was deliberately left out, since it is 17 November's news.

## How it is made

`build_image.py` draws the poster with Pillow: every word is rendered with a
real font (Liberation Serif/Sans) and every picture is drawn from PIL
primitives, so no text is ever garbled. `entry.png` is the rendered poster;
`main.ts` copies it to `/output/entry.png` (byte for byte, so both graded
runs write identical bytes).

## Stories (all 18 November 2026 events)

1. **Gulf on alert** — Kuwait's air defences down hostile drones in the
   early hours of Wednesday; Bahrain sounds the all-clear after overnight
   alerts; US jets hit an Iran missile site on Qeshm Island. (Al Jazeera,
   Reuters)
2. **Trump & Marcos** — the US president meets Ferdinand Marcos Jr. in
   Manila on Wednesday, then flies to Shenzhen for APEC; Putin meets Trump
   and Xi on Thursday. (Reuters)
3. **Nvidia soars** — quarterly revenue doubles to $115.8bn; the board says
   ousted chief Jensen Huang will not return; Anthropic prices its IPO today.
   (Reuters, The Guardian)
4. **Cyclone Akvan** — the storm over the Bay of Bengal strengthens on
   Wednesday, with heavy rain and winds of 110 km/h on the coast; landfall
   is due on Friday. (IMD)
5. **APEC opens** — leaders gather in Shenzhen as the APEC summit opens on
   Wednesday; Trump, Xi and Putin hold their trilateral on Thursday.
   (Reuters)

## Files

- `main.ts` — the entrypoint (Node 22, standard library only)
- `entry.png` — the poster (1024×1024 PNG)
- `build_image.py` — the renderer that draws `entry.png`
- `LICENSE` — MIT

## Run it locally

```
python3 build_image.py          # redraw entry.png
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```
