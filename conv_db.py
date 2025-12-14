# conv_db.py
def get_conversational_response(query):
    """Return conversational responses based on query."""
    query = query.lower().strip()

    greetings = ["hi", "hello", "hey", "good morning", "good afternoon", "good evening"]
    farewells = ["bye", "goodbye", "see you", "exit", "quit"]

    if any(greet in query for greet in greetings):
        return "Hello! How can I help you today?"

    if any(fare in query for fare in farewells):
        return "Goodbye! Have a nice day!"

    if "how are you" in query:
        return "I'm doing great! Thanks for asking. How can I assist you?"

    if "your name" in query:
        return "I'm LUMO, your personal AI assistant."

    if "thank" in query:
        return "You're welcome! Is there anything else I can help with?"

    if "joke" in query:
        return "Why don't scientists trust atoms? Because they make up everything!"

    return None