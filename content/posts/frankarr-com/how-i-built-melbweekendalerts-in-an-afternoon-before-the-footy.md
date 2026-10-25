---
title: "How I Built MelbWeekendAlerts in an Afternoon before the Footy"
platform: "frankarr-com"
era: "now"
source_url: "http://frankarr.com/2026/04/27/how-i-built-melbweekendalerts-in-an-afternoon-before-the-footy/"
date: "2026-04-27"
---

[](https://frankarr.wordpress.com/wp-content/uploads/2026/04/screenshot-2026-04-27-152322.png)

## **The Problem**

Sunday morning we got stuck behind [Run the Tan](https://runthetan.net) while taking grand-doggies [Data](https://www.instagram.com/data_the_dachshund/) and Sam on a walk, before heading the [Saints game at Marvel Stadium](https://www.afl.com.au/afl/matches/8100).

Not a big deal in isolation. But it got the family thinking: how many times has this happened? And why is there no simple way to know in advance that a fun run, triathlon, or Ironman is going to close half the roads in your suburb on Sunday morning?

There's no single place to check. Google doesn't solve it. VicRoads buries road closure notices. You find out when you're sitting in traffic.

So I built one drinking an Iced Americano, while waiting for the start of the [Saints v West Coast Eagles game at Marvel Stadium](https://www.afl.com.au/afl/matches/8100), with the help of [🦞](https://openclaw.ai).

## **What Was Built**

**[Melbourne Weekend Road Alerts](https://t.me/melbweekendalerts)** is a free Telegram channel that sends you a weekly Friday evening summary of upcoming weekend events that affect Melbourne roads.

The first alert goes out this Friday, 1 May.

## **How It Works**

The system has three parts:

### **1. A curated events calendar**

I started with a manually-maintained JSON file of recurring Melbourne events (fun runs, triathlons, marathons, parades) that happen on predictable dates each year.

It already has 11 events seeded: Run the Tan, City2Sea, Run Melbourne, the Melbourne Marathon, Ironman Melbourne, the ANZAC Day march, and more.

Each entry includes the event name, typical date, affected suburbs, affected roads, and approximate closure times. This is the reliable backbone that works regardless of whether any scraper succeeds.

### **2. A VicTraffic scraper**

VicTraffic is the official Victorian Government road disruption site. It has live event closure data, but it's a JavaScript-heavy single-page app so standard web scraping won't work.

I used [Playwright](https://playwright.dev/), a headless browser automation library, to load the page, intercept any API calls the app makes, and extract event closure data. This runs weekly on Thursday evening so the data is fresh for Friday's alert.

### **3. An alert generator**

A Python script combines the live VicTraffic data with the curated calendar, looks ahead to the coming weekend, and generates a plain-text alert:

	
		
			

🏃 Melbourne Road Alert — 2 May & 3 May📅 SATURDAY 2 MAY• No major road events found📅 SUNDAY 3 MAY• Melbourne Half Marathon (approx date — check event website) Type: Half Marathon Areas: CBD, Southbank, South Melbourne, South Yarra Roads: St Kilda Road, Kings Way, Flinders Street Hours: 07:00 – 11:00 More: https://melbournehalf.com.au—🦞 Melbourne Events Tracker — betaCurated + VicTraffic data. Always verify before heading out.
		
	

This runs every Friday at 6pm and posts to the Telegram channel automatically.

## **The Stack**

Everything runs on a Windows PC running WSL2/Ubuntu using the same infrastructure used for [SmallBizAI.au](https://smallbizai.au) with :

- **Python** for the scraper and alert generator

- **Playwright** for headless Chrome (to handle the JS-rendered VicTraffic site)

- **OpenClaw** for cron scheduling and Telegram bot integration

- **Telegram Bot API**** for posting to the channel

- A flat **JSON file**for state (no database needed at this scale)

Total cost to run: $0. No servers, no paid APIs, no hosting.

## **What's Next**

Right now it's in beta. The curated events calendar is the main source of truth, with VicTraffic as a supplement when it has live data.

Next steps:

- Expand the curated calendar (suggestions welcome)

- Improve the VicTraffic scraper to capture more granular road closure details

- Add suburb filtering so you only get alerts relevant to your area

- Potentially a web version and WhatsApp channel

- Expand nationally

- Profit $$$

## **Subscribe**

If you're in Melbourne and tired of getting stuck behind fun runs: **[t.me/melbweekendalerts](https://t.me/melbweekendalerts)**

First alert this Friday. Free forever.

**Built on 26 April 2026 — the same day [St Kilda beat West Coast by 101 points in AFL game 16,898, ](https://www.afl.com.au/afl/matches/8100)producing a scorigami (a final score that has never occurred in the history of the game). Good day.**
