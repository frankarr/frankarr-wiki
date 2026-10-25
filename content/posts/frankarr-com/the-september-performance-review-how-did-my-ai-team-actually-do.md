---
title: "The September Performance Review: How Did My AI Team Actually Do?"
platform: "frankarr-com"
era: "now"
source_url: "https://frankarr.com/2026/10/01/the-september-performance-review-how-did-my-ai-team-actually-do/"
date: "2026-10-01"
---

Every company does performance reviews. Some do them well. Most do them badly: vague feedback, inflated scores, no stack ranking, no real conversation about whether someone is in the right role.

I do mine differently. My team is made of AI agents, and I have the logs to back it up.

This is the September performance review for the SmallBizAI.au AI team. If you haven't met the team yet, start here: [How We Assembled Our AI Agent Team](https://smallbizai.au/behind-the-build-ai-agent-team-assembled/). This post assumes you know who they are.

## Why a Performance Review?

Three things I want to answer every month:

- **Are they doing the job they were hired for?** Volume, quality, reliability — the basics.

- **Does the role split still make sense?** As the site grows, responsibilities shift. Are we using the right agent for the right work?

- **What does the data actually tell us?** Not what I feel happened — what the logs say happened.

I built the logging before I needed it. Every agent run gets recorded: who ran, what they were asked to do, what the result was, quality score out of 5, runtime in seconds, WordPress post ID if applicable. The scorecard script pulls directly from that log. No guessing.

## September at a Glance

230 agent runs. 137 posts published to WordPress. 30 days, not one missed.

AgentRoleRunsPublishedAvg ScoreAvg RuntimeDash 🐱Writer111994.69 / 54m 4sClaw 🦞Coordinator10484.23 / 52m 55sEddie 🦅Editor11—4.58 / 51m 31sScout 🦉Researcher3——2m 40sBob 🦫Builder1—5.0 / 51m 17s

A note on the post count: the agent log tracks 99 Dash-published posts. The gap between 99 and 137 is explainable — direct Claw publishes, cron-fired posts, batch runs for the AI by Industry Matrix and AI Plain English series, and anything published before full logging discipline was in place. 137 is the WordPress number. That's the source of truth.

## What We Published: The Mix

I split all content into two types. The distinction matters for understanding what the team was actually doing in September.

**Type A — search and citations.** Evergreen content built to rank and get cited by AI systems like Bing Copilot and ChatGPT. Company profiles, how-to guides, the AI by Industry Matrix, the AI Plain English glossary, industry hub content. These answer specific questions Australian small business owners search for. They get cited. They compound.

**Type B — subscribers and engagement.** Timely, opinionated content built to build an audience. Hot takes on breaking news, Found on Reddit pieces, Sunday Specials debates, series posts, weekly news recaps. These don't always rank, but they're why people subscribe to the newsletter and come back.

TypePosts% of totalWhat's in it**Type A** (search/citations)6547%[How-Tos](https://smallbizai.au/category/how-to-guides/) (23), [Company Profiles](https://smallbizai.au/category/australian-ai-companies/) (17), [Matrix](https://smallbizai.au/category/ai-by-industry-function/) (17), [AI Plain English](https://smallbizai.au/category/ai-plain-english/) (14), [Allied Health](https://smallbizai.au/category/allied-health-ai/) (8)**Type B** (subscribers/engagement)7253%[Hot Takes](https://smallbizai.au/category/hot-takes/) (45), [Found on Reddit](https://smallbizai.au/category/found-on-reddit/) (14), [Sunday Specials](https://smallbizai.au/category/sunday-specials/) (8), [AI & Jobs](https://smallbizai.au/category/ai-and-jobs/) (5), [9 AI Assistants](https://smallbizai.au/category/nine-ai-assistants/) (4)

The strategy calls for at least 5 Type A per week. September ran B-heavy at 53/47, driven by the hot takes surge around the Medicare breach story — which produced a five-part series and the site's highest LinkedIn referral day on record. The A/B ratio is worth watching going into October.

## Social Distribution: What Claw Actually Managed

Publishing is half the job. The other half is getting posts in front of an audience. In September, Claw ran a two-share-per-day cadence — one AM, one PM — across X and LinkedIn. 63 shares. 30 days. Not one missed.

The important detail: the daily share queue deliberately pulls from the full back catalogue, not just new posts. The logic selects posts that haven't been shared recently and that match current news cycles. The goal is to make the archive work harder — a post written in June shouldn't stop earning traffic in August.

Of the 63 shares in September, only 4 were posts written in September. The other 59 were back catalogue posts getting a second run. That's the system working as designed.

