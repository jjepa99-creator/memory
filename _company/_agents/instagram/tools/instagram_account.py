import json
import pathlib
import sys
import urllib.error
import urllib.parse
import urllib.request


HERE = pathlib.Path(__file__).resolve().parent
AGENT_DIR = HERE.parent
CONFIG_JSON = HERE / "instagram_account.json"
CONFIG_MD = AGENT_DIR / "config.md"


def read_config():
    cfg = {}
    if CONFIG_JSON.exists():
        try:
            cfg.update(json.loads(CONFIG_JSON.read_text(encoding="utf-8") or "{}"))
        except Exception:
            pass
    if CONFIG_MD.exists():
        for line in CONFIG_MD.read_text(encoding="utf-8", errors="ignore").splitlines():
            clean = line.strip().lstrip("-").strip()
            if ":" not in clean:
                continue
            key, value = clean.split(":", 1)
            key = key.strip()
            value = value.strip()
            if key in {"META_ACCESS_TOKEN", "INSTAGRAM_BUSINESS_ID", "GRAPH_API_VERSION"} and value:
                cfg.setdefault(key, value)
    return cfg


def graph_get(version, node, params):
    query = urllib.parse.urlencode(params)
    url = f"https://graph.facebook.com/{version}/{node}?{query}"
    req = urllib.request.Request(url, headers={"User-Agent": "ConnectAI-Instagram-Tool"})
    with urllib.request.urlopen(req, timeout=15) as res:
        return json.loads(res.read().decode("utf-8") or "{}")


def main():
    cfg = read_config()
    token = (cfg.get("META_ACCESS_TOKEN") or "").strip()
    business_id = (cfg.get("INSTAGRAM_BUSINESS_ID") or "").strip()
    version = (cfg.get("GRAPH_API_VERSION") or "v20.0").strip().lstrip("/")

    report = ["# Instagram 연결 점검"]
    if not token or not business_id:
        report.append("- 상태: 미설정")
        report.append("- 필요한 값: META_ACCESS_TOKEN, INSTAGRAM_BUSINESS_ID")
        print("\n".join(report))
        return 2

    try:
        data = graph_get(
            version,
            business_id,
            {
                "fields": "id,username,name,followers_count,media_count",
                "access_token": token,
            },
        )
        report.append(f"- 계정 ID: {data.get('id', business_id)}")
        report.append(f"- username: {data.get('username', '(unknown)')}")
        if "followers_count" in data:
            report.append(f"- followers: {data.get('followers_count')}")
        if "media_count" in data:
            report.append(f"- media_count: {data.get('media_count')}")
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="ignore")[:500]
        report.append(f"- 연결 실패: HTTP {e.code}")
        report.append(f"- 응답: {body}")
        print("\n".join(report))
        return 1
    except Exception as e:
        report.append(f"- 연결 실패: {e}")
        print("\n".join(report))
        return 1

    print("\n".join(report))


if __name__ == "__main__":
    sys.exit(main() or 0)
