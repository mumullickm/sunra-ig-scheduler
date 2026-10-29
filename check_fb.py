"""Read-only: show what Meta holds for the natively scheduled legend FB posts."""
import json
from run_statics import _get, _post, TOKEN
import urllib.request, urllib.parse
page_id = _get("me").get("id")
st = json.load(open("posted_statics.json"))
print("scheduled_posts edge:", json.dumps(_get(f"{page_id}/scheduled_posts", {"fields": "id,scheduled_publish_time,is_published", "limit": 50}))[:1500])
for sid, v in st.items():
    fb = str(v.get("fb"))
    if fb.startswith("scheduled:"):
        pid = fb.split(":", 1)[1]
        for obj in (f"{page_id}_{pid}", pid):
            try:
                r = json.loads(urllib.request.urlopen("https://graph.facebook.com/v21.0/" + obj + "?" + urllib.parse.urlencode({"fields": "id,is_published,scheduled_publish_time,created_time", "access_token": TOKEN}), timeout=30).read())
                print(sid, obj, r); break
            except urllib.error.HTTPError as e:
                print(sid, obj, "ERR", e.read().decode()[:200])
