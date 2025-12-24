import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROMPT_DIR = os.path.join(BASE_DIR, "prompts")

PROMPT_MAP = {
    "college": ("academic_v1.txt", "academic_v1"),
    "ieee": ("technical_v1.txt", "technical_v1"),
    "simple": ("business_v1.txt", "business_v1"),
}


def load_prompt(format_type, topic):
    if format_type not in PROMPT_MAP:
        raise ValueError("Invalid format type")

    file_name, version = PROMPT_MAP[format_type]
    file_path = os.path.join(PROMPT_DIR, file_name)

    with open(file_path, "r", encoding="utf-8") as f:
        template = f.read()

    prompt = template.format(topic=topic)

    return prompt, version
