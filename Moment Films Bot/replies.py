# ─── CONSTANTS ────────────────────────────────────────────────────────────────

GLOBAL_REPLIES = {
    "events":
    "We cover a wide range of events 🎬\n\n"
    "1️⃣ Family Celebrations & Functions\n"
    "2️⃣ Corporate Films & Events\n"
    "3️⃣ Commercial Advertisements\n"
    "4️⃣ Documentary & Creative Projects\n\n"
    "If you already have something in mind, just tell me about it 😄",

    "pricing":
    "Pricing depends on the type of shoot, event size, editing needs, addons, and a few other details 🎥\n\n",

    "time":
    "You can message us anytime 😊\n"
    "Even if we're busy at a shoot, our team checks messages regularly and gets back as soon as possible.",

    "services": (
    "Hi, we are Films! 🎥 Here’s a quick look at our services.\n\n"
    "What are you looking for? 👇\n"
    "1️⃣ Wedding Films\n"
    "2️⃣ Corporate Films\n"
    "3️⃣ Commercial Reels\n"
    "4️⃣ Social Media Videos\n"
    "5️⃣ Documentary Films\n\n"
    "Type *numbers* to explore each service."
    ),

    "human":
    "Sure 👍 I've informed the team about your inquiry.\n"
    "They’ll reach out to you shortly.",

    "booking":
    "To start a booking, just type *book* or *2* 😄\n"
    "I’ll guide you through a few quick questions.",

    "service_help":
    "Yep, we do *XYZ* 🎬\n\n"
    "If you'd like pricing, availability, or more details, I can help with that too.\n"
    "You can also type *book* or *2* anytime to get started 😄",

    "event_help":
    "Yes 😄 We cover *XYZ* events.\n\n"
    "If you'd like pricing, availability, or shoot ideas for your event, I can help with that too 🎥",

    "bye":
    "Thanks for reaching out 😄\n"
    "Whenever you're ready for your next shoot or event, just message us again 🎬📸",

    "location":
    "We’re based in Mumbai 📍\n"
    "But we travel across India depending on the project or event.",

    "about us":
    "*Films* is a creative media team focused on filmmaking, photography, reels, ads, branding, and digital content 🎬\n\n"
    "We work with businesses, events, brands, creators, restaurants, startups, and more.\n\n"
    "Our goal is simple:\n"
    "Create visuals that actually feel alive instead of looking generic 😄",

    "help": (
        "Here’s what you can do 👇\n\n"
        "1️⃣ *explore* or *1* → explore our services\n"
        "2️⃣ *book* or *2* → start a booking\n"
        "3️⃣ *services* or *3* → see what we offer\n"
        "4️⃣ *pricing* or *4* → know about pricing\n"
        "5️⃣ *location* or *5* → where we’re based\n"
        "6️⃣ *events* or *6* → events we cover\n"
        "7️⃣ *time* or *7* → our availability\n"
        "8️⃣ *about us* or *8* → know more about us\n"
        "9️⃣ *human* or *9* → connect with our team\n"
        "🔟 *menu* or *10* → show the menu again"
    ),

    "menu": (
        "Main Menu 🎬\n\n"
        "1️⃣ Type *explore* or *1* to explore services\n"
        "2️⃣ Type *book* or *2* to start a booking\n"
        "3️⃣ Type *about us* or *8* to know more about us\n"
        "4️⃣ Type *help* or *h* to see all options"
    ),

    "greet":
    "Hey 👋\n"
    "Thanks for reaching out to *Films*.\n\n"
    "What are you planning? A wedding, reels, ad shoot, event, or something creative? 🎬",
}

FALLBACK_REPLIES = [
    "My camera just lost focus for a second 📸😵\n"
    "Try asking about *services*, *pricing*, *events*, or type *help* to explore what we do!",

    "That message flew past me faster than a drone shot 💨\n"
    "But I *can* help you with shoots, reels, weddings, ads, pricing, bookings and more! Type *help* 😄",

    "Our editor is still rendering a response for that 🎬⌛\n"
    "Meanwhile, you can ask about *photography*, *videography*, *events*, *pricing*, or type *help*.",

    "Plot twist: my cinematic brain couldn't process that scene 😭🎥\n"
    "Try something like:\n"
    "🔹 wedding shoot\n"
    "🔹 pricing\n"
    "🔹 reels\n"
    "🔹 drone coverage\n"
    "🔹 book",

    "That message deserves a behind-the-scenes breakdown 🎞️😂\n"
    "I’m best at helping with events, media shoots, pricing, bookings, reels, ads and creative services.\n"
    "Type *help* to unlock the director's menu 🎬"
]

