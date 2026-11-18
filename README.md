# The World in One Day — 18 November 2026

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/theyschool/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/theyschool/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

A one-image summary of the world's news of **Wednesday 18 November 2026**,
for make.fun's [news-image-20261118](https://make.fun/bounty/news-image-20261118)
bounty. A newspaper front page: a masthead naming the day, and the five
stories that defined it — the Crimea bridge crippled, the Gulf on alert,
Trump in Manila, Nvidia's earnings, and Cyclone Akvan.

## How it is made

`build_image.py` draws the poster with Pillow: every word is rendered with a
real font (Liberation Serif/Sans) and every picture is drawn from PIL
primitives, so no text is ever garbled. `entry.png` is the rendered poster;
`main.ts` copies it to `/output/entry.png` (byte for byte, so both graded
runs write identical bytes).

## Stories (all reported 18 November 2026)

1. **Crimea bridge crippled** — Ukraine's drones and missiles collapse the
   road arch into the sea in the war's biggest drone attack; Russia hits
   Kyiv's bridges in reply. (Reuters, AP)
2. **Gulf on alert** — Kuwait's air defences down hostile drones overnight;
   Bahrain sounds the all-clear after threat alerts; US jets hit an Iran
   missile site on Qeshm Island. (Reuters, Al Jazeera)
3. **Trump in Manila** — the US president lands for Quad talks ahead of his
   China visit; Putin is due to meet Trump and Xi in Shenzhen on Thursday.
   (Reuters)
4. **Nvidia soars** — quarterly revenue doubles to $115.8bn; the board says
   ousted chief Jensen Huang will not return; Anthropic prices its IPO today.
   (Reuters, The Guardian)
5. **Cyclone Akvan** — the storm over the Bay of Bengal strengthens, set to
   become severe by Thursday. (IMD via Reuters)

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
