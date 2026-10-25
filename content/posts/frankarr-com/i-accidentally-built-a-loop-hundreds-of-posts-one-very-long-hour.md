---
title: "I Accidentally Built a Loop. Hundreds of Posts. One Very Long Hour."
platform: "frankarr-com"
era: "now"
source_url: "http://frankarr.com/2026/07/09/i-accidentally-built-a-loop-hundreds-of-posts-one-very-long-hour/"
date: "2026-07-09"
---

Everyone's talking about AI agents getting stuck in infinite loops. Turns out you don't need agents. Two IFTTT recipes will do it.

Here's what I had running:

**Recipe 1**:When I post to X → create a WordPress post

**Recipe 2**:When I publish to WordPress → post to X

Both made sense on their own. Both were quietly enabled. I'd forgotten Recipe 2 existed.

Then I posted something to X.

X → WordPress → X → WordPress → X → WordPress…

For a few hours I was unknowingly the most prolific blogger on the internet. Hundreds of posts on my blog. Hundreds of identical posts on X. Same content, perfectly duplicated, each platform faithfully feeding the other.

By the time I noticed, the damage was done. Disabling the recipes stopped it immediately — but then came 60 minutes of manual deletion. Not my finest afternoon.

The painful thing? Nothing went wrong. Every single step worked exactly as designed. The problem was the combination — two automations that could see each other's output and treat it as a new input, with nothing in the middle asking "haven't we done this already?"

Circuit breakers exist for a reason.

Before you connect any two automations, ask yourself: can these feed each other? If yes, you need a condition that breaks the chain — "stop if this content already exists," "stop if this ran in the last hour," something.

Or just don't run both directions at once. That also works.

🤦‍♂️
