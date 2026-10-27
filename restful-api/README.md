# Python - RESTful API

## Description
This project covers consuming and building web APIs with Python. It starts with calling a public REST API using `requests`, then builds a minimal API with the standard-library `http.server`, rebuilds a more complete one with **Flask**, and finally secures it with **Basic Authentication** and **JWT** (JSON Web Tokens) including role-based access.

All scripts are written for **Python 3.8+**.

## 📝 Learning Objectives
* Send HTTP `GET` requests with `requests`, read status codes and parse JSON responses.
* Export API data to a CSV file with `csv.DictWriter`.
* Build a simple HTTP server by subclassing `BaseHTTPRequestHandler` and routing on `self.path`.
* Build a REST API with Flask: routes, JSON responses (`jsonify`), `POST` bodies and HTTP status codes (`201`, `400`, `404`, `409`).
* Protect routes with HTTP Basic Auth (`Flask-HTTPAuth`) and password hashing (`werkzeug.security`).
* Issue and verify JWT tokens (`Flask-JWT-Extended`) and restrict a route to the `admin` role (`403`).

## 🛠️ Requirements & Engineering Constraints
* **OS:** Ubuntu 20.04 LTS
* **Interpreter:** `python3` (version 3.8.5+)
* **Style Guide:** PEP 8 (check with `pycodestyle`).
* **Dependencies:** `requests`, `flask`, `flask-httpauth`, `flask-jwt-extended`.

```bash
pip3 install requests flask flask-httpauth flask-jwt-extended
```

## 📁 File List & Tasks Directory

| File | Task Title | Description |
| :--- | :--- | :--- |
| `task_02_requests.py` | Consume an API | `fetch_and_print_posts()` prints the status code and titles of the JSONPlaceholder posts; `fetch_and_save_posts()` saves their `id`, `title` and `body` to `posts.csv`. |
| `task_03_http_server.py` | Develop a simple API using `http.server` | `SimpleAPIHandler` serves `/` (text), `/data` and `/info` (JSON), `/status` (`OK`) and returns a `404` for anything else; runs on port 8000. |
| `task_04_flask.py` | Develop a simple API using Flask | In-memory user API: `/`, `/data` (list of usernames), `/status`, `/users/<username>` and `POST /add_user` with validation (`400` / `409` / `201`). |
| `task_05_basic_security.py` | API Security and Authentication | `/basic-protected` (Basic Auth), `POST /login` (returns a JWT), `/jwt-protected` (JWT required) and `/admin-only` (JWT + `admin` role), with custom `401` error handlers. |

---

## 🚀 Execution & Testing

### Consuming an API
```bash
python3 -c "import task_02_requests as t; t.fetch_and_print_posts()"
```

### Running the servers
```bash
python3 task_03_http_server.py        # http://localhost:8000
python3 task_04_flask.py              # http://localhost:5000
python3 task_05_basic_security.py     # http://localhost:5000
```

```bash
curl http://localhost:5000/status
curl -X POST -H "Content-Type: application/json" \
     -d '{"username": "jane", "name": "Jane"}' http://localhost:5000/add_user
```

### Testing the secured API
```bash
curl -u user1:password http://localhost:5000/basic-protected

TOKEN=$(curl -s -X POST -H "Content-Type: application/json" \
     -d '{"username": "admin1", "password": "password"}' \
     http://localhost:5000/login | python3 -c "import sys, json; print(json.load(sys.stdin)['access_token'])")
curl -H "Authorization: Bearer $TOKEN" http://localhost:5000/admin-only
```

### Checking PEP 8 Compliance
```bash
pycodestyle task_04_flask.py
```

> **Note:** the demo users and the `JWT_SECRET_KEY` in `task_05_basic_security.py` are for learning purposes only; use environment variables for real secrets.

---

## 👤 Author
* **Student:** [RebornLPB](https://github.com/RebornLPB)
* **GitHub:** [https://github.com/RebornLPB](https://github.com/RebornLPB)
* **School:** [Holberton School](https://www.holbertonschool.com/)
