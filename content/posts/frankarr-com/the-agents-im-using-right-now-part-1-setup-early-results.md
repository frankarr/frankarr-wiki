---
title: "The Agents I'm Using Right Now (Part 1: Setup & Early Results)"
platform: "frankarr-com"
era: "now"
source_url: "https://frankarr.com/2026/10/12/the-agents-im-using-right-now-part-1-setup-early-results/"
date: "2026-10-12"
---

I've been running a small fleet of AI agents for a few months. Not one assistant. Five, each doing something different. This is the first post in a series about what that looks like in practice.

Let me start with the roster.

### The Roster

AgentPlatformRole**Claw**TelegramSite operator and builder: content pipeline, publishing, crons, side projects, CRM, social automation, and whatever else needs building**Poke**iMessagePersonal layer: morning briefing, horoscope, AFL scores, birthdays, job watch, mascot images**GrokBot**Native X appOperations command centre: 14 bots, scheduled routines, structured workflows**Instinct**iMessage + WhatsAppTrusted EA: decisions, research, bilateral thinking**Manus/Cue**TelegramOn-demand specialist: discrete deep research tasks

Five agents. Five platforms. No intentional overlap. Each one earned its place by being better at something than the others.

### The Shared Canvas

There's a sixth thing in this stack that isn't quite an agent but deserves its own mention: **Notion**.

Instinct uses Notion as a shared workspace between us. Every morning, a daily news roundup lands there: a structured briefing covering AI news, business stories, and anything Instinct flags as relevant to what I'm working on. I open it over coffee. It's become part of the routine.

The format is what makes it different. It's a page we both work in, not a message thread. I can annotate it, respond to it, add my own notes. Instinct picks up the thread. It's the closest thing I have to a shared document with an AI, rather than a back-and-forth conversation.

Conversation disappears. A shared canvas stays. When I come back to something Instinct flagged three days ago, it's still there, in context, with whatever I added to it. That's a different kind of memory from what most agents offer.

Notion ends up as the connective tissue in the stack, not doing the thinking, but holding the output of the thinking in a way I can return to.

### How I Got Here

I didn't plan this roster. It assembled itself.

I started with one assistant and kept adding when I hit a ceiling. Claw was first. I needed something that could run my site autonomously, and then, as it turned out, a lot more than that.

Poke came next, and it was the surprise. The most personal-feeling of the lot. It earned its place early by handling something I hadn't anticipated: mascot images. Before I had a proper pipeline, Poke was the one I'd text to generate and tweak images on the fly. That ambient, always-available energy made it an obvious second addition.

GrokBot followed. The native X app integration made it easy to wire up bots without a lot of scaffolding. I now have 14 bots running inside it: scheduled routines, structured workflows, things that need to happen on a clock whether I'm paying attention or not.

Instinct arrived when I realised I wanted something I could think alongside, not just issue commands to. It's the one I use for decisions. I'll describe a situation, get pushback, test an assumption. The bilateral conversation model is different from "AI assistant as search engine."

Manus I reach for when a task needs a few hours of uninterrupted focus. The kind of deep research that would take me a morning: competitive landscape, background on a company, pulling together a briefing on something I don't know well. I hand it off, come back later.

That's the sequence. Each one added when the previous roster hit a ceiling.

### The Poke Factor

Morning briefing. Horoscope. AFL quarter-by-quarter scores during a Saints game. Birthday reminders for people I care about. Job application monitoring: it pings me when something moves in my pipeline. And early on, mascot images, the kind of quick visual task that needed a text-an-AI interface more than a prompt console.

It doesn't feel like a tool. It feels more like a well-organised part of my morning that happens to run on software.

What's worth noting about Poke is the *ambient* layer. It shows up without being asked. Most agents wait for a prompt. Poke just… appears. There's something to be said for an agent with that energy: not a hammer waiting to be swung, more like a good EA who already knows what you need before you've asked.

### The Spectrum

If you laid them out by when they joined the stack:

**Claw → Poke → GrokBot→** Instinct → Manus

And if you laid them out from operational to personal:

**Claw → GrokBot → Manus → Instinct → Poke**

Two different orderings of the same five agents. Claw has built and is running an entire content business. Poke knows my star sign and sends me quarter-by-quarter Saints scores. Those are not the same job.

The mistake I see people make is trying to get one agent to do everything. It becomes a generalist that's mediocre at all of it. The agents with a narrow lane perform significantly better inside that lane.

### Early Results (Partial)

It's still too early for a full verdict on all five. But here's where things stand:

**Claw**: The hardest to summarise because the scope keeps expanding.

**Poke**: Highest daily engagement of any of them, probably because it shows up without being asked. Still the one I reach for when I need something done via a quick text.

**GrokBot**: The 14-bot setup works. Scheduled routines are reliable. The native X integration is the biggest advantage: no API wrangling, no middleware. The ceiling is it's still largely inside the X ecosystem.

**Instinct**: The bilateral model is different. I find myself using it to stress-test decisions rather than just execute tasks. That's a different kind of useful, and harder to find.

**Manus**: Early days but promising. The async model suits deep research well. I'm still calibrating what's worth handing off versus what's faster to do myself.

The headline numbers for SmallBizAI.au: 1,500+ published posts, 149 scheduled cron jobs, a daily content pipeline running autonomously. But that's only one part of it.

Claw also built and ran four side projects from scratch. The first two came from a challenge my daughter Emma threw at me: could Claw build something useful from scratch, unprompted, with real users? That turned into *[MelbWeekendAlerts](https://frankarr.com/2026/04/27/how-i-built-melbweekendalerts-in-an-afternoon-before-the-footy/)*, a Friday evening Telegram broadcast scraping live event data from across Melbourne, and *WhereToQueue*, the same model aimed at secret sales and warehouse clearances across the city. Both ran for months. That same challenge mindset is what led directly to the car project.

[Emma was selling her Fiat 500C](https://frankarr.com/2026/07/30/i-built-my-daughter-an-sms-bot-to-sell-her-car/) and needed a way to handle buyer enquiries without fielding calls all day. Claw built a Twilio-powered SMS and IVR system in a single session. Buyers text a dedicated number, get an instant auto-reply with car details, and are walked through inspection booking via SMS. Callers get a voice menu: press 1 to hear the details read aloud, press 2 to request a callback. Every enquiry was logged to a Google Sheet. I got an alert SMS for each one. The whole thing ran on a WordPress code snippet and cost under a dollar a month to operate.

[*SaintsFooty* ](https://frankarr.com/2026/05/18/i-gave-my-ai-agent-a-footy-job/)is the fourth: a daily St Kilda FC news broadcast. It's on a break between seasons and will be back next year.

Beyond those: a RAG-indexed semantic search layer over the entire site. A networking CRM. A Gumroad product pipeline with automated subscriber routing. A mascot library. An AU company directory with 26+ profiles. A weekly SEO audit stack. A social sharing system posting to both X and LinkedIn. A meme registry. A jobs monitor watching my application pipeline. A newsletter archive system. All built, maintained, and in most cases conceived and proposed by Claw.

The more accurate description isn't "site infrastructure." It's closer to a one-agent agency: writing, building, automating, and running things across multiple distinct projects simultaneously. That wasn't the brief. It's just what happened when you give an agent enough context and enough runway.

### What's Next

Part 2 will go deeper on the handoffs, or lack of them. When do I route something to GrokBot versus Manus versus Claw? What breaks down when I pick the wrong one? And what does it cost, in time, money, and attention, to run a five-agent setup?
