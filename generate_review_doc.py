from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

doc = Document()

title = doc.add_heading('Product Manager Assessment — Candidate Reviews', 0)
title.alignment = WD_ALIGN_PARAGRAPH.CENTER
doc.add_paragraph('Prepared by: AI-assisted evaluation | Based on calibrated framework')
doc.add_paragraph('')

# ─── JERT ───
doc.add_heading('JERT', 1)

doc.add_heading('Exercise 1 — Offers Page', 2)
for b in [
    'Funnel is Entry → View → Click → Activate → Deposit with 4 illustrative rows. No mention of Gift icon, offer sections (Sports/Casino/All), banners or any element specific to the Offers Page as a product.',
    'Only 3 KPIs defined (CTR, Activation Rate, Deposit Rate) — all derived from the funnel steps themselves. No bounce rate, scroll depth, repeat visit rate, or anything that reflects how users browse and discover offers.',
    'Success defined purely as deposit conversion — misses the hub/discovery role of the product entirely.',
    'Additional KPIs section offers only 3 items (conversion by entry point, time from activation to deposit, repeat usage) qualified with "if I had access to more data" — a PM should propose these unconditionally.',
    'No engagement with the Offers Page screenshots file at all.',
]:
    doc.add_paragraph(b, style='List Bullet')

doc.add_heading('Exercise 2 — Missions', 2)
for b in [
    'Used 3 cherry-picked rows (Apr 6, Apr 20, May 4) from 13 weeks of available data — no trend, no monthly view, no aggregation.',
    'Never mentioned public vs private missions once — the core personalization lever in the product and the most actionable variable in the dataset.',
    'Sport categories (football, basketball, tennis, mixed) completely ignored — the Category tab was not touched.',
    '"Product improvements" are: simplify missions, improve visibility, optimize difficulty — generic enough to apply to any gamification product.',
    '"Drop the product" conclusion is correct but based on zero data: "high opt-ins indicate product-market fit" — that is one number from one tab.',
]:
    doc.add_paragraph(b, style='List Bullet')

doc.add_heading('Exercise 3 — Loyalty', 2)
for b in [
    'Correctly understood there is no opt-in.',
    'Framed around three dimensions: Adoption & Engagement, Progression Dynamics, Behavioral Impact — reasonable structure.',
    'Provided illustrative funnel (100K → 72K → 28K → 9.5K) and a cohort retention example (week 4: 48%, VIP week 4: 70%+) — shows effort to make it tangible.',
    'Metrics proposed are generic — no reward cost vs GGR, no coin redemption rate, no churn by stage. Stops at "are users progressing?" without asking "is this profitable for the business?"',
]:
    doc.add_paragraph(b, style='List Bullet')

doc.add_heading('Exercise 4 — NSM', 2)
for b in [
    'Chose Sportsbook Missions, NSM: Average Completed Missions per Active User — defensible but essentially a repackaging of completion rate.',
    'Supporting metrics are well-chosen (opt-in rate, completion rate, avg bets per user, retention of mission users) — the best part of this exercise.',
    'Prioritization framework (impact x effort x confidence) is textbook correct but generic — no connection to Novibet\'s specific product context.',
    'Never argued why Missions over Offers Page or Loyalty — the choice feels default, not strategic.',
]:
    doc.add_paragraph(b, style='List Bullet')

p = doc.add_paragraph()
p.add_run('Final call: No Hire.  ').bold = True
p.add_run('The submission is well-structured but hollow. Every exercise describes methodology instead of demonstrating product judgment. The Missions analysis — where real data was available — is the clearest disqualifier: 3 rows used, two of the three key variables ignored, improvements that could apply to any product. No evidence of a PM who asks "what is this product trying to do for the user and for the business?"')

p2 = doc.add_paragraph()
p2.add_run('AI signal: High.  ').bold = True
p2.add_run('Identical template structure across all 4 exercises, pervasive "I would" distancing language, no data engagement despite having it, no supporting file submitted, no voice or opinion anywhere.')

doc.add_paragraph('')

# ─── GUILLERMO ───
doc.add_heading('GUILLERMO', 1)

doc.add_heading('Exercise 1 — Offers Page', 2)
for b in [
    'Defined three distinct funnels reflecting how users actually experience the product differently: Discovery (how they find it), Navigation (how they browse inside it), Activation & Completion (how they act on it) — shows he understood the Offers Page as a hub, not a landing page.',
    'Events properly categorized into Acquisition, Engagement and Conversion — with specific events like "Offer Category Filtered/Tapped" and "Offer Abandoned" that show he thought about the browsing experience.',
    'Success defined as "a growing share of active players discover and activate at least one promotion per session, increasing bet frequency and measurable GGR" — connects user action directly to business outcome.',
    'Additional KPIs go beyond basics: Offer to Bet Ratio, Cross-product Activation (casino players activating sports offers and vice versa), Category Heatmap CTR — shows strategic product thinking about the hub\'s role across verticals.',
    'Weak spot: illustrative report is only 4 headline numbers. The Brief acknowledges this was intentional ("measurement architecture over mock data") but it leaves the report thin.',
]:
    doc.add_paragraph(b, style='List Bullet')

