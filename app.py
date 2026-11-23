# DataFix Frontend — HACK-ELITE (FINAL LOCKED BUILD)
# Kinetic Box-to-CSV Morph + Cursor-Reactive Animation + .CSV Shield Logo + Genuine/Fake Forensics
# + CSV Formula Injection Guard (CWE-1236) + PII Masking + Audit Copilot + Schema Drift + Visual Charts + Python Export
import hashlib
import html
import io
import json
import os
import re
import textwrap
from datetime import datetime, timezone
import pandas as pd

CSS = """<style>
*{box-sizing:border-box}
body{margin:0;font-family:ui-sans-serif,system-ui,'Segoe UI',Inter,Arial,sans-serif;color:#f8fafc;background:transparent;overflow-x:hidden}

@keyframes floatSlow{
  0%,100%{transform:translateY(0px)}
  50%{transform:translateY(-6px)}
}
@keyframes hackerGlow{
  0%,100%{filter:drop-shadow(0 0 8px rgba(34,211,238,.75))}
  50%{filter:drop-shadow(0 0 18px rgba(16,185,129,.95))}
}
@keyframes fadeSlideUp{
  0%{opacity:0;transform:translateY(16px)}
  100%{opacity:1;transform:translateY(0)}
}
@keyframes ringDraw{
  from{stroke-dashoffset:263.9}
}
@keyframes barGrow{
  from{width:0}
}
@keyframes revPulse{
  0%,100%{background:rgba(245,158,11,.15);box-shadow:inset 0 0 0 1px rgba(245,158,11,.9)}
  50%{background:rgba(245,158,11,.3);box-shadow:inset 0 0 12px 1px rgba(251,191,36,1)}
}
@keyframes rowFade{
  0%{opacity:0;transform:translateX(-8px)}
  100%{opacity:1;transform:translateX(0)}
}
@keyframes scanBeam{
  0%{top:0%;opacity:.15}
  50%{top:92%;opacity:.85}
  100%{top:0%;opacity:.15}
}
@keyframes pulseDot{
  0%,100%{opacity:1;transform:scale(1)}
  50%{opacity:.3;transform:scale(.75)}
}
@keyframes dialSpinCW{
  from{transform:rotate(0deg)}
  to{transform:rotate(360deg)}
}
@keyframes dialSpinCCW{
  from{transform:rotate(360deg)}
  to{transform:rotate(0deg)}
}
@keyframes hexPulse{
  0%,100%{box-shadow:0 0 14px rgba(34,211,238,.25),inset 0 0 12px rgba(34,211,238,.12)}
  50%{box-shadow:0 0 26px rgba(16,185,129,.45),inset 0 0 18px rgba(16,185,129,.22)}
}

/* Clean Top Header */
.hero-stage{
  position:relative;
  display:flex;
  flex-direction:column;
  align-items:center;
  justify-content:center;
  text-align:center;
  padding:12px 16px 18px;
  border-bottom:1px solid rgba(34,211,238,.28);
  animation:fadeSlideUp .6s cubic-bezier(.16,1,.3,1) both;
}
.hero-stage::after{
  content:"";
  position:absolute;
  bottom:-1px;
  left:20%;
  width:60%;
  height:2px;
  background:linear-gradient(90deg,transparent,#22d3ee,#c084fc,#22d3ee,transparent);
}
.hacker-pill{
  display:inline-flex;
  align-items:center;
  gap:10px;
  padding:5px 16px;
  border-radius:999px;
  background:rgba(6,18,38,.72);
  border:1px solid rgba(34,211,238,.45);
  backdrop-filter:blur(6px);
  margin-bottom:8px;
  animation:floatSlow 3.5s ease-in-out infinite;
}
.hacker-icon{animation:hackerGlow 2.6s ease-in-out infinite;display:flex;align-items:center}
.hacker-label{
  font-family:ui-monospace,Consolas,monospace;
  font-size:12px;
  font-weight:800;
  letter-spacing:.22em;
  color:#22d3ee;
  text-transform:uppercase;
}
.hero-title{
  margin:0;
  font-size:46px;
  font-weight:900;
  letter-spacing:-.03em;
  line-height:1;
  color:#ffffff;
  text-shadow:0 4px 28px rgba(2,6,23,.95),0 0 24px rgba(34,211,238,.35);
}
.hero-title span{
  background:linear-gradient(90deg,#22d3ee,#38bdf8,#c084fc);
  -webkit-background-clip:text;
  -webkit-text-fill-color:transparent;
}
.hero-sub{
  margin:8px 0 12px;
  font-family:ui-monospace,Consolas,monospace;
  font-size:13px;
  color:#e2e8f0;
  text-shadow:0 2px 10px rgba(2,6,23,.95);
}
.pipeline-strip{
  display:flex;
  align-items:center;
  gap:8px;
  flex-wrap:wrap;
  justify-content:center;
  font-family:ui-monospace,Consolas,monospace;
  font-size:11px;
  font-weight:700;
  color:#7dd3fc;
  letter-spacing:.08em;
}
.pipeline-strip span{
  padding:3px 9px;
  border-bottom:1.5px solid rgba(34,211,238,.55);
  transition:all .2s ease;
}
.pipeline-strip span:hover{color:#ffffff;border-bottom-color:#c084fc;transform:translateY(-2px)}
.pipeline-strip i{color:#475569;font-style:normal}

/* Cyber Glass Panels */
.hud-card{
  position:relative;
  overflow:hidden;
  background:rgba(6,14,32,.76);
  backdrop-filter:blur(12px);
  -webkit-backdrop-filter:blur(12px);
  border:1px solid rgba(34,211,238,.38);
  border-left:4px solid #22d3ee;
  border-radius:12px;
  padding:20px 22px;
  box-shadow:0 16px 40px rgba(2,6,23,.72);
  animation:fadeSlideUp .55s cubic-bezier(.16,1,.3,1) both;
}
.hud-card.purple{
  border-left:1px solid rgba(192,132,252,.38);
  border-right:4px solid #c084fc;
}
.hud-card .scan-line{
  position:absolute;
  left:0;
  width:100%;
  height:2px;
  background:linear-gradient(90deg,transparent,#22d3ee,#c084fc,transparent);
  box-shadow:0 0 14px #22d3ee;
  animation:scanBeam 4.2s ease-in-out infinite;
  pointer-events:none;
}
.card-head{
  display:flex;
  justify-content:space-between;
  align-items:center;
  margin-bottom:14px;
  padding-bottom:10px;
  border-bottom:1px solid rgba(34,211,238,.24);
}
.card-title{
  font-family:ui-monospace,Consolas,monospace;
  font-size:13px;
  font-weight:800;
  letter-spacing:.14em;
  color:#22d3ee;
  text-transform:uppercase;
}
.card-title.purple{color:#d8b4fe}
.live-badge{
  display:inline-flex;
  align-items:center;
  gap:6px;
  font-family:ui-monospace,Consolas,monospace;
  font-size:11px;
  font-weight:700;
  color:#34d399;
}
.live-badge i{
  width:8px;height:8px;border-radius:50%;background:#10b981;display:inline-block;
  animation:pulseDot 1.3s infinite;
}

/* Unique Chamfered Hex-Core Genuine % Box */
.verdict-box{
  position:relative;
  display:flex;
  justify-content:space-between;
  align-items:center;
  gap:14px;
  padding:12px 16px;
  margin-bottom:12px;
  background:linear-gradient(135deg, rgba(10,24,52,.9), rgba(22,16,54,.85));
  border:1px solid rgba(34,211,238,.45);
  clip-path:polygon(12px 0%, 100% 0%, 100% calc(100% - 12px), calc(100% - 12px) 100%, 0% 100%, 0% 12px);
  animation:hexPulse 3.5s ease-in-out infinite;
}
.verdict-box.genuine{border-color:#10b981;background:linear-gradient(135deg, rgba(6,44,38,.88), rgba(10,24,52,.9))}
.verdict-box.suspicious{border-color:#f59e0b;background:linear-gradient(135deg, rgba(52,34,8,.88), rgba(10,24,52,.9))}
.verdict-box.fake{border-color:#ef4444;background:linear-gradient(135deg, rgba(56,12,18,.9), rgba(10,24,52,.9))}
.vb-sub{font-family:ui-monospace,Consolas,monospace;font-size:10px;color:#cbd5e1;letter-spacing:.1em;text-transform:uppercase}
.vb-main{font-family:ui-monospace,Consolas,monospace;font-size:16px;font-weight:900;margin-top:2px}
.vb-main.genuine{color:#34d399}
.vb-main.suspicious{color:#fbbf24}
.vb-main.fake{color:#fca5a5}

.hex-score-pod{
  position:relative;
  min-width:96px;
  padding:8px 12px;
  text-align:center;
  background:rgba(3,8,20,.92);
  border:1.5px solid #22d3ee;
  clip-path:polygon(10px 0%, calc(100% - 10px) 0%, 100% 50%, calc(100% - 10px) 100%, 10px 100%, 0% 50%);
  box-shadow:0 0 18px rgba(34,211,238,.35);
}
.hex-score-pod.genuine{border-color:#34d399;box-shadow:0 0 18px rgba(52,211,153,.4)}
.hex-score-pod.suspicious{border-color:#fbbf24;box-shadow:0 0 18px rgba(251,191,36,.4)}
.hex-score-pod.fake{border-color:#f87171;box-shadow:0 0 18px rgba(248,113,113,.45)}
.hex-score-pod .num{
  font-family:ui-monospace,Consolas,monospace;
  font-size:22px;
  font-weight:900;
  line-height:1.05;
  color:#ffffff;
  text-shadow:0 0 12px rgba(34,211,238,.75);
}
.hex-score-pod .tag{
  font-family:ui-monospace,Consolas,monospace;
  font-size:8.5px;
  font-weight:800;
  letter-spacing:.12em;
  color:#22d3ee;
  margin-top:2px;
}

.csv-logo-banner{
  display:flex;
  align-items:center;
  gap:14px;
  padding:12px 14px;
  border-radius:8px;
  background:rgba(12,26,54,.72);
  border:1px solid rgba(34,211,238,.32);
  margin-bottom:12px;
}
.csv-logo-banner h4{
  margin:0 0 3px;
  font-family:ui-monospace,Consolas,monospace;
  font-size:13px;
  font-weight:800;
  color:#ffffff;
}
.csv-logo-banner p{
  margin:0;
  font-family:ui-monospace,Consolas,monospace;
  font-size:11px;
  color:#cbd5e1;
  line-height:1.45;
}

.probe-list{display:flex;flex-direction:column;gap:8px;margin-bottom:12px}
.probe-item{
  display:flex;
  justify-content:space-between;
  align-items:center;
  padding:8px 12px;
  background:rgba(12,26,54,.68);
  border:1px solid rgba(56,189,248,.22);
  border-radius:6px;
  font-family:ui-monospace,Consolas,monospace;
  font-size:11.5px;
}
.probe-tag{
  padding:2px 8px;
  border-radius:4px;
  font-size:10px;
  font-weight:800;
  letter-spacing:.08em;
}
.probe-tag.ok{background:rgba(16,185,129,.22);color:#34d399;border:1px solid rgba(52,211,153,.4)}
.probe-tag.warn{background:rgba(245,158,11,.22);color:#fbbf24;border:1px solid rgba(251,191,36,.4)}
.probe-tag.bad{background:rgba(239,68,68,.24);color:#fca5a5;border:1px solid rgba(248,113,113,.45)}
.probe-tag.scan{background:rgba(34,211,238,.22);color:#22d3ee;border:1px solid rgba(34,211,238,.4)}
.probe-tag.purple{background:rgba(192,132,252,.22);color:#e9d5ff;border:1px solid rgba(192,132,252,.45)}

.detect-terminal{
  background:rgba(3,8,20,.86);
  border:1px solid rgba(34,211,238,.25);
  border-radius:8px;
  padding:10px 14px;
  font-family:ui-monospace,Consolas,monospace;
  font-size:11px;
  line-height:1.68;
  color:#94a3b8;
}
.detect-terminal span{color:#22d3ee;font-weight:700}
.detect-terminal em{color:#c084fc;font-style:normal;font-weight:700}

/* Copilot Response Card */
.copilot-box{
  background:rgba(6,16,36,.84);
  border:1px solid rgba(34,211,238,.45);
  border-left:4px solid #c084fc;
  border-radius:10px;
  padding:14px 16px;
  font-family:ui-monospace,Consolas,monospace;
  font-size:12.5px;
  line-height:1.65;
  color:#f1f5f9;
  margin-top:8px;
}
.copilot-box b{color:#22d3ee}
.copilot-box em{color:#fbbf24;font-style:normal;font-weight:700}

/* Floating Telemetry Ribbon */
.hud-metrics-strip{
  display:grid;
  grid-template-columns:repeat(5,1fr);
  gap:14px;
  padding:6px 2px;
}
.metric-node{
  position:relative;
  padding:11px 14px;
  border-left:3px solid #22d3ee;
  background:linear-gradient(90deg,rgba(10,24,52,.72),rgba(10,24,52,.28));
  backdrop-filter:blur(8px);
  border-radius:0 8px 8px 0;
  opacity:0;
  animation:fadeSlideUp .5s cubic-bezier(.16,1,.3,1) forwards;
  transition:transform .22s ease,background .22s ease;
}
.metric-node:nth-child(1){animation-delay:.05s;border-left-color:#38bdf8}
.metric-node:nth-child(2){animation-delay:.10s;border-left-color:#f87171}
.metric-node:nth-child(3){animation-delay:.15s;border-left-color:#34d399}
.metric-node:nth-child(4){animation-delay:.20s;border-left-color:#fbbf24}
.metric-node:nth-child(5){animation-delay:.25s;border-left-color:#c084fc}
.metric-node:hover{transform:translateX(4px);background:linear-gradient(90deg,rgba(34,211,238,.25),rgba(10,24,52,.45))}
.m-top{display:flex;align-items:center;gap:8px;font-family:ui-monospace,Consolas,monospace;font-size:11px;font-weight:700;letter-spacing:.12em;color:#94a3b8;text-transform:uppercase}
.m-code{padding:1px 6px;border-radius:3px;font-size:10px}
.m-code.blue{background:rgba(56,189,248,.22);color:#38bdf8}
.m-code.red{background:rgba(248,113,113,.22);color:#f87171}
.m-code.green{background:rgba(52,211,153,.22);color:#34d399}
.m-code.amber{background:rgba(251,191,36,.22);color:#fbbf24}
.m-code.purple{background:rgba(192,132,252,.22);color:#d8b4fe}
.m-val{font-size:28px;font-weight:900;color:#ffffff;line-height:1.1;margin:4px 0;font-family:ui-monospace,Consolas,monospace;text-shadow:0 2px 16px rgba(2,6,23,.9)}
.m-detail{font-size:11.5px;font-weight:600}
.m-detail.blue{color:#38bdf8}.m-detail.red{color:#f87171}.m-detail.green{color:#34d399}.m-detail.amber{color:#fbbf24}.m-detail.purple{color:#d8b4fe}

/* Unique Cyber-Radar % Dial & Rule Progress Stream */
.telemetry-flow{
  display:flex;
  align-items:center;
  gap:20px;
  flex-wrap:wrap;
  background:rgba(6,14,32,.72);
  backdrop-filter:blur(10px);
  border:1px solid rgba(34,211,238,.3);
  border-radius:12px;
  padding:16px 20px;
  animation:fadeSlideUp .55s cubic-bezier(.16,1,.3,1) both;
}
.cyber-dial{
  position:relative;
  display:flex;
  flex-direction:column;
  align-items:center;
  padding:10px 12px 8px;
  border-radius:14px;
  background:radial-gradient(circle at 50% 45%, rgba(16,36,74,.72), rgba(4,10,26,.85));
  border:1px solid rgba(34,211,238,.32);
  box-shadow:0 8px 24px rgba(2,6,23,.75), inset 0 0 18px rgba(34,211,238,.08);
  transition:transform .25s ease, border-color .25s ease;
}
.cyber-dial:hover{
  transform:translateY(-3px) scale(1.04);
  border-color:#22d3ee;
}
.cyber-dial .orbit-cw{
  transform-origin:60px 60px;
  animation:dialSpinCW 18s linear infinite;
}
.cyber-dial .orbit-ccw{
  transform-origin:60px 60px;
  animation:dialSpinCCW 12s linear infinite;
}
.ring-prog{animation:ringDraw 1.15s cubic-bezier(.22,1,.36,1) forwards}
.cyber-dial .rl{
  margin-top:4px;
  padding:2px 10px;
  border-radius:999px;
  background:rgba(12,26,54,.85);
  border:1px solid rgba(34,211,238,.35);
  font-family:ui-monospace,Consolas,monospace;
  font-size:10px;
  font-weight:800;
  letter-spacing:.14em;
  color:#e2e8f0;
  text-transform:uppercase;
}
.arrow{font-size:24px;color:#22d3ee;font-weight:800}
.bars{flex:1;min-width:220px;display:flex;flex-direction:column;gap:10px}
.bar-row{display:flex;flex-direction:column;gap:4px}
.bar-head{display:flex;justify-content:space-between;font-size:12px;color:#f1f5f9;font-weight:600}
.bar-track{height:6px;background:rgba(15,29,56,.85);border-radius:999px;overflow:hidden}
.bar-fill{height:100%;border-radius:999px;animation:barGrow 1s cubic-bezier(.22,1,.36,1) forwards}

/* Translucent Diff & Audit Matrix */
.legend{
  display:flex;gap:18px;flex-wrap:wrap;font-size:12px;color:#e2e8f0;
  padding:6px 4px;margin:0 0 8px;
}
.legend span{display:inline-flex;align-items:center;gap:6px;font-weight:600}
.sw{width:12px;height:12px;border-radius:2px;display:inline-block}
.wrap{
  overflow:auto;max-height:560px;
  border:1px solid rgba(34,211,238,.38);
  border-radius:10px;
  background:rgba(4,10,24,.76);
  backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);
  animation:fadeSlideUp .5s ease-out both;
}
table{border-collapse:collapse;width:100%;font-family:ui-monospace,SFMono-Regular,Consolas,monospace;font-size:13px;color:#f8fafc}
th{
  position:sticky;top:0;background:rgba(8,18,40,.94);color:#22d3ee;
  text-align:left;padding:11px 13px;font-weight:700;
  border-bottom:1px solid rgba(34,211,238,.35);z-index:2;
  text-transform:uppercase;font-size:11px;letter-spacing:.08em;
}
tbody tr{animation:rowFade .3s ease both;transition:background .15s ease}
tbody tr:nth-child(1){animation-delay:.02s}tbody tr:nth-child(2){animation-delay:.04s}
tbody tr:nth-child(3){animation-delay:.06s}tbody tr:nth-child(4){animation-delay:.08s}
tbody tr:nth-child(5){animation-delay:.10s}tbody tr:nth-child(6){animation-delay:.12s}
tbody tr:nth-child(7){animation-delay:.14s}tbody tr:nth-child(8){animation-delay:.16s}
tbody tr:nth-child(9){animation-delay:.18s}tbody tr:nth-child(10){animation-delay:.20s}
td{padding:9px 13px;border-top:1px solid rgba(34,211,238,.12);white-space:nowrap}
tbody tr:hover td{background:rgba(34,211,238,.14)}
td.idx{color:#64748b;font-weight:700}
.nul{color:#64748b;font-style:italic}
td.bad{background:rgba(239,68,68,.24);color:#fca5a5;font-weight:700}
tr.dup td{background:rgba(239,68,68,.14)}
tr.rm td{color:#64748b;text-decoration:line-through;background:rgba(4,8,20,.65)}
td.chg{background:rgba(16,185,129,.22)}td.chg.medium{background:rgba(245,158,11,.22)}
td.chg s{color:#94a3b8}td.chg i{color:#22d3ee;font-style:normal;margin:0 5px}
td.chg b{color:#34d399}td.chg.medium b{color:#fbbf24}
td.rev{color:#fbbf24;font-weight:700;animation:revPulse 2.3s ease-in-out infinite}
.pill-conf{display:inline-block;padding:2px 8px;border-radius:3px;font-size:11px;font-weight:700;text-transform:uppercase}
.pill-conf.high{background:rgba(16,185,129,.25);color:#34d399}
.pill-conf.medium{background:rgba(245,158,11,.25);color:#fbbf24}
</style>"""

