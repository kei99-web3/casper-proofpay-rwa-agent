from __future__ import annotations

import json
import os
import shutil
import subprocess
from pathlib import Path
from typing import Callable

from PIL import Image, ImageDraw, ImageFont, ImageOps


ROOT = Path(__file__).resolve().parents[1]
MEDIA = ROOT / "media"
ASSETS = MEDIA / "winning_demo_assets"
AUDIO = MEDIA / "audio"
CAPTURE = MEDIA / "_v2_build"
BUILD = MEDIA / "_winning_video_build"
FINAL = MEDIA / "casper-proofpay-demo-final.mp4"
V2 = MEDIA / "casper-proofpay-demo-final-v2.mp4"
CONTACT_SHEET = MEDIA / "casper-proofpay-demo-final-v2-contact-sheet.jpg"
BGM = AUDIO / "mixkit-hazy-after-hours-132.mp3"
POP_SFX = AUDIO / "mixkit-message-pop-alert-2354.mp3"

FPS = 30
W = 1920
H = 1080

FFMPEG = os.environ.get("FFMPEG_BIN") or (
    "C:/Users/PC_User/Videos/ffmpeg-master-latest-win64-gpl-shared/bin/ffmpeg.exe"
    if Path("C:/Users/PC_User/Videos/ffmpeg-master-latest-win64-gpl-shared/bin/ffmpeg.exe").exists()
    else "ffmpeg"
)

PACKAGE_HASH = "b1ba96bf374ab52f3f6560a5e88ce4fe56324eb7846c5751f7f2c4ca90e499f2"
CONTRACT_HASH = "f56cf425f3a10ed7f3e9e2622b64ca2f2a0609c9446b1cb79ea2b58167293c61"
RECEIPT_DEPLOY = "2da236ad980f1a82943fe5485d36fdaa6c3c1cdd8b38dd42808aaaf1b25b3994"
RECEIPT_URL = f"https://testnet.cspr.live/deploy/{RECEIPT_DEPLOY}"

BG = "#0d1117"
PANEL = "#111827"
PANEL_2 = "#161b22"
INK = "#f7fafc"
MUTED = "#93a4b8"
LINE = "#2b3546"
RED = "#d71920"
GREEN = "#32d583"
AMBER = "#f7b955"
BLUE = "#7dd3fc"


def font(size: int, bold: bool = False, mono: bool = False) -> ImageFont.FreeTypeFont:
    if mono:
        candidates = [
            Path("C:/Windows/Fonts/consola.ttf"),
            Path("C:/Windows/Fonts/cour.ttf"),
            Path("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"),
        ]
    else:
        candidates = [
            Path("C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf"),
            Path("C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf"),
            Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
        ]
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size=size)
    return ImageFont.load_default()


FONT_18 = font(18)
FONT_22 = font(22)
FONT_24 = font(24)
FONT_26 = font(26)
FONT_30 = font(30)
FONT_34_B = font(34, True)
FONT_42_B = font(42, True)
FONT_56_B = font(56, True)
FONT_72_B = font(72, True)
MONO_20 = font(20, mono=True)
MONO_22 = font(22, mono=True)
MONO_24 = font(24, mono=True)
MONO_26 = font(26, mono=True)
MONO_28 = font(28, mono=True)


def run_capture(command: str, output: Path) -> None:
    with output.open("w", encoding="utf-8", newline="\n") as handle:
        subprocess.run(command, cwd=ROOT, shell=True, check=True, stdout=handle, stderr=subprocess.STDOUT)


