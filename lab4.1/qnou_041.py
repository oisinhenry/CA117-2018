import sys

words = []

def q_nou(s):
    if "qu" in s.lower() or "q'u" in s.lower() or "q-u" in s.lower():
        return False

    elif "q" in s.lower() and "qu" not in s.lower():
        return True


for line in sys.stdin:
    words.append(line.strip())

print("Words with q but no u: {}".format([w for w in words if q_nou(w)]))