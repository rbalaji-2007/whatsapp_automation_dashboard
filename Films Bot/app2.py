import string as st
import random as rd
import datetime
import requests
import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import random
from replies import *
from mapping import *
from ai import *
import psycopg2 as psql
from psycopg2 import sql
from psycopg2.extras import RealDictCursor

load_dotenv()

app = Flask(__name__)

# ─── CONFIG ───────────────────────────────────────────────────────────────────
VERIFY_TOKEN = os.getenv("VERIFY_TOKEN", "zflow_demo_token")   
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")                        
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")         
SQL_PASSWORD = os.getenv("SQL_PASSWORD")           

META_API_URL = f"https://graph.facebook.com/v19.0/{PHONE_NUMBER_ID}/messages"

# ─── IN-MEMORY STORE (Renamed to avoid shadowing conflicts) ──────────────────
USER_STATE_CACHE = {}
GLOBAL_STEPS = {}
GLOBAL_FLOWS = {}
TEMP_ANSWERS = {}

# ─── HELPERS ──────────────────────────────────────────────────────────────────
def init_db():
    try:
        return psql.connect(
            host="localhost",
            database="zflow",
            user="postgres",
            password="06102007",
            port="5432",
            cursor_factory=RealDictCursor
        )
    except Exception as e:
        print(f"Database Connection Error: {e} ❌")
        return None

def fetchdata(table, user=None):
    con = init_db()
    if not con:
        return []
    cur = con.cursor()
    if user:
        cur.execute(sql.SQL('SELECT * FROM {} WHERE phone_number = %s').format(sql.Identifier(table)), (user, ))
        data = cur.fetchall()
    else:
        cur.execute(sql.SQL("SELECT * FROM {}").format(sql.Identifier(table)))
        data = cur.fetchall()
    cur.close()
    con.close()
    return data

def initialize_user(user):
    con = init_db()
    if not con: return
    cur = con.cursor()
    data = fetchdata("users")
    next_id = data[-1]['id'] + 1 if data else 1
    
    cur.execute(
        "INSERT INTO users (id, name, phone_number, is_new, intent, service, looking_service, message_count, orders, last_order) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
        (next_id, None, user, True, None, None, False, 0, 0, None)
    )
    con.commit()
    cur.close()
    con.close()

def clean_text(msg):
    return ''.join(c for c in msg if c not in st.punctuation).lower().strip()

# ─── SEND MESSAGE ─────────────────────────────────────────────────────────────
def send_msg(to, text):
    if not ACCESS_TOKEN or not PHONE_NUMBER_ID:
        print(f"[DEV] → {to}: {text}\n")
        return

    data = fetchdata('users')
    if to in [_['phone_number'] for _ in data]:
        con = init_db()
        cur = con.cursor()
        cur.execute("UPDATE users SET message_count = message_count+1 WHERE phone_number = %s", (to,))
        print('updated!')
        con.commit()
        cur.close()
        con.close()

    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {"body": text}
    }
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type":  "application/json"
    }
    resp = requests.post(META_API_URL, json=payload, headers=headers)
    if not resp.ok:
        print(f"[ERROR] Meta API {resp.status_code}: {resp.text}")
        return
    if to in USER_STATE_CACHE:
        USER_STATE_CACHE[to]["message_count"] = USER_STATE_CACHE[to].get("message_count", 0) + 1

