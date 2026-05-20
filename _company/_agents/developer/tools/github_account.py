import json
import pathlib
import sys
import urllib.error
import urllib.request


HERE = pathlib.Path(__file__).resolve().parent
AGENT_DIR = HERE.parent
CONFIG_JSON = HERE / "github_account.json"
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
            if ":" not in line:
                continue
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            if key in {"GITHUB_TOKEN", "GITHUB_DEFAULT_REPO"} and value:
                cfg.setdefault(key, value)
    return cfg


def github_get(path, token):
    req = urllib.request.Request(
        "https://api.github.com" + path,
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "ConnectAI-GitHub-Tool",
            **({"Authorization": f"Bearer {token}"} if token else {}),
        },
    )
    with urllib.request.urlopen(req, timeout=15) as res:
        return json.loads(res.read().decode("utf-8") or "{}")


def main():
    cfg = read_config()
    token = (cfg.get("GITHUB_TOKEN") or "").strip()
    repo = (cfg.get("GITHUB_DEFAULT_REPO") or "").strip().replace("https://github.com/", "").removesuffix(".git")

    report = ["# GitHub 연결 점검"]
    if not token:
        report.append("- 상태: 미설정")
        report.append("- 필요한 값: GITHUB_TOKEN")
        print("\n".join(report))
        return 2

    try:
        me = github_get("/user", token)
        report.append(f"- 인증 계정: {me.get('login', '(unknown)')}")
    except urllib.error.HTTPError as e:
        report.append(f"- 인증 실패: HTTP {e.code}")
        print("\n".join(report))
        return 1
    except Exception as e:
        report.append(f"- 연결 실패: {e}")
        print("\n".join(report))
        return 1

    if repo:
        try:
            r = github_get(f"/repos/{repo}", token)
            report.append(f"- 기본 저장소: {r.get('full_name', repo)}")
            report.append(f"- private: {r.get('private')}")
            report.append(f"- 기본 브랜치: {r.get('default_branch', '')}")
            report.append(f"- open issues: {r.get('open_issues_count', 0)}")
        except urllib.error.HTTPError as e:
            report.append(f"- 저장소 확인 실패: {repo} (HTTP {e.code})")
        except Exception as e:
            report.append(f"- 저장소 확인 실패: {e}")
    else:
        report.append("- 기본 저장소: 미설정")

    print("\n".join(report))


if __name__ == "__main__":
    sys.exit(main() or 0)
