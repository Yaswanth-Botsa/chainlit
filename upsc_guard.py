# upsc_guard.py
upsc_keywords = [
    "upsc", "ias", "ips", "polity", "constitution", "history",
    "geography", "economy", "economics", "environment", "ecology",
    "science", "technology", "ethics", "governance", "current affairs",
    "international relations", "csat", "parliament", "president",
    "prime minister", "fundamental rights", "directive principles",
    "ncert", "ancient india", "medieval india", "modern india",
    "indian constitution", "el nino", "el niño", "monsoon", "river",
    "mountain", "plateau", "revolution", "war", "dynasty", "empire",
    "amendment", "article", "schedule", "act", "bill", "policy",
    "inflation", "gdp", "poverty", "agriculture", "industry",
    "climate", "biodiversity", "pollution", "treaty", "summit",
    "organization", "united nations", "world bank", "imf",
    "photosynthesis", "cell", "atom", "disease", "vaccine",
    "green revolution", "blue revolution", "white revolution",
    "federalism", "judiciary", "legislature", "executive",
    "preamble", "citizenship", "election", "commission"
]

def is_upsc_related(query: str) -> bool:
    return any(keyword in query.lower() for keyword in upsc_keywords)