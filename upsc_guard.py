def is_upsc_related(query: str) -> bool:

    upsc_keywords = [
        "upsc",
        "ias",
        "ips",
        "polity",
        "constitution",
        "history",
        "geography",
        "economy",
        "economics",
        "environment",
        "ecology",
        "science",
        "technology",
        "ethics",
        "governance",
        "current affairs",
        "international relations",
        "csat",
        "parliament",
        "president",
        "prime minister",
        "fundamental rights",
        "directive principles",
        "ncert",
        "ancient india",
        "medieval india",
        "modern india",
        "indian constitution"
    ]

    query = query.lower()

    return any(keyword in query for keyword in upsc_keywords)