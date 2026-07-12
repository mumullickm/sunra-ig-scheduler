# sunra-ig-scheduler

Auto-posts the [Sunra Content Studio](https://mumullickm.github.io/sunra-calendar/) assets to
Instagram + Facebook (@sunraevbd) on a schedule, via the Meta Graph API. Wasilah/Hirra pattern.

**Schedule (from 12 Jul 2026, 30 days):** statics 09:00 / 18:00 / 23:00 BD, reel 21:00 BD.
Self-healing: any due-but-unposted asset goes out on the next cron tick or manual run.

**One secret required:** `META_PAGE_TOKEN` — a long-lived Facebook Page access token for the
Sunra page (with the linked IG Business account). The publisher derives Page + IG IDs from it.
Until the secret is set, every run is a no-op ("scheduler idle").

- `run_statics.py` / `run_reels.py` — publishers
- `statics.json` / `reels.json` — schedule (asset id + ISO UTC)
- `static_captions.json` / `reel_captions.json` — captions
- `config.json` — graph version + public asset base URLs
- state in `posted_statics.json` / `posted_reels.json`