POSITIVE_REPLIES = [
    "Perfect 😄",
    "Sounds good 👍",
    "Awesome 🎬",
    "Gotcha 😄",
    "Nicee ✨",
    "Cool 😄",
    "Great! 🎉",
    ]

WELCOME_MSG = (
    "Hi, we are Films! 🎥 Here’s a quick look at our services.\n\n"
    "What are you looking for? 👇\n"
    "1️⃣ Wedding Films\n"
    "2️⃣ Corporate Films\n"
    "3️⃣ Commercial Reels\n"
    "4️⃣ Social Media Videos\n"
    "5️⃣ Documentary Films\n"
    "6️⃣ Something Creative / Other\n"
    "7️⃣ To explore our service\n\n"
    "Just reply with the *number* or *name* of the service to explore! 😄"
    )

SERVICE_FLOWS = {

    "family": [

        ("date",
        "Could you please share the event date? 📅✨"),

        ("venue",
        "Perfect 😄\n\n"
        "Where is the event venue/location, XYZ? 📍🎬"),

        ("requirements",
        "Almost done 😊\n\n"
        "Any specific requirements you'd like us to include?\n\n"
        "Drone, reels, photography + videography, same-day edits, etc. ✨"),

        ("price", 130000)
    ],


    "corporate": [

        ("date",
        "Perfect 😊\n\n"
        "Do you already have a preferred shoot date or timeline in mind? 📅✨"),

        ("requirements",
        "Almost done ✨\n\n"
        "Any specific requirements or expectations for the production?\n\n"
        "Interviews, cinematic shots, drone coverage, reels, testimonials, etc. 🎥"),

        ("price", 100000)
    ],


    "advertisement": [

        ("date",
        "Awesome ✨\n\n"
        "Do you already have a preferred campaign launch date or shoot timeline? 📅🚀"),

        ("requirements",
        "Almost done 😊\n\n"
        "Any specific expectations or creative requirements you'd like us to include? 🎥✨"),

        ("price", 150000)
    ],


    "social_media": [
        ("content_type",
        "What kind of content are you planning?\n\n"
        "Fashion, business, food, fitness, personal branding, etc. 🎬"),

        ("platform",
        "Sounds good 👍\n\n"
        "Will this content be mainly for Instagram, YouTube Shorts, or multiple platforms? 📱✨"),

        ("date",
        "Love that 🔥\n\n"
        "When are you planning to start the content shoot or posting schedule? 📅🚀"),

        ("requirements",
        "Almost done 😊\n\n"
        "Any additional requirements you'd like us to include?\n\n"
        "Drone shots, multiple outfits, indoor/outdoor shoot, regular content plan, etc. 🚀"),

        ("price", 25000)
    ],


    "documentary": [

        ("date",
        "Amazing 👍\n\n"
        "Do you already have a preferred production timeline or shoot dates in mind? 📅🎥"),

        ("requirements",
        "Almost done 😊\n\n"
        "Any special requirements you'd like us to include?\n\n"
        "Drone shots, interviews, voice-over, travel coverage, cinematic edits, subtitles, etc. 🚀"),

        ("price", 90000)
    ],


    "generic_flow": [

        ("project_type",
        "Could you tell us a little more about the project or event you're planning? 🎬"),

        ("date",
        "Perfect 👍\n\n"
        "Do you already have any preferred timeline or event date in mind? 📅✨"),

        ("requirements",
        "Almost done 😄\n\n"
        "Any additional ideas or requirements we'd should know about?\n\n"
        "Drone shots, reels, cinematic edits, branding visuals, storytelling style, etc. 🚀🎥"),

        ("price", 50000)
    ],
}

