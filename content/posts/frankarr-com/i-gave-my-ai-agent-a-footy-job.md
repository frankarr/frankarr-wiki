---
title: "I Gave My AI Agent a Footy Job"
platform: "frankarr-com"
era: "now"
source_url: "http://frankarr.com/2026/05/18/i-gave-my-ai-agent-a-footy-job/"
date: "2026-05-18"
---

I've been a St Kilda member for over 40 years. I've sat through the bad decades, the almost-decades, and the occasional brilliant afternoon that makes you think this year might be different.

Last Saturday, I was out when the Saints played Richmond at Docklands. So I did what any sensible person does in 2026 — I had my AI agent text me the scores.

Here's how that went.

## What I built

SaintsFooty is a side project I've been running for a while. It's a Telegram channel — [@saintsfooty](https://t.me/saintsfooty) — that gets a daily Saints news broadcast every morning at 7:15am, a Friday night preview with team selections and win probability before each game, and on game days, live score updates sent at each quarter break.

The whole thing runs on OpenClaw, my AI setup at home. No manual intervention. I get the updates the same as any subscriber.

## Round 10 — Saints vs Richmond

Pre-game fired at 1:15pm, two hours before bounce. Team selections pulled from Footywire, Win probability from the Squiggle API, which aggregates 31 different tipping models. The Saints were favorites. I was as usual optimistic looking forward to a win.

Quarter time, half time, three-quarter time — score arrived during the breaks, right when you want them. That part worked exactly as designed.

Then the siren went.

Final score: Saints 16.13 (109) def Richmond 11.7 (73). Thirty-six point win. A good afternoon.

I didn't get the final score message.

## The bug

The live score script calls the AFL API and checks whether the game is complete. A completed game returns complete: 100. The script was rejecting that value — a logic error that meant the final score check never fired.

Found it within a few minutes of me noticing the silence. Fixed the same session. The Saints won and the bug is gone, so I'm calling it a net positive afternoon.

[](https://frankarr.wordpress.com/wp-content/uploads/2026/05/image.png)

## Rating: 4/5

The core plumbing worked. Right scores at the right times. The misses were bugs, not design problems. For a first live game day run, that's a decent result. Small issue with the emoji colors – but an easy fix…

Friday night is Round 11 — Saints vs Fremantle in Perth. The fixed version runs then.

If you're a Saints fan and want the updates: [t.me/saintsfooty](https://t.me/saintsfooty). Free, no spam, just Saints.