# ─── BOOKING FLOW ─────────────────────────────────────────────────────────────
def book(user, inp):
    if user not in GLOBAL_STEPS:
        GLOBAL_STEPS[user] = []	
    if user not in GLOBAL_FLOWS:
        GLOBAL_FLOWS[user] = []
    if user not in TEMP_ANSWERS:
        TEMP_ANSWERS[user] = []

    cleaned_inp = clean_text(inp)
    user_steps = GLOBAL_STEPS[user]
    user_flows = GLOBAL_FLOWS[user]
    
    data = fetchdata('users', user)
    name = data[0]['name'] if data else None
    service = data[0]['service'] if data else None

    # Step 0: Initializing and asking Name
    if not user_steps:
        if not name:
            send_msg(user, "Hey 👋\n\nThank you for reaching out to *BUSINESS NAME* ✨\n\nMay I know your name? 😊")
            GLOBAL_STEPS[user].append("name")
            GLOBAL_FLOWS[user].append("name")
            return
        GLOBAL_STEPS[user].append("name")
        GLOBAL_FLOWS[user].append("name")

    # Step 1: Processing Name, asking Event Type
    if user_steps == ["name"]:
        name = clean_text(inp.split()[-1]).capitalize() if not name else name 
        if not name:
            send_msg(user, "That was not a name! Type your name again.")
            return
        if not service:
            send_msg(user, f"{random.choice(INTRO).replace('XYZ', name)}\n\nCould you tell us what kind of event or project you're planning? 😊\n\n1. Wedding / Pre-wedding,\n2. Corporate film,\n3. Advertisement shoots,\n4. Social Media Videos,\n5. Documentary film,\n6. Or something creative 🎬\n\nYou can type your choice or type 1, 2, etc.\n\nWe’d love to understand your vision and create something truly memorable 🚀")
            con = init_db()
            if con:
                cur = con.cursor()
                cur.execute("UPDATE users SET name = %s WHERE phone_number = %s", (name, user)) # Fixed 'to' bug! 🎯
                con.commit()
                cur.close()
                con.close()
            TEMP_ANSWERS[user].append(name)
            GLOBAL_STEPS[user].append("event_type")
            GLOBAL_FLOWS[user].append("event_type")
            return
        
        con = init_db()
        if con:
            cur = con.cursor()
            cur.execute("UPDATE users SET name = %s WHERE phone_number = %s", (name, user))
            con.commit()
            cur.close()
            con.close()
        TEMP_ANSWERS[user].append(name)
        GLOBAL_STEPS[user].append("event_type")
        GLOBAL_FLOWS[user].append("event_type")

    # Step 2: Processing Event Type, determining the flow
    if user_steps == ["name", "event_type"]:
        con = init_db()
        if not con: return
        cur = con.cursor()
        if not cleaned_inp:
            send_msg(user, "That is not a valid input!")
            cur.close()
            con.close()
            return
        if not service:
            if cleaned_inp in SERVICE_MAPPING:
                ser = SERVICE_MAPPING.get(cleaned_inp, "generic_flow")
            else:
                w = next((s for s in service_kw_booking if s in cleaned_inp), None)
                ser = service_kw_booking.get(w, "generic_flow")
            
            cur.execute("UPDATE users SET service = %s WHERE phone_number = %s", (ser, user))
            con.commit()
        cur.close()
        con.close()
        
        # Pull updated user service data safely
        user_data = fetchdata('users', user)
        service = user_data[0]['service'] if user_data else "generic_flow"
        
        GLOBAL_FLOWS[user].extend(service_fields.get(service, []))
        TEMP_ANSWERS[user].append(service)
		
    if len(user_steps) < len(user_flows):
        if not cleaned_inp:
            send_msg(user, "That is not a valid input!")
            return
        send_msg(user, SERVICE_FLOWS[service][len(user_steps)-2][-1])
        GLOBAL_STEPS[user].append(user_flows[len(user_steps)])
        if len(GLOBAL_STEPS[user]) == 3:
            return
        TEMP_ANSWERS[user].append(cleaned_inp)

    else:
        TEMP_ANSWERS[user].append(cleaned_inp)
        summarise(user)
        
        current_service = fetchdata('users', user)[0]['service']
        portfolio_msg = PORTFOLIO_STATIC_BLOCK["family"] if current_service == "family" else PORTFOLIO_STATIC_BLOCK["other"]
        send_msg(user, f"{random.choice(PUSH_TO_CALL_VARIENTS)}{portfolio_msg}")
        
        con = init_db()
        if con:
            cur = con.cursor()
            cur.execute("UPDATE users SET intent = %s WHERE phone_number = %s", (None, user))
            user_info = fetchdata('users', user)[0]
            cur.execute(
                "INSERT INTO orders (id, name, phone_number, event_type, questions, answers) VALUES (%s, %s, %s, %s, %s, %s)", 
                (user_info['id'], user_info['name'], user, user_info['service'], ','.join(GLOBAL_FLOWS[user]), ','.join(TEMP_ANSWERS[user]))
            )
            cur.execute("UPDATE users SET service = %s WHERE phone_number = %s", (None, user))
            con.commit()
            cur.close()
            con.close()
            
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        send_order(user)
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        GLOBAL_STEPS[user] = []
        GLOBAL_FLOWS[user] = []
        TEMP_ANSWERS[user] = []

def summarise(user):
    user_info = fetchdata('users', user)[0]
    service = user_info['service']
    text = SUMMARY_MESSAGES.get(service, "Thank you for the details.")
    
    text = text.replace("XYZ", user_info.get('name') or '')
	
    price = SERVICE_FLOWS.get(service, [])[-1][-1] if SERVICE_FLOWS.get(service) else None
    if price:
        text = text.replace("PRICE", f"{price:,}")
    send_msg(user, text)