FLOW_OPENERS = {

    "family": [

        "That sounds beautiful already, XYZ ❤️\n\n",
        "This is going to be such a special celebration, XYZ ✨\n\n",
        "Excited already for your big day, XYZ 💖🎬\n\n",
        "This sounds lovely, XYZ 😊\n\n",
        "We’d love to make this celebration memorable for you, XYZ 🎉📸\n\n",
        "That already feels magical, XYZ ✨❤️\n\n",
        "Sounds like a beautiful event is coming up, XYZ 🎬\n\n",
        "Can already imagine the beautiful moments, XYZ 📸✨\n\n",
    ],


    "corporate": [

        "Sounds exciting, XYZ ✨\n\n",
        "This project sounds promising already, XYZ 🚀\n\n",
        "Great to hear about this initiative, XYZ 👍\n\n",
        "Sounds like an impactful project, XYZ 🎬\n\n",
        "This already feels like a strong brand story, XYZ 📈✨\n\n",
        "Excited to hear more about your project, XYZ 😊\n\n",
        "Sounds like something professionally exciting, XYZ 🏢🎥\n\n",
        "Love the direction this is heading, XYZ 🚀\n\n",
    ],


    "advertisement": [

        "Love that idea already, XYZ 🚀\n\n",
        "This campaign sounds exciting, XYZ 🔥\n\n",
        "Sounds like a powerful brand concept already, XYZ 🎯✨\n\n",
        "This already feels visually exciting, XYZ 🎬\n\n",
        "Sounds like a strong campaign direction, XYZ 📈🔥\n\n",
        "Excited to hear more about this campaign, XYZ 🚀🎥\n\n",
        "This sounds creatively fun already, XYZ ✨\n\n",
        "Looks like something attention-grabbing is cooking, XYZ 👀🎬\n\n",
    ],


    "social_media": [

        "This sounds fun already, XYZ 😄\n\n",
        "Love the content vibes already, XYZ 🎬✨\n\n",
        "Sounds creatively exciting, XYZ 🚀\n\n",
        "This already feels like content people would love watching, XYZ 📱🔥\n\n",
        "Sounds like a strong content idea already, XYZ 🎥✨\n\n",
        "Excited to hear more about your content plans, XYZ 😄\n\n",
        "This sounds visually interesting already, XYZ 👀🎬\n\n",
        "Love where this is going already, XYZ 🚀✨\n\n",
    ],


    "music_video": [

        "This already feels cinematic, XYZ 🎵✨\n\n",
        "Sounds creatively powerful already, XYZ 🔥🎬\n\n",
        "Love the artistic energy already, XYZ 🎥✨\n\n",
        "This sounds visually exciting, XYZ 🚀🎵\n\n",
        "Can already imagine some crazy visuals here, XYZ 👀✨\n\n",
        "This project sounds super creative already, XYZ 🎬🔥\n\n",
        "Sounds like something emotionally powerful, XYZ 🎵❤️\n\n",
        "This already feels like a cinematic experience, XYZ 🎥✨\n\n",
    ],

    "documentary": [

    "This sounds meaningful already, XYZ 🎬✨\n\n",
    "Love projects with real stories like this, XYZ 😊\n\n",
    "This already feels emotionally powerful, XYZ ❤️\n\n",
    "Sounds like a documentary with depth, XYZ 🎥✨\n\n",
    "Excited to hear more about this story, XYZ 🚀\n\n",
    "This sounds creatively inspiring already, XYZ 🌍🎬\n\n",
    "Can already imagine some powerful visuals here, XYZ 👀✨\n\n",
    "This feels like a story worth telling, XYZ 🎞️❤️\n\n",  
    ],

    "generic_flow": [

        "Sounds exciting already, XYZ ✨\n\n",
        "This sounds interesting, XYZ 😊\n\n",
        "Love hearing about creative ideas like this, XYZ 🎬\n\n",
        "Excited to know more about your project, XYZ 🚀\n\n",
        "This already sounds promising, XYZ ✨\n\n",
        "Sounds like something memorable is coming up, XYZ 📸🎉\n\n",
        "This sounds creatively exciting already, XYZ 🎥✨\n\n",
        "Would love to hear more about this, XYZ 😄\n\n",
    ]
}

INTRO = [
    "Lovely to meet you, XYZ ✨",
    "Great connecting with you, XYZ 👍",
    "Hey XYZ 👋",
    "Nice to meet you, XYZ 😄",
    "Hello XYZ 👋",
    "Hi XYZ 👋",
    "Welcome XYZ 👋",
    "It's a pleasure to meet you, XYZ ✨",
    "Happy to connect with you, XYZ 😄",
    "Excited to chat with you, XYZ 🎬",
]

