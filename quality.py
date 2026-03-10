def validate_docstring(docstring: str) -> bool:
    required = ["Parameters", "Returns"]
    return all(word in docstring for word in required)