doc.add_heading('Exercise 2 — Missions', 2)
for b in [
    'Identified the June completion drop precisely: active users completing at least one mission fell from 2,499 (May 18) to 1,234 (Jun 29) — a 51% decline — while opt-in users remained stable at ~4,600–4,750. The problem is not discovery, it\'s completion.',
    'Correctly identified private missions as a personalization lever and flagged they were underused — only 0–5 per week across 13 weeks — with a clear recommendation to expand targeting for high-value segments.',
    'Sport category analysis is strong: football as backbone, basketball disappearing in June (end of NBA), Mixed missions peaking on the best week (May 18: 6 Mixed, 25,432 opt-ins), tennis unable to fill the gap. Connected seasonality to supply-side decisions.',
    'Success definition includes concrete thresholds: at least 20% of weekly active users opt-in, CR stays above 35%, no widening gap between opt-in and completion users.',
    '"Drop the product" response is structured around four distinct arguments with data: absolute scale (182K opt-ins), growing user base (+30%), supply-side root cause, and the product\'s unique retention mechanic (rewards regardless of win/loss).',
]:
    doc.add_paragraph(b, style='List Bullet')

doc.add_heading('Exercise 3 — Loyalty', 2)
for b in [
    'Correctly understood no opt-in, correctly distinguished Premium (one-off) vs VIP (monthly recurring).',
    'Time-phased structure — Launch (Jan–Feb), Growth (Mar–May), Maturity (Jun–Aug) plus a pre-launch baseline (Oct–Dec 2024) — is sharp product thinking: you cannot assess a program without a before/after reference.',
    'Illustrative dashboard is the most business-grounded: 68% Premium completion, 31% Premium to VIP, +22% GGR uplift vs non-loyalty cohort, 4.7x sessions for VIP users — these numbers tell a product story.',
    'Additional KPIs include Reward to Cost Ratio and GGR Lift (loyalty vs control cohort) — demonstrates awareness that loyalty programs need to be commercially justified, not just engagement-tracked.',
    'Brief adds a sharp further exploration question: "Are players earning coins but not redeeming them? Low redemption would indicate an awareness or UX issue in the reward flow, not a product design problem" — this is PM thinking.',
]:
    doc.add_paragraph(b, style='List Bullet')

doc.add_heading('Exercise 4 — NSM', 2)
for b in [
    'Chose Offers Page — Weekly Active Players with at least 1 Offer Activation — and argued why this metric filters out passive browsing while capturing real intent: a player who activates has received the core value of the product.',
    'The decision framework is the most actionable of all candidates: Awareness Driver (Entry Point CTR) → Engagement Driver (Offer Click Rate) → Conversion Driver (Opt-In Rate), each with a specific initiative attached. This is how a PM actually runs a weekly product review.',
    'Explicitly noted how to detect trade-offs: "more offers shown but lower CTR may signal relevance issues rather than a volume problem" — shows he has thought about how the metric can mislead.',
    'Weak spot: did not argue why Offers Page over Loyalty or Missions. The choice is well-justified on its own terms but the comparative reasoning is absent.',
]:
    doc.add_paragraph(b, style='List Bullet')

p = doc.add_paragraph()
p.add_run('Final call: Hire — #1.  ').bold = True
p.add_run('Guillermo demonstrates consistent product-first thinking across all four exercises. He understands what each product is trying to do for the user, connects observations to business outcomes, and proposes improvements that are strategic rather than generic. The Brief in particular shows a candidate who can reflect on his own methodology — a strong PM signal.')

p2 = doc.add_paragraph()
p2.add_run('AI signal: Low.  ').bold = True
p2.add_run('Has a distinct voice, genuine data observations grounded in the actual dataset, personal assumptions in the Brief that feel authored, and a visual presentation style that reflects individual choices.')

doc.add_paragraph('')

# ─── GALLARDO ───
doc.add_heading('GALLARDO', 1)

doc.add_heading('Exercise 1 — Offers Page', 2)
for b in [
    'The work document is the most comprehensive event taxonomy of all candidates — Traffic & Discovery, Engagement & Interaction, Offer Discovery & Selection, Conversion & Funnel, Retention & Behavioral — mapped to a full Buyer Journey (Awareness → Consideration → Conversion → Retention). Nothing is missing.',
    'Illustrative report is the richest: 120K users, entry points (Gift icon 48%, homepage banner 27%, push/email 15%), scroll depth split (22%/46%/32%), section click distribution, per-offer CTR and activations, full funnel (120K→54K→26K→18.5K), and post-offer behavior (loyalty users returning at 68% vs 39% non-loyalty).',
    'The 68% vs 39% retention comparison is a genuinely strong product insight — it demonstrates why the Offers Page has business value beyond just activations.',
    'Additional KPIs include "time to activation" and "steps to activation" as friction indicators — more actionable than what other candidates proposed.',
    'Weak spot: the final PDF condenses all of exercise 1 into a single short paragraph. The depth lives in the work document — a PM presenting to leadership would need to bridge that gap.',
]:
    doc.add_paragraph(b, style='List Bullet')

