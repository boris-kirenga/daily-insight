#  Daily Insight Dispatcher

A minimalist, full-stack micro-project that bridges a **Python backend** with a **Next.js frontend**.

Daily Insight Dispatcher features a simple, single-button control panel that triggers an asynchronous Python service to generate an AI-powered insight and automatically deliver it to your inbox.

Built with FastAPI, Next.js, Google Gemini, and Resend, the application demonstrates a clean separation of concerns between frontend interactions, AI-powered content generation, and email delivery.

##  Features

- **Decoupled Architecture:** Independent FastAPI backend and Next.js App Router frontend.
- **Asynchronous AI Generation:** Integrates the Google Gen AI SDK to generate lightweight, AI-powered insights without blocking the application.
- **Automated Email Delivery:** Uses Resend to deliver generated insights directly to your inbox.
- **Cross-Origin Resource Sharing (CORS):** Configured to allow secure communication between the frontend and backend during development.
- **Environment Variable Isolation:** Keeps sensitive API credentials on the backend while exposing only necessary configuration to the frontend.
- **Minimalist Interface:** A simple, single-button dashboard for triggering the entire workflow.

## 🛠️ Tech Stack

| Technology | Purpose |
| --- | --- |
| Python | Backend programming language |
| FastAPI | Backend API framework |
| Uvicorn | ASGI development server |
| Google Gen AI SDK | AI-powered insight generation |
| Resend | Email delivery service |
| Next.js | Frontend framework |
| React | User interface |
| TypeScript | Frontend type safety |

## 📁 Project Structure

text

```text
daily-insight-dispatcher/
│
├── backend/
│   ├── main.py
│   ├── .env
│   └── requirements.txt
│
└── frontend/
    ├── app/
    │   └── page.tsx
    ├── .env.local
    └── package.json
```

## ⚙️ Getting Started

Follow these instructions to set up and run the project locally.

### Prerequisites

Make sure you have the following installed:

- [Python 3.9+](<https://www.python.org/downloads/>)
- [Node.js and npm](<https://nodejs.org/>)
- A [Google Gemini API key](<https://aistudio.google.com/apikey>)
- A [Resend API key](<https://resend.com/>)

## 🐍 Backend Setup (Python & FastAPI)

### 1\. Navigate to the Backend Directory

bash

```bash
cd backend
```

### 2\. Create and Activate a Virtual Environment

Create an isolated Python environment:

bash

```bash
python -m venv venv
```

Activate the environment:

**Windows:**

bash

```bash
venv\Scripts\activate
```

**macOS / Linux:**

bash

```bash
source venv/bin/activate
```

### 3\. Install Dependencies

Install the required Python packages:

bash

```bash
pip install fastapi uvicorn google-genai python-dotenv resend
```

Alternatively, add the dependencies to `requirements.txt`:

text

```text
fastapi
uvicorn
google-genai
python-dotenv
resend
```

Then install them using:

bash

```bash
pip install -r requirements.txt
```

### 4\. Configure Environment Variables

Create a `.env` file inside the `backend/` directory:

env

```env
GEMINI_API_KEY=your_gemini_api_key_here
RESEND_API_KEY=your_resend_api_key_here
TO_EMAIL=your_verified_destination_email@example.com
```

Replace the placeholder values with your actual API credentials and destination email address.

**Important:** Never commit your `.env` file or expose your API keys in frontend code.

### 5\. Start the Backend Server

Run the FastAPI application using Uvicorn:

bash

```bash
uvicorn main:app --reload
```

The backend API will be available at:

text

```text
http://localhost:8000
```

FastAPI interactive API documentation is available at:

text

```text
http://localhost:8000/docs
```

## 💻 Frontend Setup (Next.js & React)

### 1\. Navigate to the Frontend Directory

Open a new terminal window and navigate to the frontend folder:

bash

```bash
cd frontend
```

### 2\. Install Dependencies

Install the required Node.js packages:

bash

```bash
npm install
```

### 3\. Configure Environment Variables

Create a `.env.local` file inside the `frontend/` directory:

env

```env
NEXT_PUBLIC_BACKEND_URL=http://localhost:8000
```

This variable defines the URL used by the frontend to communicate with the FastAPI backend.

### 4\. Start the Development Server

Run the Next.js development server:

bash

```bash
npm run dev
```

The frontend application will be accessible at:

text

```text
http://localhost:3000
```

Open the URL in your browser to access the Daily Insight Dispatcher dashboard.

## 📡 API Reference

### Trigger Insight Generation and Email Dispatch

Triggers the backend service to generate an AI-powered insight and send it to the configured email address.

| Property | Value |
| --- | --- |
| Endpoint | `/trigger` |
| Method | `POST` |
| Content-Type | `application/json` |
| Success Status | `200 OK` |

**Example Success Response:**

json

```json
{
  "status": "success",
  "message": "Insight successfully generated and dispatched!"
}
```

## 🔄 Application Workflow

The application follows a simple three-step process:

1. **User Interaction:** The user clicks the trigger button on the Next.js dashboard.
2. **AI Generation:** The frontend sends a POST request to the FastAPI backend, which uses Google Gemini to generate an insight.
3. **Email Dispatch:** The generated insight is delivered to the configured inbox through Resend.

text

```text
┌──────────────────────┐
│   Next.js Frontend   │
│                      │
│    [Trigger Button]  │
└──────────┬───────────┘
           │
           │ POST /trigger
           ▼
┌──────────────────────┐
│   FastAPI Backend    │
│                      │
│  Google Gemini API   │
│  Insight Generation  │
└──────────┬───────────┘
           │
           │ Generated Insight
           ▼
┌──────────────────────┐
│     Resend API       │
│                      │
│    Email Delivery    │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│    User's Inbox      │
│                      │
│   Daily AI Insight   │
└──────────────────────┘
```

## 🔐 Security Notes

- Keep API keys and sensitive credentials in backend environment variables.
- Never expose `GEMINI_API_KEY` or `RESEND_API_KEY` through client-side code.
- Ensure `.env` and `.env.local` are included in `.gitignore`.
- Restrict CORS origins to trusted frontend domains when deploying to production.
- Use HTTPS and appropriate request validation in production environments.

## 🚀 Future Improvements

Potential enhancements include:

- [ ]Scheduled daily insight delivery.
- [ ]User-configurable email destinations.
- [ ]Customizable insight categories and topics.
- [ ]Insight history and storage.
- [ ]User authentication.
- [ ]Deployment with production-ready infrastructure.
- [ ]Retry handling and improved error reporting.

## 📄 License

This project is open-source and available for learning, experimentation, and personal development. Add a license file if you intend to distribute it under a specific open-source license.

---

**Built with ❤️ using Python, FastAPI, Next.js, Google Gemini, and Resend.**

Small recommendation: Add a `.gitignore` file at the project root to exclude `backend/.env`, `frontend/.env.local`, Python virtual environments, `node_modules`, and build artifacts before pushing the project to GitHub.