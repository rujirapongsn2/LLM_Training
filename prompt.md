Design a modern, conversational chat interface for AI Library — a smart university library assistant that helps students find and borrow books easily. The chatbot should be user-friendly and intelligent, supporting four core features: book search, borrowing/returning books, borrowing status checking, and new book recommendations.

The interface must be built using React.js, styled with TailwindCSS, and use Shadcn UI components for polished UI consistency. Backend logic will be powered by Python, with a lightweight SQLite database handling book and user records.

Design Guidelines:
Visual Style: Clean academic aesthetic with calming colors (off-white, muted blue, sage green). Rounded chat bubbles, smooth padding, and readable typography (e.g., Geist or Space Grotesk).
Layout: Fixed-height sidebar with options like “Search”, “My Books”, “Recommendations”. Main area is a chat window where the bot interacts conversationally.
Functionality:
Users can type natural language queries like “หา Python เบื้องต้น” or “หนังสือที่ฉันยืมอยู่”.
Book results appear as rich cards (title, author, availability, borrow button).
When borrowing, confirmation flows appear in chat with real-time updates.
Recommendations dynamically suggest new arrivals with thumbnails and summaries.
Interactions:
Typing indicator for chatbot
Smooth fade/slide for chat messages
Borrow buttons animate on click
Option to switch between Thai/English in the UI
Technical Notes:
All chat interactions handled in React components
SQLite serves as local storage for books and user borrowing history
Use Tailwind for fast layout and spacing control; extend with custom colors if needed
Ensure accessibility for screen readers and keyboard navigation
This should feel like a smart, helpful university companion — friendly, quick, and intuitive. Think of it as “ChatGPT meets campus library desk.”