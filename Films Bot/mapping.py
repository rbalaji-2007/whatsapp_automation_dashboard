from replies import SERVICE_FLOWS
GR_INDEX = {
    "h": "help",
    "help": "help",
    #"1": "explore",
    #"2": "book",
    "3": "services",
    "4": "pricing",
    "5": "location",
    "6": "events",
    "7": "time",
    "8": "about us",
    "9": "human",
    "10": "menu"
}

NEWUSER_INDEX = {
    "1": "family",
    "2": "corporate",
    "3": "advertisement",
    "4": "social_media",
    "5": "generic_flow",
    "6": "documentary",
    "7": "explore",
}

services_kw = {
    # Photography
    "photo": "photography",
    "camera": "photography",
    "portrait": "photography",

    # Videography
    "video": "videography",

    # Drone
    "drone": "drone shoots",
    "aerial": "drone shoots",
    "fpv": "drone shoots",

    # Editing
    "edit": "editing",
    "colour": "editing",
    "thumbnail": "editing",
    "poster": "editing",
    "motion": "editing",

    # General
    "media": "media coverage",
    "event": "event coverage",
}

events_kw = {

    # Birthday
    "birthday": "birthday event",
    "bday": "birthday event",

    # Wedding
    "wedding": "wedding",
    "marriage": "wedding",
    "nikah": "wedding",
    "reception": "wedding reception",
    "engagement": "engagement",
    "mehendi": "mehendi function",
    "haldi": "haldi function",
    "prewedding": "prewedding shoot",
    "couple shoot": "couple shoot",

    # Family Events
    "baby shower": "baby shower",
    "puberty": "puberty ceremony",
    "ear piercing": "ear piercing ceremony",
    "house warming": "house warming",
    "gruha pravesh": "house warming",

    # College / School
    "college": "college event",
    "school": "school event",
    "culturals": "college culturals",
    "symposium": "college symposium",
    "farewell": "farewell event",
    "freshers": "freshers event",
    "annual day": "school annual day",
    "graduation": "graduation event",

    # Corporate
    "conference": "corporate event",
    "seminar": "seminar",
    "meeting": "corporate meeting",
    "launch": "product launch",
    "corporate": "corporate shoot",
    "office": "corporate shoot",
    "brand": "brand shoot",

    # Advertisement / Commercial
    "advertisement": "commercial advertisement",
    "advertising": "commercial advertisement",
    "ad": "commercial advertisement",
    "ads": "commercial advertisement",
    "commercial": "commercial advertisement",
    "promo": "promotional video",
    "promotion": "promotional video",
    "campaign": "marketing campaign",

    # Social Media Content
    "instagram": "instagram content",
    "insta": "instagram content",
    "reel": "instagram reels",
    "reels": "instagram reels",
    "youtube": "youtube production",
    "yt": "youtube production",
    "shorts": "youtube shorts",
    "vlog": "vlog production",
    "podcast": "podcast production",
    "content": "content creation",

    # Film / Creative
    "short film": "short film production",
    "film": "film production",
    "movie": "cinematic production",
    "documentary": "documentary film",
    "music video": "music video production",
    "album song": "music video production",

    # Food / Business
    "restaurant": "restaurant shoot",
    "cafe": "cafe shoot",
    "hotel": "hospitality shoot",
    "real estate": "real estate shoot",
    "property": "real estate shoot",
    "showroom": "showroom shoot",

    # Generic
    "function": "event",
    "program": "event",
    "celebration": "event",
    "party": "party event",
    "shoot": "media shoot",
}

service_kw_booking = {

    # ─── FAMILY EVENTS ─────────────────────────────

    "wedding": "family",
    "marriage": "family",
    "engagement": "family",
    "mehendi": "family",
    "haldi": "family",
    "nikah": "family",
    "birthday": "family",
    "baby shower": "family",
    "puberty": "family",
    "ear piercing": "family",
    "house warming": "family",
    "anniversary": "family",
    "function": "family",
    "celebration": "family",
    "party": "family",


    # ─── CORPORATE ────────────────────────────────

    "corporate": "corporate",
    "conference": "corporate",
    "seminar": "corporate",
    "meeting": "corporate",
    "startup": "corporate",
    "company": "corporate",
    "industrial": "corporate",
    "factory": "corporate",
    "interview": "corporate",
    "testimonial": "corporate",
    "presentation": "corporate",
    "business": "corporate",
    "movie": "corporate",
    "film": "corporate",


    # ─── ADVERTISEMENTS ───────────────────────────

    "advertisement": "advertisement",
    "commercial": "advertisement",
    "ad": "advertisement",
    "promo": "advertisement",
    "campaign": "advertisement",
    "marketing": "advertisement",
    "brand": "advertisement",
    "launch": "advertisement",


    # ─── SOCIAL MEDIA / REELS ─────────────────────

    "reel": "social_media",
    "instagram": "social_media",
    "youtube": "social_media",
    "shorts": "social_media",
    "content": "social_media",
    "influencer": "social_media",
    "creator": "social_media",
    "podcast": "social_media",
    "vlog": "social_media",
    "social media": "social_media",
    "media": "social_media",

    # ─── DOCUMENTARY ───────────────────────────────

    "documentary": "documentary",
    "docu": "documentary",
    "story": "documentary",
    "real story": "documentary",
    "biography": "documentary",
    "journey": "documentary",
    "interview": "documentary",
    "awareness": "documentary",
    "social issue": "documentary",
    "culture": "documentary",
    "travel film": "documentary",
    "history": "documentary",
    "behind the scenes": "documentary",
    "bts": "documentary",
    "case study": "documentary",
    "founder story": "documentary",
    "brand story": "documentary",
    "human story": "documentary",
    "life story": "documentary",
    "mini documentary": "documentary",

}

