def generate_docstring(func: dict) -> str:
    name = func["name"]
    args = func["args"]
    returns = func["returns"]

    args_block = "\n".join([f"    {arg}: description" for arg in args])

    docstring = f'''"""
{name} function.

Parameters:
{args_block if args_block else "    None"}

Returns:
    {returns}
"""'''

    return docstring
