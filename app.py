import streamlit as st


def add_docstrings_to_code(code):
    lines = code.split("\n")
    updated_lines = []

    for line in lines:
        updated_lines.append(line)

        stripped = line.strip()

        # Check if line is a function definition
        if stripped.startswith("def "):
            function_name = stripped.split("(")[0].replace("def ", "")

            indent = " " * (len(line) - len(line.lstrip()) + 4)

            docstring = f'{indent}"""This function {function_name} performs its intended operation."""'
            updated_lines.append(docstring)

    return "\n".join(updated_lines), None


# -------- Streamlit UI --------
st.title(" Automatic Python Docstring Generator")

uploaded_file = st.file_uploader("Upload a Python (.py) file", type=["py"])

if uploaded_file is not None:
    code = uploaded_file.read().decode("utf-8")

    updated_code, error = add_docstrings_to_code(code)

    if error:
        st.error(error)
    else:
        st.success("Docstrings Generated Successfully!")

        st.subheader("Updated Code Preview")
        st.code(updated_code, language="python")

        st.download_button(
            label="Download Updated File",
            data=updated_code,
            file_name="updated_code.py",
            mime="text/x-python"
        )