intent_kw = {

    # Pricing
    "pricing": [
        "price",
        "pricing",
        "cost",
        "charge",
        "rate",
        "budget",
        "quotation",
        "quote",
        "how",
        "package",
        "fees",
        "payment",
        "estimate",
    ],

    # Events
    "events": [
        "event",
        "events",
        "cover",
        "coverage",
        "occasion",
        "function",
        "celebration",
    ],

    # Location
    "location": [
        "location",
        "located",
        "address",
        "where",
        "city",
        "area",
        "place",
        "office",
        "branch",
        "near",
        "based",
    ],

    # Services
    "services": [
        "service",
        "offer",
        "provide",
        "work",
        "speciality",
        "specialize",
    ],

    # Time
    "time": [
        "time",
        "timing",
        "open",
        "close",
        "available",
        "availability",
        "when",
        "busy",
        "free",
    ],

    # About Us
    "about us": [
        "us",
        "who",
        "introduction",
    ],

    # Human Support
    "human": [
        "human",
        "person",
        "staff",
        "team",
        "support",
        "call",
        "contact",
        "speak",
        "representative",
        "manager",
        "customer",
        "care",
    ],

    # Greetings
    "greet": [
        "hi",
        "hello",
        "hey",
        "sup",
    ],

    # Positive Replies
    "positive_clauses": [
        "thank",
        "thx",
        "ok",
        "fine",
        "great",
        "awesome",
        "perfect",
        "cool",
        "nice",
    ],

    # Goodbye
    "bye": [
        "bye",
        "exit",
        "quit",
    ],
}

service_fields = {
    service: [field for field, _ in SERVICE_FLOWS[service] if field != "price"]
    for service in SERVICE_FLOWS
}

PROJECT_GOAL_KEYWORDS = [

    # ─── BRANDING / AWARENESS ───────────────────

    "branding",
    "brand awareness",
    "awareness",
    "visibility",
    "recognition",
    "identity",
    "presence",
    "positioning",

    # ─── MARKETING / SALES ──────────────────────

    "marketing",
    "promotion",
    "sales",
    "lead generation",
    "conversion",
    "engagement",
    "reach",
    "campaign",
    "advertising",
    "launch",

    # ─── BUSINESS / CORPORATE ───────────────────

    "presentation",
    "company profile",
    "corporate",
    "recruitment",
    "hiring",
    "training",
    "internal communication",
    "investor pitch",
    "business growth",
    "credibility",
    "professionalism",

    # ─── SOCIAL MEDIA / CONTENT ─────────────────

    "social media",
    "content creation",
    "viral",
    "audience growth",
    "personal branding",
    "influencer growth",
    "youtube growth",
    "instagram growth",

    # ─── EMOTIONAL / STORYTELLING ───────────────

    "storytelling",
    "emotional connection",
    "memory",
    "cinematic experience",
    "luxury feel",
    "premium feel",

    # ─── EVENT / DOCUMENTATION ──────────────────

    "event coverage",
    "documentation",
    "highlights",
    "aftermovie",
    "memories",
    "archive",

    # ─── PRODUCT / COMMERCIAL ───────────────────

    "product showcase",
    "product launch",
    "demo",
    "visual appeal",
    "commercial performance",

]

SERVICE_MAPPING = {
    "1": "family",
    "2": "corporate",
    "3": "advertisement",
    "4": "social_media",
    "5": "documentary",
    "6": "generic_flow",
}

SERVICE_WORD_MAPPING = {
    "1": "Wedding Films",
    "2": "Corporate Films",
    "3": "Commercial Reels",
    "4": "Social Media Videos",
    "5": "Documentary Films",
}