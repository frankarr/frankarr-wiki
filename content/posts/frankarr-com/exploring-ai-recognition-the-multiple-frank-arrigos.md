---
title: "Exploring AI Recognition: The Multiple Frank Arrigos"
platform: "frankarr-com"
era: "now"
source_url: "http://frankarr.com/2026/06/21/exploring-ai-recognition-the-multiple-frank-arrigos/"
date: "2026-06-21"
---

I first saw this on X, first [Matt Barrie](https://x.com/matt_barrie/status/2068112998699561011?s=20), then [Jeremy Howard](https://x.com/jeremyphoward/status/2068278444295946708?s=20) and I thought, good enough for those legends, well good enough from me. The site was called [intheweights.com](https://intheweights.com/). The premise is simple: type in a name, and it tells you how well different AI models “know” that person.

I typed in my name. It turns out there are several Frank Arrigos embedded in AI training data. Only one of them is me, but my name appeared a few different times. Is this the new "google yourself" trend?

## What “in the weights” actually means

When a large language model is trained, it processes billions of text documents. The information doesn’t get stored like a database. It gets compressed into billions of numerical values called weights. If you appeared in enough of that text, traces of you end up embedded in those numbers. The model doesn’t “remember” you the way Google indexes a page. You’re just… in there. Somewhere.

The higher your score on [intheweights.com](https://intheweights.com), the more thoroughly you’re embedded. It’s a rough measure, but it’s a real one.

I got a bunch of results. Here’s what the first few said about “[Frank Arrigo](https://intheweights.com/p/frank-arrigo).”

## Card one: GPT knows the 1990s version of me

GPT-5.5 gave me a strength score of 170, top 40% globally. Its description: “Developer Evangelist and longtime Microsoft Australia technology community figure associated with .NET and developer outreach.” That’s accurate. I joined Microsoft Australia in 1991 and stayed until 2014. A lot of what I did back then got written up on blogs, in conference writeups, on MSDN, in community forums. That era left a big footprint.

On this card, Claude Opus showed a reasonable recognition bar. GPT-4 Mini had a decent one. Everyone else (Grok, Gemini, Llama, DeepSeek, Mistral, Qwen) basically nothing.

So the AI that runs my current business (Claude, which I call Claw) knows roughly who I am, but only just. That’s its own kind of irony.

GPT got the right person, frozen at about 2010. The [Telstra years](https://frankarr.com/category/telstra/), the [AWS years](https://frankarr.com/category/aws/), this site: none of it registers. An accurate portrait of someone I used to be.

## Card two: Gemini invented a job I never had

[](https://frankarr.wordpress.com/wp-content/uploads/2026/06/img_0181.jpg)

Gemini 3.1 Lite, strength score of 71, top 70%. Title: “IBM/Telstra API Strategist.” Description: “A technology professional known for developer relations, API strategy, and advocacy, notably at companies like IBM and Telstra.”

Half of that is correct. [I did work at Telstra from 2014 to late 2017](https://frankarr.com/category/telstra/), doing exactly that: API strategy, developer relations. But IBM? I’ve never worked at IBM. Not for a day.

The model didn’t hedge or say it was unsure. It paired a real employer with a made-up one and presented both as facts with equal confidence. If you read that card without knowing me, you’d have no reason to question it.

IBM and Telstra are both large enterprise tech companies with developer programs that appear in similar contexts in training data. The model found a pattern and filled in the gap. Plausible. Wrong.

## Card three: DeepSeek found a completely different Frank Arrigo

[](https://frankarr.wordpress.com/wp-content/uploads/2026/06/img_0184.jpg)

This is where it gets funny.

DeepSeek V4, strength score of 95, top 60%. Title: “American Football Coach.” Description: “Frank Arrigo was an American football coach and college athletics administrator, notably serving as head coach at the University of Detroit.”

Bright blue bar. Most confident reading on the card. Llama 3.3 70B showed a small bar alongside it. Everyone else: zero.

There is an actual Frank Arrigo who coached American football at the University of Detroit. DeepSeek knows him well. It just applied all of that to me, because we share a name.

I have never coached American football. I’ve never been to Detroit. And yet here’s a model with a strength score of 95, confidently describing someone else’s career as mine.

## Card four: GLM found a third Frank Arrigo

[](https://frankarr.wordpress.com/wp-content/uploads/2026/06/img_0185.jpg)

GLM 4.7 Flash, strength score of 67, top 80%. Title: “Freeport Mayor/NY Senator.” Description: “American politician and former mayor of the Village of Freeport, New York.”

Bright pink bar on GLM 4.7 Flash. Everyone else near zero.

This is yet another Frank Arrigo: a New York politician, not the football coach from Detroit, and not me. GLM latched onto him with full confidence. Same name, third different human being.

## What’s actually going on

“Frank Arrigo” isn’t a unique name. There’s a Microsoft developer evangelist (me), an American football coach, a New York politician, and probably others. GPT-5.5 has enough training data to distinguish between them. The smaller models grab whichever Frank Arrigo they know best and report back as if the question were settled.

GPT-5.5: right person. Gemini: right person, invented an employer. DeepSeek and GLM: different wrong people, full confidence.

My time at [AWS (2018 to 2024)](https://frankarr.com/category/aws/) barely register in any model. That work never produced public text. [SmallBizAI.au](https://SmallBizAI.au) doesn’t exist in any model’s training data yet. It launched after the cutoff dates for the current generation.

## What your AI fingerprint looks like

You can see [my full profile here](https://intheweights.com/p/frank-arrigo). Head to [intheweights.com](https://intheweights.com/), type in your own name, and see what comes back.

If you have a common name, check whether the model knows you or someone else who shares it. If your name is unusual, watch for hallucinated details filling in gaps the model couldn’t source.

For me: GPT has the 2010 version, Gemini added IBM to my CV, DeepSeek made me a football coach, and GLM ran me for mayor of a New York village I’ve never visited.

Four cards. One name. Four different answers.