def ensure_captures() -> None:
    CAPTURE.mkdir(parents=True, exist_ok=True)
    if not (CAPTURE / "test_out.txt").exists():
        run_capture("npm test", CAPTURE / "test_out.txt")
    if not (CAPTURE / "demo_out.txt").exists():
        run_capture("npm run demo", CAPTURE / "demo_out.txt")
    if not (CAPTURE / "payload_out.txt").exists():
        run_capture("npm run payload", CAPTURE / "payload_out.txt")
    if not (CAPTURE / "tamper_out.txt").exists():
        tamper = (
            "node -e \"const {validateRevenueBatch}=require('./src/proofpay-agent.js'); "
            "const batch=[{sourceId:'merchant-parking-a',day:'2026-06-10',grossUsd:1842.25,txCount:121},"
            "{sourceId:'merchant-parking-a',day:'2026-06-10',grossUsd:9999,txCount:0}]; "
            "console.log(JSON.stringify(validateRevenueBatch(batch),null,2));\""
        )
        run_capture(tamper, CAPTURE / "tamper_out.txt")


def parse_first_json(path: Path, before_marker: str | None = None) -> dict:
    text = path.read_text(encoding="utf-8")
    if before_marker and before_marker in text:
        text = text.split(before_marker, 1)[0]
    start = text.find("{")
    if start < 0:
        raise ValueError(f"No JSON object found in {path}")
    return json.loads(text[start:].strip())


def load_data() -> dict:
    scenario = parse_first_json(CAPTURE / "demo_out.txt", "Submission payload:")
    payload = parse_first_json(CAPTURE / "payload_out.txt")
    tamper = parse_first_json(CAPTURE / "tamper_out.txt")
    receipt_hash = payload["proofReceiptArgs"]["receipt_hash"]
    expected = "0a420465974a5784c005ea47ead958d1ed3ed733ac2b2145c3d42e64224d5197"
    if receipt_hash != expected:
        raise SystemExit(f"receipt_hash mismatch: {receipt_hash} != {expected}")
    if tamper.get("verdict") != "needs_review":
        raise SystemExit("tamper verdict did not return needs_review")
    return {"scenario": scenario, "payload": payload, "tamper": tamper}


def short_hash(value: str, left: int = 10, right: int = 8) -> str:
    if len(value) <= left + right + 3:
        return value
    return f"{value[:left]}...{value[-right:]}"


def ease(x: float) -> float:
    x = max(0.0, min(1.0, x))
    return x * x * (3 - 2 * x)


def lerp(a: float, b: float, t: float) -> float:
    return a + (b - a) * t


def new_frame() -> Image.Image:
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)
    for y in range(0, H, 54):
        tone = 17 + int(8 * (y / H))
        draw.line((0, y, W, y), fill=(tone, tone + 5, tone + 12), width=1)
    for x in range(0, W, 96):
        draw.line((x, 0, x, H), fill="#111923", width=1)
    draw.rectangle((0, 0, W, 10), fill=RED)
    return img


def text_size(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.ImageFont) -> tuple[int, int]:
    box = draw.textbbox((0, 0), text, font=fnt)
    return box[2] - box[0], box[3] - box[1]