COUNT_UP_JS = """<script>
document.querySelectorAll('[data-count-to]').forEach(el => {
  const target = parseFloat(el.getAttribute('data-count-to'));
  const suffix = el.getAttribute('data-suffix') || '';
  const decimals = (el.getAttribute('data-count-to').split('.')[1] || '').length;
  const dur = 850;
  const start = performance.now();
  function step(now) {
    const t = Math.min(1, (now - start) / dur);
    const ease = 1 - Math.pow(1 - t, 3);
    const val = (target * ease).toFixed(decimals);
    el.textContent = (decimals === 0 ? Number(val).toLocaleString() : val) + suffix;
    if (t < 1) requestAnimationFrame(step);
  }
  requestAnimationFrame(step);
});
</script>"""


def _csv_logo_svg(size=28):
    """Animated .CSV File & Integrity Shield Emblem."""
    return (
        f'<span class="hacker-icon">'
        f'<svg viewBox="0 0 64 64" width="{size}" height="{size}">'
        '  <defs>'
        '    <linearGradient id="csvG" x1="0%" y1="0%" x2="100%" y2="100%">'
        '      <stop offset="0%" stop-color="#22d3ee"/>'
        '      <stop offset="100%" stop-color="#c084fc"/>'
        '    </linearGradient>'
        '  </defs>'
        '  <path d="M14 6 H40 L52 18 V54 C52 56.2 50.2 58 48 58 H14 C11.8 58 10 56.2 10 54 V10 C10 7.8 11.8 6 14 6 Z" '
        '        fill="rgba(34,211,238,0.16)" stroke="url(#csvG)" stroke-width="2.6" stroke-linejoin="round"/>'
        '  <path d="M40 6 V18 H52" fill="none" stroke="#22d3ee" stroke-width="2.4" stroke-linejoin="round"/>'
        '  <rect x="16" y="23" width="13" height="6" rx="1.5" fill="rgba(34,211,238,0.3)" stroke="#22d3ee" stroke-width="1.3"/>'
        '  <rect x="32" y="23" width="14" height="6" rx="1.5" fill="rgba(192,132,252,0.2)" stroke="#c084fc" stroke-width="1.3"/>'
        '  <rect x="16" y="32" width="13" height="6" rx="1.5" fill="rgba(192,132,252,0.2)" stroke="#c084fc" stroke-width="1.3"/>'
        '  <rect x="32" y="32" width="14" height="6" rx="1.5" fill="rgba(34,211,238,0.3)" stroke="#22d3ee" stroke-width="1.3"/>'
        '  <rect x="15" y="42" width="32" height="11" rx="2.5" fill="#22d3ee"/>'
        '  <text x="31" y="50.5" text-anchor="middle" font-family="ui-monospace,Consolas,monospace" font-size="8.5" font-weight="900" fill="#030712" letter-spacing="1.2">CSV</text>'
        '  <circle cx="50" cy="48" r="9" fill="#030712" stroke="#10b981" stroke-width="2.2"/>'
        '  <path d="M46.5 48.2 L49 50.8 L54 45.5" fill="none" stroke="#34d399" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>'
        '</svg>'
        '</span>'
    )


def _generate_fake_demo_csv():
    """Synthetic/spoofed CSV dataset with formula injection payload to demonstrate Genuine vs Fake & CWE-1236 Guard."""
    lines = [
        "id,name,age,city,phone,signup_date",
        "101,test1,999,dummy,12345,2026-01-10",
        "102,user1,-15,asdf,00000,15/02/2026",
        "103,dummy,250,fake,999999,2026-03-01",
        "103,dummy,250,fake,999999,2026-03-01",
        "104,=CMD|' /C calc'!A0,0,xxx,11111,invalid_date",
        "105,sample1,180,none,22222,2026-04-12",
    ]
    raw_text = "\n".join(lines) + "\n"
    raw_bytes = raw_text.encode("utf-8")
    return "fake_spoofed_demo.csv", raw_bytes, raw_text, pd.read_csv(io.BytesIO(raw_bytes))


def _is_formula_injection(val):
    """Detect CWE-1236 CSV / Spreadsheet Formula Injection payloads."""
    if pd.isna(val):
        return False
    s = str(val).strip()
    if not s:
        return False
    if s[0] in ("=", "@"):
        return True
    if s[0] in ("+", "-") and not re.match(r"^[+-]?\d+(\.\d+)?$", s) and not re.match(r"^\+91[-\s]?\d+$", s):
        return True
    return False


