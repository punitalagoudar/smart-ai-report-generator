import re

REQUIRED_SECTIONS = [
    "introduction",
    "problem_statement",
    "solution",
    "conclusion"
]

KEYWORDS = [
    "system",
    "implementation",
    "analysis",
    "design",
    "solution"
]


def validate_sections(sections):
    score = 0
    remarks = []

    # 1️⃣ Section completeness
    for section in REQUIRED_SECTIONS:
        text = sections.get(section, "").strip()
        if len(text.split()) >= 40:
            score += 25
        else:
            remarks.append(f"{section} too short")

    # 2️⃣ Keyword relevance
    combined_text = " ".join(sections.values()).lower()
    keyword_hits = sum(1 for k in KEYWORDS if k in combined_text)

    if keyword_hits >= 3:
        score += 15
    else:
        remarks.append("Low keyword relevance")

    # 3️⃣ Readability check
    sentence_count = len(re.findall(r"[.!?]", combined_text))
    word_count = len(combined_text.split())

    if sentence_count > 5 and word_count > 150:
        score += 10
    else:
        remarks.append("Poor readability")

    # 4️⃣ Final status
    if score >= 70:
        status = "PASSED"
    elif score >= 50:
        status = "REVIEW"
    else:
        status = "FAILED"

    return score, status, remarks
