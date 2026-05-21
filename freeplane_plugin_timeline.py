#!/usr/bin/env python3
"""
Freeplane Plugin Timeline Analyzer
Uso:
    python freeplane_plugin_timeline.py --repo C:/path/to/freeplane
    python freeplane_plugin_timeline.py --repo C:/path/to/freeplane --output report.html
    python freeplane_plugin_timeline.py --repo C:/path/to/freeplane --since 2018-01-01
    python freeplane_plugin_timeline.py --repo C:/path/to/freeplane --format markdown --output report.md
    python freeplane_plugin_timeline.py --repo C:/path/to/freeplane --format json   --output report.json
    python freeplane_plugin_timeline.py --repo C:/path/to/freeplane --format text   --output report.txt

Formati disponibili:
    html     (default) — dashboard interattiva con sidebar, filtri, timeline per plugin
    markdown           — report leggibile con descrizioni plugin, tabelle e commit notevoli
    json               — dati strutturati machine-readable
    text               — testo semplice, utile per grep/less
"""

import subprocess, re, json, argparse, sys
from datetime import datetime
from collections import defaultdict
from pathlib import Path

# ─────────────────────────────────────────────────────────────
PLUGIN_MODULES = {
    "freeplane_plugin_script":      ["freeplane_plugin_script"],
    "freeplane_plugin_formula":     ["freeplane_plugin_formula"],
    "freeplane_plugin_latex":       ["freeplane_plugin_latex"],
    "freeplane_plugin_svg":         ["freeplane_plugin_svg"],
    "freeplane_plugin_markdown":    ["freeplane_plugin_markdown"],
    "freeplane_plugin_openmaps":    ["freeplane_plugin_openmaps"],
    "freeplane_plugin_jsyntaxpane": ["freeplane_plugin_jsyntaxpane"],
    "freeplane_plugin_bugreport":   ["freeplane_plugin_bugreport"],
    "freeplane_api":                ["freeplane_api"],
    "freeplane_framework":          ["freeplane_framework"],
    "freeplane_debughelper":        ["freeplane_debughelper"],
    "freeplane_core":               ["freeplane/src", "freeplane/main",
                                     "freeplane/resources", "freeplane/test"],
    "addons":                       ["addons", "addon", "AddOn"],
}
PLUGIN_LABELS = {
    "freeplane_plugin_script":      "Script / Groovy",
    "freeplane_plugin_formula":     "Formula",
    "freeplane_plugin_latex":       "LaTeX",
    "freeplane_plugin_svg":         "SVG",
    "freeplane_plugin_markdown":    "Markdown",
    "freeplane_plugin_openmaps":    "OpenMaps",
    "freeplane_plugin_jsyntaxpane": "JSyntaxPane",
    "freeplane_plugin_bugreport":   "Bug Report",
    "freeplane_api":                "API pubblica",
    "freeplane_framework":          "Framework OSGi",
    "freeplane_debughelper":        "Debug Helper",
    "freeplane_core":               "Core",
    "addons":                       "Add-ons",
    "other":                        "Altro",
}
PLUGIN_COLORS = {
    "freeplane_plugin_script":      "#6366f1",
    "freeplane_plugin_formula":     "#f59e0b",
    "freeplane_plugin_latex":       "#10b981",
    "freeplane_plugin_svg":         "#ec4899",
    "freeplane_plugin_markdown":    "#14b8a6",
    "freeplane_plugin_openmaps":    "#3b82f6",
    "freeplane_plugin_jsyntaxpane": "#8b5cf6",
    "freeplane_plugin_bugreport":   "#ef4444",
    "freeplane_api":                "#f97316",
    "freeplane_framework":          "#64748b",
    "freeplane_debughelper":        "#94a3b8",
    "freeplane_core":               "#22c55e",
    "addons":                       "#a855f7",
    "other":                        "#475569",
}
COMMIT_CATEGORIES = {
    "feature":    [r"\badd\b", r"\bnew\b", r"\bfeat\b", r"\bimplement\b",
                   r"\bsupport\b", r"\bintroduc\b", r"\benable\b", r"\bcreate\b"],
    "fix":        [r"\bfix\b", r"\bbug\b", r"\bpatch\b", r"\bresolv\b",
                   r"\bcorrect\b", r"\brepair\b", r"\bregression\b"],
    "refactor":   [r"\brefactor\b", r"\bcleanup\b", r"\bclean up\b",
                   r"\brenaming\b", r"\bmove\b", r"\bextract\b", r"\brestructur\b"],
    "api_change": [r"\bapi\b", r"\binterface\b", r"\bdeprecate\b",
                   r"\bbreak\b", r"\bmigrat\b", r"\bupgrade\b"],
    "docs":       [r"\bdoc\b", r"\bjavadoc\b", r"\bcomment\b", r"\breadme\b"],
    "test":       [r"\btest\b", r"\bjunit\b", r"\bspec\b", r"\bassert\b"],
    "build":      [r"\bbuild\b", r"\bgradle\b", r"\bmaven\b", r"\bpom\b",
                   r"\bdependenc\b", r"\bversion\b", r"\brelease\b"],
}
CAT_COLORS = {
    "feature": "#22c55e", "fix": "#ef4444", "refactor": "#f59e0b",
    "api_change": "#8b5cf6", "docs": "#3b82f6", "test": "#06b6d4",
    "build": "#6b7280", "other": "#94a3b8",
}