def send_order(user):
    order_data = fetchdata('orders', user)[0]
    name = fetchdata('users', user)[0]['name']
    print(f"You got an order from {name}! ({user}) 🔥")
    for k, v in order_data.items():
        print(f"{k} : {v}")

# ─── MAIN LOGIC ───────────────────────────────────────────────────────────────
def handle_newuser(user, msg):
    inp = clean_text(msg)
    serv_mw = next((word for word in service_kw_booking.keys() if word in clean_text(inp).split()), None)
    if inp.isdigit() and int(inp) <= 7:
        if NEWUSER_INDEX.get(inp) != 'explore':
            con = init_db()
            if con:
                cur = con.cursor()
                cur.execute("UPDATE users SET intent = %s WHERE phone_number = %s", ('book', user))
                ser = NEWUSER_INDEX.get(inp, "generic_flow")
                cur.execute("UPDATE users SET service = %s WHERE phone_number = %s", (ser, user))
                con.commit()
                cur.close()
                con.close()
            book(user, inp)
        else:
            con = init_db()
            if con:
                cur = con.cursor()
                cur.execute("UPDATE users SET intent = %s WHERE phone_number = %s", ('explore', user))
                con.commit()
                cur.close()
                con.close()
            send_msg(user, "Sure! You can ask about:\n🔹 *services* — what we offer\n🔹 *pricing* — how we charge\n🔹 *events* — types we cover\n🔹 *time* — working hours")
    elif serv_mw:
        con = init_db()
        if con:
            cur = con.cursor()
            cur.execute("UPDATE users SET intent = %s WHERE phone_number = %s", ('book', user))
            ser = service_kw_booking.get(serv_mw, None)
            cur.execute("UPDATE users SET service = %s WHERE phone_number = %s", (ser, user))
            con.commit()
            cur.close()
            con.close()
        book(user, inp)
    else:
        send_msg(user, f"Whoops! That didn't match our menu options. 🎥 Just type a number from 1 to 7 or reply with the service name so I can show you the right details! 😄\n\n{WELCOME_MSG[53:]}")

def logic(inp_raw, user):
    inp = clean_text(inp_raw)
    services_mw = next((word for word in services_kw.keys() if word in clean_text(inp).split()), None)
    events_mw = next((word for word in events_kw.keys() if word in clean_text(inp).split()), None)
    intent_mw = next((intent for intent, keywords in intent_kw.items() if any(word in clean_text(inp).split() for word in keywords)), None)
    responded = False

    user_data = fetchdata('users', user)[0]

    if user_data['looking_service']:
        if inp.isdigit() and int(inp) <= 5:
            if int(inp) == 1:
                send_msg(user, f"Absolutely! ✨\n\nWe do offer {SERVICE_WORD_MAPPING[inp]} 📸🎬\n\n{PORTFOLIO_STATIC_BLOCK['family'][13:].capitalize()}")
            else:
                send_msg(user, f"{PORTFOLIO_STATIC_BLOCK['other'][13:].capitalize()}")
            
            con = init_db()
            if con:
                cur = con.cursor()
                cur.execute("UPDATE users SET looking_service = %s WHERE phone_number = %s", (False, user))
                con.commit()
                cur.close()
                con.close()
            return
        else:
            send_msg(user, "Whoops! That didn't match our menu options. 🎥 Just type a number from 1 to 5 or reply with the service name so I can show you the right details! 😄")

    elif inp in GR_INDEX and user_data['intent'] != 'book':
        responded = True
        send_msg(user, GLOBAL_REPLIES[GR_INDEX[inp]])
    
    elif (any(word in inp for word in ["book", "reserve", "order"]) or inp == '2') and user_data["intent"] != "book":
        responded = True
        if inp == "book" or inp == "2":
            last = user_data['last_order']
            if last and (datetime.date.today() - last).days < 7:
                send_msg(user, "You already have a recent booking with us. 📅\nPlease wait for our team to get back to you, or type *human* to reach us directly.")
                return

            GLOBAL_STEPS[user] = []
            con = init_db()
            if con:
                cur = con.cursor()
                cur.execute("UPDATE users SET intent = %s WHERE phone_number = %s", ('book', user))
                con.commit()
                cur.close()
                con.close()         
            send_msg(user, "Awesome 😄\nLet’s get your booking started.\n\nI’ll ask a few quick questions so our team can understand exactly what you need.\nYou can type *cancel* anytime if you change your mind.")
            book(user, inp)
            return

        send_msg(user, GLOBAL_REPLIES["booking"])
        return

    elif inp == "explore" or inp == "1":
        responded = True
        con = init_db()
        if con:
            cur = con.cursor()
            cur.execute("UPDATE users SET intent = %s WHERE phone_number = %s", ('explore', user))
            con.commit()
            cur.close()
            con.close()
        send_msg(user, "Sure! You can ask about:\n🔹 *services* — what we offer\n🔹 *pricing* — how we charge\n🔹 *events* — types we cover\n🔹 *time* — working hours")

    elif intent_mw == "pricing" and events_mw:
        service = service_kw_booking.get(events_mw)
        price = SERVICE_FLOWS.get(service, "generic_flow")[-1][-1]
        send_msg(user, f"Our pricing for {events_mw} events starts at around *₹{price:,}*.\n\nWe are happy to make your celebrations memorable with our video and photography services! 🎬📸\n\nFor a more accurate quote, please type 'human' to reach out our team!")
        return

    elif intent_mw:
        responded = True
        if intent_mw == "positive_clauses":
            send_msg(user, rd.choice(POSITIVE_REPLIES))
        elif intent_mw == "services":
            send_msg(user, GLOBAL_REPLIES["services"])
            con = init_db()
            if con:
                cur = con.cursor()
                cur.execute("UPDATE users SET looking_service = %s WHERE phone_number = %s", (True, user))
                con.commit()
                cur.close()
                con.close()
        else:
            send_msg(user, GLOBAL_REPLIES[intent_mw])

    elif events_mw:
        responded = True
        send_msg(user, GLOBAL_REPLIES["event_help"].replace("XYZ", events_kw[events_mw]).replace("NUM", "9876543210"))

    elif services_mw:
        responded = True
        send_msg(user, GLOBAL_REPLIES["service_help"].replace("XYZ", services_kw[services_mw]).replace("NUM", "9876543210"))

    if not responded:
        send_msg(get_reply(inp_raw), GLOBAL_REPLIES)

