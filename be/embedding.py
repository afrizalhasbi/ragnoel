from database import get_connection

def embed(string):
    conn, cursor = get_connection()
    model = call_embed_model()
    # embedding = command pakai conn & cursor
    pass

def call_embed_model():
    return None
