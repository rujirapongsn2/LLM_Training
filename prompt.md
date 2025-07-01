# Prompt: Design a Frontend-Only Conversational Chat Interface for "AI Library"

## Project Overview

Design a modern, conversational frontend-only chat interface for **AI Library** — a smart university library assistant for students to search books, borrow/return, check borrow status, and receive new book recommendations.

This is a **frontend-only implementation** — focus purely on the visual and interactive layer. All backend functionality will be simulated or mocked.

## Tech Stack

- **UI Framework:** React.js
- **Styling:** TailwindCSS
- **Component Library:** Shadcn UI

## Design Guidelines

### Visual Style
- **Aesthetic:** Clean, minimal academic aesthetic.
- **Colors:** Soft backgrounds (muted blue/white).
- **UI Elements:** Rounded corners and well-spaced chat bubbles with soft shadows and hover transitions.
- **Typography:** A modern sans-serif font like Geist or Space Grotesk.

### Layout
- **Sidebar:** Fixed-height left sidebar with icons or tabs for "Search", "My Books", and "Recommendations".
- **Main Panel:** A vertically scrolling chat window where users interact with the assistant.

### UI Features
- **Chat Bubbles:** Styled for both user and assistant messages.
- **Search Results:** Displayed as interactive cards (title, author, availability badge, "Borrow" button).
- **Borrow Status:** Shown in collapsible message blocks.
- **Recommendations:** Presented in a horizontally scrolling carousel (optional).

### UX Interactions
- **Bot Replies:** Include a typing animation.
- **Message Transitions:** Animate sending/receiving messages smoothly.
- **Button Clicks:** Use soft animations (scale/tap) for feedback.
- **Data:** Use placeholder data and mocked API responses for book details and user status.

## Constraints

- **No Backend:** Mock all data using local state or sample JSON. No server or API code.
- **Responsive Design:** Ensure the interface works well on mobile, tablet, and desktop.
- **Technology:** Use only React, TailwindCSS, and Shadcn UI.

## Final Goal

The goal is to simulate a polished and responsive library chatbot that looks and feels real, even if the logic is mocked.