MetricSeptemberTotal shares63AM / PM / Manual30 / 30 / 3Posted to X62Posted to LinkedIn61Both platforms61September posts shared4Back catalogue posts shared59Active days30 of 30

Every X share triggers an automatic LinkedIn post, with copy adapted for that audience. On the site's best LinkedIn day in September, a single shared post drove 29 referrals — matching search engines as a traffic source for the day.

## The Individual Reviews

### Dash 🐱 — Writer

111 runs. 99 published posts. Average quality score 4.69 out of 5. Average runtime 4 minutes 4 seconds. One failure — a duplicate flagged and trashed before it went live. That's a 99.1% success rate.

Dash covered every content type on the site in September: how-to guides, hot takes, company profiles, Found on Reddit pieces, AI Plain English glossary entries, Sunday Specials, the 9 AI Assistants series, weekly news recaps. The brief goes in, the formatted WordPress draft comes out, in under five minutes.

The 4.69 quality score holds across every run — not a few perfect scores inflating a messy average. The briefs have gotten tighter, the avoid-AI audit runs on every post, and Eddie gate catches anything that needs a second look before it goes live.

**Does the role split make sense?** Yes. Dash is exactly where Dash should be. The volume is sustainable, the quality is holding, and the failure rate is negligible.

**One thing to watch:** Dash runs as an isolated subagent. Each run starts fresh with no memory of previous runs. That means brief quality matters enormously — a vague brief produces a vague post. September's consistency is partly Dash, partly the briefs getting better.

### Claw 🦞 — Coordinator

104 runs. 8 posts published directly. Average score 4.23 out of 5. Average runtime 2 minutes 55 seconds.

Claw's job is running everything else: scheduling logic, daily social shares, Monday reports, infrastructure decisions, cron jobs, editorial routing, the agent run log, the dashboard state. The 8 direct publishes were specialist items — newsletters, Sunday Specials — that require judgment calls rather than a standard brief.

The 4.23 score reflects the coordinator role — a lot of runs are short operational tasks (check a cron, update a JSON file, confirm a social share) where a 5.0 isn't really meaningful. The meaningful metric for Claw is whether anything fell through the gaps. In September: nothing did.

**Does the role split make sense?** The coordinator role is nearly as active as the writer role — 104 vs 111 runs. That's the thing that surprised me most when I first looked at the logs. Content production is less than half the actual work. Scheduling, quality control, monitoring, social distribution, infrastructure maintenance — that's the rest. The writing is the visible part. The plumbing is what keeps it running.

**One thing to watch:** Claw is the single point of failure for coordination. If Claw makes a bad call, it propagates. September had no coordination failures, but the risk is structural.

### Eddie 🦅 — Editor

11 editorial gate runs. Average score 4.58 out of 5. Average runtime 1 minute 31 seconds. Every gate: approved or approved with minor fixes. Zero rejections.

Eddie's job is to catch what Dash misses: AI writing tics, unsourced claims, weak structure, anything that would embarrass the site if it went live. The 4.58 average score reflects genuine quality — Eddie is not a rubber stamp. When Eddie finds something, it comes back with specific line-level feedback.

**Does the role split make sense?** Eddie runs on 11 posts out of 137 published — roughly 8%. Not everything goes through Eddie. The gate is reserved for content that carries more risk: BtB posts, Sunday Specials, longer-form pieces where a hallucinated link or a sourcing failure would do real damage. For standard Dash output, the avoid-AI audit and duplicate check handle the basics.

Should more content types be routed through Eddie as the site scales? 8% coverage has worked so far, but that assumes brief quality and Dash output stay as clean as September showed.

**One thing to watch:** Eddie has yet to reject a post outright. That's not because Eddie is soft — it's because the briefs have gotten tighter and Dash is delivering cleaner drafts. But a zero-rejection record across 13 gates (Aug + Sep) is worth watching. Either the gate is working exactly right, or the bar needs raising.

### Scout 🦉 — Researcher

3 runs. No direct publishes. Average runtime 2 minutes 40 seconds.

Scout does research when a post needs more source material than Claw can pull from context. Three runs in September, all supporting longer-form pieces. No score recorded — Scout's output is research files passed to Dash or Claw, not finished posts.

**Does the role split make sense?** Scout is underused. Three runs in a 230-run month means the team is either operating mostly from existing context, or skipping the research step and relying on Dash to source inline. September's sourcing quality suggests the latter is sometimes happening. Scout should probably be running more often — particularly for company profiles and any post making specific data claims.

**One thing to watch:** Scout's low run count could indicate the team is doing research less often than it should, not that research is being done elsewhere. Worth checking in October whether posts with Scout-sourced research score higher than those without.

