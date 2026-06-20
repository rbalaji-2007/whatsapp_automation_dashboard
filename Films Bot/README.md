# WhatsApp Business Automation Platform

A Python-based automation platform that integrates with the WhatsApp Cloud API to automate customer interactions, lead collection, service enquiries, and booking workflows.

The system is designed to help businesses handle customer communication efficiently through structured conversational flows while maintaining customer data in a PostgreSQL database.

---

## Features

### WhatsApp Integration

* WhatsApp Cloud API webhook support
* Automated message handling
* Real-time customer interaction
* Verification webhook endpoint

### Customer Management

* User onboarding
* Customer state tracking
* Conversation management
* Message analytics

### Booking Automation

* Multi-step booking workflows
* Dynamic service selection
* Lead qualification
* Automated order collection

### Database Integration

* PostgreSQL support
* Persistent customer storage
* Order management
* Customer activity tracking

### AI Support

* AI-powered fallback responses
* Natural language processing integration
* Intent-based routing

---

## Tech Stack

### Backend

* Python
* Flask

### Database

* PostgreSQL

### APIs

* WhatsApp Cloud API

### Libraries

* Requests
* Psycopg2
* Python Dotenv

---

## Project Structure

```text
project/
├── app.py
├── ai.py
├── mapping.py
├── replies.py
├── data.py
├── requirements.txt
├── .env.example
└── README.md
```

---

## Environment Variables

Create a `.env` file and configure:

```env
VERIFY_TOKEN=your_verify_token
ACCESS_TOKEN=your_access_token
PHONE_NUMBER_ID=your_phone_number_id
SQL_PASSWORD=your_database_password
```

---

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

---

## Use Cases

* Photography & Videography Businesses
* Appointment Booking Systems
* Service-Based Businesses
* Customer Support Automation
* Lead Generation Workflows

---

## Learning Outcomes

This project explores:

* REST API Integration
* Webhook Development
* PostgreSQL Database Design
* Conversation Flow Management
* Business Process Automation
* AI-Assisted Customer Communication

---

## Disclaimer

This repository is intended for educational and portfolio purposes. All sensitive credentials, customer data, business information, and production configurations have been removed.
