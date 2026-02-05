import random
import re

METRICS = {
    "performance": ["reduced latency by {}%", "improved throughput by {}%"],
    "scale": ["handled {}+ daily users", "processed {}+ requests/day"],
    "accuracy": ["improved accuracy to {}%", "reduced error rate by {}%"],
    "efficiency": ["cut processing time by {}%", "reduced memory usage by {}%"]
}

def smart(low, high):
    return random.randint(low, high)

def already_has_number(text):
    return bool(re.search(r"\d+%|\d+\+", text))

def add_metrics(bullet):
    b = bullet.lower()

    # ✅ Never double inject
    if already_has_number(bullet):
        return bullet

    # 🎯 Performance related
    if any(k in b for k in ["latency", "performance", "speed", "throughput"]):
        return bullet + f" ({random.choice(METRICS['performance']).format(smart(25,55))})"

    # 🎯 Scale related (much stricter now)
    if any(k in b for k in ["scalable", "high volume", "large scale", "concurrent"]):
        return bullet + f" ({random.choice(METRICS['scale']).format(smart(800,5000))})"

    # 🎯 ML related
    if any(k in b for k in ["accuracy", "model", "prediction"]):
        return bullet + f" ({random.choice(METRICS['accuracy']).format(smart(88,97))})"

    # 🎯 Optimization related
    if any(k in b for k in ["optimized", "reduced", "streamlined"]):
        return bullet + f" ({random.choice(METRICS['efficiency']).format(smart(20,45))})"

    return bullet

def smart_metrics(bullet):
    if "%" in bullet or "x" in bullet or "seconds" in bullet or "users" in bullet:
        return bullet   # already strong
    return add_metrics(bullet)