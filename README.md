# ZFlow CRM Dashboard

A simple CRM dashboard built with Flask and PostgreSQL for managing customer conversations.

## Features

* User authentication using Flask sessions
* Client list view
* Chat history retrieval
* Message storage
* PostgreSQL database integration
* Environment variable support using `.env`
* REST API endpoints for frontend integration

## Tech Stack

* Python
* Flask
* PostgreSQL
* psycopg2
* HTML/CSS/JavaScript
* Flask-CORS

## Project Structure

```
project/
│
├── app.py
├── requirements.txt
├── .env.example
│
├── templates/
│   ├── login.html
│   └── index.html
│
├── static/ 
│   └── images/
|       └── ZFlow_Logo.png
│
└── README.md
```

## Environment Variables

Create a `.env` file in the project root:

```
SEC_KEY=your_flask_secret_key
DB_PASSWORD=your_postgres_password
```

## Installation

Clone the repository:

```bash
git clone https://github.com/rbalaji-2007/whatsapp_automation_dashboard
cd whatsapp_automation_dashboard
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Database Setup

Create a PostgreSQL database:

```sql
CREATE DATABASE zflowcrm;
```

Required tables:

### zusers

Stores dashboard user accounts.

### users

Stores client information.

### chats

Stores incoming and outgoing messages.

## Run the Application

```bash
python app.py
```

Open:

```
http://127.0.0.1:5000
```

## Current Limitations

* Passwords are currently stored in plain text.
* Real-time messaging is not implemented yet.
* Message delivery APIs are not integrated.

## Future Improvements

* Password hashing
* WhatsApp API integration
* User roles and permissions
* Analytics dashboard
* Search and filtering
