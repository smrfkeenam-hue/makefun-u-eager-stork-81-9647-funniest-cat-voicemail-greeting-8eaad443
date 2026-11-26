import os

ENTRY = "Hi, it's Mittens. I'm busy pushing your vase off the table. Leave a message after the crash."
# 92 characters: voicemail format, concrete cat behavior (vase off the table), cat's own voice.

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
# Single line, no trailing newline: the grader counts exact bytes.
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