def analyze_csv_authenticity(raw_bytes, raw_text, df):
    """Verify whether the uploaded CSV is GENUINE, SUSPICIOUS, or FAKE / CORRUPT + CWE-1236 Formula Check."""
    sha256 = hashlib.sha256(raw_bytes).hexdigest()[:16].upper()
    signals = []
    score = 100

    magic_sigs = [
        (b"PK\x03\x04", "XLSX / ZIP archive renamed to .csv"),
        (b"%PDF", "PDF binary renamed to .csv"),
        (b"\x89PNG", "PNG image renamed to .csv"),
        (b"MZ", "Executable binary renamed to .csv"),
    ]
    spoofed = next((desc for sig, desc in magic_sigs if raw_bytes.startswith(sig)), None)
    if spoofed or (b"\x00" in raw_bytes[:4096]):
        score -= 65
        signals.append(("File Magic-Bytes", spoofed or "Binary null-bytes detected in CSV", "bad"))
    else:
        signals.append(("File Magic-Bytes", "Valid UTF-8 / ASCII CSV text stream", "ok"))

    inj_count = 0
    for col in df.columns:
        inj_count += sum(1 for v in df[col] if _is_formula_injection(v))
    if inj_count > 0:
        score -= min(35, inj_count * 18)
        signals.append(("Formula Injection (CWE-1236)", f"{inj_count} executable formula payload(s) detected", "bad"))
    else:
        signals.append(("Formula Injection (CWE-1236)", "Zero malicious spreadsheet formulas", "ok"))

    lines = [ln for ln in raw_text.splitlines() if ln.strip()]
    if len(lines) < 2:
        score -= 40
        signals.append(("CSV Structure", "Empty or header-only CSV (< 2 rows)", "bad"))
    else:
        expected_cols = len(lines[0].split(","))
        mismatched = sum(1 for ln in lines[1:] if len(ln.split(",")) != expected_cols)
        if mismatched == 0:
            signals.append(("CSV Structure", f"Consistent {expected_cols} columns across {len(lines)} lines", "ok"))
        else:
            score -= min(30, mismatched * 6)
            signals.append(("CSV Structure", f"{mismatched} row(s) have broken column counts", "warn"))

    dummy_cols = 0
    for col in df.columns:
        vals = df[col].dropna().astype(str).str.strip().tolist()
        if not vals:
            continue
        synth = sum(
            1 for v in vals
            if re.match(r"^(test|user|sample|dummy|fake|temp|asdf|qwerty|xxx|none|n/a)\d*$", v.lower())
        )
        if synth >= max(2, int(len(vals) * 0.25)):
            dummy_cols += 1
    if dummy_cols > 0:
        score -= min(45, dummy_cols * 20)
        signals.append(("Synthetic Data Check", f"{dummy_cols} column(s) contain fake/dummy placeholders", "bad"))
    else:
        signals.append(("Synthetic Data Check", "Authentic non-synthetic field patterns", "ok"))

    dup_cnt = int(df.duplicated().sum())
    if dup_cnt > 0:
        score -= min(18, dup_cnt * 6)
        signals.append(("Record Uniqueness", f"{dup_cnt} duplicate row(s) found", "warn"))
    else:
        signals.append(("Record Uniqueness", "100% unique row signatures", "ok"))

    score = max(0, min(100, score))
    if score >= 75:
        verdict, tone = "GENUINE CSV FILE", "genuine"
    elif score >= 45:
        verdict, tone = "SUSPICIOUS / NOISY CSV", "suspicious"
    else:
        verdict, tone = "FAKE / CORRUPTED CSV", "fake"

    return {
        "verdict": verdict,
        "tone": tone,
        "score": score,
        "sha256": sha256,
        "size_kb": round(len(raw_bytes) / 1024, 2),
        "inj_count": inj_count,
        "signals": signals,
    }


def apply_security_and_pii_guards(df, mask_pii=False, neutralize_formulas=True):
    """PII Scanner/Masker (GDPR/DPDP) + CSV Formula Injection Neutralizer (CWE-1236)."""
    email_re = re.compile(r"^([A-Za-z0-9._%+-])[A-Za-z0-9._%+-]*(@[A-Za-z0-9.-]+\.[A-Za-z]{2,})$")
    phone_re = re.compile(r"^(\+91[-\s]?)?[6-9]\d{9}$")
    aadhaar_re = re.compile(r"^\d{4}[\s-]?\d{4}[\s-]?\d{4}$")
    pan_re = re.compile(r"^[A-Z]{5}\d{4}[A-Z]$")

    out_df = df.copy()
    pii_counts = {"Emails": 0, "Phones": 0, "Aadhaar/PAN IDs": 0}
    neutralized_count = 0

    for col in out_df.columns:
        for idx in out_df.index:
            val = out_df.at[idx, col]
            if pd.isna(val):
                continue
            s = str(val).strip()

            if _is_formula_injection(s):
                if neutralize_formulas:
                    out_df.at[idx, col] = f"'{s}"
                    neutralized_count += 1
                continue

            m_email = email_re.match(s)
            if m_email:
                pii_counts["Emails"] += 1
                if mask_pii:
                    out_df.at[idx, col] = f"{m_email.group(1)}****{m_email.group(2)}"
                continue
            if phone_re.match(s):
                pii_counts["Phones"] += 1
                if mask_pii:
                    digits = re.sub(r"\D", "", s)
                    prefix = "+91-" if len(digits) == 12 else ""
                    out_df.at[idx, col] = f"{prefix}XXXXXX{digits[-4:]}"
                continue
            if aadhaar_re.match(s) or pan_re.match(s):
                pii_counts["Aadhaar/PAN IDs"] += 1
                if mask_pii:
                    out_df.at[idx, col] = f"XXXX-XXXX-{s[-4:]}"

    total_pii = sum(pii_counts.values())
    return out_df, total_pii, pii_counts, neutralized_count


def apply_rule_filters_and_reverts(raw_df, base_clean_df, base_log, base_review, rules_enabled, reverted_ids):
    """Reconstruct clean_df & active log based on toggled sidebar rules and reverted fixes."""
    if base_log.empty:
        return base_clean_df.copy(), base_log.copy(), base_review.copy()

    def _rule_allowed(rec):
        col = str(rec["column"]).lower()
        reason = str(rec["reason"]).lower()
        if col == "(whole row)" or "duplicate" in reason:
            return rules_enabled["dedupe"]
        if "city" in col or "city" in reason:
            return rules_enabled["city"]
        if "date" in col or "iso" in reason or "date" in reason:
            return rules_enabled["date"]
        if "phone" in col or "mobile" in col or "digit" in reason:
            return rules_enabled["phone"]
        return True

    kept_indices = [
        idx for idx, rec in base_log.iterrows()
        if idx not in reverted_ids and _rule_allowed(rec)
    ]
    active_log = base_log.loc[kept_indices].copy()

    rebuilt_df = raw_df.copy()
    rows_to_drop = []
    for _, rec in active_log.iterrows():
        r_idx = rec["row"]
        col = rec["column"]
        if col == "(whole row)":
            if r_idx in rebuilt_df.index:
                rows_to_drop.append(r_idx)
        else:
            if r_idx in rebuilt_df.index and col in rebuilt_df.columns:
                rebuilt_df.at[r_idx, col] = rec["new"]

    if rows_to_drop:
        rebuilt_df = rebuilt_df.drop(index=rows_to_drop)

    return rebuilt_df, active_log, base_review.copy()


def build_column_health_df(raw_df, clean_df):
    """Before-vs-After Column Health & Schema Profiler."""
    rows = []
    total_before = max(1, len(raw_df))
    total_after = max(1, len(clean_df))
    for col in raw_df.columns:
        nulls_before = int(raw_df[col].isna().sum())
        nulls_after = int(clean_df[col].isna().sum()) if col in clean_df.columns else 0
        uniq_after = int(clean_df[col].nunique(dropna=True)) if col in clean_df.columns else 0
        dtype_str = str(clean_df[col].dtype) if col in clean_df.columns else str(raw_df[col].dtype)
        health_before = round(100.0 * (total_before - nulls_before) / total_before, 1)
        health_after = round(100.0 * (total_after - nulls_after) / total_after, 1)
        rows.append({
            "column": col,
            "inferred_type": dtype_str,
            "unique_values": uniq_after,
            "nulls_before": nulls_before,
            "nulls_after": nulls_after,
            "health_before_%": f"{health_before}%",
            "health_after_%": f"{health_after}%",
        })
    return pd.DataFrame(rows)


def compute_schema_drift(baseline_df, current_df):
    """Cross-CSV Schema Drift Detector comparing a baseline master CSV against the incoming CSV."""
    base_cols = set(baseline_df.columns)
    curr_cols = set(current_df.columns)
    missing_cols = sorted(base_cols - curr_cols)
    new_cols = sorted(curr_cols - base_cols)
    shared_cols = sorted(base_cols & curr_cols)

    drift_rows = []
    for col in shared_cols:
        b_type = str(baseline_df[col].dtype)
        c_type = str(current_df[col].dtype)
        b_null = round(100.0 * baseline_df[col].isna().mean(), 1)
        c_null = round(100.0 * current_df[col].isna().mean(), 1)
        status = "STABLE"
        if b_type != c_type:
            status = "TYPE DRIFT"
        elif abs(c_null - b_null) >= 15.0:
            status = "NULL SPIKE"
        drift_rows.append({
            "column": col,
            "baseline_type": b_type,
            "incoming_type": c_type,
            "baseline_null_%": f"{b_null}%",
            "incoming_null_%": f"{c_null}%",
            "drift_status": status,
        })
    for col in missing_cols:
        drift_rows.append({
            "column": col,
            "baseline_type": str(baseline_df[col].dtype),
            "incoming_type": "MISSING",
            "baseline_null_%": "—",
            "incoming_null_%": "100%",
            "drift_status": "DROPPED COLUMN",
        })
    for col in new_cols:
        drift_rows.append({
            "column": col,
            "baseline_type": "ABSENT",
            "incoming_type": str(current_df[col].dtype),
            "baseline_null_%": "—",
            "incoming_null_%": f"{round(100.0 * current_df[col].isna().mean(), 1)}%",
            "drift_status": "NEW COLUMN",
        })
    return pd.DataFrame(drift_rows), missing_cols, new_cols


def answer_audit_copilot(query, fname, forensic_info, before_score, after_score, log_df, review_df, total_pii, pii_counts, pii_masked, neutralized_count):
    """Deterministic Audit Copilot grounded 100% in actual forensic & audit records."""
    q = query.strip().lower()
    if not q:
        return "Ask a question about authenticity, formula injection security, flagged rows, repaired columns, or PII exposure."

    if "inject" in q or "formula" in q or "security" in q or "cmd" in q or "exploit" in q:
        inj = forensic_info["inj_count"]
        if inj == 0:
            return f"<b>Formula Injection Guard (CWE-1236):</b> Zero executable spreadsheet formulas found in <b>{html.escape(fname)}</b>."
        status = f"DEFANGED ({neutralized_count} cell(s) escaped with leading apostrophe)" if neutralized_count > 0 else "ACTIVE THREAT (enable 'Neutralize Formula Payloads' in sidebar)"
        return (
            f"<b>Formula Injection Alert (CWE-1236):</b> Detected <em>{inj}</em> executable formula payload(s) in <b>{html.escape(fname)}</b>.<br>"
            f"<b>Shield Status:</b> <b>{status}</b>."
        )

    if "fake" in q or "genuine" in q or "authentic" in q or "spoof" in q:
        sig_summary = "; ".join(f"{k}: {v}" for k, v, _ in forensic_info["signals"])
        return (
            f"<b>Authenticity Verdict for {html.escape(fname)}:</b> <em>{html.escape(forensic_info['verdict'])}</em> "
            f"(Score: <b>{forensic_info['score']}%</b>, SHA-256: <b>{forensic_info['sha256']}</b>).<br>"
            f"<b>Forensic Breakdown:</b> {html.escape(sig_summary)}."
        )

    if "pii" in q or "privacy" in q or "mask" in q or "gdpr" in q or "sensitive" in q:
        detail = ", ".join(f"{k}: {v}" for k, v in pii_counts.items())
        state = "MASKED for export" if pii_masked else "UNMASKED (toggle 'Mask PII Before Export' in sidebar to anonymize)"
        return (
            f"<b>PII Compliance Scan:</b> Detected <em>{total_pii}</em> sensitive field(s) ({html.escape(detail)}).<br>"
            f"<b>Current Export Status:</b> <b>{state}</b>."
        )

    if "flag" in q or "review" in q or "human" in q or "untouched" in q:
        if review_df.empty:
            return f"<b>Human Review Queue:</b> Zero cells in <b>{html.escape(fname)}</b> required manual review."
        items = [
            f"Row {r.row} [<b>{html.escape(str(r.column))}</b>] = <em>{html.escape(str(r.value))}</em> ({html.escape(str(r.why))})"
            for r in review_df.head(5).itertuples(index=False)
        ]
        return (
            f"<b>Why {len(review_df)} cell(s) were held for Human Review (Zero-Guess Policy):</b><br>• "
            + "<br>• ".join(items)
        )

    if "column" in q or "fix" in q or "change" in q or "most" in q or "repair" in q:
        if log_df.empty:
            return f"<b>Repair Summary:</b> No automatic repairs were applied to <b>{html.escape(fname)}</b>."
        top_col = log_df["column"].value_counts().idxmax()
        top_cnt = int(log_df["column"].value_counts().max())
        return (
            f"<b>Repair Telemetry:</b> Applied <b>{len(log_df)}</b> verified change(s), boosting quality from "
            f"<em>{before_score}%</em> to <b>{after_score}%</b>. Most repaired target: <b>{html.escape(str(top_col))}</b> ({top_cnt} fix(es))."
        )

    return (
        f"<b>Executive Audit Summary ({html.escape(fname)}):</b><br>"
        f"• <b>Authenticity:</b> {html.escape(forensic_info['verdict'])} ({forensic_info['score']}%)<br>"
        f"• <b>Security Guard:</b> {forensic_info['inj_count']} formula payload(s) detected ({neutralized_count} neutralized)<br>"
        f"• <b>Data Quality:</b> {before_score}% &rarr; <b>{after_score}%</b> ({len(log_df)} repairs, {len(review_df)} flagged)<br>"
        f"• <b>PII Exposure:</b> {total_pii} sensitive cell(s) ({'Masked' if pii_masked else 'Unmasked'})"
    )


