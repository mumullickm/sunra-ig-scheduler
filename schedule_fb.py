"""One-shot: schedule upcoming legend statics natively on the FB Page (Meta posts them at the exact time).
Marks state fb as "scheduled:<id>" so run_statics.py only handles IG for them."""
import datetime, json
from run_statics import _get, _post, image_url, CAPS, TOKEN

now = datetime.datetime.now(datetime.timezone.utc)
sched = json.load(open("statics.json"))
state = json.load(open("posted_statics.json"))
page_id = _get("me").get("id")
fails = 0
for s in sched:
    sid = s["static"]; t = datetime.datetime.fromisoformat(s["iso"].replace("Z", "+00:00"))
    if not sid.startswith("legend-") or t < now + datetime.timedelta(minutes=15) or state.get(sid, {}).get("fb"):
        continue
    r = _post(f"{page_id}/photos", {"url": image_url(sid), "message": CAPS[sid], "published": "false",
                                    "scheduled_publish_time": str(int(t.timestamp()))})
    pid = r.get("post_id") or r.get("id")
    if pid:
        state.setdefault(sid, {"ig": False, "fb": False})["fb"] = f"scheduled:{pid}"
    else:
        fails += 1
    print(f"FB {sid} @ {s['iso']}: {'scheduled ' + str(pid) if pid else r.get('_error')}")
json.dump(state, open("posted_statics.json", "w"), ensure_ascii=False, indent=2)
raise SystemExit(1 if fails else 0)
