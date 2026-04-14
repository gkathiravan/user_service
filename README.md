# User Service

Simple FastAPI microservice for user data.

## Run

From project root:

```bash
uvicorn main:app --reload --port 8001 --app-dir service-user
```

## Database

- SQLite file: `service-user/user.db`
- Created automatically on startup
- Seed data inserted if DB is empty

## Endpoints

- `GET /` : service health/status
- `GET /users` : list all users
- `GET /users/{user_id}` : get one user by id
- `GET /users/search?name=alice` : search users by name
- `POST /users` : create user

Example request body for `POST /users`:

```json
{
  "name": "Charlie"
}
```

## Modules

- `main.py` : API routes
- `db.py` : SQLite connection and DB initialization
- `repository.py` : user data queries
- `schemas.py` : request schema models