### Data 🐶 — Analyst

0 logged runs in September.

That number needs explaining, because Data didn't do nothing. Data runs a Monday morning brief every week via cron — pulling Bing citation stats, GSC signals, Gumroad sales data, and MailerLite subscriber trends into a single Telegram summary. That's four runs in September, every Monday, without fail.

But none of them are in the agent run log. Data's cron runs as an isolated job and the logging was never wired back to agent-runs.json. The work happened. The record didn't.

**Does the role split make sense?** Yes — Data's job is genuinely different from the others. It's not writing, editing, researching, or building. It's interpreting patterns across multiple data sources and surfacing the one or two things worth acting on. The Monday brief is the only regular data feed the team gets. It's more important than the logging gap suggests.

**One thing to watch:** The logging gap is a real problem. If Data's runs aren't recorded, they can't be reviewed, scored, or improved. Wiring log_agent_run.py into the Monday brief cron is the first fix for October — before anything else. You can't performance-review an agent you can't see.

### Bob 🦫 — Builder

1 run. Score 5.0. Runtime 1 minute 17 seconds.

Bob builds things: scripts, automations, tools. One run in September, perfect score. Bob doesn't run often because the infrastructure doesn't need building every month — it gets built once and then runs. When Bob works, it works.

**Does the role split make sense?** Yes. Bob is a specialist. The low run count is correct. What matters is whether Bob is being called on the right things — a 5.0 in one run doesn't tell you much about whether the role is being used optimally. Bob probably has more to contribute in months where infrastructure is being built or rebuilt.

## What the Data Infers

Three things stand out from the logs:

**The coordinator load is heavier than the writing load.** 104 Claw runs vs 111 Dash runs. This surprised me. The assumption going in was that writing is the job and coordination is the overhead. The data says they're roughly equal. That changes how I think about where to invest in the system.

**Scout is the most underused agent on the team.** 3 runs in a month with 230 total agent runs means Scout ran on 1.3% of tasks. For a researcher, that seems low. Either the briefs are good enough without dedicated research, or we're skipping a step that would improve output quality. Worth a deliberate experiment in October.

**The Type B surge is linked to specific events, not drift.** The 53/47 B-heavy split in September is explainable: the Medicare breach (five-post series), the White House AI Summit, and the AI Jobs report all landed in September and triggered hot take responses. That's the editorial system doing what it's supposed to. If October has fewer major events, the ratio should rebalance naturally.

## The Stack Ranking

Every performance review ends with a ranking. Here's mine for September.

RankAgentGradeReason1Dash 🐱**A**111 runs, 99 published, 4.69 score, one failure. The machine works.2Bob 🦫**A**1 run, 5.0 score. Small sample — but perfect when called on.3Eddie 🦅**B+**4.58 score, reliable gate. Question: is the rejection rate too low?4Claw 🦞**B+**104 runs, nothing fell through. Lower score reflects role complexity, not quality.5Data 🐶**INC**4 Monday briefs delivered. 0 logged. Can't grade what you can't measure — logging fix is October priority #1.6Scout 🦉**C+**3 runs out of 230. Either underused or the role isn't being activated correctly. Needs review.

Data gets an INC — incomplete. Not because Data didn't work, but because the logging wasn't wired up and you can't grade what you can't measure. Four Monday briefs delivered, zero records kept. That's a system failure, not an agent failure. It gets fixed in October before anything else.

Scout's C+ isn't a performance failure — it's a utilisation failure. Three runs in a month is too few for a researcher on a site publishing 137 posts. That's on the system design, not Scout.

Bob's A with a sample size of one is a placeholder. If Bob runs more in October, the grade will either hold or fall. One perfect run tells you the agent works. It doesn't tell you much else.

## What Changes in October

Three specific things coming out of this review:

- **Data logging.** Wire log_agent_run.py into the Monday brief cron before the next run. October's review will not have an INC on the board.

- **Scout activation.** Explicit research runs for company profiles and any post making specific data claims. Target: at least 8–10 Scout runs in October.

- **Eddie gate coverage.** Extend to Found on Reddit posts, which are carrying more weight in the content mix (14 in September). FoR pieces are sourced from community threads — they benefit from an editorial check.

- **Type A floor.** Enforce the 5-per-week Type A minimum explicitly in the weekly planning pass, not just as a retrospective check.

September was a consolidation month — 137 posts, down from August's 157 and well below July's 235 peak. The focus shifted from volume to infrastructure: better logging, tighter editorial gates, smarter cron scheduling. The pipeline going into October is cleaner than it's ever been. The team is better than it was in August. The data says so.