# ─────────────────────────────────────────────────────────────
# GIT
# ─────────────────────────────────────────────────────────────
def run_git(repo, args):
    r = subprocess.run(["git", "-C", repo] + args,
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        print(f"[WARN] git: {r.stderr.strip()[:120]}", file=sys.stderr)
    return r.stdout

def get_all_commits(repo, since=None, until=None):
    RS, US = chr(0x1E), chr(0x1F)
    fmt = US.join(["%H", "%ai", "%an", "%ae", "%s", "%b"]) + RS
    ma = ["log", "--pretty=format:" + fmt, "--no-merges", "--encoding=utf-8"]
    if since: ma += ["--since=" + since]
    if until: ma += ["--until=" + until]
    meta_map = {}
    for block in run_git(repo, ma).split(RS):
        block = block.strip()
        if not block: continue
        parts = block.split(US)
        if len(parts) < 5: continue
        h = parts[0].strip()
        if not h or len(h) != 40: continue
        try:    date = datetime.fromisoformat(parts[1].strip())
        except: date = None
        meta_map[h] = {
            "hash": h, "date": date,
            "author": parts[2].strip(), "email": parts[3].strip(),
            "subject": parts[4].strip(),
            "body": parts[5].strip() if len(parts) > 5 else "",
            "files": [],
        }
    if not meta_map:
        print("[WARN] Nessun commit letto.", file=sys.stderr)
        return []
    print(f"      Metadati: {len(meta_map)} commit", file=sys.stderr)
    fa = ["log", "--pretty=format:##%H", "--name-only", "--no-merges"]
    if since: fa += ["--since=" + since]
    if until: fa += ["--until=" + until]
    cur, nf = None, 0
    for line in run_git(repo, fa).splitlines():
        line = line.rstrip()
        if not line: continue
        if line.startswith("##") and len(line) == 42:
            cur = line[2:]
        elif cur and cur in meta_map:
            meta_map[cur]["files"].append(line); nf += 1
    print(f"      File: {nf} path associati", file=sys.stderr)
    return sorted(meta_map.values(), key=lambda x: x["date"] or datetime.min, reverse=True)

# ─────────────────────────────────────────────────────────────
# ANALISI
# ─────────────────────────────────────────────────────────────
def identify_plugins(commit):
    fs = " ".join(commit["files"])
    found = set()
    for key, pats in PLUGIN_MODULES.items():
        for p in pats:
            if p in fs: found.add(key); break
    return sorted(found) if found else ["other"]

def classify_commit(commit):
    text = (commit["subject"] + " " + commit["body"]).lower()
    for cat, pats in COMMIT_CATEGORIES.items():
        for p in pats:
            if re.search(p, text, re.IGNORECASE): return cat
    return "other"

def build_plugin_map(commits):
    pm = defaultdict(list)
    n = len(commits)
    for i, c in enumerate(commits):
        plugins = identify_plugins(c)
        cat     = classify_commit(c)
        entry   = {**c, "category": cat, "plugins": plugins}
        for p in plugins: pm[p].append(entry)
        if (i+1) % 500 == 0:
            print(f"      {i+1}/{n}...", file=sys.stderr)
    for k in pm:
        pm[k].sort(key=lambda x: x["date"] or datetime.min)
    return dict(pm)

def to_json_data(plugin_map):
    out = {}
    for pk, commits in plugin_map.items():
        out[pk] = [{
            "hash":     c["hash"][:8],
            "fullhash": c["hash"],
            "date":     c["date"].strftime("%Y-%m-%d") if c["date"] else "?",
            "year":     c["date"].year if c["date"] else 0,
            "author":   c["author"],
            "subject":  c["subject"],
            "body":     c["body"][:400] if c["body"] else "",
            "category": c["category"],
            "plugins":  c["plugins"],
            "files":    c["files"][:25],
        } for c in commits]
    def ser(o): return o.isoformat() if isinstance(o, datetime) else str(o)
    return json.dumps(out, default=ser, ensure_ascii=False, separators=(',',':'))

def to_json_meta(plugin_map):
    sp = sorted(plugin_map.items(), key=lambda x: -len(x[1]))
    return json.dumps({
        pk: {"label": PLUGIN_LABELS.get(pk, pk),
             "color": PLUGIN_COLORS.get(pk, "#475569"),
             "total": len(commits)}
        for pk, commits in sp
    }, ensure_ascii=False, separators=(',',':'))

# ─────────────────────────────────────────────────────────────
# HTML TEMPLATE — dati iniettati via .replace() su __TOKEN__
# Layout a 3 colonne:
#   sidebar(240) | stats panel(280, fixed) | commit list(flex, scroll)
# Nessuna f-string nel template: zero conflitti di escape.
# ─────────────────────────────────────────────────────────────
HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Freeplane Plugin Timeline</title>
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{
  --bg:#0b1120;--surf:#111827;--brd:#1e293b;--brd2:#334155;
  --txt:#e2e8f0;--mut:#94a3b8;--dim:#64748b;--drk:#0f172a;
}
html{height:100%}
body{height:100%;overflow:hidden;font-family:system-ui,-apple-system,sans-serif;background:var(--bg);color:var(--txt);display:flex}

/* ── SIDEBAR (plugin list) ── */
#sb{width:220px;min-width:220px;display:flex;flex-direction:column;
    background:var(--surf);border-right:1px solid var(--brd)}
#sb-hd{padding:12px 12px 8px;border-bottom:1px solid var(--brd);flex-shrink:0}
#sb-hd h1{font-size:12px;font-weight:700;color:#60a5fa}
#sb-hd p{font-size:10px;color:var(--dim);margin-top:2px}
#sb-hd input{display:block;width:100%;margin-top:7px;padding:5px 8px;
             background:var(--drk);border:1px solid var(--brd2);
             border-radius:5px;color:var(--txt);font-size:11px}
#sb-hd input:focus{outline:none;border-color:#3b82f6}
#sb-list{flex:1;overflow-y:auto}
.pni{display:flex;align-items:center;gap:8px;padding:6px 12px;
     cursor:pointer;border-left:3px solid transparent;transition:background .1s}
.pni:hover{background:var(--brd)}
.pni.act{background:var(--brd);border-left-color:var(--pc,#60a5fa)}
.pni-dot{width:8px;height:8px;border-radius:50%;flex-shrink:0}
.pni-lbl{font-size:11px;flex:1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.pni-n{font-size:10px;color:var(--dim);background:var(--drk);border-radius:8px;padding:1px 6px;flex-shrink:0}

/* ── MAIN AREA ── */
#main{flex:1;display:flex;flex-direction:column;overflow:hidden;min-width:0}

/* ── TOOLBAR ── */
#tb{display:flex;align-items:center;gap:6px;padding:7px 14px;
    background:var(--surf);border-bottom:1px solid var(--brd);flex-shrink:0;flex-wrap:wrap}
#tb-ttl{font-size:13px;font-weight:700;white-space:nowrap}
#tb-cnt{font-size:10px;color:var(--dim);margin-right:auto;white-space:nowrap}
#tb-srch{padding:5px 9px;background:var(--drk);border:1px solid var(--brd2);
         border-radius:5px;color:var(--txt);font-size:11px;width:160px}
#tb-srch:focus{outline:none;border-color:#3b82f6}
#yr-sel{padding:4px 5px;background:var(--drk);border:1px solid var(--brd2);
        border-radius:5px;color:var(--txt);font-size:11px}
.fb{padding:3px 8px;border-radius:10px;border:1px solid var(--brd2);
    background:var(--drk);color:var(--mut);font-size:10px;cursor:pointer}
.fb:hover{background:var(--brd);color:var(--txt)}
.fb.on{color:#fff!important}
#back-btn{display:none;padding:4px 9px;background:var(--brd);
          border:1px solid var(--brd2);border-radius:5px;
          color:var(--mut);font-size:11px;cursor:pointer;white-space:nowrap}