def generate_standalone_python_script(fname, rules_enabled, pii_masked, neutralize_formulas):
    """Generate a reproducible zero-dependency Python pipeline script matching current UI settings."""
    return textwrap.dedent(f'''\
        #!/usr/bin/env python3
        """
        DataFix Reproducible Cleaning, Security & PII Compliance Pipeline
        Generated for: {fname}
        Active Rules: {json.dumps(rules_enabled)}
        PII Masking Enabled: {pii_masked}
        Neutralize Formula Injection (CWE-1236): {neutralize_formulas}
        """
        import re
        import pandas as pd
        import cleaner

        INPUT_CSV = "{fname}"
        OUTPUT_CSV = "cleaned_{fname}"

        def apply_guards(df: pd.DataFrame) -> pd.DataFrame:
            email_re = re.compile(r"^([A-Za-z0-9._%+-])[A-Za-z0-9._%+-]*(@[A-Za-z0-9.-]+\\.[A-Za-z]{{2,}})$")
            phone_re = re.compile(r"^(\\+91[-\\s]?)?[6-9]\\d{{9}}$")
            out = df.copy()
            for col in out.columns:
                for idx in out.index:
                    val = out.at[idx, col]
                    if pd.isna(val):
                        continue
                    s = str(val).strip()
                    if {neutralize_formulas} and s and s[0] in ("=", "@"):
                        out.at[idx, col] = "'" + s
                        continue
                    if {pii_masked}:
                        m = email_re.match(s)
                        if m:
                            out.at[idx, col] = f"{{m.group(1)}}****{{m.group(2)}}"
                        elif phone_re.match(s):
                            digits = re.sub(r"\\D", "", s)
                            prefix = "+91-" if len(digits) == 12 else ""
                            out.at[idx, col] = f"{{prefix}}XXXXXX{{digits[-4:]}}"
            return out

        def run():
            raw_df = pd.read_csv(INPUT_CSV)
            clean_df, audit_log, review_queue = cleaner.clean(raw_df)
            clean_df = apply_guards(clean_df)
            clean_df.to_csv(OUTPUT_CSV, index=False)
            audit_log.to_csv("audit_log_" + INPUT_CSV, index=False)
            print(f"Saved {{OUTPUT_CSV}} ({{len(clean_df)}} rows) | Flagged for review: {{len(review_queue)}}")

        if __name__ == "__main__":
            run()
    ''').encode("utf-8")


def build_audit_certificate_json(
    fname, operator, forensic_info, before_score, after_score, active_log, review_df, rules_enabled, reverted_ids, total_pii, pii_masked, neutralized_count
):
    """Downloadable Cryptographic JSON Audit Certificate."""
    payload = {
        "certificate_type": "DataFix Autonomous CSV Integrity, Security & Audit Certificate",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "operator": operator,
        "target_file": {
            "filename": fname,
            "sha256_prefix": forensic_info["sha256"],
            "size_kb": forensic_info["size_kb"],
            "authenticity_verdict": forensic_info["verdict"],
            "authenticity_score": forensic_info["score"],
            "forensic_checks": [
                {"check": k, "detail": v, "status": t} for k, v, t in forensic_info["signals"]
            ],
        },
        "security_and_compliance": {
            "cwe_1236_formula_payloads_detected": forensic_info["inj_count"],
            "cwe_1236_payloads_neutralized": neutralized_count,
            "pii_sensitive_cells_detected": total_pii,
            "pii_masked_in_export": pii_masked,
        },
        "quality_metrics": {
            "before_quality_score": before_score,
            "after_quality_score": after_score,
            "net_improvement": round(after_score - before_score, 2),
        },
        "active_rule_policy": rules_enabled,
        "reverted_fix_count": len(reverted_ids),
        "applied_repairs": active_log.to_dict(orient="records") if not active_log.empty else [],
        "human_review_queue": review_df.to_dict(orient="records") if not review_df.empty else [],
    }
    return json.dumps(payload, indent=2, default=str).encode("utf-8")


def _ensure_dark_theme():
    """Force Streamlit's native theme config to dark obsidian."""
    cfg_dir = ".streamlit"
    cfg_path = os.path.join(cfg_dir, "config.toml")
    desired = textwrap.dedent("""\
        [theme]
        base = "dark"
        primaryColor = "#06b6d4"
        backgroundColor = "#040916"
        secondaryBackgroundColor = "#071024"
        textColor = "#f8fafc"
        font = "sans serif"
    """)
    try:
        os.makedirs(cfg_dir, exist_ok=True)
        with open(cfg_path, "w", encoding="utf-8") as f:
            f.write(desired)
    except Exception:
        pass


