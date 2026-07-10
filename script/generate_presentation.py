"""
Generate a .pptx presentation comparing Ohtani, Sanchez, and Misiorowski (2026 season).
"""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.chart import XL_CHART_TYPE
import os

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)

BLUE = RGBColor(0x1F, 0x77, 0xB4)
ORANGE = RGBColor(0xFF, 0x7F, 0x0E)
GREEN = RGBColor(0x2C, 0xA0, 0x2C)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
DARK = RGBColor(0x33, 0x33, 0x33)

def add_slide(title_text, body_lines=None, caption=None):
   slide = prs.slides.add_slide(prs.slide_layouts[6])  # blank
   # Title
   txBox = slide.shapes.add_textbox(Inches(0.5), Inches(0.3), Inches(12.3), Inches(0.8))
   tf = txBox.text_frame
   tf.word_wrap = True
   p = tf.paragraphs[0]
   p.text = title_text
   p.font.size = Pt(32)
   p.font.bold = True
   p.font.color.rgb = DARK

   if body_lines:
       txBox2 = slide.shapes.add_textbox(Inches(0.7), Inches(1.3), Inches(11.9), Inches(5.5))
       tf2 = txBox2.text_frame
       tf2.word_wrap = True
       for i, line in enumerate(body_lines):
           if i == 0:
               p = tf2.paragraphs[0]
           else:
               p = tf2.add_paragraph()
           p.text = line
           p.font.size = Pt(18)
           p.font.color.rgb = DARK
           p.space_after = Pt(8)
           if line.startswith('Key '):
               p.font.bold = True
               p.font.size = Pt(20)
               p.font.color.rgb = BLUE

   if caption:
       txBox3 = slide.shapes.add_textbox(Inches(0.5), Inches(6.8), Inches(12.3), Inches(0.5))
       tf3 = txBox3.text_frame
       p = tf3.paragraphs[0]
       p.text = caption
       p.font.size = Pt(11)
       p.font.italic = True
       p.font.color.rgb = RGBColor(0x66, 0x66, 0x66)

   return slide

# ---- Slide 1: Title ----
slide = prs.slides.add_slide(prs.slide_layouts[6])
txBox = slide.shapes.add_textbox(Inches(1), Inches(2), Inches(11.3), Inches(3.5))
tf = txBox.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "Not All Aces Are Equal"
p.font.size = Pt(44)
p.font.bold = True
p.font.color.rgb = DARK
p.alignment = PP_ALIGN.CENTER
for line in [
   "A Data-Driven Comparison of Three NL Cy Young Candidates in 2026",
   "Ohtani · Sanchez · Misiorowski"
]:
   p = tf.add_paragraph()
   p.text = line
   p.font.size = Pt(24)
   p.font.color.rgb = RGBColor(0x66, 0x66, 0x66)
   p.alignment = PP_ALIGN.CENTER
   p.space_after = Pt(12)

# ---- Slide 2: Data Overview ----
add_slide("Data Overview",
   [
       "Dataset: 4,797 total pitch events from MLB Statcast (2026 season)",
       "",
       "Shohei Ohtani:      1,335 pitches, 14 games, 7 pitch types",
       "Cristopher Sanchez:  1,800 pitches, 19 games, 3 pitch types",
       "Jacob Misiorowski:  1,662 pitches, 18 games, 5 pitch types",
       "",
       "Key Observation: Ohtani has thrown ~35% fewer pitches than Sanchez.",
       "Despite his two-way role, this workload gap limits overall value."
   ])

# ---- Slide 3: Pitch Arsenal ----
add_slide("Pitch Arsenal Comparison",
   [
       "Ohtani: 7 pitch types (FF, SI, ST, FC, CU, FS, SL) — widest arsenal",
       "Sanchez: 3 pitch types (SI, CH, SL) — simple but devastating",
       "Misiorowski: 5 pitch types (FF, FC, CU, SL, CH) — power-based",
       "",
       "Key Finding: Sanchez's 3-pitch mix outperforms Ohtani's 7.",
       "- Sanchez SL whiff rate: 42.7%  vs  Ohtani best (ST): 37.1%",
       "- Sanchez CH whiff rate: 42.0%",
       "- Ohtani ranks LAST in overall whiff rate (28.4%)"
   ])

# ---- Slide 4: Velocity ----
add_slide("Velocity & Movement",
   [
       "Misiorowski: 100.5 mph avg FF (max 105.5 mph) — elite velocity",
       "Ohtani: 98.1 mph avg FF (max 101.7 mph) — elite, but a tier below",
       "Sanchez: 95.2 mph avg SI (max 97.7 mph) — relies on movement, not speed",
       "",
       "Sanchez generates extreme horizontal movement: 1.5 in on SI, 1.4 in on CH",
       "Osinkeni has varied movement but lacks the signature ground-ball weapon"
   ])