def draw_center(draw: ImageDraw.ImageDraw, y: int, text: str, fnt: ImageFont.ImageFont, fill: str = INK) -> None:
    tw, th = text_size(draw, text, fnt)
    draw.text(((W - tw) // 2, y), text, fill=fill, font=fnt)


def truncate(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.ImageFont, max_width: int) -> str:
    if draw.textlength(text, font=fnt) <= max_width:
        return text
    suffix = "..."
    while text and draw.textlength(text + suffix, font=fnt) > max_width:
        text = text[:-1]
    return text + suffix


def wrap(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.ImageFont, width: int) -> list[str]:
    out: list[str] = []
    for raw in text.splitlines():
        words = raw.split(" ")
        line = ""
        for word in words:
            test = word if not line else f"{line} {word}"
            if draw.textlength(test, font=fnt) <= width:
                line = test
            else:
                if line:
                    out.append(line)
                line = word
        if line:
            out.append(line)
    return out


def draw_tag(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, fill: str = RED, ink: str = "#ffffff") -> None:
    x, y = xy
    tw, th = text_size(draw, text, FONT_22)
    draw.rounded_rectangle((x, y, x + tw + 28, y + 38), radius=19, fill=fill)
    draw.text((x + 14, y + 7), text, fill=ink, font=FONT_22)


def draw_caption(draw: ImageDraw.ImageDraw, text: str, sub: str | None = None) -> None:
    y = 902 if sub else 925
    draw.rounded_rectangle((120, y - 22, W - 120, 1012), radius=26, fill="#0b1220", outline="#253247", width=2)
    for i, line in enumerate(wrap(draw, text, FONT_34_B, W - 300)[:2]):
        draw.text((150, y + i * 42), line, fill=INK, font=FONT_34_B)
    if sub:
        draw.text((150, y + 80), sub, fill=MUTED, font=FONT_22)


def draw_footer(draw: ImageDraw.ImageDraw, text: str) -> None:
    draw.text((64, H - 48), text, fill="#7f8fa5", font=FONT_18)


def draw_terminal(
    img: Image.Image,
    box: tuple[int, int, int, int],
    title: str,
    lines: list[str],
    highlights: tuple[str, ...] = (),
    progress: float = 1.0,
    font_obj: ImageFont.ImageFont = MONO_24,
) -> None:
    draw = ImageDraw.Draw(img)
    x1, y1, x2, y2 = box
    draw.rounded_rectangle(box, radius=22, fill="#050b14", outline="#2d3a4f", width=2)
    draw.rounded_rectangle((x1, y1, x2, y1 + 54), radius=22, fill="#111827")
    draw.rectangle((x1, y1 + 28, x2, y1 + 54), fill="#111827")
    draw.ellipse((x1 + 22, y1 + 20, x1 + 38, y1 + 36), fill="#ff5f56")
    draw.ellipse((x1 + 48, y1 + 20, x1 + 64, y1 + 36), fill="#ffbd2e")
    draw.ellipse((x1 + 74, y1 + 20, x1 + 90, y1 + 36), fill="#27c93f")
    draw.text((x1 + 112, y1 + 15), title, fill=MUTED, font=FONT_22)

    all_text = "\n".join(lines)
    limit = int(len(all_text) * max(0.0, min(1.0, progress)))
    visible = all_text[:limit]
    visible_lines = visible.splitlines()
    y = y1 + 78
    line_h = font_obj.size + 9 if hasattr(font_obj, "size") else 32
    max_lines = max(1, (y2 - y - 24) // line_h)
    for line in visible_lines[:max_lines]:
        fit = truncate(draw, line, font_obj, x2 - x1 - 56)
        if any(term in line for term in highlights):
            draw.rounded_rectangle((x1 + 20, y - 4, x2 - 20, y + line_h - 3), radius=8, fill="#17351f")
        elif "needs_review" in line or "non_positive" in line or "duplicate" in line:
            draw.rounded_rectangle((x1 + 20, y - 4, x2 - 20, y + line_h - 3), radius=8, fill="#3a2b12")
        color = GREEN if any(term in line for term in highlights) else INK
        if "402" in line or "mock" in line:
            color = BLUE
        if "needs_review" in line or "non_positive" in line or "duplicate" in line:
            color = AMBER
        draw.text((x1 + 28, y), fit, fill=color, font=font_obj)
        y += line_h


def paste_screenshot(
    img: Image.Image,
    source: Image.Image,
    box: tuple[int, int, int, int],
    crop: tuple[int, int, int, int] | None = None,
    outline: str = "#303b4c",
    centering: tuple[float, float] = (0.5, 0.5),
) -> None:
    draw = ImageDraw.Draw(img)
    x1, y1, x2, y2 = box
    src = source.crop(crop) if crop else source
    fitted = ImageOps.fit(src, (x2 - x1, y2 - y1), Image.Resampling.LANCZOS, centering=centering)
    mask = Image.new("L", fitted.size, 0)
    md = ImageDraw.Draw(mask)
    md.rounded_rectangle((0, 0, fitted.size[0], fitted.size[1]), radius=24, fill=255)
    img.paste(fitted, (x1, y1), mask)
    draw.rounded_rectangle(box, radius=24, outline=outline, width=3)


def load_image(path: Path) -> Image.Image:
    if path.exists():
        return Image.open(path).convert("RGB")
    placeholder = Image.new("RGB", (1920, 1080), "#111827")
    draw = ImageDraw.Draw(placeholder)
    draw_center(draw, 470, f"Missing screenshot: {path.name}", FONT_42_B, AMBER)
    return placeholder


def draw_scene_badge(draw: ImageDraw.ImageDraw, step: str, label: str) -> None:
    draw_tag(draw, (64, 44), step, RED)
    draw.text((64, 98), label, fill=INK, font=FONT_34_B)


def hook_lines() -> list[str]:
    return [
        "$ npm run demo",
        'revenueBatch: merchant-parking-a / synthetic_rwa_revenue',
        "2026-06-10  grossUsd=1842.25  txCount=121",
        "2026-06-11  grossUsd=1904.10  txCount=127",
        "2026-06-12  grossUsd=1775.40  txCount=116",
        "2026-06-13  grossUsd=2011.80  txCount=134",
        '"qualityScore": 96,',
        '"verdict": "verified"',
    ]


def make_scene_functions(data: dict, images: dict[str, Image.Image]) -> list[tuple[str, float, Callable[[Image.Image, float], None]]]:
    scenario = data["scenario"]
    payload = data["payload"]
    tamper = data["tamper"]
    challenge = scenario["challenge"]
    payment_proof = scenario["paymentProof"]
    receipt = scenario["receipt"]
    args = payload["proofReceiptArgs"]
    mcp_tools = scenario["mcp"]["tools"]

    pay_lines = [
        "$ npm run demo",
        "STEP 1 / PAY - x402-shaped flow",
        f'"status": {challenge["status"]},',
        f'"scheme": "{challenge["scheme"]}",',
        f'"network": "{challenge["network"]}",',
        f'"amount": "{challenge["amount"]}" {challenge["asset"]},',
        f'"challengeHash": "{short_hash(challenge["challengeHash"], 14, 10)}",',
        "paymentProof accepted",
        f'"paymentHash": "{short_hash(payment_proof["paymentHash"], 14, 10)}"',
        '"authorization": "mock_authorization_no_private_key_used"',
    ]
    verify_lines = [
        "$ npm run demo",
        "STEP 2 / VERIFY - synthetic RWA revenue batch",
        f'"grossUsd": {receipt["validation"]["totals"]["grossUsd"]},',
        f'"txCount": {receipt["validation"]["totals"]["txCount"]},',
        f'"averageTicketUsd": {receipt["validation"]["totals"]["averageTicketUsd"]},',
        f'"anomalies": {json.dumps(receipt["validation"]["anomalies"])},',
        f'"qualityScore": {receipt["validation"]["qualityScore"]},',
        f'"verdict": "{receipt["validation"]["verdict"]}"',
    ]
    tamper_lines = [
        "$ node tamper-check",
        "duplicate day + zero transaction count",
        f'"grossUsd": {tamper["totals"]["grossUsd"]},',
        f'"qualityScore": {tamper["qualityScore"]},',
        f'"reason": "{tamper["anomalies"][0]["reason"]}",',
        f'"reason": "{tamper["anomalies"][1]["reason"]}",',
        f'"verdict": "{tamper["verdict"]}"',
    ]
    payload_lines = [
        "$ npm run payload",
        f'"entryPoint": "{payload["entryPoint"]}",',
        '"transactionProducing": true,',
        f'"proof_id": "{args["proof_id"]}",',
        f'"proof_root": "{short_hash(args["proof_root"], 16, 12)}",',
        f'"payment_hash": "{short_hash(args["payment_hash"], 16, 12)}",',
        f'"receipt_hash": "{short_hash(args["receipt_hash"], 16, 12)}",',
        f'"quality_score": {args["quality_score"]}',
    ]
    mcp_lines = [
        "$ npm run demo",
        "STEP 4 / RE-VERIFY - MCP-style tools",
        f'tool: "{mcp_tools[0]["name"]}"',
        f'call.proof_id: "{mcp_tools[0]["call"]["proof_id"]}"',
        f'result.verified: {str(mcp_tools[0]["result"]["verified"]).lower()}',
        f'result.qualityScore: {mcp_tools[0]["result"]["qualityScore"]}',
        f'tool: "{mcp_tools[1]["name"]}"',
        f'reputation: "{mcp_tools[1]["result"]["reputation"]}"',
    ]

    def s1(img: Image.Image, t: float) -> None:
        draw = ImageDraw.Draw(img)
        if t < 0.16:
            draw_center(draw, 450, "Would you lend against this revenue stream?", FONT_56_B)
            draw_center(draw, 530, "Casper ProofPay asks the underwriting question first.", FONT_30, MUTED)
            draw_footer(draw, "synthetic demo data / no private revenue data")
        elif t < 0.64:
            p = ease((t - 0.16) / 0.48)
            draw_terminal(img, (190, 165, 1730, 760), "local deterministic proof run", hook_lines(), ("qualityScore", "verified"), progress=p, font_obj=MONO_28)
            draw_caption(draw, "An AI agent just bought the proof.", "x402-shaped mock payment unlocks proof access.")
        elif t < 0.90:
            paste_screenshot(img, images["cspr"], (260, 145, 1660, 780), crop=(350, 235, 1580, 830))
            draw_caption(draw, "Receipt recorded on Casper Testnet.", f"record_proof_receipt / status: Success / deploy {short_hash(RECEIPT_DEPLOY)}")
        else:
            draw_center(draw, 360, "Casper ProofPay", FONT_72_B)
            draw_center(draw, 455, "Revenue Proof Market for AI Agents", FONT_42_B, MUTED)
            draw_tag(draw, (760, 560), "Casper Testnet receipt verified", GREEN, "#04110a")
            draw_footer(draw, RECEIPT_URL)

    def s2(img: Image.Image, t: float) -> None:
        draw = ImageDraw.Draw(img)
        draw_scene_badge(draw, "THESIS", "Financial agents need proof before they act")
        draw_center(draw, 230, "AI agents lend, underwrite, and allocate.", FONT_56_B)
        draw_center(draw, 306, "They should never act on unverified revenue.", FONT_42_B, AMBER)
        labels = ["Buyer Agent", "x402 Gate", "Proof Agent", "Casper Receipt", "MCP Verify"]
        x = 160
        for i, label in enumerate(labels):
            bx = x + i * 340
            active = t > i * 0.13
            color = RED if i == 3 else ("#1f6f55" if active else "#243246")
            draw.rounded_rectangle((bx, 510, bx + 250, 640), radius=22, fill=PANEL_2, outline=color, width=4)
            draw.text((bx + 28, 555), label, fill=INK if active else MUTED, font=FONT_26)
            if i < len(labels) - 1:
                ax1 = bx + 260
                ax2 = bx + 330
                y = 575
                draw.line((ax1, y, ax2, y), fill=GREEN if active else LINE, width=5)
                draw.polygon([(ax2, y), (ax2 - 14, y - 10), (ax2 - 14, y + 10)], fill=GREEN if active else LINE)
        draw_caption(draw, "ProofPay: agents BUY verified revenue proofs before they act.", "RWA proof, x402-shaped payment, MCP-style verification, Casper Testnet receipt.")

    def s3(img: Image.Image, t: float) -> None:
        draw = ImageDraw.Draw(img)
        draw_scene_badge(draw, "STEP 1 / PAY", "x402-shaped access control")
        draw_terminal(img, (112, 190, 1810, 782), "actual npm run demo output excerpt", pay_lines, ("402", "paymentHash"), progress=ease(t), font_obj=MONO_28)
        draw_tag(draw, (1150, 90), "x402 mock - protocol-shaped, no real payment settled", "#374151")
        draw_caption(draw, "HTTP 402: payment required before proof access.", "The demo uses a mock authorization; no real payment or private key is present.")

    def s4(img: Image.Image, t: float) -> None:
        draw = ImageDraw.Draw(img)
        draw_scene_badge(draw, "STEP 2 / VERIFY", "Synthetic RWA revenue batch")
        if t < 0.56:
            draw_terminal(img, (88, 182, 1015, 790), "verified batch excerpt", hook_lines() + verify_lines[2:], ("qualityScore", "verified"), progress=ease(t / 0.56), font_obj=MONO_24)
            draw.rounded_rectangle((1090, 244, 1775, 620), radius=28, fill=PANEL_2, outline="#205a43", width=4)
            draw.text((1130, 285), "quality_score", fill=MUTED, font=FONT_30)
            draw.text((1130, 345), "96", fill=GREEN, font=FONT_72_B)
            draw.text((1130, 455), 'verdict: "verified"', fill=INK, font=FONT_34_B)
            draw.text((1130, 525), "anomalies: []", fill=MUTED, font=MONO_24)
            draw_caption(draw, "4 days of merchant revenue -> totals, anomaly scan, verified proof.", "synthetic demo data - no real customer revenue")
        else:
            p = ease((t - 0.56) / 0.44)
            draw_terminal(img, (88, 182, 1015, 790), "tamper check excerpt", tamper_lines, ("needs_review",), progress=p, font_obj=MONO_26)
            draw.rounded_rectangle((1090, 244, 1775, 620), radius=28, fill=PANEL_2, outline="#8a5a12", width=4)
            draw.text((1130, 285), "tampered batch", fill=MUTED, font=FONT_30)
            draw.text((1130, 345), "needs_review", fill=AMBER, font=FONT_56_B)
            draw.text((1130, 455), "duplicate_source_day", fill=INK, font=MONO_28)
            draw.text((1130, 505), "non_positive_tx_count", fill=INK, font=MONO_28)
            draw_caption(draw, "The proof agent refuses to anchor junk.", "This is the trust signal: the verifier can say no.")

    def s5(img: Image.Image, t: float) -> None:
        draw = ImageDraw.Draw(img)
        draw_scene_badge(draw, "STEP 3 / ANCHOR", "Casper Testnet real transaction")
        draw_terminal(img, (70, 175, 895, 785), "local payload", payload_lines, ("receipt_hash", "transactionProducing"), progress=ease(min(1, t * 2.35)), font_obj=MONO_22)
        paste_screenshot(img, images["cspr"], (980, 175, 1835, 785), crop=(350, 235, 1580, 830))
        # Connector from local payload to explorer action.
        y = int(410 + 20 * ease(t))
        draw.line((895, y, 980, y), fill=RED, width=6)
        draw.polygon([(980, y), (958, y - 14), (958, y + 14)], fill=RED)
        draw.rounded_rectangle((735, 815, 1185, 870), radius=18, fill="#170b0d", outline=RED, width=2)
        draw_center(draw, 827, "Local payload -> record_proof_receipt -> Testnet Success", FONT_24, INK)
        draw_caption(draw, "The local proof payload is anchored by a real Casper Testnet receipt.", f"deploy {short_hash(RECEIPT_DEPLOY, 12, 10)} / package {short_hash(PACKAGE_HASH, 10, 8)}")

    def s6(img: Image.Image, t: float) -> None:
        draw = ImageDraw.Draw(img)
        draw_scene_badge(draw, "STEP 4 / MCP", "Downstream agents re-verify")
        draw_terminal(img, (118, 180, 1800, 782), "MCP-style tool output excerpt", mcp_lines, ("verified", "trusted_demo_agent"), progress=ease(t), font_obj=MONO_28)
        draw_tag(draw, (1090, 90), "MCP-style tool schema - local demo surface", "#374151")
        draw_caption(draw, "Other agents can verify the paid proof before lending or underwriting.", "The demo shows tool-shaped verification; external MCP hosting is not required for this submission.")

    def s7(img: Image.Image, t: float) -> None:
        draw = ImageDraw.Draw(img)
        if t < 0.42:
            center_y = 0.36 + 0.24 * ease(t / 0.42)
            paste_screenshot(img, images["demo"], (110, 120, 1810, 830), centering=(0.5, center_y))
            draw_caption(draw, "Paid proof in. Verified receipt out. Anchored on Casper.", "Hosted demo page: kei99-web3.github.io/casper-proofpay-rwa-agent")
        elif t < 0.74:
            paste_screenshot(img, images["github"], (110, 120, 1810, 830), centering=(0.5, 0.24))
            draw_caption(draw, "Open-source repo, README, usage instructions, and final video are public.", "github.com/kei99-web3/casper-proofpay-rwa-agent")
        else:
            draw_center(draw, 190, "Casper ProofPay", FONT_72_B)
            draw_center(draw, 290, "Revenue Proof Market for AI Agents", FONT_42_B, MUTED)
            cards = [
                ("Public repo", "github.com/kei99-web3/casper-proofpay-rwa-agent"),
                ("Hosted demo", "kei99-web3.github.io/casper-proofpay-rwa-agent"),
                ("Run it", "npm test && npm run demo && npm run payload"),
                ("Testnet receipt", short_hash(RECEIPT_DEPLOY, 14, 12)),
            ]
            y0 = 430
            for i, (label, value) in enumerate(cards):
                y = y0 + i * 98
                draw.rounded_rectangle((310, y, 1610, y + 70), radius=18, fill=PANEL_2, outline=LINE, width=2)
                draw.text((350, y + 19), label, fill=MUTED, font=FONT_24)
                draw.text((620, y + 19), value, fill=INK, font=MONO_22 if i in (0, 1, 3) else FONT_24)
            draw_footer(draw, "Synthetic data demo. No private keys, no real funds. x402 flow is protocol-shaped mock. Casper Testnet receipt is real.")

    return [
        ("hook", 10.0, s1),
        ("thesis", 12.0, s2),
        ("pay", 18.0, s3),
        ("verify", 20.0, s4),
        ("anchor", 18.0, s5),
        ("mcp", 14.0, s6),
        ("close", 13.0, s7),
    ]


def render_video(data: dict) -> None:
    images = {
        "demo": load_image(ASSETS / "hosted_demo.png"),
        "github": load_image(ASSETS / "github_repo.png"),
        "cspr": load_image(ASSETS / "cspr_receipt.png"),
    }
    if BUILD.exists():
        shutil.rmtree(BUILD)
    BUILD.mkdir(parents=True)

    scenes = make_scene_functions(data, images)
    transition_times: list[float] = []
    elapsed = 0.0
    for index, (_, duration, _) in enumerate(scenes):
        if index:
            transition_times.append(elapsed)
        elapsed += duration

    frame_index = 0
    representative: list[tuple[str, Path]] = []
    for scene_name, duration, renderer in scenes:
        total = int(duration * FPS)
        for i in range(total):
            img = new_frame()
            local_t = i / max(1, total - 1)
            renderer(img, local_t)
            frame_path = BUILD / f"frame_{frame_index:05d}.png"
            img.save(frame_path)
            if i == total // 2:
                representative.append((scene_name, frame_path))
            frame_index += 1
    video_duration = frame_index / FPS

    tmp = BUILD / "casper-proofpay-demo-final-v2.video-only.tmp.mp4"
    subprocess.run(
        [
            FFMPEG,
            "-y",
            "-framerate",
            str(FPS),
            "-i",
            str(BUILD / "frame_%05d.png"),
            "-c:v",
            "libx264",
            "-pix_fmt",
            "yuv420p",
            "-r",
            str(FPS),
            "-movflags",
            "+faststart",
            str(tmp),
        ],
        check=True,
    )
    mux_audio(tmp, V2, video_duration, transition_times)
    shutil.copy2(V2, FINAL)
    build_contact_sheet(representative)


def audio_filter(duration: float, transition_times: list[float]) -> str:
    if not transition_times:
        raise ValueError("transition_times must not be empty")
    fade_out_start = max(0.0, duration - 2.5)
    parts = [
        (
            f"[1:a]aformat=sample_fmts=fltp:channel_layouts=stereo,"
            f"atrim=0:{duration:.3f},asetpts=PTS-STARTPTS,volume=0.15,"
            f"afade=t=in:st=0:d=0.8,afade=t=out:st={fade_out_start:.3f}:d=2.5[bgm]"
        )
    ]
    split_labels = "".join(f"[s{i}]" for i in range(len(transition_times)))
    parts.append(
        f"[2:a]aformat=sample_fmts=fltp:channel_layouts=stereo,asplit={len(transition_times)}{split_labels}"
    )
    for index, seconds in enumerate(transition_times):
        delay_ms = int(round(seconds * 1000))
        parts.append(
            f"[s{index}]atrim=0:1.05,asetpts=PTS-STARTPTS,volume=0.52,"
            f"adelay={delay_ms}|{delay_ms}[p{index}]"
        )
    inputs = "[bgm]" + "".join(f"[p{i}]" for i in range(len(transition_times)))
    parts.append(
        f"{inputs}amix=inputs={len(transition_times) + 1}:duration=first:normalize=0,"
        "alimiter=limit=0.92[aout]"
    )
    return ";".join(parts)


def mux_audio(video_only: Path, output: Path, duration: float, transition_times: list[float]) -> None:
    missing = [path for path in (BGM, POP_SFX) if not path.exists()]
    if missing:
        raise FileNotFoundError(
            "Missing third-party audio assets: "
            + ", ".join(str(path.relative_to(ROOT)) for path in missing)
        )
    subprocess.run(
        [
            FFMPEG,
            "-y",
            "-i",
            str(video_only),
            "-stream_loop",
            "-1",
            "-i",
            str(BGM),
            "-i",
            str(POP_SFX),
            "-filter_complex",
            audio_filter(duration, transition_times),
            "-map",
            "0:v:0",
            "-map",
            "[aout]",
            "-c:v",
            "copy",
            "-c:a",
            "aac",
            "-b:a",
            "160k",
            "-shortest",
            "-movflags",
            "+faststart",
            str(output),
        ],
        check=True,
    )


def build_contact_sheet(frames: list[tuple[str, Path]]) -> None:
    thumb_w, thumb_h = 480, 270
    cols = 2
    rows = (len(frames) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * thumb_w, rows * (thumb_h + 40)), "#0b1220")
    draw = ImageDraw.Draw(sheet)
    for index, (label, frame_path) in enumerate(frames):
        row, col = divmod(index, cols)
        img = Image.open(frame_path).convert("RGB")
        img.thumbnail((thumb_w, thumb_h), Image.Resampling.LANCZOS)
        x = col * thumb_w
        y = row * (thumb_h + 40)
        sheet.paste(img, (x, y))
        draw.text((x + 12, y + thumb_h + 8), label, fill=INK, font=FONT_22)
    sheet.save(CONTACT_SHEET, quality=92)


def main() -> None:
    ensure_captures()
    data = load_data()
    render_video(data)
    print(V2)
    print(FINAL)
    print(CONTACT_SHEET)


if __name__ == "__main__":
    main()
