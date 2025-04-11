# ABC Lighting Conversational AI Chatbot

A Django-based conversational AI chatbot designed for ABC Lighting Company. This project simulates a customer service representative that handles inquiries about the company and its three solar-powered lighting products. It features a customizable Django admin panel, a REST API endpoint for chat interactions, and a modern animated frontend that dynamically displays stored product images.

## Overview

The ABC Lighting Chatbot provides customers with detailed information about solar-powered street, driveway, and wall lights. Users interact with the chatbot via a responsive and intuitive user interface that supports rich media (product images) and animated interactions. The project leverages Django and Django REST Framework on the backend and uses HTML5, CSS3, and JavaScript on the frontend.

## Features

- **Conversational AI:**  
  - Handles user queries about products and company information.
  - Distinguishes between general questions and specific product inquiries using exact name matching and keyword recognition.

- **Customizable Admin Panel:**  
  - Manage company details, product information, and product images using Django’s built-in admin interface.
  
- **Rich Product Details:**  
  - Each product includes a name, description, detailed specifications, and an uploaded image.
  
- **Modern, Animated UI:**  
  - Animated, responsive single-page chat interface with fade-in message effects and typing indicators.
  - Uses a gradient animated background and modern typography for a polished look.

- **REST API Endpoint:**  
  - The `/api/converse/` endpoint handles chat messages and returns HTML-formatted responses (including images) to be rendered on the frontend.

## Technologies Used

- **Backend:** Python, Django, Django REST Framework
- **Frontend:** HTML5, CSS3, JavaScript, Font Awesome, Google Fonts
- **Database:** SQLite (default configuration)
- **Media Handling:** Django ImageField, MEDIA_ROOT and MEDIA_URL for serving uploaded images

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/abc-lighting-chatbot.git
   cd abc-lighting-chatbot
