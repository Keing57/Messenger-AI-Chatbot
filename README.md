# Messenger AI Chatbot

A fun experimental project where I created a digital clone of myself. The goal was to build a chatbot that can respond to Messenger texts exactly the way I would, using my vocabulary, slang, and typical sentence structures.

## Architecture
This project consists of two main parts:
1.  **The Scraper:** A Python automation script utilizing Selenium WebDriver to securely log into Messenger, navigate chats, and extract historical conversation data to build a custom dataset.
2.  **The Brain:** An integration with the Gemini Pro API, prompt-engineered and context-fed with the scraped dataset to generate responses that match my personal tone.

## Tech Stack
*   Python 3
*   Selenium (WebDriver)
*   Google Gemini Pro API

*Note: For privacy reasons, the dataset and my personal API keys are not included in this repository. To run this yourself, you will need to provide your own scraping target and credentials.*