doc.add_heading('Exercise 2 — Missions', 2)
for b in [
    'Pinpointed the exact inflection point: May 25 (45.47% CR, 40% Private) → June 1 (26.70%, 0 Private, 5 missions) — framed as a signal of an operational or configuration change, not a product failure. That is precise PM thinking.',
    'Quantified the opt-in/completion divergence explicitly: opt-in rate grew from ~16% to over 17% while completion rate fell from ~8–9% to 4.5% by June 29. Correctly diagnosed as a completion-stage issue, not a discovery problem.',
    'Full Category analysis: April Football+Basketball dominant, May most diverse with Mixed missions (43% of May 18 week), June collapsed to Football+Tennis only — identified as likely a seasonality or operational constraint and connected directly to the performance drop.',
    'Private missions framed as a personalization strategy: recommended a 60–70% Public / 30–40% Private mix as optimal, with A/B tests to validate.',
    '"Drop the product" response is the most structured: four specific reasons (strong absolute scale, growing opt-in user base, supply-side root cause, unique retention mechanic) — mirrors how a PM would defend a product in a leadership meeting.',
]:
    doc.add_paragraph(b, style='List Bullet')

doc.add_heading('Exercise 3 — Loyalty', 2)
for b in [
    'Correctly understood no opt-in from the first line, correctly distinguished Premium vs VIP mechanics.',
    'Introduced a Reward Effectiveness dimension (redemption rate, time between earning and redemption, behavior before and after milestones) that no other candidate raised — this is a product maturity question: are players actually getting value from the rewards?',
    'Perimeter is well-defined and respects the assignment guidance: casino-only, excludes competitive comparisons, excludes over-focus on coin numerics.',
    'Four-dimension framework (Adoption, Engagement & Progression, Reward Effectiveness, Retention & Behavioral Impact) covers the full lifecycle of the product.',
    'Weak spot: no visuals, no pre-launch baseline (Oct–Dec 2024) for comparison — Guillermo\'s time-phased approach with a before/after anchor is sharper here.',
]:
    doc.add_paragraph(b, style='List Bullet')

doc.add_heading('Exercise 4 — NSM', 2)
for b in [
    'Chose Casino Loyalty — Monthly Active Casino Loyalty Users — and articulated all four design pillars of the product in the rationale: frictionless, activity-driven, progressive, retention-focused. Shows he actually read and internalized the product description.',
    'Explicitly distinguished the NSM from vanity metrics: "unlike total registered users, this captures ongoing, value-creating usage" — a PM who understands what a metric is really measuring.',
    'Decision framework is crisp and tied to the product\'s structure: if NSM declines → investigate discovery; if Premium completion low → simplify milestones; if VIP stagnates → optimize rewards; if engagement drops → introduce progression boosters.',
    'Secondary metrics are all genuinely complementary and non-redundant: Premium completion rate, VIP monthly active users, avg coins per active user, retention lift vs non-loyalty.',
]:
    doc.add_paragraph(b, style='List Bullet')

p = doc.add_paragraph()
p.add_run('Final call: Hire — #2.  ').bold = True
p.add_run('Gallardo is analytically the deepest of all candidates and that depth is mostly in service of product decisions — the private mission personalization argument, the reward effectiveness dimension in loyalty, the operational change hypothesis on May 25. The main risk is that the work document reads like an analyst report rather than a PM presentation. Worth probing in interview on how he communicates product decisions to non-analytical stakeholders.')

p2 = doc.add_paragraph()
p2.add_run('AI signal: Low-Medium.  ').bold = True
p2.add_run('The analytical granularity feels genuinely worked through. However, the writing in the work document is unusually thorough and formally structured throughout — possible heavy AI editing even if the thinking is his own.')

doc.add_paragraph('')

# ─── SUMMARY TABLE ───
doc.add_heading('Final Summary', 1)
table = doc.add_table(rows=4, cols=3)
table.style = 'Table Grid'
hdr = table.rows[0].cells
hdr[0].text = 'Candidate'
hdr[1].text = 'Final Call'
hdr[2].text = 'AI Signal'
for cell in hdr:
    for para in cell.paragraphs:
        for run in para.runs:
            run.bold = True

for i, (c, f, a) in enumerate([
    ('Guillermo', 'Hire — #1', 'Low'),
    ('Gallardo',  'Hire — #2', 'Low-Medium'),
    ('JERT',      'No Hire',   'High'),
]):
    row = table.rows[i+1].cells
    row[0].text = c
    row[1].text = f
    row[2].text = a

doc.save('Candidate_Reviews_PM_Assessment.docx')
print('Done')