def _inject_center_csv_and_canvas():
    """Inject Interactive Cursor-Reactive Canvas + Portfolio Box-to-Full-Screen Morph + .CSV Shield Emblem."""
    import streamlit as st
    import streamlit.components.v1 as components

    global_css = textwrap.dedent("""\
        <style>
        .stApp, [data-testid="stAppViewContainer"], [data-testid="stMain"],
        header[data-testid="stHeader"], [data-testid="stToolbar"], [data-testid="stDecoration"] {
          background: transparent !important;
          color: #f8fafc !important;
        }
        body {
          background-color: #030712 !important;
        }
        [data-testid="stMain"] .block-container {
          position: relative;
          z-index: 2;
          padding-top: 1rem;
          max-width: 1440px;
        }

        /* Tactical Cyber-Neural Sidebar */
        [data-testid="stSidebar"] {
          background: linear-gradient(180deg, rgba(6, 15, 36, 0.92) 0%, rgba(11, 14, 38, 0.94) 55%, rgba(5, 11, 26, 0.96) 100%) !important;
          backdrop-filter: blur(14px);
          border-right: 1px solid rgba(34, 211, 238, 0.38);
          box-shadow: 6px 0 32px rgba(2, 6, 23, 0.85);
          z-index: 3;
        }
        [data-testid="stSidebar"] * { color: #e2e8f0; }

        [data-testid="stSidebar"] [role="radiogroup"] {
          display: flex;
          flex-direction: column;
          gap: 7px;
        }
        [data-testid="stSidebar"] [role="radiogroup"] label {
          background: rgba(12, 26, 56, 0.65) !important;
          border: 1px solid rgba(56, 189, 248, 0.25) !important;
          border-left: 3px solid rgba(56, 189, 248, 0.45) !important;
          border-radius: 8px !important;
          padding: 8px 12px !important;
          margin: 0 !important;
          font-family: ui-monospace, Consolas, monospace !important;
          font-size: 12px !important;
          font-weight: 600 !important;
          transition: all 0.2s ease !important;
        }
        [data-testid="stSidebar"] [role="radiogroup"] label:hover {
          background: rgba(14, 116, 144, 0.35) !important;
          border-color: #22d3ee !important;
          transform: translateX(3px);
        }
        [data-testid="stSidebar"] [role="radiogroup"] label:has(input:checked) {
          background: linear-gradient(90deg, rgba(6, 182, 212, 0.28), rgba(139, 92, 246, 0.22)) !important;
          border-color: #22d3ee !important;
          border-left: 4px solid #22d3ee !important;
          box-shadow: 0 0 16px rgba(34, 211, 238, 0.25);
        }

        .sb-operator-card {
          position: relative;
          overflow: hidden;
          background: linear-gradient(135deg, rgba(14, 32, 68, 0.85), rgba(30, 20, 62, 0.8));
          border: 1px solid rgba(34, 211, 238, 0.42);
          border-top: 3px solid #22d3ee;
          border-radius: 10px;
          padding: 13px 14px;
          margin-bottom: 12px;
          box-shadow: 0 8px 24px rgba(2, 6, 23, 0.65);
        }
        .sb-op-top { display: flex; align-items: center; gap: 10px; margin-bottom: 8px; }
        .sb-op-title { font-family: ui-monospace, Consolas, monospace; font-size: 15px; font-weight: 900; color: #ffffff; letter-spacing: 0.04em; }
        .sb-op-title span { color: #22d3ee; }
        .sb-op-sub { font-family: ui-monospace, Consolas, monospace; font-size: 10px; font-weight: 700; letter-spacing: 0.14em; color: #c084fc; }
        .sb-status-bar {
          display: flex; justify-content: space-between; align-items: center;
          font-family: ui-monospace, Consolas, monospace; font-size: 10px; font-weight: 700; color: #34d399;
          background: rgba(3, 9, 22, 0.72); padding: 5px 9px; border-radius: 5px; border: 1px solid rgba(16, 185, 129, 0.3);
        }
        .sb-sec-label {
          font-family: ui-monospace, Consolas, monospace; font-size: 11px; font-weight: 800;
          letter-spacing: 0.14em; color: #22d3ee; text-transform: uppercase; margin: 10px 0 6px;
        }
        .sb-telemetry-foot {
          margin-top: 12px; background: rgba(3, 8, 20, 0.82); border: 1px solid rgba(192, 132, 252, 0.3);
          border-radius: 8px; padding: 9px 11px; font-family: ui-monospace, Consolas, monospace;
          font-size: 10px; line-height: 1.6; color: #94a3b8;
        }
        .sb-telemetry-foot span { color: #22d3ee; font-weight: 700; }

        h1, h2, h3 {
          color: #f8fafc !important; font-family: ui-monospace, Consolas, monospace !important;
          letter-spacing: 0.04em; text-shadow: 0 2px 14px rgba(2, 6, 23, 0.95);
        }
        p, label { color: #f8fafc !important; }
        .stTabs [data-baseweb="tab-list"] {
          gap: 10px; background: rgba(6, 14, 32, 0.72) !important; backdrop-filter: blur(10px);
          border: 1px solid rgba(34, 211, 238, 0.28); border-radius: 10px; padding: 6px 10px;
        }
        .stTabs [data-baseweb="tab"] {
          background: transparent !important; color: #94a3b8; font-family: ui-monospace, Consolas, monospace;
          font-weight: 700; padding: 6px 12px; transition: all 0.2s ease;
        }
        .stTabs [aria-selected="true"] { color: #22d3ee !important; text-shadow: 0 0 12px rgba(34, 211, 238, 0.65); }
        .stTabs [data-baseweb="tab-highlight"] { background-color: #22d3ee !important; height: 2px !important; }
        .stTextInput input, .stSelectbox div[data-baseweb="select"] > div {
          background-color: rgba(7, 16, 36, 0.88) !important; color: #f8fafc !important;
          border: 1px solid rgba(34, 211, 238, 0.38) !important;
        }
        [data-testid="stFileUploader"] {
          background: rgba(6, 14, 32, 0.78) !important; backdrop-filter: blur(12px);
          border: 1.5px dashed rgba(34, 211, 238, 0.55) !important; border-radius: 12px !important;
          padding: 18px 20px !important; box-shadow: 0 16px 40px rgba(2, 6, 23, 0.72);
        }
        [data-testid="stFileUploader"] section {
          background: rgba(10, 22, 48, 0.65) !important; border: 1px solid rgba(56, 189, 248, 0.3) !important;
          border-radius: 8px !important;
        }
        .stForm {
          background: rgba(6, 14, 32, 0.78) !important; backdrop-filter: blur(12px);
          border: 1px solid rgba(192, 132, 252, 0.45) !important; border-right: 4px solid #c084fc !important;
          border-radius: 12px !important; padding: 22px 24px !important; box-shadow: 0 16px 40px rgba(2, 6, 23, 0.75);
        }
        .stButton > button, .stFormSubmitButton > button, .stDownloadButton > button {
          background: linear-gradient(90deg, #06b6d4, #8b5cf6); border: none; color: #ffffff;
          font-weight: 800; font-family: ui-monospace, Consolas, monospace; border-radius: 6px;
          padding: 0.58rem 1.2rem; box-shadow: 0 0 20px rgba(34, 211, 238, 0.38);
          transition: transform 0.2s ease, box-shadow 0.2s ease;
        }
        .stButton > button:hover, .stFormSubmitButton > button:hover, .stDownloadButton > button:hover {
          transform: translateY(-2px); box-shadow: 0 0 28px rgba(192, 132, 252, 0.72);
        }

        /* Portfolio Box-to-Full-Screen CSV Emblem Morph */
        @keyframes portfolioBoxToFullScreen {
          0%   {
            opacity: 0;
            transform: translate(-50%, -50%) scale(0.18) rotate(-14deg);
            filter: drop-shadow(0 0 8px rgba(34,211,238,.4));
          }
          35%  {
            opacity: 0.85;
            transform: translate(-50%, -50%) scale(0.55) rotate(6deg);
            filter: drop-shadow(0 0 26px rgba(192,132,252,.75));
          }
          70%  {
            opacity: 0.55;
            transform: translate(-50%, -50%) scale(1.06) rotate(-2deg);
            filter: drop-shadow(0 0 42px rgba(34,211,238,.85));
          }
          100% {
            opacity: 0.38;
            transform: translate(-50%, -50%) scale(1) rotate(0deg);
            filter: drop-shadow(0 0 30px rgba(34,211,238,.55)) drop-shadow(0 0 68px rgba(168,85,247,.35));
          }
        }
        @keyframes csvBreathe {
          0%, 100% { filter: drop-shadow(0 0 30px rgba(34,211,238,.5)) drop-shadow(0 0 65px rgba(168,85,247,.32)); }
          50%      { filter: drop-shadow(0 0 46px rgba(34,211,238,.78)) drop-shadow(0 0 90px rgba(192,132,252,.55)); }
        }
        @keyframes gyroSpinCW {
          from { transform: rotate(0deg); }
          to   { transform: rotate(360deg); }
        }
        @keyframes gyroSpinCCW {
          from { transform: rotate(360deg); }
          to   { transform: rotate(0deg); }
        }
        @keyframes shockwaveExpand {
          0%   { r: 40; opacity: 0.72; stroke-width: 2.4; }
          100% { r: 245; opacity: 0; stroke-width: 0.4; }
        }
        @keyframes laserScanCSV {
          0%, 100% { transform: translateY(0px); opacity: 0.45; }
          50%      { transform: translateY(130px); opacity: 1; }
        }

        #hack-elite-center-csv {
          position: fixed;
          top: 52%;
          left: 50%;
          width: min(580px, 86vw);
          height: min(580px, 86vw);
          transform: translate(-50%, -50%);
          z-index: 1;
          pointer-events: none;
          opacity: 0.38;
          transition: transform 0.14s ease-out;
          animation:
            portfolioBoxToFullScreen 1.65s cubic-bezier(0.16, 1, 0.3, 1) forwards,
            csvBreathe 6.5s ease-in-out 1.65s infinite;
        }
        #hack-elite-center-csv .gyro-cw { transform-origin: 250px 250px; animation: gyroSpinCW 30s linear infinite; }
        #hack-elite-center-csv .gyro-ccw { transform-origin: 250px 250px; animation: gyroSpinCCW 20s linear infinite; }
        #hack-elite-center-csv .gyro-fast { transform-origin: 250px 250px; animation: gyroSpinCW 12s linear infinite; }
        #hack-elite-center-csv .shockwave { animation: shockwaveExpand 4.2s cubic-bezier(0.16, 1, 0.3, 1) infinite; }
        #hack-elite-center-csv .shockwave-2 { animation: shockwaveExpand 4.2s cubic-bezier(0.16, 1, 0.3, 1) 2.1s infinite; }
        #hack-elite-center-csv .csv-laser { animation: laserScanCSV 3.2s ease-in-out infinite; }
        </style>
    """)
    st.markdown(global_css, unsafe_allow_html=True)

    stage_script = textwrap.dedent("""\
        <script>
        (function() {
          const win = window.parent;
          const doc = win.document;

          if (!doc.getElementById('hack-elite-neural-canvas')) {
            const canvas = doc.createElement('canvas');
            canvas.id = 'hack-elite-neural-canvas';
            Object.assign(canvas.style, {
              position: 'fixed',
              top: '0',
              left: '0',
              width: '100vw',
              height: '100vh',
              zIndex: '0',
              pointerEvents: 'none',
              background: 'radial-gradient(circle at 50% 50%, #0d2347 0%, #050c1e 60%, #02050c 100%)'
            });
            doc.body.prepend(canvas);

            const ctx = canvas.getContext('2d');
            let w, h, boxes = [], startTime = performance.now();
            let trail = [], ripples = [];
            let mouse = { x: win.innerWidth / 2, y: win.innerHeight / 2, active: false };

            win.addEventListener('mousemove', (e) => {
              mouse.x = e.clientX;
              mouse.y = e.clientY;
              mouse.active = true;

              for (let k = 0; k < 2; k++) {
                trail.push({
                  x: e.clientX + (Math.random() - 0.5) * 10,
                  y: e.clientY + (Math.random() - 0.5) * 10,
                  vx: (Math.random() - 0.5) * 1.8,
                  vy: (Math.random() - 0.5) * 1.8 - 0.4,
                  life: 1.0,
                  size: Math.random() * 3.2 + 1.4,
                  color: Math.random() > 0.45 ? '#22d3ee' : '#c084fc'
                });
              }
              if (trail.length > 90) trail.splice(0, trail.length - 90);

              const emblem = doc.getElementById('hack-elite-center-csv');
              if (emblem) {
                const dx = (e.clientX / win.innerWidth - 0.5) * 24;
                const dy = (e.clientY / win.innerHeight - 0.5) * 24;
                emblem.style.transform = `translate(calc(-50% + ${dx}px), calc(-50% + ${dy}px))`;
              }
            });

            win.addEventListener('click', (e) => {
              ripples.push({ x: e.clientX, y: e.clientY, r: 8, alpha: 0.85, color: '#22d3ee' });
              ripples.push({ x: e.clientX, y: e.clientY, r: 2, alpha: 0.65, color: '#c084fc' });
            });

            function initBoxes() {
              w = canvas.width = win.innerWidth;
              h = canvas.height = win.innerHeight;
              const cx = w / 2, cy = h / 2;
              boxes = Array.from({ length: 68 }, (_, i) => {
                const angle = (i / 68) * Math.PI * 2 + (i % 5) * 0.2;
                const radius = 140 + (i % 8) * (Math.min(w, h) * 0.065);
                return {
                  startX: cx + ((i % 8) - 3.5) * 18,
                  startY: cy + (Math.floor(i / 8) - 3.5) * 18,
                  targetX: cx + Math.cos(angle) * radius * (w / Math.max(w, h) * 1.15),
                  targetY: cy + Math.sin(angle) * radius,
                  x: cx,
                  y: cy,
                  size: (i % 3 === 0) ? 14 : 9,
                  angle: (i % 4) * (Math.PI / 4),
                  spin: (i % 2 === 0 ? 1 : -1) * 0.008,
                  hue: i % 3 === 0 ? '#c084fc' : (i % 2 === 0 ? '#22d3ee' : '#38bdf8'),
                  driftPhase: i * 0.45
                };
              });
            }
            initBoxes();
            win.addEventListener('resize', initBoxes);

            function draw(now) {
              ctx.clearRect(0, 0, w, h);
              const elapsed = (now - startTime) / 1000;
              const morph = Math.min(1, elapsed / 1.6);
              const ease = 1 - Math.pow(1 - morph, 4);

              if (mouse.active) {
                const spot = ctx.createRadialGradient(mouse.x, mouse.y, 0, mouse.x, mouse.y, 340);
                spot.addColorStop(0, 'rgba(34, 211, 238, 0.16)');
                spot.addColorStop(0.5, 'rgba(192, 132, 252, 0.07)');
                spot.addColorStop(1, 'rgba(0, 0, 0, 0)');
                ctx.fillStyle = spot;
                ctx.fillRect(0, 0, w, h);
              }

              ctx.strokeStyle = 'rgba(34, 211, 238, 0.04)';
              ctx.lineWidth = 1;
              for (let x = 0; x < w; x += 64) {
                ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, h); ctx.stroke();
              }
              for (let y = 0; y < h; y += 64) {
                ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(w, y); ctx.stroke();
              }

              for (let i = 0; i < boxes.length; i++) {
                const b = boxes[i];
                const driftX = Math.cos(elapsed * 0.7 + b.driftPhase) * 14 * ease;
                const driftY = Math.sin(elapsed * 0.6 + b.driftPhase) * 14 * ease;
                let bx = b.startX + (b.targetX - b.startX) * ease + driftX;
                let by = b.startY + (b.targetY - b.startY) * ease + driftY;

                let cursorBoost = 0;
                if (mouse.active) {
                  const dx = bx - mouse.x;
                  const dy = by - mouse.y;
                  const mDist = Math.hypot(dx, dy);
                  if (mDist < 230 && mDist > 0.1) {
                    const force = (1 - mDist / 230);
                    cursorBoost = force;
                    bx += (dx / mDist) * force * 24;
                    by += (dy / mDist) * force * 24;

                    ctx.strokeStyle = `rgba(34, 211, 238, ${force * 0.48})`;
                    ctx.lineWidth = 1.25;
                    ctx.beginPath();
                    ctx.moveTo(mouse.x, mouse.y);
                    ctx.lineTo(bx, by);
                    ctx.stroke();
                  }
                }

                b.x = bx;
                b.y = by;
                b.angle += b.spin + cursorBoost * 0.045;

                for (let j = i + 1; j < boxes.length; j++) {
                  const b2 = boxes[j];
                  const dist = Math.hypot(b.x - b2.x, b.y - b2.y);
                  if (dist < 165) {
                    ctx.strokeStyle = `rgba(34, 211, 238, ${(1 - dist / 165) * 0.18 * ease})`;
                    ctx.lineWidth = 1;
                    ctx.beginPath();
                    ctx.moveTo(b.x, b.y);
                    ctx.lineTo(b2.x, b2.y);
                    ctx.stroke();
                  }
                }

                ctx.save();
                ctx.translate(b.x, b.y);
                ctx.rotate(b.angle);
                const curSize = b.size * (1.3 - 0.45 * ease) * (1 + cursorBoost * 0.55);
                ctx.strokeStyle = b.hue;
                ctx.lineWidth = 1.2 + cursorBoost;
                ctx.globalAlpha = Math.min(1, 0.25 + 0.35 * (1 - ease) + cursorBoost * 0.65);
                ctx.strokeRect(-curSize / 2, -curSize / 2, curSize, curSize);

                ctx.fillStyle = b.hue;
                ctx.globalAlpha = Math.min(1, 0.65 + cursorBoost * 0.35);
                ctx.beginPath();
                ctx.arc(0, 0, 2.1 + cursorBoost * 1.8, 0, Math.PI * 2);
                ctx.fill();
                ctx.restore();
              }

              for (let t = trail.length - 1; t >= 0; t--) {
                const p = trail[t];
                p.x += p.vx;
                p.y += p.vy;
                p.life -= 0.032;
                if (p.life <= 0) {
                  trail.splice(t, 1);
                  continue;
                }
                ctx.save();
                ctx.globalAlpha = p.life * 0.85;
                ctx.fillStyle = p.color;
                ctx.shadowBlur = 10;
                ctx.shadowColor = p.color;
                ctx.beginPath();
                ctx.arc(p.x, p.y, p.size * p.life, 0, Math.PI * 2);
                ctx.fill();
                ctx.restore();
              }

              if (mouse.active) {
                ctx.save();
                ctx.strokeStyle = 'rgba(34, 211, 238, 0.55)';
                ctx.lineWidth = 1.3;
                ctx.setLineDash([6, 6]);
                ctx.translate(mouse.x, mouse.y);
                ctx.rotate(elapsed * 1.4);
                ctx.beginPath();
                ctx.arc(0, 0, 18, 0, Math.PI * 2);
                ctx.stroke();
                ctx.restore();
              }

              for (let r = ripples.length - 1; r >= 0; r--) {
                const rp = ripples[r];
                rp.r += 4.2;
                rp.alpha -= 0.022;
                if (rp.alpha <= 0) {
                  ripples.splice(r, 1);
                  continue;
                }
                ctx.save();
                ctx.strokeStyle = rp.color;
                ctx.globalAlpha = rp.alpha;
                ctx.lineWidth = 1.8;
                ctx.beginPath();
                ctx.arc(rp.x, rp.y, rp.r, 0, Math.PI * 2);
                ctx.stroke();
                ctx.restore();
              }

              requestAnimationFrame(draw);
            }
            requestAnimationFrame(draw);
          }

          if (!doc.getElementById('hack-elite-center-csv')) {
            const holder = doc.createElement('div');
            holder.id = 'hack-elite-center-csv';
            holder.innerHTML = `
              <svg viewBox="0 0 500 500" width="100%" height="100%">
                <defs>
                  <linearGradient id="csvGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" stop-color="#22d3ee"/>
                    <stop offset="48%" stop-color="#38bdf8"/>
                    <stop offset="100%" stop-color="#c084fc"/>
                  </linearGradient>
                </defs>

                <circle class="shockwave" cx="250" cy="245" r="40" fill="none" stroke="#22d3ee"/>
                <circle class="shockwave-2" cx="250" cy="245" r="40" fill="none" stroke="#c084fc"/>

                <circle class="gyro-cw" cx="250" cy="250" r="228" fill="none" stroke="#22d3ee" stroke-width="1.3" stroke-dasharray="32 14 4 14" opacity="0.55"/>
                <circle class="gyro-ccw" cx="250" cy="250" r="204" fill="none" stroke="#c084fc" stroke-width="1.3" stroke-dasharray="16 16" opacity="0.5"/>
                <circle class="gyro-fast" cx="250" cy="250" r="180" fill="none" stroke="#38bdf8" stroke-width="0.9" stroke-dasharray="6 20" opacity="0.45"/>

                <path d="M155 105 H295 L350 160 V375 C350 386 341 395 330 395 H155 C144 395 135 386 135 375 V125 C135 114 144 105 155 105 Z"
                      fill="rgba(34,211,238,0.07)" stroke="url(#csvGrad)" stroke-width="3.2" stroke-linejoin="round"/>
                <path d="M295 105 V160 H350" fill="none" stroke="#22d3ee" stroke-width="2.8" stroke-linejoin="round"/>

                <rect x="165" y="182" width="155" height="24" rx="4" fill="rgba(34,211,238,0.2)" stroke="#22d3ee" stroke-width="1.6"/>
                <rect x="165" y="218" width="72" height="22" rx="3" fill="rgba(56,189,248,0.08)" stroke="#38bdf8" stroke-width="1.4"/>
                <rect x="248" y="218" width="72" height="22" rx="3" fill="rgba(192,132,252,0.08)" stroke="#c084fc" stroke-width="1.4"/>
                <rect x="165" y="250" width="72" height="22" rx="3" fill="rgba(56,189,248,0.08)" stroke="#38bdf8" stroke-width="1.4"/>
                <rect x="248" y="250" width="72" height="22" rx="3" fill="rgba(34,211,238,0.22)" stroke="#22d3ee" stroke-width="1.5"/>
                <rect x="165" y="282" width="72" height="22" rx="3" fill="rgba(56,189,248,0.08)" stroke="#38bdf8" stroke-width="1.4"/>
                <rect x="248" y="282" width="72" height="22" rx="3" fill="rgba(192,132,252,0.08)" stroke="#c084fc" stroke-width="1.4"/>

                <line class="csv-laser" x1="150" y1="176" x2="335" y2="176" stroke="#22d3ee" stroke-width="2.5" opacity="0.9"/>

                <rect x="165" y="324" width="118" height="44" rx="7" fill="url(#csvGrad)"/>
                <text x="224" y="354" text-anchor="middle" font-family="ui-monospace,Consolas,monospace" font-size="26" font-weight="900" fill="#030712" letter-spacing="3">.CSV</text>

                <path d="M332 308 L368 322 V352 C368 376 351 394 332 402 C313 394 296 376 296 352 V322 Z"
                      fill="#030712" stroke="#10b981" stroke-width="2.8" stroke-linejoin="round"/>
                <path d="M318 354 L328 364 L348 342" fill="none" stroke="#34d399" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            `;
            doc.body.appendChild(holder);
          }
        })();
        </script>
    """)
    components.html(stage_script, height=0, width=0)


