from db import get_connection


def _row_to_user(row) -> dict:
    return {"id": row["id"], "name": row["name"]}


def get_user_by_id(user_id: int) -> dict | None:
    with get_connection() as conn:
        row = conn.execute("SELECT id, name FROM users WHERE id = ?", (user_id,)).fetchone()

    if not row:
        return None
    return _row_to_user(row)


def list_all_users() -> list[dict]:
    with get_connection() as conn:
        rows = conn.execute("SELECT id, name FROM users ORDER BY id").fetchall()

    return [_row_to_user(row) for row in rows]


def search_users_by_name(name: str) -> list[dict]:
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT id, name FROM users WHERE name LIKE ? ORDER BY id",
            (f"%{name}%",),
        ).fetchall()

    return [_row_to_user(row) for row in rows]


def create_new_user(name: str) -> dict:
    with get_connection() as conn:
        cursor = conn.execute("INSERT INTO users(name) VALUES (?)", (name,))
        conn.commit()

    return {"id": cursor.lastrowid, "name": name}