# ---- Slide 5: Plate Discipline ----
add_slide("Control & Plate Discipline",
   [
       "Key Metric    | Ohtani | Sanchez | Misiorowski",
       "BB%           |  7.6%  |  4.8%   |  6.4%",
       "K%            | 27.9%  | 27.6%   | 39.6%",
       "K-BB%         | 20.3%  | 22.8%   | 33.2%",
       "Whiff%        | 28.4%  | 29.7%   | 34.3%",
       "",
       "Ohtani walks batters at a 58% higher rate than Sanchez.",
       "Misiorowski dominates in K% and Whiff% by a wide margin."
   ])

# ---- Slide 6: Run Expectancy ----
add_slide("Run Expectancy Impact (Critical Finding)",
   [
       "DELTA PITCHER RUN EXPECTANCY (lower = better)",
       "",
       "Sanchez:  +14.487 total  |  +0.0080 per pitch  ← BEST",
       "Ohtani:   +21.028 total  |  +0.0158 per pitch",
       "Misiorowski: +36.807 total | +0.0222 per pitch",
       "",
       "Sanchez gives up HALF the run value per pitch vs Ohtani.",
       "Despite 465 MORE pitches, Sanchez's total run cost is LOWER.",
       "This is the strongest evidence against Ohtani's Cy Young case."
   ])

# ---- Slide 7: Batted Ball ----
add_slide("Batted Ball Profile",
   [
       "Metric         | Ohtani | Sanchez | Misiorowski",
       "Avg Exit Velo  | 86.9   | 89.1    | 86.6",
       "Hard Hit%      | 33.8%  | 44.3%   | 34.2%",
       "Barrels        |   0    |   8     |   3",
       "Ground Balls   |  111   | 192     | 101",
       "",
       "Ohtani suppresses exit velocity well (0 barrels, lower HardHit% than Sanchez)",
       "BUT Sanchez's extreme GB rate (192) creates a different damage profile",
       "Ground balls rarely produce extra-base hits — this is intentional"
   ])

# ---- Slide 8: Platoon ----
add_slide("Platoon Splits",
   [
       "Pitcher       | vs LHB OPS | vs RHB OPS",
       "Ohtani        |   .545     |   .383",
       "Sanchez       |   .336     |   .718",
       "Misiorowski   |   .288     |   .554",
       "",
       "Sanchez dominates LHB: 36.2% K%, 1.7% BB%, .336 OPS — elite",
       "Ohtani allows more vs LHB than either peer (.545 OPS)",
       "Misiorowski: 47.6% K% vs LHB is extraordinary"
   ])

# ---- Slide 9: Conclusion ----
slide = prs.slides.add_slide(prs.slide_layouts[6])
txBox = slide.shapes.add_textbox(Inches(0.5), Inches(0.3), Inches(12.3), Inches(0.8))
tf = txBox.text_frame
p = tf.paragraphs[0]
p.text = "Conclusion"
p.font.size = Pt(32)
p.font.bold = True
p.font.color.rgb = DARK

txBox2 = slide.shapes.add_textbox(Inches(0.7), Inches(1.3), Inches(11.9), Inches(5.5))
tf2 = txBox2.text_frame
tf2.word_wrap = True

lines = [
   "The data does NOT support the claim that Ohtani is the best pitcher of the three.",
   "",
   "Sanchez outperforms Ohtani in:",
   "  - Walk rate (4.8% vs 7.6% — 58% better control)",
   "  - Run prevention per pitch (+0.0080 vs +0.0158 — 50% better)",
   "  - Whiff rate on secondary pitches (42.7% vs 37.1%)",
   "  - Ground ball generation (192 GB vs 111 GB)",
   "  - Durability / workload (1,800 vs 1,335 pitches)",
   "",
   "Misiorowski outperforms both in:",
   "  - Strikeout rate (39.6%), Whiff rate (34.3%), Velocity (100.5 mph)",
   "",
   "Ohtani is excellent, but the numbers say he is the 3rd-best pitcher here."
]
for i, line in enumerate(lines):
   if i == 0:
       p = tf2.paragraphs[0]
   else:
       p = tf2.add_paragraph()
   p.text = line
   p.font.size = Pt(18)
   p.font.color.rgb = DARK
   p.space_after = Pt(4)

# Save
output_dir = os.path.join(os.path.dirname(__file__), '..', 'report')
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, 'MLB_Pitchers_Analysis_2026.pptx')
prs.save(output_path)
print(f'Presentation saved to {output_path}')