#back-btn:hover{color:var(--txt)}

/* ── BODY (below toolbar) ── */
#body{flex:1;display:flex;overflow:hidden;min-height:0}

/* ── OVERVIEW (replaces full body) ── */
#ov{flex:1;overflow-y:auto;padding:16px;display:none}
.ov-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(190px,1fr));gap:10px;margin-bottom:18px}
.ov-card{background:var(--surf);border:1px solid var(--brd);border-radius:8px;
         padding:11px 13px;cursor:pointer;border-left:4px solid var(--pc,#475569);
         transition:transform .1s,border-color .15s}
.ov-card:hover{transform:translateY(-2px);border-color:var(--pc,#475569)}
.ov-nm{font-size:12px;font-weight:600}
.ov-key{font-size:9px;color:var(--dim);font-family:monospace;margin-top:1px}
.ov-num{font-size:22px;font-weight:800;margin-top:5px}
.mini-spark{height:24px;display:flex;align-items:flex-end;gap:1px;margin-top:5px}
.mini-spark span{flex:1;border-radius:1px 1px 0 0;min-width:3px}
.gb-box{background:var(--surf);border:1px solid var(--brd);border-radius:8px;padding:13px 15px}
.gb-box h3{font-size:10px;text-transform:uppercase;letter-spacing:.08em;color:var(--dim);margin-bottom:10px}
.br{display:flex;align-items:center;gap:8px;margin:3px 0;cursor:pointer}
.br:hover .br-lbl{color:var(--txt)}
.br-lbl{width:150px;font-size:11px;color:var(--mut);text-align:right;
        white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.br-trk{flex:1;background:var(--brd);border-radius:3px;height:11px;overflow:hidden}
.br-fil{height:100%;border-radius:3px}
.br-n{width:34px;font-size:11px;color:var(--txt)}

/* ── DETAIL: side-by-side stats | commits ── */
#det{flex:1;display:none;overflow:hidden;min-height:0}

/* Left stats panel — fixed width, scrolls independently */
#det-left{width:280px;min-width:280px;display:flex;flex-direction:column;
          overflow-y:auto;border-right:1px solid var(--brd);padding:14px;gap:12px}

/* Right commit list — flex:1, scrolls independently */
#det-right{flex:1;display:flex;flex-direction:column;overflow:hidden;min-width:0}

/* Plugin header strip */
#ph{padding:12px 14px;border-bottom:1px solid var(--brd);flex-shrink:0;
    display:flex;align-items:center;gap:10px}
#ph-dot{width:10px;height:10px;border-radius:50%;flex-shrink:0}
#ph-name{font-size:14px;font-weight:700}
#ph-key{font-size:10px;color:var(--dim);font-family:monospace;margin-left:4px}
#ph-tot{margin-left:auto;font-size:20px;font-weight:800}
#ph-totlbl{font-size:10px;color:var(--dim);margin-left:4px;align-self:flex-end;padding-bottom:2px}

/* Stat cards */
.sc{background:var(--drk);border:1px solid var(--brd);border-radius:7px;padding:10px 12px}
.sc h4{font-size:9px;text-transform:uppercase;letter-spacing:.08em;color:var(--dim);margin-bottom:8px}
.det-spark{height:34px;display:flex;align-items:flex-end;gap:1px;margin-bottom:3px}
.det-spark span{flex:1;border-radius:1px 1px 0 0;min-width:3px;cursor:default}
.yr-lbl-row{display:flex;gap:1px;font-size:8px;color:var(--dim)}
.yr-lbl-row span{flex:1;overflow:hidden;white-space:nowrap}
.au-row{display:flex;justify-content:space-between;align-items:center;
        padding:3px 0;border-bottom:1px solid var(--brd);font-size:11px}
.au-nm{color:var(--mut);overflow:hidden;text-overflow:ellipsis;white-space:nowrap;max-width:160px}
.au-n{font-weight:700;color:var(--txt)}
.cat-pills{display:flex;flex-wrap:wrap;gap:3px}
.cpill{border-radius:4px;padding:2px 7px;font-size:10px;font-weight:700;
       color:#fff;cursor:pointer;opacity:.8;transition:opacity .1s}
.cpill:hover{opacity:1}
.cpill.on{opacity:1;outline:2px solid rgba(255,255,255,.35)}

/* Commit list header */
#cl-hd{display:flex;align-items:center;justify-content:space-between;
       padding:7px 14px;border-bottom:1px solid var(--brd);flex-shrink:0;
       font-size:10px;text-transform:uppercase;letter-spacing:.08em;color:var(--dim)}
#cl-hd span:last-child{color:var(--txt)}

/* Commit scroll container */
#cl-scroll{flex:1;overflow-y:auto;min-height:0}

/* Year separator */
.yr-sep{padding:4px 14px 2px;font-size:10px;font-weight:700;
        color:var(--dim);background:var(--bg);
        position:sticky;top:0;z-index:5;
        border-bottom:1px solid var(--brd);letter-spacing:.06em}

/* Commit row */
.ci{display:grid;grid-template-columns:82px 74px 1fr 54px;
    gap:6px;padding:7px 14px;border-bottom:1px solid var(--brd);
    cursor:pointer;transition:background .1s;align-items:start}
.ci:hover{background:var(--brd)}
.ci.open{background:var(--drk)}
.ci-dt{font-size:10px;color:var(--dim);padding-top:1px}
.ci-badge{border-radius:3px;padding:1px 0;font-size:9px;
          font-weight:700;color:#fff;text-align:center}
.ci-subj{font-size:12px;line-height:1.4;word-break:break-word}
.ci-hash{font-size:9px;color:var(--brd2);font-family:monospace;text-align:right;padding-top:1px}

/* Expanded detail */
.cd{display:none;padding:7px 14px 10px calc(14px + 82px + 74px + 12px);
    background:var(--drk);border-bottom:1px solid var(--brd);
    font-size:11px;color:var(--dim)}
.cd.open{display:block}
.cd-body{white-space:pre-wrap;color:var(--mut);line-height:1.55;margin-bottom:6px}
.cd-meta{margin-bottom:5px}
.cd-meta a{color:#3b82f6;text-decoration:none}
.cd-meta a:hover{text-decoration:underline}
.cd-files{font-family:monospace;font-size:10px;color:#334155;
          max-height:80px;overflow-y:auto;margin-top:5px;line-height:1.5}
.cd-cross{margin-top:5px;display:flex;flex-wrap:wrap;gap:4px}
.cd-xbadge{border-radius:4px;padding:1px 7px;font-size:10px;cursor:pointer}

#no-res{padding:30px;text-align:center;color:var(--dim);font-size:13px;display:none}

::-webkit-scrollbar{width:5px;height:5px}
::-webkit-scrollbar-track{background:transparent}
::-webkit-scrollbar-thumb{background:var(--brd2);border-radius:3px}
</style>
</head>
<body>

<!-- SIDEBAR -->
<div id="sb">
  <div id="sb-hd">
    <h1>&#128193; Freeplane Plugins</h1>
    <p>__PERIOD__ &middot; __TOTAL__ commit</p>
    <input id="sb-srch" type="text" placeholder="&#128269; Filtra plugin...">
  </div>
  <div id="sb-list">
    <div class="pni act" data-pk="__ov__" style="--pc:#60a5fa">
      <div class="pni-dot" style="background:#60a5fa"></div>
      <span class="pni-lbl">&#128202; Panoramica</span>
      <span class="pni-n">__TOTAL__</span>
    </div>
  </div>
</div>

<!-- MAIN -->
<div id="main">
  <!-- Toolbar -->
  <div id="tb">
    <span id="tb-ttl">Panoramica</span>
    <span id="tb-cnt"></span>
    <input id="tb-srch" type="text" placeholder="&#128269; Cerca nei commit...">
    <select id="yr-sel"><option value="">Tutti gli anni</option></select>
    <div id="cat-f" style="display:flex;gap:3px;flex-wrap:wrap"></div>
    <button id="back-btn" onclick="showOv()">&#8592; Tutti i plugin</button>
  </div>

  <!-- Body area -->
  <div id="body">

    <!-- OVERVIEW -->
    <div id="ov">
      <div class="ov-grid" id="ov-grid"></div>
      <div class="gb-box">
        <h3>Commit per plugin</h3>
        <div id="gb"></div>
      </div>
    </div>

    <!-- DETAIL: left stats | right commits -->
    <div id="det">

      <!-- LEFT: stats panel -->
      <div id="det-left">
        <div class="sc" id="sc-spark">
          <h4>Attivita per anno</h4>
          <div class="det-spark" id="d-spark"></div>
          <div class="yr-lbl-row" id="d-yrl"></div>
        </div>
        <div class="sc">
          <h4>Tipo modifica</h4>
          <div class="cat-pills" id="d-cats"></div>
        </div>
        <div class="sc">
          <h4>Top contributor</h4>
          <div id="d-authors"></div>
        </div>
      </div>

      <!-- RIGHT: plugin header + commit list -->
      <div id="det-right">
        <!-- Plugin header -->
        <div id="ph">
          <div id="ph-dot"></div>
          <span id="ph-name"></span>
          <span id="ph-key"></span>
          <span id="ph-tot"></span>
          <span id="ph-totlbl">commit</span>
        </div>

        <!-- Commit list header -->
        <div id="cl-hd">
          <span id="cl-lbl">Commit (dal piu recente)</span>
          <span id="cl-vis"></span>
        </div>

        <!-- SCROLL CONTAINER — questa e la parte critica -->
        <div id="cl-scroll">
          <div id="cl-inner"></div>
          <div id="no-res">Nessun commit corrisponde ai filtri.</div>
        </div>
      </div>

    </div><!-- /det -->
  </div><!-- /body -->
</div><!-- /main -->

<script>
const DATA = __DATA_JSON__;
const META = __META_JSON__;
const CC   = __CAT_COLORS_JSON__;

let curPk = '__ov__', fCat = null, fYear = '', fSearch = '';

const allYears = [...new Set(
  Object.values(DATA).flatMap(cs => cs.map(c => c.year).filter(Boolean))
)].sort();

/* ── INIT ── */
function init() {
  // Sidebar items
  const list = document.getElementById('sb-list');
  Object.entries(META).forEach(([pk, m]) => {
    const el = document.createElement('div');
    el.className = 'pni'; el.dataset.pk = pk;
    el.style.setProperty('--pc', m.color);
    el.innerHTML =
      '<div class="pni-dot" style="background:' + m.color + '"></div>' +
      '<span class="pni-lbl">' + esc(m.label) + '</span>' +
      '<span class="pni-n">' + m.total + '</span>';
    el.addEventListener('click', () => showPlugin(pk));
    list.appendChild(el);
  });

  // Year select
  const ys = document.getElementById('yr-sel');
  allYears.forEach(y => {
    const o = document.createElement('option');
    o.value = y; o.textContent = y; ys.appendChild(o);
  });

  // Cat filter buttons
  const cf = document.getElementById('cat-f');
  Object.entries(CC).forEach(([cat, color]) => {
    const b = document.createElement('button');
    b.className = 'fb'; b.dataset.cat = cat;
    b.textContent = cat;
    b.addEventListener('click', () => toggleCat(cat, b, color));
    cf.appendChild(b);
  });

  // Sidebar search
  document.getElementById('sb-srch').addEventListener('input', e => {
    const q = e.target.value.toLowerCase();
    document.querySelectorAll('.pni[data-pk]').forEach(el => {
      if (el.dataset.pk === '__ov__') return;
      el.style.display =
        (!q || el.querySelector('.pni-lbl').textContent.toLowerCase().includes(q)) ? '' : 'none';
    });
  });

  // Toolbar search
  document.getElementById('tb-srch').addEventListener('input', e => {
    fSearch = e.target.value.toLowerCase();
    if (curPk !== '__ov__') renderCommits(curPk);
  });

  // Year filter
  document.getElementById('yr-sel').addEventListener('change', e => {
    fYear = e.target.value;
    if (curPk !== '__ov__') renderCommits(curPk);
  });

  showOv();
}

function toggleCat(cat, btn, color) {
  if (fCat === cat) {
    fCat = null;
    document.querySelectorAll('.fb,.cpill').forEach(b => {
      b.classList.remove('on');
      b.style.removeProperty('background');
    });
  } else {
    fCat = cat;
    document.querySelectorAll('.fb').forEach(b => {
      b.classList.remove('on'); b.style.removeProperty('background');
    });
    btn.classList.add('on'); btn.style.background = color;
    // sync pills
    document.querySelectorAll('.cpill').forEach(p => {
      p.classList.toggle('on', p.dataset.cat === cat);
    });
  }
  if (curPk !== '__ov__') renderCommits(curPk);
}

/* ── OVERVIEW ── */
function showOv() {
  curPk = '__ov__';
  setAct('__ov__');
  document.getElementById('ov').style.display  = 'block';
  document.getElementById('det').style.display = 'none';
  document.getElementById('back-btn').style.display = 'none';
  document.getElementById('tb-ttl').textContent = 'Panoramica';
  document.getElementById('tb-cnt').textContent = '';
  renderOvGrid(); renderGlobalBar();
}

function renderOvGrid() {
  const g = document.getElementById('ov-grid'); g.innerHTML = '';
  Object.entries(META).forEach(([pk, m]) => {
    const cs = DATA[pk] || [], byY = {};
    cs.forEach(c => { byY[c.year] = (byY[c.year]||0)+1; });
    const maxY = Math.max(...Object.values(byY), 1);
    const bars = allYears.map(y => {
      const h = Math.max(2, Math.round(((byY[y]||0)/maxY)*20));
      return '<span style="height:'+h+'px;background:'+m.color+'" title="'+y+': '+(byY[y]||0)+'"></span>';
    }).join('');
    const card = document.createElement('div');
    card.className = 'ov-card'; card.style.setProperty('--pc', m.color);
    card.innerHTML =
      '<div class="ov-nm">'+esc(m.label)+'</div>'+
      '<div class="ov-key">'+esc(pk)+'</div>'+
      '<div class="ov-num" style="color:'+m.color+'">'+m.total+'</div>'+
      '<div class="mini-spark">'+bars+'</div>';
    card.addEventListener('click', () => showPlugin(pk));
    g.appendChild(card);
  });
}

function renderGlobalBar() {
  const gb = document.getElementById('gb'); gb.innerHTML = '';
  const max = Math.max(...Object.values(META).map(m => m.total), 1);
  Object.entries(META).sort((a,b) => b[1].total-a[1].total).forEach(([pk, m]) => {
    const pct = Math.round(m.total/max*100);
    const row = document.createElement('div');
    row.className = 'br';
    row.innerHTML =
      '<span class="br-lbl" title="'+pk+'">'+esc(m.label)+'</span>'+
      '<div class="br-trk"><div class="br-fil" style="width:'+pct+'%;background:'+m.color+'"></div></div>'+
      '<span class="br-n">'+m.total+'</span>';
    row.addEventListener('click', () => showPlugin(pk));
    gb.appendChild(row);
  });
}

/* ── PLUGIN DETAIL ── */
function showPlugin(pk) {
  const m = META[pk]; if (!m) return;
  curPk = pk; setAct(pk);
  document.getElementById('ov').style.display   = 'none';
  document.getElementById('det').style.display  = 'flex';
  document.getElementById('back-btn').style.display = '';
  document.getElementById('tb-ttl').textContent = m.label;

  // Plugin header (right panel)
  document.getElementById('ph-dot').style.background = m.color;
  const phn = document.getElementById('ph-name');
  phn.textContent = m.label; phn.style.color = m.color;
  document.getElementById('ph-key').textContent = pk;
  const pht = document.getElementById('ph-tot');
  pht.textContent = m.total; pht.style.color = m.color;

  renderSparkline(pk, m.color);
  renderCatStats(pk);
  renderAuthors(pk);
  renderCommits(pk);

  document.getElementById('cl-scroll').scrollTop = 0;
  document.getElementById('det-left').scrollTop  = 0;
}

function renderSparkline(pk, color) {
  const cs = DATA[pk]||[], byY = {};
  cs.forEach(c => { byY[c.year]=(byY[c.year]||0)+1; });
  const maxY = Math.max(...Object.values(byY), 1);
  const spark = document.getElementById('d-spark');
  const lbl   = document.getElementById('d-yrl');
  spark.innerHTML = lbl.innerHTML = '';
  allYears.forEach(y => {
    const n = byY[y]||0, h = Math.max(2, Math.round(n/maxY*30));
    const s = document.createElement('span');
    s.style.cssText = 'height:'+h+'px;background:'+color;
    s.title = y+': '+n+' commit';
    spark.appendChild(s);
    const l = document.createElement('span');
    l.textContent = String(y).slice(2); l.title = y;
    lbl.appendChild(l);
  });
}

function renderCatStats(pk) {
  const cs = DATA[pk]||[], byCat = {};
  cs.forEach(c => { byCat[c.category]=(byCat[c.category]||0)+1; });
  const ct = document.getElementById('d-cats'); ct.innerHTML = '';
  Object.entries(byCat).sort((a,b)=>b[1]-a[1]).forEach(([cat, n]) => {
    const p = document.createElement('span');
    p.className = 'cpill' + (fCat===cat?' on':'');
    p.dataset.cat = cat;
    p.style.background = CC[cat]||'#94a3b8';
    p.textContent = cat+' '+n;
    p.addEventListener('click', () => {
      const btn = document.querySelector('.fb[data-cat="'+cat+'"]');
      if (btn) toggleCat(cat, btn, CC[cat]||'#94a3b8');
    });
    ct.appendChild(p);
  });
}

function renderAuthors(pk) {
  const cs = DATA[pk]||[], byA = {};
  cs.forEach(c => { byA[c.author]=(byA[c.author]||0)+1; });
  const au = document.getElementById('d-authors');
  au.innerHTML = Object.entries(byA).sort((a,b)=>b[1]-a[1]).slice(0,8)
    .map(([name,n]) =>
      '<div class="au-row">'+
      '<span class="au-nm" title="'+esc(name)+'">'+esc(name)+'</span>'+
      '<span class="au-n">'+n+'</span></div>'
    ).join('');
}

/* ── COMMIT LIST ── */
function getFiltered(pk) {
  return (DATA[pk]||[]).filter(c => {
    if (fCat    && c.category !== fCat)              return false;
    if (fYear   && String(c.year) !== String(fYear)) return false;
    if (fSearch && !(c.subject+' '+c.author+' '+c.hash).toLowerCase().includes(fSearch)) return false;
    return true;
  });
}

function renderCommits(pk) {
  const filtered = getFiltered(pk);
  const total    = (DATA[pk]||[]).length;

  document.getElementById('tb-cnt').textContent =
    filtered.length < total ? filtered.length+' / '+total+' commit' : total+' commit';
  document.getElementById('cl-vis').textContent =
    filtered.length < total ? filtered.length+' visibili' : '';

  const inner = document.getElementById('cl-inner');
  const noRes = document.getElementById('no-res');
  inner.innerHTML = '';

  if (filtered.length === 0) { noRes.style.display='block'; return; }
  noRes.style.display = 'none';

  // Raggruppa per anno, dal più recente
  const byY = {};
  [...filtered].reverse().forEach(c => {
    const y = c.year||'?';
    if (!byY[y]) byY[y] = [];
    byY[y].push(c);
  });

  Object.entries(byY).sort((a,b) => b[0]-a[0]).forEach(([year, commits]) => {
    // Year separator
    const sep = document.createElement('div');
    sep.className = 'yr-sep';
    sep.textContent = year + '  (' + commits.length + ')';
    inner.appendChild(sep);

    commits.forEach(c => {
      const col = CC[c.category]||'#94a3b8';

      // Row
      const row = document.createElement('div');
      row.className = 'ci';
      row.innerHTML =
        '<span class="ci-dt">'+c.date+'</span>'+
        '<span class="ci-badge" style="background:'+col+'">'+c.category+'</span>'+
        '<span class="ci-subj">'+esc(c.subject)+'</span>'+
        '<span class="ci-hash">'+c.hash+'</span>';

      // Expandable detail
      const det = document.createElement('div');
      det.className = 'cd';

      let html = '';
      if (c.body) html += '<div class="cd-body">'+esc(c.body)+'</div>';
      html +=
        '<div class="cd-meta">by <strong>'+esc(c.author)+'</strong> &nbsp;&middot;&nbsp; '+
        '<a href="https://github.com/freeplane/freeplane/commit/'+c.fullhash+'" target="_blank">'+
        'Apri su GitHub &#8599;</a></div>';
      if (c.files && c.files.length) {
        html += '<div class="cd-files">'+
          c.files.slice(0,20).map(f=>'<div>'+esc(f)+'</div>').join('')+
          (c.files.length>20?'<div style="color:var(--dim)">...e altri</div>':'')+
          '</div>';
      }
      const others = (c.plugins||[]).filter(p=>p!==pk);
      if (others.length) {
        html += '<div class="cd-cross">';
        others.forEach(p => {
          const mc = META[p];
          html += '<span class="cd-xbadge" '+
            'style="background:'+(mc?mc.color:'#475569')+'22;color:'+(mc?mc.color:'#94a3b8')+'" '+
            'onclick="showPlugin(\''+p+'\')">'+esc(mc?mc.label:p)+'</span>';
        });
        html += '</div>';
      }
      det.innerHTML = html;

      // Toggle on click
      row.addEventListener('click', () => {
        const wasOpen = det.classList.contains('open');
        document.querySelectorAll('.cd.open').forEach(d => {
          d.classList.remove('open');
          if (d.previousElementSibling) d.previousElementSibling.classList.remove('open');
        });
        if (!wasOpen) { det.classList.add('open'); row.classList.add('open'); }
      });

      inner.appendChild(row);
      inner.appendChild(det);
    });
  });
}

/* ── UTILS ── */
function setAct(pk) {
  document.querySelectorAll('.pni').forEach(el =>
    el.classList.toggle('act', el.dataset.pk === pk)
  );
}
function esc(s) {
  return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;')
                  .replace(/>/g,'&gt;').replace(/"/g,'&quot;');
}

init();
</script>
</body>
</html>
"""

def render_html(plugin_map, repo_path, since, until):
    total  = sum(len(v) for v in plugin_map.values())
    period = (since or '...') + ' → ' + (until or 'oggi') if (since or until) else 'tutta la storia'
    html = HTML_TEMPLATE
    html = html.replace('__DATA_JSON__',      to_json_data(plugin_map))
    html = html.replace('__META_JSON__',      to_json_meta(plugin_map))
    html = html.replace('__CAT_COLORS_JSON__', json.dumps(CAT_COLORS, ensure_ascii=False, separators=(',',':')))
    html = html.replace('__PERIOD__',         period)
    html = html.replace('__TOTAL__',          str(total))
    return html

# ─────────────────────────────────────────────────────────────
# OUTPUT ALTERNATIVI
# ─────────────────────────────────────────────────────────────
PLUGIN_DESCRIPTIONS = {
    "freeplane_plugin_script":
        "Permette di eseguire script **Groovy** (e altri linguaggi JVM) direttamente sulle mappe. "
        "È il cuore dell'automazione in Freeplane: si usa per generare nodi, trasformare testo, "
        "interrogare API esterne o costruire workflow personalizzati.",
    "freeplane_plugin_formula":
        "Aggiunge il supporto alle **formule** nei nodi (sintassi simile a spreadsheet). "
        "Consente calcoli automatici, riferimenti ad altri nodi e aggregazioni, "
        "trasformando Freeplane in uno strumento di analisi dati visuale.",
    "freeplane_plugin_latex":
        "Integra il rendering **LaTeX/MathJax** nei nodi. "
        "Indispensabile per chi usa Freeplane in ambito scientifico, matematico o accademico "
        "per inserire equazioni e notazione formale nelle mappe.",
    "freeplane_plugin_svg":
        "Supporto per immagini e grafici **SVG** embedded nei nodi. "
        "Permette di arricchire le mappe con grafica vettoriale scalabile "
        "e di visualizzare diagrammi generati da script.",
    "freeplane_plugin_markdown":
        "Rendering **Markdown** nel pannello note dei nodi. "
        "Consente di scrivere note ricche (titoli, grassetti, liste, codice) "
        "in sintassi standard Markdown invece di HTML.",
    "freeplane_plugin_openmaps":
        "Integrazione con **OpenStreetMap**: permette di visualizzare e agganciare "
        "coordinate geografiche ai nodi, utile per mappe concettuali con componente spaziale.",
    "freeplane_plugin_jsyntaxpane":
        "Evidenziazione della **sintassi del codice** nell'editor script interno. "
        "Rende più leggibile e modificabile il codice Groovy/script direttamente nell'interfaccia.",
    "freeplane_plugin_bugreport":
        "Strumento interno per la **segnalazione bug**: raccoglie informazioni di sistema, "
        "log e contesto della mappa per facilitare il reporting agli sviluppatori.",
    "freeplane_api":
        "L'**API pubblica** di Freeplane: le interfacce e le classi esposte agli sviluppatori "
        "di plugin e script. Definisce il contratto stabile tra il core e le estensioni esterne.",
    "freeplane_framework":
        "Il **framework OSGi** che gestisce il ciclo di vita dei plugin: "
        "caricamento, dipendenze, isolamento dei moduli. È la spina dorsale dell'architettura "
        "modulare di Freeplane.",
    "freeplane_debughelper":
        "Utilità per il **debug** in sviluppo: strumenti di ispezione dello stato interno, "
        "logging avanzato e assistenza agli sviluppatori di plugin.",
    "freeplane_core":
        "Il **nucleo** dell'applicazione: gestione delle mappe `.mm`, rendering del canvas, "
        "sistema di nodi/edge, filtri, export, UI principale e tutto ciò che non è un plugin separato.",
    "addons":
        "**Add-on di terze parti** distribuiti tramite il repository ufficiale. "
        "Pacchetti installabili dall'utente che estendono Freeplane senza modificare il core.",
    "other":
        "Commit che toccano aree **trasversali** o non classificabili in un singolo plugin: "
        "build system, CI, traduzioni, documentazione generale del progetto.",
}

def render_markdown(pm):
    from datetime import datetime as dt
    lines = []
    lines.append("# Freeplane Plugin Timeline — Rapporto storico\n")
    lines.append(f"_Generato il {dt.now().strftime('%Y-%m-%d %H:%M')}_\n")
    lines.append("---\n")

    # Indice
    lines.append("## Indice dei plugin\n")
    for pk, cs in sorted(pm.items(), key=lambda x: -len(x[1])):
        label = PLUGIN_LABELS.get(pk, pk)
        anchor = pk.replace("_", "-")
        lines.append(f"- [{label}](#{anchor}) — **{len(cs)}** commit")
    lines.append("")
    lines.append("---\n")

    # Sezione per ogni plugin
    for pk, cs in sorted(pm.items(), key=lambda x: -len(x[1])):
        label  = PLUGIN_LABELS.get(pk, pk)
        color  = PLUGIN_COLORS.get(pk, "#475569")
        desc   = PLUGIN_DESCRIPTIONS.get(pk, "")
        anchor = pk.replace("_", "-")

        lines.append(f"## {label}")
        lines.append(f"**Chiave modulo:** `{pk}`  ")
        lines.append(f"**Commit totali:** {len(cs)}\n")

        if desc:
            lines.append(f"> {desc}\n")

        # Statistiche per anno
        by_year = {}
        for c in cs:
            y = c["date"].year if c["date"] else 0
            by_year[y] = by_year.get(y, 0) + 1
        if by_year:
            lines.append("### Attività per anno\n")
            lines.append("| Anno | Commit |")
            lines.append("|------|--------|")
            for y in sorted(by_year, reverse=True):
                bar = "█" * min(20, max(1, by_year[y] // max(1, max(by_year.values()) // 20)))
                lines.append(f"| {y} | {by_year[y]:4d}  {bar} |")
            lines.append("")

        # Statistiche per categoria
        by_cat = {}
        for c in cs:
            cat = classify_commit(c)
            by_cat[cat] = by_cat.get(cat, 0) + 1
        if by_cat:
            lines.append("### Tipi di modifica\n")
            lines.append("| Categoria | Commit | % |")
            lines.append("|-----------|--------|---|")
            total_c = len(cs)
            for cat, n in sorted(by_cat.items(), key=lambda x: -x[1]):
                pct = round(n / total_c * 100)
                lines.append(f"| {cat} | {n} | {pct}% |")
            lines.append("")

        # Top contributor
        by_author = {}
        for c in cs:
            a = c["author"]
            by_author[a] = by_author.get(a, 0) + 1
        top = sorted(by_author.items(), key=lambda x: -x[1])[:6]
        if top:
            lines.append("### Top contributor\n")
            for author, n in top:
                lines.append(f"- **{author}** — {n} commit")
            lines.append("")

        # Ultimi 20 commit significativi (feature/fix/api_change)
        notable = [c for c in reversed(cs) if classify_commit(c) in ("feature","fix","api_change")][:20]
        if notable:
            lines.append("### Commit rilevanti (ultimi 20 tra feature/fix/api)\n")
            lines.append("| Data | Tipo | Descrizione | Hash |")
            lines.append("|------|------|-------------|------|")
            for c in notable:
                d    = c["date"].strftime("%Y-%m-%d") if c["date"] else "?"
                cat  = classify_commit(c)
                subj = c["subject"][:80].replace("|", "\\|")
                h    = c["hash"][:8]
                url  = f"https://github.com/freeplane/freeplane/commit/{c['hash']}"
                lines.append(f"| {d} | `{cat}` | {subj} | [{h}]({url}) |")
            lines.append("")

        lines.append("---\n")

    # Footer con legenda categorie
    lines.append("## Legenda categorie\n")
    lines.append("| Categoria | Significato |")
    lines.append("|-----------|-------------|")
    lines.append("| `feature` | Nuova funzionalità o comportamento aggiunto |")
    lines.append("| `fix` | Correzione di bug o regressione |")
    lines.append("| `refactor` | Ristrutturazione del codice senza cambi funzionali |")
    lines.append("| `api_change` | Modifica alle interfacce pubbliche / breaking change |")
    lines.append("| `docs` | Documentazione, commenti, JavaDoc |")
    lines.append("| `test` | Test unitari o di integrazione |")
    lines.append("| `build` | Sistema di build, dipendenze, release |")
    lines.append("| `other` | Traduzioni, merge, configurazione, non classificato |")
    lines.append("")

    return "\n".join(lines)


def render_json(pm):
    def ser(o): return o.isoformat() if isinstance(o, datetime) else str(o)
    return json.dumps({
        pk: {"label": PLUGIN_LABELS.get(pk,pk), "total": len(cs),
             "commits": [{"hash":c["hash"][:8],"date":c["date"].strftime("%Y-%m-%d") if c["date"] else "?",
                          "author":c["author"],"subject":c["subject"],"category":classify_commit(c)}
                         for c in cs]}
        for pk, cs in pm.items()
    }, default=ser, indent=2, ensure_ascii=False)

def render_text(pm):
    lines = []
    for pk, cs in sorted(pm.items(), key=lambda x: -len(x[1])):
        lines += ["\n"+"="*60, f"PLUGIN: {PLUGIN_LABELS.get(pk,pk)}  ({pk})",
                  f"Commit: {len(cs)}", "="*60]
        for c in reversed(cs[-30:]):
            d = c["date"].strftime("%Y-%m-%d") if c["date"] else "?"
            lines.append(f"  {d}  [{classify_commit(c):10s}]  {c['subject'][:80]}")
        if len(cs) > 30: lines.append(f"  ... e altri {len(cs)-30}")
    return "\n".join(lines)

# ─────────────────────────────────────────────────────────────
# PER-PLUGIN DETAIL FILES
# ─────────────────────────────────────────────────────────────
NOTABLE_CATS = {"feature", "fix", "api_change"}

def render_plugin_detail_md(pk, cs):
    """Genera un file Markdown per un singolo plugin con tutti i commit
    di tipo feature, fix e api_change, raggruppati per anno."""
    from datetime import datetime as dt

    label = PLUGIN_LABELS.get(pk, pk)
    desc  = PLUGIN_DESCRIPTIONS.get(pk, "")

    # filtra solo i commit rilevanti
    notable = [c for c in cs if classify_commit(c) in NOTABLE_CATS]
    notable_sorted = sorted(notable, key=lambda c: c["date"] or dt.min, reverse=True)

    lines = []
    lines.append(f"# {label} — Commit rilevanti")
    lines.append(f"\n**Modulo:** `{pk}`  ")
    lines.append(f"**Commit rilevanti (feature / fix / api_change):** {len(notable_sorted)} "
                 f"su {len(cs)} totali\n")

    if desc:
        lines.append(f"> {desc}\n")

    lines.append(f"_Generato il {dt.now().strftime('%Y-%m-%d %H:%M')}_\n")
    lines.append("---\n")

    if not notable_sorted:
        lines.append("_Nessun commit di tipo feature, fix o api_change trovato per questo plugin._\n")
        return "\n".join(lines)

    # indice rapido per anno
    by_year = {}
    for c in notable_sorted:
        y = c["date"].year if c["date"] else 0
        by_year.setdefault(y, []).append(c)

    lines.append("## Indice per anno\n")
    for y in sorted(by_year, reverse=True):
        lines.append(f"- [{y}](#{y}) — {len(by_year[y])} commit")
    lines.append("")
    lines.append("---\n")

    # sezioni per anno
    for y in sorted(by_year, reverse=True):
        year_commits = sorted(by_year[y], key=lambda c: c["date"] or dt.min, reverse=True)
        lines.append(f"## {y}\n")
        lines.append("| Data | Tipo | Descrizione | File principali | Hash |")
        lines.append("|------|------|-------------|-----------------|------|")
        for c in year_commits:
            d    = c["date"].strftime("%Y-%m-%d") if c["date"] else "?"
            cat  = classify_commit(c)
            subj = c["subject"][:90].replace("|", "\\|")
            # mostra al massimo 2 file, abbreviando il path
            files = c.get("files", [])
            files_short = [f.split("/")[-1] for f in files[:2]]
            files_str   = ", ".join(f"`{f}`" for f in files_short)
            if len(files) > 2:
                files_str += f" +{len(files)-2}"
            h   = c["hash"][:8]
            url = f"https://github.com/freeplane/freeplane/commit/{c['hash']}"
            lines.append(f"| {d} | `{cat}` | {subj} | {files_str} | [{h}]({url}) |")

        # body dei commit (se non vuoto) come dettaglio collassabile
        with_body = [c for c in year_commits if c.get("body","").strip()]
        if with_body:
            lines.append("")
            lines.append("### Dettagli commit con note\n")
            for c in with_body:
                d    = c["date"].strftime("%Y-%m-%d") if c["date"] else "?"
                h    = c["hash"][:8]
                url  = f"https://github.com/freeplane/freeplane/commit/{c['hash']}"
                body = c["body"].strip().replace("\n", "\n> ")
                lines.append(f"**[{h}]({url})** ({d}) — {c['subject']}\n")
                lines.append(f"> {body}\n")

        lines.append("")
        lines.append("---\n")

    # legenda in fondo
    lines.append("## Legenda\n")
    lines.append("| Tipo | Significato |")
    lines.append("|------|-------------|")
    lines.append("| `feature` | Nuova funzionalità aggiunta |")
    lines.append("| `fix` | Correzione di bug o regressione |")
    lines.append("| `api_change` | Modifica alle interfacce pubbliche |")
    lines.append("")

    return "\n".join(lines)


def write_plugin_detail_files(pm, out_dir: Path):
    """Scrive un file .md per ogni plugin nella cartella out_dir/plugins/."""
    plugins_dir = out_dir / "plugins"
    plugins_dir.mkdir(parents=True, exist_ok=True)
    written = []
    for pk, cs in sorted(pm.items(), key=lambda x: -len(x[1])):
        content  = render_plugin_detail_md(pk, cs)
        filename = f"{pk}.md"
        dest     = plugins_dir / filename
        dest.write_text(content, encoding="utf-8")
        label    = PLUGIN_LABELS.get(pk, pk)
        notable  = sum(1 for c in cs if classify_commit(c) in NOTABLE_CATS)
        written.append((label, pk, notable, dest))
        print(f"      {label:30s}: {notable} commit rilevanti → {dest.name}", file=sys.stderr)
    return plugins_dir, written


# ─────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────
def main():
    p = argparse.ArgumentParser(description="Freeplane Plugin Timeline")
    p.add_argument("--repo",         required=True)
    p.add_argument("--output",       default="freeplane_plugin_timeline.html")
    p.add_argument("--format",       choices=["html","json","text","markdown"], default="html")
    p.add_argument("--since",        default=None)
    p.add_argument("--until",        default=None)
    p.add_argument("--no-per-plugin", action="store_true",
                   help="Non generare i file per-plugin (generati di default)")
    args = p.parse_args()

    repo = str(Path(args.repo).resolve())
    chk  = subprocess.run(["git","-C",repo,"rev-parse","--git-dir"], capture_output=True, text=True)
    if chk.returncode != 0:
        print(f"[ERRORE] '{repo}' non e' una repo Git valida.\ngit: {chk.stderr.strip()}", file=sys.stderr)
        sys.exit(1)

    print(f"[1/4] Lettura commit da {repo}...", file=sys.stderr)
    commits = get_all_commits(repo, args.since, args.until)
    print(f"      {len(commits)} commit totali", file=sys.stderr)

    print("[2/4] Raggruppamento per plugin...", file=sys.stderr)
    pm = build_plugin_map(commits)
    for pk, lst in sorted(pm.items(), key=lambda x: -len(x[1])):
        print(f"      {PLUGIN_LABELS.get(pk,pk):30s}: {len(lst)}", file=sys.stderr)

    print("[3/4] Scrittura report principale...", file=sys.stderr)
    content = render_html(pm, repo, args.since, args.until) if args.format=="html" \
         else render_json(pm) if args.format=="json" \
         else render_markdown(pm) if args.format=="markdown" \
         else render_text(pm)

    out = Path(args.output)
    out.write_text(content, encoding="utf-8")
    print(f"      Salvato: {out.resolve()}", file=sys.stderr)

    if not args.no_per_plugin:
        print("[4/4] Scrittura file per-plugin...", file=sys.stderr)
        plugins_dir, written = write_plugin_detail_files(pm, out.parent)
        print(f"\n  Report principale : {out.resolve()}", file=sys.stderr)
        print(f"  File per-plugin   : {plugins_dir.resolve()}/", file=sys.stderr)
        print(f"  Plugin scritti    : {len(written)}", file=sys.stderr)
    else:
        print(f"\n  Salvato: {out.resolve()}", file=sys.stderr)

if __name__ == "__main__":
    main()