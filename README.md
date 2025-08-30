# AI-Powered Resume Generator

## Setup Instructions
1. Create virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate   # Windows
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run backend:
   ```bash
   cd backend
   uvicorn main:app --reload
   ```

4. Run frontend:
   ```bash
   cd frontend
   streamlit run streamlit_app.py
   ```

5. Open browser:
   - Backend: http://127.0.0.1:8000/docs
   - Frontend: http://localhost:8501