SUMMARY_MESSAGES = {

    "family": (
        "Hi XYZ ✨\n\n"
        "Based on your event details, we’ve prepared the most suitable coverage approach for your celebration ❤️\n\n"
        "Our event productions typically start from *₹1,30,000* depending on the scale, coverage style, and production requirements 🎬\n\n"
        "Let's jump on a *quick call* to talk details and see how we can bring this special day to life! 📞 Let us know when you're free! 🕒"
    ),

    "corporate": (
        "Hi XYZ ✨\n\n"
        "Thank you for sharing your project details.\n\n"
        "We focus on creating professional visual content that not only looks premium, but also communicates business value clearly and effectively 📈🎬\n\n"
        "I would love to work on your concept! Let's jump on a *quick call* to map out the ideation and discuss how we can pull this off. 🧠 Let us know a good time to connect! 📞"
    ),

    "advertisement": (
        "Hi XYZ 🚀\n\n"
        "Based on your campaign goals, we’ve prepared a creative direction focused on strong visual storytelling and audience engagement 🎯\n\n"
        "Our commercial productions typically start from *₹25,000* depending on campaign complexity, production requirements, and deliverables ✨\n\n"
        "To make sure we nail your exact brand vibe, let’s do a *quick creative call* to discuss the concept and ideation! 🎯 When is a good time to get you on the phone? 🤙"
    ),

    "social_media": (
        "Hi XYZ ✨\n\n"
        "Based on your content plans, we’ve prepared a content production approach designed for engagement, consistency, and visual quality 📱🎬\n\n"
        "Our social media content productions vary depending on content volume, shoot complexity, and editing style 🚀\n\n"
        "Let's skip the endless texting back and forth and jump on a *quick call* to brainstorm the strategy! ⚡ Drop a time that works best for you!"
    ),

    "documentary": (
        "Hi XYZ 🎬✨\n\n"
        "Thank you for sharing your documentary vision.\n\n"
        "Our documentary productions typically start from a base premium rate depending on the storytelling scope, shoot days, and production requirements 🎥\n\n"
        "Every epic film starts with a great conversation! Let’s hop on a *call* to talk ideation and narrative structure. Hit us with your availability! 👇"
    ),

    "generic_flow": (
        "Hi XYZ ✨\n\n"
        "Thank you for sharing your project details.\n\n"
        "Our custom productions are tailored entirely around your project scope, creative requirements, and deliverables 🎬\n\n"
        "Every unique project needs a unique blueprint! Let’s hop on a *brief call* to bring this vision to life. 📞 Hit us with a time slot that works for you! 👇"
    ),
}

# ─── RANDOMIZED PUSH TO CALL VARIATIONS ──────────────────────────────────────

PUSH_TO_CALL_VARIENTS = [
    # Option 1: High Energy & Creative 🚀
    "Woohoo! 🎉 Your details have successfully reached our director's desk! 🚀\n\n"
    "📞 *What's next?*\n"
    "Our team is already brainstorming creative concepts for your shoot! We'll give you a call within the next 24 hours to chat about your vision, double-check availability, and get the ball rolling. 🙌✨",

    # Option 2: Pure Cinematic / Film Director Vibe 🎬
    "And... CUT! 🎬 We've locked in your details, and they look absolutely amazing! 🎞️\n\n"
    "📞 *What's next?*\n"
    "We treat every project like a feature film. Our team will ring you within 24 hours for a quick production briefing to map out your style, lock the date, and make it legendary! 🎥🔥",

    # Option 3: Premium & Highly Professional 💼
    "Awesome! ✨ Your project brief has been successfully logged into our system.\n\n"
    "📞 *What's next?*\n"
    "To ensure we capture every detail flawlessly, one of our production managers will call you within 24 hours. We'll finalize custom packaging, answer your questions, and lock in your slot. 📈🌟",

    # Option 4: Urgent & Action-Oriented (Great for FOMO) ⚡
    "Got it! 🙌 Your booking request is officially in our queue.\n\n"
    "📞 *What's next?*\n"
    "Our calendar fills up fast, so we want to secure your spot ASAP! Keep your phone close—our team will call you within 24 hours to lock down dates, discuss logistics, and kick off planning! 🕒🚀"
]

# ─── STATIC PORTFOLIO BLOCK ──────────────────────────────────────────────────

PORTFOLIO_STATIC_BLOCK = {
    "family":
    (
        "\n\n"
        "Meanwhile, grab some popcorn 🍿 and check out some of our favorite masterpieces here 👇\n\n"
        "✨ Wedding Photos\n"
        "<link>\n\n"

        "✨ Our Pre-Wedding & Wedding Work Profile\n"
        "<link>\n\n"

        "✨ Our Album Work Portfolio\n"
        "<link>\n\n"

       "Can't wait to create some magic together! ✨❤️\n\n"
        "Cheers,\n"
        "*Team Films* 🎬"
    ),

    "other":
    (
    "\n\n"
    "Meanwhile, grab some popcorn 🍿 and check out some of our favorite masterpieces here 👇\n\n"
    "🎥 *Our Official Work Portfolio:*\n"
    "<link>\n\n"
    "Can't wait to create some magic together! ✨❤️\n\n"
    "Cheers,\n"
    "*Team Films* 🎬"
    )
    }