def process(user, msg_body):
    all_users = [_['phone_number'] for _ in fetchdata('users')] # Renamed local variable safely! ⚡
    if user not in all_users:
        initialize_user(user)
        send_msg(user, WELCOME_MSG)
        con = init_db()
        if con:
            cur = con.cursor()
            cur.execute("UPDATE users SET intent = %s WHERE phone_number = %s", ('new_user', user))
            con.commit()
            cur.close()
            con.close()
        return
	
    user_status = fetchdata('users', user)[0]['intent']
    if user_status == 'new_user':
        handle_newuser(user, msg_body)
        return

    if user_status == "book":
        inp = clean_text(msg_body)
        if inp == "cancel":
            con = init_db()
            if con:
                cur = con.cursor()
                cur.execute("UPDATE users SET intent = %s WHERE phone_number = %s", (None, user))
                con.commit()
                cur.close()
                con.close()
            GLOBAL_STEPS[user] = []
            TEMP_ANSWERS[user] = []
            send_msg(user, "Booking cancelled. No worries! Type *book* anytime to start again. 😊")
            return

        if inp in GLOBAL_REPLIES:
            send_msg(user, "Quick answer before we continue:\n\n" + GLOBAL_REPLIES[inp] + "\n\nType *book* to continue where you left off, or *cancel* to start fresh.")
            con = init_db()
            if con:
                cur = con.cursor()
                cur.execute("UPDATE users SET intent = %s WHERE phone_number = %s", (None, user))
                con.commit()
                cur.close()
                con.close()
            return

        book(user, msg_body)
        return

    logic(msg_body, user)

# ─── FLASK ROUTES ─────────────────────────────────────────────────────────────
@app.route("/webhook", methods=["GET"])
def verify_webhook():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")
    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("[Webhook] Verified successfully.")
        return challenge, 200
    return "Forbidden", 403

@app.route("/webhook", methods=["POST"])
def receive_message():
    data = request.get_json()
    try:
        entries = data.get("entry", [])
        for entry in entries:
            for change in entry.get("changes", []):
                value = change.get("value", {})
                if "messages" not in value:
                    continue
                bot_number_id = value.get("metadata", {}).get("phone_number_id")
                for message in value["messages"]:
                    if message.get("type") != "text":
                        continue
                    sender = message["from"]
                    if sender == bot_number_id:
                        continue
                    msg_body = message["text"]["body"]
                    print(f"{sender}: {msg_body}")
                    process(sender, msg_body)
    except Exception as e:
        print(f"[ERROR] {e} ❌")
    return jsonify({"status": "ok"}), 200

@app.errorhandler(404)
def not_found(e):
    return "", 200

if __name__ == "__main__":
    app.run(debug=True, port=5000)