def render(markup, height):
    """Show custom HTML in the Streamlit page."""
    import streamlit as st
    try:
        import streamlit.components.v1 as components
        components.html(CSS + markup + COUNT_UP_JS, height=height, scrolling=True)
    except Exception:
        st.markdown(CSS + markup, unsafe_allow_html=True)


def hero_html(team="HACK-ELITE", subtitle="Every change, on the record."):
    stages = "<i>//</i>".join(
        f"<span>{i:02d} {v.upper()}</span>"
        for i, v in enumerate(["Upload CSV", "Genuine Check", "CWE-1236 Guard", "PII Mask", "Safe Repair", "Cert & Code"], start=1)
    )
    return (
        f'<div class="hero-stage">'
        f'<div class="hacker-pill">{_csv_logo_svg(26)}<span class="hacker-label">TEAM {html.escape(team)} // CSV FORENSICS &amp; COMPLIANCE SUITE</span></div>'
        f'<h1 class="hero-title">Data<span>Fix</span></h1>'
        f'<div class="hero-sub">{html.escape(subtitle)}</div>'
        f'<div class="pipeline-strip">{stages}</div>'
        f'</div>'
    )


def detection_box_html():
    """Live CSV Forensics & Detection Box displayed before Login."""
    return (
        '<div class="hud-card">'
        '  <div class="scan-line"></div>'
        '  <div class="card-head">'
        '    <span class="card-title">// CSV AUTHENTICITY &amp; SECURITY ENGINE</span>'
        '    <span class="live-badge"><i></i>ARMED &amp; SCANNING</span>'
        '  </div>'
        '  <div class="probe-list">'
        '    <div class="probe-item"><span>01. Magic-Byte &amp; Genuine vs. Fake Detector</span><span class="probe-tag scan">READY</span></div>'
        '    <div class="probe-item"><span>02. CWE-1236 Formula Injection Threat Shield</span><span class="probe-tag bad">GUARDED</span></div>'
        '    <div class="probe-item"><span>03. GDPR / DPDP PII Leakage &amp; Auto-Masker</span><span class="probe-tag ok">ACTIVE</span></div>'
        '    <div class="probe-item"><span>04. SHA-256 JSON Cert + Python Pipeline Export</span><span class="probe-tag purple">VERIFIED</span></div>'
        '  </div>'
        '  <div class="detect-terminal">'
        '    <div><span>[CSV]</span> Inspects magic-bytes, synthetic patterns, CWE-1236 &amp; PII</div>'
        '    <div><span>[RULE]</span> Safe-audit policy loaded from <em>cleaner.py</em></div>'
        '    <div><span>[GATE]</span> Authenticate on the right to enter workspace &rarr;</div>'
        '  </div>'
        '</div>'
    )


def upload_blueprint_html():
    """Right-side CSV Logo & Genuine/Fake Verification Blueprint on the Upload Screen."""
    return (
        '<div class="hud-card purple">'
        '  <div class="scan-line"></div>'
        '  <div class="card-head">'
        '    <span class="card-title purple">// CSV INGESTION &amp; GENUINE CHECK</span>'
        '    <span class="live-badge"><i></i>AWAITING .CSV</span>'
        '  </div>'
        '  <div class="csv-logo-banner">'
        f'    {_csv_logo_svg(56)}'
        '    <div>'
        '      <h4>.CSV INTEGRITY &amp; SECURITY SHIELD</h4>'
        '      <p>Every uploaded CSV is fingerprinted (SHA-256), scanned for Genuine vs. Fake records, neutralized against CWE-1236 formula injection, and audited for PII.</p>'
        '    </div>'
        '  </div>'
        '  <div class="probe-list">'
        '    <div class="probe-item"><span>SPOOFED &amp; FAKE DATA DETECTION</span><span class="probe-tag scan">MAGIC + ENTROPY</span></div>'
        '    <div class="probe-item"><span>FORMULA INJECTION + PII MASKING</span><span class="probe-tag ok">CWE-1236 + GDPR</span></div>'
        '    <div class="probe-item"><span>PYTHON PIPELINE + JSON CERT</span><span class="probe-tag purple">REPRODUCIBLE</span></div>'
        '  </div>'
        '</div>'
    )


def audit_summary_deck_html(fname, rows, cols, forensic_info, total_pii, pii_masked, neutralized_count, high_fixes, med_fixes, review_cnt):
    """Right-side Genuine vs. Fake Verdict with Chamfered Hex-Core % Pod & Security Status."""
    tone = forensic_info["tone"]
    sig_html = "".join(
        f'<div class="probe-item"><span>{html.escape(k)}: {html.escape(v)}</span>'
        f'<span class="probe-tag {t}">{"PASS" if t == "ok" else ("WARN" if t == "warn" else "FAKE")}</span></div>'
        for k, v, t in forensic_info["signals"][:2]
    )
    pii_tag = "ok" if (total_pii == 0 or pii_masked) else "warn"
    pii_label = "MASKED" if (total_pii > 0 and pii_masked) else ("CLEAN" if total_pii == 0 else "EXPOSED")
    sig_html += (
        f'<div class="probe-item"><span>PII Scan: {total_pii} sensitive • CWE-1236 Neutralized: {neutralized_count}</span>'
        f'<span class="probe-tag {pii_tag}">{pii_label}</span></div>'
    )
    return (
        '<div class="hud-card purple">'
        '  <div class="card-head">'
        '    <span class="card-title purple">// CSV AUTHENTICITY &amp; COMPLIANCE VERDICT</span>'
        '    <span class="live-badge"><i></i>RECORD LOCKED</span>'
        '  </div>'
        f'  <div class="verdict-box {tone}">'
        '    <div>'
        f'      <div class="vb-sub">{html.escape(fname)} ({rows}x{cols} • {forensic_info["size_kb"]} KB)</div>'
        f'      <div class="vb-main {tone}">{html.escape(forensic_info["verdict"])}</div>'
        '    </div>'
        f'    <div class="hex-score-pod {tone}">'
        f'      <div class="num" data-count-to="{forensic_info["score"]}" data-suffix="%">{forensic_info["score"]}%</div>'
        '      <div class="tag">GENUINE</div>'
        '    </div>'
        '  </div>'
        f'  <div class="probe-list">{sig_html}</div>'
        '  <div class="detect-terminal">'
        f'    <div><span>[SHA-256]</span> {forensic_info["sha256"]} &bull; Fixes: <em>{high_fixes}H / {med_fixes}M</em> &bull; Flagged: <em>{review_cnt}</em></div>'
        '  </div>'
        '</div>'
    )


def kpi_cards_html(cards):
    """Box-free floating HUD metric nodes with animated number count-up."""
    items = []
    for code, tone, label, val, detail in cards:
        num_str = str(val).replace(",", "")
        val_attr = f' data-count-to="{html.escape(num_str)}"' if num_str.replace(".", "", 1).isdigit() else ""
        items.append(
            f'<div class="metric-node">'
            f'<div class="m-top"><span class="m-code {tone}">{html.escape(code)}</span><span>{html.escape(str(label))}</span></div>'
            f'<div class="m-val"{val_attr}>{html.escape(str(val))}</div>'
            f'<div class="m-detail {tone}">{html.escape(str(detail))}</div>'
            f'</div>'
        )
    return f'<div class="hud-metrics-strip">{"".join(items)}</div>'


def ring(score, label, color):
    """Unique Cyber-Radar Segmented % Dial with rotating reticle rings and neon glow."""
    c = 263.9
    pct = max(0.0, min(float(score), 100.0))
    offset = c * (1.0 - pct / 100.0)
    uid = re.sub(r"[^a-zA-Z0-9]", "", label)
    return (
        f'<div class="cyber-dial">'
        f'  <svg viewBox="0 0 120 120" width="128" height="128">'
        f'    <defs>'
        f'      <filter id="glow_{uid}" x="-30%" y="-30%" width="160%" height="160%">'
        f'        <feGaussianBlur stdDeviation="2.8" result="blur"/>'
        f'        <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>'
        f'      </filter>'
        f'    </defs>'
        f'    <circle class="orbit-cw" cx="60" cy="60" r="54" fill="none" stroke="{color}" stroke-width="1.2" stroke-dasharray="14 8 3 8" opacity="0.55"/>'
        f'    <circle class="orbit-ccw" cx="60" cy="60" r="48" fill="none" stroke="#38bdf8" stroke-width="1" stroke-dasharray="4 10" opacity="0.45"/>'
        f'    <circle cx="60" cy="60" r="42" fill="rgba(3,9,22,0.85)" stroke="rgba(30,45,74,0.85)" stroke-width="7"/>'
        f'    <circle class="ring-prog" cx="60" cy="60" r="42" fill="none" stroke="{color}" stroke-width="7" '
        f'      stroke-linecap="butt" stroke-dasharray="{c}" stroke-dashoffset="{offset:.1f}" '
        f'      transform="rotate(-90 60 60)" filter="url(#glow_{uid})"/>'
        f'    <line x1="60" y1="3" x2="60" y2="10" stroke="{color}" stroke-width="2"/>'
        f'    <line x1="60" y1="110" x2="60" y2="117" stroke="{color}" stroke-width="2"/>'
        f'    <line x1="3" y1="60" x2="10" y2="60" stroke="{color}" stroke-width="2"/>'
        f'    <line x1="110" y1="60" x2="117" y2="60" stroke="{color}" stroke-width="2"/>'
        f'    <text x="60" y="65" text-anchor="middle" font-family="ui-monospace,Consolas,monospace" '
        f'      font-size="19" font-weight="900" fill="#ffffff" '
        f'      data-count-to="{score}" data-suffix="%">{score}%</text>'
        f'  </svg>'
        f'  <div class="rl">{html.escape(label)}</div>'
        f'</div>'
    )


