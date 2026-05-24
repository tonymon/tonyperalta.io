#!/usr/bin/env python3
"""
apply-theme.py
--------------
Rewrites the inline <style> block in the DRR compliance report HTML
to match the tonyperalta.io landing page aesthetic (styles-v4.css).

Usage:
    python3 apply-theme.py                  # rewrites index.html in place
    python3 apply-theme.py path/to/report.html

Run this once after generating a new quarterly report, before pushing to GitHub.
"""

import re
import sys
import os

THEMED_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=Inter:wght@300;400;500;600&family=DM+Mono:wght@400;500&display=swap');

:root {
  --bg:       #F6F3EE;
  --bg-alt:   #EDE9E0;
  --navy:     #1A2E4A;
  --ink:      #111111;
  --ink-2:    #454545;
  --ink-3:    #888888;
  --rule:     #C9C4BB;
  --red:      #B91C1C;
  --green:    #15803D;
  --amber:    #92400E;
  --red-bg:   #FEF2F2;
  --green-bg: #F0FDF4;
  --amber-bg: #FFFBEB;
}

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

body {
  font-family: 'Inter', -apple-system, sans-serif;
  background: var(--bg);
  color: var(--ink);
  font-size: 14px;
  line-height: 1.65;
}

/* ── Header ── */
header {
  background: var(--navy);
  color: #F0ECE4;
  padding: 2rem 2.5rem;
}

header h1 {
  font-family: 'Cormorant Garamond', Georgia, serif;
  font-size: 1.85rem;
  font-weight: 500;
  letter-spacing: -0.01em;
  line-height: 1.2;
}

header p {
  font-size: 0.78rem;
  color: rgba(240,236,228,0.55);
  margin-top: 0.5rem;
  letter-spacing: 0.02em;
}

/* ── Layout ── */
.wrap { max-width: 1320px; margin: 0 auto; padding: 2rem; }

/* ── Section labels ── */
.sec {
  font-size: 0.67rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.13em;
  color: var(--ink-3);
  margin: 2.25rem 0 0.9rem;
  padding-bottom: 0.5rem;
  border-bottom: 1px solid var(--rule);
}

/* ── KPI strip ── */
.kpis {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
  gap: 0;
  margin-bottom: 1rem;
  border-top: 1px solid var(--rule);
  border-left: 1px solid var(--rule);
}

.kpi {
  background: #fff;
  padding: 1.25rem;
  border-right: 1px solid var(--rule);
  border-bottom: 1px solid var(--rule);
  border-top: 2px solid var(--navy);
  border-radius: 0;
  box-shadow: none;
}

.kpi.red   { border-top-color: var(--red); }
.kpi.green { border-top-color: var(--green); }
.kpi.amber { border-top-color: #B45309; }

.kpi .v {
  font-family: 'Cormorant Garamond', Georgia, serif;
  font-size: 2.1rem;
  font-weight: 600;
  color: var(--ink);
  line-height: 1;
}

.kpi .l {
  font-size: 0.71rem;
  font-weight: 600;
  color: var(--ink);
  margin-top: 0.4rem;
  text-transform: uppercase;
  letter-spacing: 0.07em;
}

.kpi .sub {
  font-size: 0.69rem;
  color: var(--ink-3);
  margin-top: 0.2rem;
}

/* ── Two-column grid ── */
.grid2 {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
  margin-bottom: 1rem;
}

/* ── Cards ── */
.card {
  background: #fff;
  border: 1px solid var(--rule);
  border-radius: 0;
  padding: 1.5rem;
  margin-bottom: 1rem;
  box-shadow: none;
}

.card h2 {
  font-family: 'Inter', sans-serif;
  font-size: 0.72rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--ink-3);
  margin-bottom: 1rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

/* ── Badges ── */
.bdg {
  font-size: 0.63rem;
  padding: 0.15rem 0.45rem;
  border-radius: 2px;
  font-weight: 600;
  letter-spacing: 0.05em;
}
.bdg-warn { background: var(--amber-bg); color: var(--amber); }
.bdg-good { background: var(--green-bg); color: var(--green); }
.bdg-info { background: var(--bg-alt);   color: var(--navy);  }

/* ── Charts ── */
canvas { max-height: 300px; }

/* ── Tables ── */
table { width: 100%; border-collapse: collapse; font-size: 0.79rem; }

th {
  background: var(--bg-alt);
  color: var(--ink-3);
  padding: 0.6rem 0.75rem;
  text-align: left;
  border-bottom: 1px solid var(--rule);
  font-size: 0.68rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  white-space: nowrap;
  position: sticky;
  top: 0;
}

td {
  padding: 0.55rem 0.75rem;
  border-bottom: 1px solid #EDE9E0;
  vertical-align: middle;
}

tr:hover td { background: var(--bg); }

.up { color: var(--green); font-weight: 600; }
.dn { color: var(--red);   font-weight: 600; }
.fl { color: var(--ink-3); }

/* ── Progress bars ── */
.bar-wrap { display: flex; align-items: center; gap: 6px; min-width: 100px; }
.bar-bg   { flex: 1; background: var(--rule); border-radius: 1px; height: 6px; overflow: hidden; }
.bar-fill { height: 100%; border-radius: 1px; transition: width 0.4s; }
.pct-lbl  { font-size: 0.72rem; width: 38px; text-align: right; color: var(--ink-3); }

/* ── Controls ── */
input, select {
  padding: 0.42rem 0.7rem;
  border-radius: 2px;
  border: 1px solid var(--rule);
  font-size: 0.82rem;
  background: #fff;
  font-family: 'Inter', sans-serif;
  color: var(--ink);
}
input { width: 240px; }
.ctrl { display: flex; gap: 0.5rem; margin-bottom: 0.85rem; flex-wrap: wrap; align-items: center; }

/* ── Tags ── */
.tag {
  display: inline-block;
  padding: 0.15rem 0.45rem;
  border-radius: 2px;
  font-size: 0.64rem;
  font-weight: 600;
  letter-spacing: 0.06em;
}
.tag-cfo { background: var(--navy); color: #F0ECE4; }
.tag-non { background: var(--bg-alt); color: var(--ink-3); }

/* ── Findings ── */
.finding {
  padding: 0.85rem 1.1rem;
  border-radius: 0;
  border-left: 3px solid var(--navy);
  background: rgba(26,46,74,0.04);
  margin-bottom: 0.6rem;
  font-size: 0.83rem;
  line-height: 1.65;
}
.finding.warn { border-left-color: var(--red);   background: var(--red-bg);   }
.finding.good { border-left-color: var(--green);  background: var(--green-bg); }

/* ── Footer ── */
footer {
  text-align: center;
  color: var(--ink-3);
  font-size: 0.73rem;
  padding: 2rem 1rem;
  border-top: 1px solid var(--rule);
  margin-top: 2rem;
}

@media (max-width: 800px) {
  .grid2 { grid-template-columns: 1fr; }
  .kpis  { grid-template-columns: repeat(2, 1fr); }
  header { padding: 1.5rem; }
  .wrap  { padding: 1.25rem; }
}
"""


def apply_theme(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Replace the entire <style>...</style> block
    updated, count = re.subn(
        r'<style>.*?</style>',
        f'<style>{THEMED_CSS}</style>',
        html,
        flags=re.DOTALL
    )

    if count == 0:
        print("Warning: no <style> block found — nothing changed.")
        return

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(updated)

    print(f"Theme applied to {filepath}  ({count} style block(s) replaced)")


if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else \
             os.path.join(os.path.dirname(os.path.abspath(__file__)), 'index.html')
    apply_theme(target)
