# Flask Web App Tutorial (Auth + SQLite)

A minimal Flask application demonstrating **user registration**, **login/logout**, session management with **Flask‑Login**, and **SQLite** persistence via **SQLAlchemy**. Uses Bootstrap-styled templates and flash messages.


## ✨ Features
- User **Sign Up / Login / Logout**
- Session management via **Flask‑Login**
- **SQLite** database with **SQLAlchemy**
- Bootstrap 4 layout + flash alerts
- Blueprint structure: `views` (pages) & `auth` (auth routes)
- Accessibility tweaks (navbar toggler/alerts, `lang` attribute)


## 🧱 Tech stack
- Python 3.9+
- Flask, Flask‑Login, Flask‑SQLAlchemy
- SQLite
- Jinja2 + Bootstrap 4


## 🗂 Project structure
```
FLASK WEB APP TUTORIAL/
├─ main.py
├─ database.db                # created on first run
└─ website/
   ├─ __init__.py             # app factory, login manager, DB
   ├─ models.py               # User, Note models
   ├─ views.py                # public routes (home)
   ├─ auth.py                 # login, logout, sign-up
   ├─ static/
   │  └─ index.js
   └─ templates/
      ├─ base.html
      ├─ home.html
      ├─ login.html
      └─ sign_up.html
```


## 🚀 Getting started

### 1) Create & activate a virtual environment
```bash
# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Windows (PowerShell)
py -m venv venv
.env\Scripts\Activate.ps1
```

### 2) Install dependencies
```bash
pip install flask flask_sqlalchemy flask_login
```

*(Optional) Save a requirements file:*
```bash
pip freeze > requirements.txt
```

### 3) Run the app
**Option A – Python entrypoint**
```bash
python main.py
```
**Option B – Flask CLI**
```bash
export FLASK_APP=main.py
export FLASK_ENV=development  # auto-reload + debugger
flask run
```
Then open: <http://127.0.0.1:5000>


## 🔑 Usage flow
1. Visit **/sign-up**, create an account.  
2. You’ll be logged in and redirected to **/** (Home).  
3. Use **/logout** to end the session.  
4. Use **/login** to log back in.


## 🗃 Database
- Default DB: `sqlite:///database.db` (created on first run).
- Models in `website/models.py`:
  - `User(id, email, password, first_name, notes)`
  - `Note(id, data, date, user_id)`
- To reset during development, stop the server, delete `database.db`, then run again.


## ⚙️ Configuration
`website/__init__.py` sets:
```python
app.config['SECRET_KEY'] = 'dev-secret-change-me'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
```
Replace the secret in production and prefer environment variables.


## 🧭 Blueprints & routes
- `views` blueprint
  - `/` → `home.html`
- `auth` blueprint
  - `/login`  (GET/POST)
  - `/logout` (GET, protected)
  - `/sign-up` (GET/POST)


## 🎨 Templates & accessibility
- `base.html` includes Bootstrap CSS/JS and a navbar.
- a11y warnings (Edge/axe) fixed by:
  - `lang="en-GB"` on `<html>`
  - `aria-label`/`title` on navbar toggler
  - `aria-label="Close"` on alert close buttons


## 🧰 Troubleshooting
- **`npm run dev` fails** → This is a Flask app; you don’t need npm.
- **`zsh: command not found: #`** → You pasted comment lines; they aren’t commands.
- **`Created Database!` twice** → Normal with Flask’s dev auto‑reloader.
- **Flask‑Login errors** → Ensure `LoginManager` is initialised and `@user_loader` is defined.


## 🛣 Roadmap 
- Password reset flow (email token)
- CSRF protection via Flask‑WTF forms
- Role-based access / admin
- Database migrations (Flask‑Migrate)
- Proper asset pipeline if frontend grows


## 📄 Licence
MIT 