def score_panel(before, after=None, chip_items=()):
    """Animated Cyber-Radar % dials + rule-by-rule repair progress stream."""
    if after is None:
        rings = ring(before, "Quality Score", "#22d3ee")
    else:
        rings = (
            ring(before, "Before Fix", "#f59e0b")
            + '<div class="arrow">&rarr;</div>'
            + ring(after, "After Fix", "#10b981")
        )
    palette = {"red": "#ef4444", "green": "#10b981", "amber": "#f59e0b", "ink": "#22d3ee"}
    total = sum(n for _, n, _ in chip_items) or 1
    bars = []
    for label, n, tone in chip_items:
        pct = min(100, round(100 * n / total))
        color = palette.get(tone, "#22d3ee")
        bars.append(
            f'<div class="bar-row">'
            f'<div class="bar-head"><span>{html.escape(str(label))}</span><span>{n} ({pct}%)</span></div>'
            f'<div class="bar-track"><div class="bar-fill" style="width:{pct}%;background:{color}"></div></div>'
            f'</div>'
        )
    return f'<div class="telemetry-flow">{rings}<div class="bars">{"".join(bars)}</div></div>'


def _show(v):
    if v is None or (not isinstance(v, str) and pd.isna(v)) or str(v) in ("empty", "nan", "None"):
        return '<span class="nul">&empty;</span>'
    if isinstance(v, float) and v.is_integer():
        v = int(v)
    return html.escape(str(v))


def dark_table_html(df):
    """Sleek translucent HTML table for Change Log, Review Queue, Profiler, Drift, and Cleaned CSV preview."""
    head = "<tr>" + "".join(f"<th>{html.escape(str(c))}</th>" for c in df.columns) + "</tr>"
    body = []
    for _, rec in df.iterrows():
        tds = []
        for col in df.columns:
            v = rec[col]
            if col == "confidence" and str(v) in ("high", "medium"):
                tds.append(f'<td><span class="pill-conf {v}">{html.escape(str(v))}</span></td>')
            elif col == "drift_status":
                tone = "high" if str(v) == "STABLE" else "medium"
                tds.append(f'<td><span class="pill-conf {tone}">{html.escape(str(v))}</span></td>')
            else:
                tds.append(f"<td>{_show(v)}</td>")
        body.append("<tr>" + "".join(tds) + "</tr>")
    return f'<div class="wrap"><table>{head}<tbody>{"".join(body)}</tbody></table></div>'


def annotated_table(df, issues=None, log=None, review=None):
    """The DataFix diff view."""
    dupes, bad, removed, changed, flagged = set(), {}, set(), {}, {}
    if log is None and issues is not None:
        for r in issues.itertuples(index=False):
            if r.column == "(whole row)":
                dupes.add(r.row)
            else:
                bad[(r.row, r.column)] = r.problem
    if log is not None:
        for r in log.itertuples(index=False):
            if r.column == "(whole row)":
                removed.add(r.row)
            else:
                changed[(r.row, r.column)] = (r.old, r.new, r.confidence, r.reason)
    if review is not None:
        for r in review.itertuples(index=False):
            flagged[(r.row, r.column)] = r.why

    head = "<tr><th>#</th>" + "".join(f"<th>{html.escape(str(c))}</th>" for c in df.columns) + "</tr>"
    body = []
    for idx, rec in df.iterrows():
        cls = "rm" if idx in removed else ("dup" if idx in dupes else "")
        tds = [f'<td class="idx">{idx}</td>']
        for col in df.columns:
            key, v = (idx, col), rec[col]
            if key in changed and idx not in removed:
                old, new, conf, why = changed[key]
                tds.append(
                    f'<td class="chg {conf}" title="{html.escape(str(why))} ({conf} confidence)">'
                    f'<s>{_show(old)}</s><i>&rarr;</i><b>{_show(new)}</b></td>'
                )
            elif key in flagged:
                tds.append(f'<td class="rev" title="{html.escape(str(flagged[key]))}">{_show(v)}</td>')
            elif key in bad:
                tds.append(f'<td class="bad" title="{html.escape(str(bad[key]))}">{_show(v)}</td>')
            else:
                tds.append(f"<td>{_show(v)}</td>")
        body.append(f'<tr class="{cls}">' + "".join(tds) + "</tr>")

    if log is None:
        legend = (
            '<span><i class="sw" style="background:rgba(239,68,68,.55)"></i>Problem found</span>'
            '<span><i class="sw" style="background:rgba(239,68,68,.28)"></i>Duplicate row</span>'
            '<span>Hover any cell for diagnostic details</span>'
        )
    else:
        legend = (
            '<span><i class="sw" style="background:rgba(16,185,129,.55)"></i>Fixed, high confidence</span>'
            '<span><i class="sw" style="background:rgba(245,158,11,.55)"></i>Fixed, medium confidence</span>'
            '<span><i class="sw" style="border:1.5px dashed #f59e0b;background:transparent"></i>Flagged for human review</span>'
            '<span><i class="sw" style="background:rgba(100,116,139,.3)"></i>Duplicate removed</span>'
            '<span>Hover any cell for audit reason</span>'
        )
    return f'<div class="legend">{legend}</div><div class="wrap"><table>{head}<tbody>{"".join(body)}</tbody></table></div>'


