---
title: "Hello Cloudflare!"
platform: "frankarr-com"
era: "now"
source_url: "https://frankarr.com/2026/10/22/hello-cloudflare/"
date: "2026-10-22"
---

I moved SmallBizAI onto Cloudflare last night. Start to finish, about an hour. The site didn't go down, the SSL held, and this morning everything is faster and I can see traffic data I couldn't see before.

But I did break email. Briefly. Here's the full story.

## Why Cloudflare

A few weeks ago I learned that Cloudflare is running a pilot with OpenAI around AI discovery signals, essentially, sites on their network get better visibility to AI crawlers. That was enough to move this to the top of the list.

The rest of the reasons are just good infrastructure hygiene. Free CDN. DDoS protection. A global network sitting in front of the VentraIP server that hosts the site. And access to Cloudflare Workers and analytics that I couldn't get while the DNS was still pointing straight at the host.

Free plan. No good reason not to do it.

## How it went

The migration itself is straightforward. You add your domain in the Cloudflare dashboard, it scans your existing DNS records, you review them, flip the nameservers at your registrar, and wait.

One thing to know: the registrar for smallbizai.au is CrazyDomains, not VentraIP. VentraIP is the host. They're different companies. I know that. I still had to think about it for a second when it came time to change the nameservers.

Propagation took under an hour. SSL came through automatically via Let's Encrypt. I cleared the LiteSpeed cache on the VentraIP side, checked the site, all good.

## What I got wrong: the MX records

When Cloudflare imports your DNS, it makes decisions about which records to proxy through its network. Root domain and www, yes, that makes sense, you want the CDN benefit. Mail records, no, absolutely not.

The problem is that email doesn't work through Cloudflare's proxy. Their network isn't built for it. So mail.smallbizai.au needs to point directly at the VentraIP server, not route through Cloudflare's IPs. Same for cpanel and ftp, anything that needs a direct connection to the host has to stay as DNS-only (what Cloudflare calls a "grey cloud" record, as opposed to the orange proxied ones).

Cloudflare knows this. They warn you. But in the middle of reviewing a dozen records and ticking things off, I missed the MX record and it ended up proxied. Email to hello@smallbizai.au would have failed for anyone who tried it during that window.

I caught it during the verification pass, I had a checklist and "email still works" was on it. Fixed it, all three records back to DNS-only, done. No actual mail was lost as far as I can tell, but it was a genuine mistake and not a small one.

The lesson is basic: **make a list of every record that must not be proxied before you start, not while you're in the middle of it.**

## What also went wrong: the orange cloud confusion

Mail wasn't the only one. cpanel.smallbizai.au and ftp.smallbizai.au both ended up proxied too. If I'd needed to access cPanel during that window it would have been broken. Same deal, fixed quickly, but shouldn't have happened.

The pattern here is that Cloudflare auto-proxies anything it can, and "anything it can" includes records it shouldn't. The safe approach is to proxy root and www, set everything else to DNS-only by default, and only flip things to proxied deliberately and one at a time.

## The MCP bit

The day after the migration I wired up the Cloudflare MCP server to OpenClaw. MCP is a protocol that lets AI tools talk to external services, in this case, it means Claw can now manage the Cloudflare zone directly from a chat session.

DNS changes, cache rules, analytics queries, all available without me going into the dashboard. I can ask "what's the traffic looking like today?" and get an answer. I can say "add a DNS record for this subdomain" and it happens.

This is actually the more interesting development from a build perspective. I've been doing this stuff manually for years. The Cloudflare dashboard is fine, but fine isn't the same as fast. Having Claw able to make infrastructure changes in the same session where we're discussing them changes the pace of how we work.

## The data

Cloudflare analytics are different from GA4 in one important way: they sit at the network layer, before the browser. So they catch bots, crawlers, blocked requests, and anything that never executes JavaScript. GA4 only sees sessions where the tracking script fires.

The numbers I can see now: total requests, page views, unique visitors, threats blocked, bandwidth. I can also see where traffic is coming from geographically, which requests are being cached vs hitting the origin server, and response codes across the board.

I'm not going to publish specific numbers here, they're mine to see, not benchmarks anyone else can act on, but the picture is more complete than what I had before. GA4 remains useful for behaviour data (what pages people visit, how long they stay). Cloudflare is useful for infrastructure data (how many requests are actually hitting the site, what's being served from cache, what's getting blocked).

Both together is better than either alone.

## Where this is going

**Workers and custom domains.** I can now deploy Cloudflare Workers with a custom subdomain on smallbizai.au. That opens up serverless endpoints, edge functions, redirect logic, things I'd otherwise need a server for.

**AutoSSL renewal.** The current Let's Encrypt cert expires in December. There's a DNS challenge record that needs to be in place for auto-renewal to work. That's on the checklist.

**The OpenAI pilot.** Still speculative, still not something I control. But being on the Cloudflare network is the prerequisite. Box ticked.

The actual work of moving the domain took an hour. The cleanup took another thirty minutes. What it gives back over time, better data, faster infrastructure management, edge compute options, is worth it.

Just don't forget the MX records.
