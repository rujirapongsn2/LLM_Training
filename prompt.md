# Prompt: Design a Modern Conversational Chat Interface for "AI Library"

## Project Overview

Design a modern, conversational chat interface for **AI Library** — a smart university library assistant that helps students find and borrow books easily. The chatbot should be user-friendly and intelligent, supporting four core features.

The interface must be built using **React.js**, styled with **TailwindCSS**, and use **Shadcn UI** components for polished UI consistency. Backend logic will be powered by **Python**, with a lightweight **SQLite** database handling book and user records.

## Core Features

1.  **Book Search:** Find books using natural language.
2.  **Borrowing/Returning Books:** Manage the entire loan process within the chat.
3.  **Borrowing Status Checking:** Allow users to check the status of their current loans.
4.  **New Book Recommendations:** Proactively suggest new and relevant books.

## Design Guidelines

### Visual Style
- **Aesthetic:** Clean academic aesthetic with calming colors.
- **Color Palette:** Off-white, muted blue, sage green.
- **UI Elements:** Rounded chat bubbles, smooth padding.
- **Typography:** Readable and modern fonts (e.g., Geist or Space Grotesk).

### Layout
- **Sidebar:** A fixed-height sidebar with primary navigation options like “Search”, “My Books”, and “Recommendations”.
- **Main Area:** A dedicated chat window where the bot interacts conversationally with the user.

### Functionality
- **Natural Language Queries:** Users can type queries naturally, such as “หา Python เบื้องต้น” or “หนังสือที่ฉันยืมอยู่”.
- **Rich Book Results:** Display search results as rich cards containing the book's title, author, availability, and a "Borrow" button.
- **In-Chat Confirmation:** Handle the borrowing process with confirmation flows and real-time updates directly within the chat.
- **Dynamic Recommendations:** Suggest new arrivals dynamically with thumbnails and short summaries.

### Interactions
- **Typing Indicator:** Show a typing indicator when the chatbot is preparing a response.
- **Smooth Animations:** Use smooth fade/slide animations for new chat messages.
- **Button Feedback:** Animate borrow buttons on click to provide visual feedback.
- **Localization:** Include an option to switch the UI language between Thai and English.

## Technical Notes

- **Frontend:** All chat interactions are to be handled within React components.
- **Database:** Use SQLite as a local storage solution for managing the book inventory and user borrowing history.
- **Styling:** Utilize TailwindCSS for fast layout and spacing control. The default theme should be extended with the custom color palette.
- **Accessibility:** Ensure the interface is fully accessible, supporting screen readers and keyboard navigation.

## Final Goal

The final product should feel like a smart, helpful university companion — friendly, quick, and intuitive. Think of it as **“ChatGPT meets the campus library desk.”**