# --- Main Streamlit Application ---
if __name__ == "__main__":
    import streamlit as st
    import cleaner

    _ensure_dark_theme()

    st.set_page_config(
        page_title="DataFix | HACK-ELITE CSV Forensics",
        layout="wide",
        initial_sidebar_state="collapsed" if not st.session_state.get("authenticated") else "expanded",
    )

    _inject_center_csv_and_canvas()

    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False
    if "operator" not in st.session_state:
        st.session_state["operator"] = "JUDGE-01"
    if "dataset_choice" not in st.session_state:
        st.session_state["dataset_choice"] = "Upload Your CSV"
    if "uploader_key" not in st.session_state:
        st.session_state["uploader_key"] = 0
    if "reverted_fixes" not in st.session_state:
        st.session_state["reverted_fixes"] = set()
    if "active_dataset_sig" not in st.session_state:
        st.session_state["active_dataset_sig"] = ""
    if "copilot_q" not in st.session_state:
        st.session_state["copilot_q"] = "Summarize Genuine vs. Fake check & security risks"

    def _reset_workspace():
        st.session_state["dataset_choice"] = "Upload Your CSV"
        st.session_state["uploader_key"] += 1
        st.session_state["reverted_fixes"] = set()
        st.session_state["active_dataset_sig"] = ""

    # --- PRE-LOGIN GATE: Detection Box (Left) + Login Terminal (Right) ---
    if not st.session_state["authenticated"]:
        render(hero_html("HACK-ELITE", "AUTONOMOUS CSV INTEGRITY, CWE-1236 SECURITY, PII MASKING & AUDIT TERMINAL"), height=175)
        st.markdown("<div style='height:14px'></div>", unsafe_allow_html=True)

        col_detect, col_spacer, col_login = st.columns([1.15, 0.08, 1.0])

        with col_detect:
            render(detection_box_html(), height=365)

        with col_login:
            with st.form("hack_elite_login_form"):
                st.markdown("### // OPERATOR ACCESS LOGIN")
                st.caption("Enter credentials or launch instant judge demo access.")
                user_id = st.text_input("Operator ID", value="hack-elite@datafix.ai")
                passcode = st.text_input("Security Passcode", value="••••••••••••", type="password")
                c_btn1, c_btn2 = st.columns(2)
                with c_btn1:
                    submitted = st.form_submit_button("INITIALIZE SESSION", use_container_width=True)
                with c_btn2:
                    demo_login = st.form_submit_button("JUDGE DEMO BYPASS", use_container_width=True)

                if submitted or demo_login:
                    if user_id.strip() and passcode.strip():
                        st.session_state["authenticated"] = True
                        st.session_state["operator"] = user_id.strip().split("@")[0].upper()
                        st.rerun()
                    else:
                        st.error("Please enter an Operator ID and Passcode.")
        st.stop()

    # --- AUTHENTICATED WORKSPACE: TACTICAL CYBER-NEURAL SIDEBAR ---
    with st.sidebar:
        op_name = html.escape(st.session_state["operator"])
        st.markdown(
            f'<div class="sb-operator-card">'
            f'  <div class="sb-op-top">'
            f'    {_csv_logo_svg(30)}'
            f'    <div>'
            f'      <div class="sb-op-title">Data<span>Fix</span> // CSV</div>'
            f'      <div class="sb-op-sub">OP: {op_name}</div>'
            f'    </div>'
            f'  </div>'
            f'  <div class="sb-status-bar"><span>CSV SHIELD: ONLINE</span><span>CWE-1236</span></div>'
            f'</div>',
            unsafe_allow_html=True,
        )

        c_sb1, c_sb2 = st.columns(2)
        with c_sb1:
            if st.button("CLEAR / RESET", use_container_width=True):
                _reset_workspace()
                st.rerun()
        with c_sb2:
            if st.button("LOGOUT", use_container_width=True):
                st.session_state["authenticated"] = False
                st.rerun()

        st.markdown('<div class="sb-sec-label">// 01. DATA INGESTION</div>', unsafe_allow_html=True)
        source = st.radio(
            "Select CSV Dataset",
            [
                "Upload Your CSV",
                "Sample: messy_data.csv",
                "Sample: messy_data_big.csv",
                "Demo: Fake / Spoofed CSV",
            ],
            key="dataset_choice",
            label_visibility="collapsed",
        )

        st.markdown('<div class="sb-sec-label">// 02. PIPELINE MODE</div>', unsafe_allow_html=True)
        mode = st.radio(
            "Workflow Stage",
            ["Step 1: Detect & Verify CSV", "Step 2: Fix Safely & Audit"],
            index=1,
            label_visibility="collapsed",
        )

        st.markdown('<div class="sb-sec-label">// 03. CUSTOM RULE TOGGLES</div>', unsafe_allow_html=True)
        r_dedupe = st.checkbox("Deduplicate Rows", value=True)
        r_city = st.checkbox("Normalize City Names", value=True)
        r_date = st.checkbox("Standardize ISO Dates", value=True)
        r_phone = st.checkbox("Format IN Mobile Numbers", value=True)
        neutralize_formulas = st.checkbox("Neutralize Formula Payloads", value=True)
        pii_masked = st.checkbox("Mask PII Before Export (GDPR)", value=False)
        rules_enabled = {
            "dedupe": r_dedupe,
            "city": r_city,
            "date": r_date,
            "phone": r_phone,
        }

        st.markdown(
            '<div class="sb-telemetry-foot">'
            '  <div><span>ENGINE:</span> cleaner.py v3.1</div>'
            '  <div><span>SECURITY:</span> CWE-1236 + PII</div>'
            '  <div><span>TEAM:</span> HACK-ELITE</div>'
            '</div>',
            unsafe_allow_html=True,
        )

    # --- FULL-VIEWPORT TWO-COLUMN UPLOAD STAGE ---
    raw_bytes = None
    raw_text = ""

    if source == "Upload Your CSV":
        render(hero_html("HACK-ELITE", "CSV INGESTION BAY // UPLOAD ANY .CSV FILE TO CHECK GENUINE VS. FAKE & REPAIR"), height=175)
        st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)

        col_up_left, col_up_gap, col_up_right = st.columns([1.1, 0.06, 1.04])
        with col_up_left:
            st.markdown("### // 01. UPLOAD MESSY CSV DATASET")
            uploaded = st.file_uploader(
                "Drop your .CSV file here to verify Genuine vs. Fake status & run autonomous repair",
                type=["csv"],
                key=f"csv_uploader_{st.session_state['uploader_key']}",
            )
            if uploaded is None:
                st.caption("Or launch a pre-loaded genuine messy CSV or synthetic fake CSV demo:")
                b1, b2, b3 = st.columns(3)
                with b1:
                    if st.button("messy_data.csv", use_container_width=True):
                        st.session_state["dataset_choice"] = "Sample: messy_data.csv"
                        st.rerun()
                with b2:
                    if st.button("messy_data_big.csv", use_container_width=True):
                        st.session_state["dataset_choice"] = "Sample: messy_data_big.csv"
                        st.rerun()
                with b3:
                    if st.button("Fake CSV Demo", use_container_width=True):
                        st.session_state["dataset_choice"] = "Demo: Fake / Spoofed CSV"
                        st.rerun()

        with col_up_right:
            render(upload_blueprint_html(), height=380)

        if uploaded is None:
            st.stop()

        raw_bytes = uploaded.getvalue()
        raw_text = raw_bytes.decode("utf-8", errors="replace")
        fname = uploaded.name
        try:
            df = pd.read_csv(io.BytesIO(raw_bytes))
        except Exception as exc:
            st.error(f"FAKE / CORRUPT CSV DETECTED: Unable to parse CSV structure ({exc}).")
            if st.button("Clear & Upload New CSV"):
                _reset_workspace()
                st.rerun()
            st.stop()

    elif source == "Sample: messy_data.csv":
        fname = "messy_data.csv"
        with open(fname, "rb") as f:
            raw_bytes = f.read()
        raw_text = raw_bytes.decode("utf-8", errors="replace")
        df = pd.read_csv(io.BytesIO(raw_bytes))
    elif source == "Sample: messy_data_big.csv":
        fname = "messy_data_big.csv"
        with open(fname, "rb") as f:
            raw_bytes = f.read()
        raw_text = raw_bytes.decode("utf-8", errors="replace")
        df = pd.read_csv(io.BytesIO(raw_bytes))
    else:
        fname, raw_bytes, raw_text, df = _generate_fake_demo_csv()

    ds_sig = f"{fname}:{len(raw_bytes)}"
    if st.session_state["active_dataset_sig"] != ds_sig:
        st.session_state["active_dataset_sig"] = ds_sig
        st.session_state["reverted_fixes"] = set()

    forensic_info = analyze_csv_authenticity(raw_bytes, raw_text, df)
    issues = cleaner.find_issues(df)
    before_score = cleaner.quality_score(df)
    base_clean_df, base_log, base_review = cleaner.clean(df)

    clean_df, log, review = apply_rule_filters_and_reverts(
        df, base_clean_df, base_log, base_review, rules_enabled, st.session_state["reverted_fixes"]
    )
    export_df, total_pii, pii_counts, neutralized_count = apply_security_and_pii_guards(
        clean_df, mask_pii=pii_masked, neutralize_formulas=neutralize_formulas
    )
    after_score = cleaner.quality_score(clean_df)

    render(
        hero_html("HACK-ELITE", f"TARGET: {fname} // {forensic_info['verdict']} ({forensic_info['score']}%) // SHA-256: {forensic_info['sha256']}"),
        height=175,
    )

    high_fixes = int((log["confidence"] == "high").sum()) if not log.empty else 0
    med_fixes = int((log["confidence"] == "medium").sum()) if not log.empty else 0

    kpi_cards = [
        ("CSV", "blue", "Authenticity", f"{forensic_info['score']}%", forensic_info["verdict"]),
        ("ERR", "red", "Issues Found", len(issues), f"{before_score}% initial quality"),
        ("FIX", "green", "Auto-Repaired", len(log), f"{high_fixes}H • {med_fixes}M confidence"),
        ("REV", "amber", "Human Review", len(review), "Untouched — never guessed"),
        ("SEC", "purple", "PII & Inject", f"{total_pii} / {forensic_info['inj_count']}", "Masked & Defanged" if (pii_masked and neutralize_formulas) else "Guard Active"),
    ]
    render(kpi_cards_html(kpi_cards), height=110)

    if mode == "Step 1: Detect & Verify CSV":
        st.subheader("CSV Forensics & Diagnostic Scan (Read-Only)")
        if not issues.empty:
            issue_counts = issues["problem"].value_counts()
            chips = [(prob, int(cnt), "red") for prob, cnt in issue_counts.items()]
        else:
            chips = [("Clean Cells", df.shape[0] * df.shape[1], "green")]

        c_left, c_right = st.columns([1.35, 1.0])
        with c_left:
            render(score_panel(before_score, chip_items=chips), height=max(290, 44 * len(chips)))
        with c_right:
            render(
                audit_summary_deck_html(
                    fname, df.shape[0], df.shape[1], forensic_info, total_pii, pii_masked, neutralized_count, high_fixes, med_fixes, len(review)
                ),
                height=310,
            )

        render(annotated_table(df, issues=issues), height=520)

    else:
        st.subheader("CSV Forensics, Diff & Audit Trail")
        chips = [
            ("High-Confidence Repairs", high_fixes, "green"),
            ("Medium-Confidence Repairs", med_fixes, "amber"),
            ("Flagged for Human Review", len(review), "red"),
        ]

        c_left, c_right = st.columns([1.35, 1.0])
        with c_left:
            render(score_panel(before_score, after_score, chip_items=chips), height=310)
        with c_right:
            render(
                audit_summary_deck_html(
                    fname, df.shape[0], df.shape[1], forensic_info, total_pii, pii_masked, neutralized_count, high_fixes, med_fixes, len(review)
                ),
                height=310,
            )

        render(annotated_table(df, issues=issues, log=log, review=review), height=460)

        tab_log, tab_review, tab_copilot, tab_profiler, tab_drift, tab_export = st.tabs([
            f"Change Log & Undo ({len(log)})",
            f"Human Review ({len(review)})",
            "Audit Copilot",
            f"Column Health & Charts ({len(df.columns)})",
            "Schema Drift Detector",
            f"Export, Cert & Code ({len(export_df)} rows)",
        ])

        with tab_log:
            if not log.empty:
                render(dark_table_html(log), height=min(350, 56 + 38 * len(log)))
                st.caption("Select any automatic repair to revert it back to its original value:")
                u1, u2 = st.columns([3, 1.2])
                with u1:
                    fix_indices = list(log.index)
                    fix_labels = [
                        f"Fix #{idx} • Row {log.loc[idx, 'row']} [{log.loc[idx, 'column']}]: {log.loc[idx, 'old']} → {log.loc[idx, 'new']}"
                        for idx in fix_indices
                    ]
                    chosen_fix = st.selectbox("Select repair to undo", fix_labels)
                with u2:
                    st.markdown("<div style='height:26px'></div>", unsafe_allow_html=True)
                    if st.button("Revert Selected Fix", use_container_width=True):
                        target_idx = fix_indices[fix_labels.index(chosen_fix)]
                        st.session_state["reverted_fixes"].add(target_idx)
                        st.rerun()
            else:
                st.success("No automatic changes active.")

            if st.session_state["reverted_fixes"]:
                if st.button(f"Restore All Reverted Fixes ({len(st.session_state['reverted_fixes'])})"):
                    st.session_state["reverted_fixes"] = set()
                    st.rerun()

        with tab_review:
            if not review.empty:
                render(dark_table_html(review), height=min(340, 56 + 38 * len(review)))
                st.caption("Optionally patch a flagged cell below before downloading:")
                c1, c2 = st.columns([2, 2])
                with c1:
                    options = [
                        f"Row {r.row} • {r.column} (current: {r.value})"
                        for r in review.itertuples(index=False)
                    ]
                    picked = st.selectbox("Select flagged cell", options)
                with c2:
                    new_val = st.text_input("Replacement value (leave blank to keep untouched)")
                if new_val.strip():
                    sel_idx = options.index(picked)
                    rec = review.iloc[sel_idx]
                    if rec["row"] in export_df.index:
                        export_df.at[rec["row"], rec["column"]] = new_val.strip()
                        st.success(f"Updated row {rec['row']} `{rec['column']}` to `{new_val.strip()}` for export.")
            else:
                st.success("Zero cells require manual review!")

        with tab_copilot:
            st.caption("Interrogate the audit log, Genuine vs. Fake check, CWE-1236 injection guard, flagged rows, and PII status in plain English:")
            qp1, qp2, qp3, qp4 = st.columns(4)
            with qp1:
                if st.button("Genuine vs Fake?", use_container_width=True):
                    st.session_state["copilot_q"] = "Is this file genuine or fake?"
            with qp2:
                if st.button("Formula injection?", use_container_width=True):
                    st.session_state["copilot_q"] = "Check formula injection security"
            with qp3:
                if st.button("Why rows flagged?", use_container_width=True):
                    st.session_state["copilot_q"] = "Why were rows flagged for human review?"
            with qp4:
                if st.button("Check PII risks", use_container_width=True):
                    st.session_state["copilot_q"] = "Check PII & privacy exposure"

            user_q = st.text_input("Ask Audit Copilot", value=st.session_state["copilot_q"])
            ans_html = answer_audit_copilot(
                user_q, fname, forensic_info, before_score, after_score, log, review, total_pii, pii_counts, pii_masked, neutralized_count
            )
            st.markdown(f'<div class="copilot-box">{ans_html}</div>', unsafe_allow_html=True)

        with tab_profiler:
            prof_df = build_column_health_df(df, export_df)
            render(dark_table_html(prof_df), height=min(320, 56 + 40 * len(prof_df)))
            ch1, ch2 = st.columns(2)
            with ch1:
                st.caption("Null Values Per Column (Before vs. After Repair)")
                null_chart_df = prof_df.set_index("column")[["nulls_before", "nulls_after"]]
                st.bar_chart(null_chart_df, height=230)
            with ch2:
                st.caption("Audit Action Breakdown (High-Conf vs. Medium-Conf vs. Flagged)")
                action_df = pd.DataFrame(
                    {"count": [high_fixes, med_fixes, len(review)]},
                    index=["High-Confidence Fix", "Medium-Confidence Fix", "Flagged for Review"],
                )
                st.bar_chart(action_df, height=230)

        with tab_drift:
            st.caption("Upload a baseline / previous master CSV to detect column drops, additions, type shifts, or null spikes:")
            baseline_file = st.file_uploader("Upload Baseline Master CSV for Schema Drift Comparison", type=["csv"], key="drift_uploader")
            if baseline_file is not None:
                try:
                    base_df = pd.read_csv(baseline_file)
                    drift_df, missing_c, new_c = compute_schema_drift(base_df, export_df)
                    if missing_c or new_c:
                        st.warning(f"Schema Drift Detected — Dropped columns: {missing_c or 'None'} | New columns: {new_c or 'None'}")
                    else:
                        st.success("Zero structural column drift detected against baseline master CSV.")
                    render(dark_table_html(drift_df), height=min(380, 56 + 40 * len(drift_df)))
                except Exception as exc:
                    st.error(f"Could not read baseline CSV: {exc}")
            else:
                st.info("Select a baseline CSV above to compare schema compatibility before downstream ingestion.")

        with tab_export:
            render(dark_table_html(export_df), height=min(380, 56 + 38 * len(export_df)))
            cert_bytes = build_audit_certificate_json(
                fname,
                st.session_state["operator"],
                forensic_info,
                before_score,
                after_score,
                log,
                review,
                rules_enabled,
                st.session_state["reverted_fixes"],
                total_pii,
                pii_masked,
                neutralized_count,
            )
            py_bytes = generate_standalone_python_script(fname, rules_enabled, pii_masked, neutralize_formulas)

            c_dl, c_cert, c_py, c_rst = st.columns([1.2, 1.3, 1.3, 1.0])
            with c_dl:
                st.download_button(
                    "Download Cleaned CSV",
                    data=export_df.to_csv(index=False).encode("utf-8"),
                    file_name=f"cleaned_{fname}",
                    mime="text/csv",
                    use_container_width=True,
                )
            with c_cert:
                st.download_button(
                    "JSON Audit Certificate",
                    data=cert_bytes,
                    file_name=f"audit_certificate_{os.path.splitext(fname)[0]}.json",
                    mime="application/json",
                    use_container_width=True,
                )
            with c_py:
                st.download_button(
                    "Export Python Script (.py)",
                    data=py_bytes,
                    file_name=f"datafix_pipeline_{os.path.splitext(fname)[0]}.py",
                    mime="text/x-python",
                    use_container_width=True,
                )
            with c_rst:
                if st.button("Clear & Reset", use_container_width=True):
                    _reset_workspace()
                    st.rerun()