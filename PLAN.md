
# Propaganda Detector - Implementation Plan

This document outlines the step-by-step plan for building the Propaganda Detector application.

## Phase 1: Backend (FastAPI)

**Objective:** Create a robust API that can analyze text and URLs for propaganda.

*   **Step 1.1: Project Setup**
    *   Create a `backend` directory.
    *   Set up a Python virtual environment inside `backend`.
    *   Install dependencies: `fastapi`, `uvicorn`, `requests`, `beautifulsoup4`, `pydantic`, `python-dotenv`.
    *   Create `backend/main.py` and `backend/.env`.

*   **Step 1.2: API Endpoint & Models**
    *   In `main.py`, create a `/analyze` endpoint (POST request).
    *   Define Pydantic models for the request (`text` or `url`) and the response (`propaganda_score`, `identified_techniques`, `explanation`).

*   **Step 1.3: URL Content Fetching**
    *   Create a helper function in a new `backend/utils.py` file to fetch and parse text content from a URL using `requests` and `BeautifulSoup`.

*   **Step 1.4: Gemini API Integration**
    *   Create a `backend/gemini_service.py` file.
    *   Define a function `analyze_text` that takes text as input.
    *   This function will contain the prompt for the Gemini API. The prompt will instruct the model to act as a propaganda analysis expert, identify techniques, provide a score from 0.0 to 1.0, and give an explanation.
    *   For initial development, this function will return a mock, hard-coded result.
    *   We will use the `.env` file for the Gemini API key.

*   **Step 1.5: CORS Configuration**
    *   Add CORS middleware to the FastAPI app in `main.py` to allow requests from our web frontend.

*   **Step 1.6: Testing**
    *   Manually test the `/analyze` endpoint using `curl` or a similar tool to ensure it handles both text and URL inputs correctly.

## Phase 2: Web Frontend (React)

**Objective:** Build a clean, user-friendly web interface for the application.

*   **Step 2.1: Project Setup**
    *   Use `npx create-react-app frontend --template typescript` to create the `frontend` directory.
    *   Install dependencies: `axios` (for API requests) and `bootstrap`.

*   **Step 2.2: UI Components**
    *   Create a `frontend/src/components` directory.
    *   Create `PropagandaForm.tsx` for the URL and text inputs.
    *   Create `ResultsDisplay.tsx` to show the analysis results in a user-friendly format (e.g., using progress bars and cards).
    *   Create a `LoadingSpinner.tsx` component.

*   **Step 2.3: API Service**
    *   Create a `frontend/src/services/api.ts` file to encapsulate the logic for making requests to the backend API.

*   **Step 2.4: Main App Component**
    *   In `frontend/src/App.tsx`, assemble the UI components.
    *   Manage the application's state (form inputs, loading status, API results) using React hooks (`useState`, `useEffect`).

*   **Step 2.5: Styling**
    *   Import `bootstrap/dist/css/bootstrap.min.css` in `frontend/src/index.tsx`.
    *   Apply styling to components to ensure a polished look and feel.

## Phase 3: Mobile App (Flutter)

**Objective:** Create a cross-platform mobile app for both Android and iOS.

*   **Step 3.1: Project Setup**
    *   Run `flutter create mobile` to create the `mobile` directory.
    *   Add the `http` package to `pubspec.yaml` for making API requests.

*   **Step 3.2: API Service**
    *   Create a `mobile/lib/services` directory.
    *   Create `api_service.dart` to handle communication with the backend API.
    *   Define Dart models for the request and response data.

*   **Step 3.3: UI (Widgets)**
    *   In `mobile/lib/main.dart`, build the main application UI.
    *   Create a `HomeScreen` widget that will contain the input form and results display.
    *   Use `TextField` for user input and an `ElevatedButton` to submit.
    *   Display the results using `Card` and `LinearProgressIndicator` widgets.

*   **Step 3.4: State Management**
    *   Use a `StatefulWidget` and `setState` for basic state management to handle user input, loading states, and displaying results.
