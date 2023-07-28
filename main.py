import streamlit as st
from pathlib import Path
import re

def select_page():
    st.title(f"Streamlit by Examples")
    name = st.selectbox("Select Page", paths.keys())

    st.divider()
    return name

re_doc = re.compile('"""(.*)"""(.*)', re.M|re.DOTALL)
def read_file(name):
    path = paths[name]
    code = path.read_text()
    m = re_doc.match(code)
    if m:
        doc, code = m.groups()
        return doc.strip(), code.strip()
    else:
        return "", code

def show_demo(name):
    doc, code = read_file(name)

    st.markdown(doc)

    st.code(code)
    st.divider()

    exec(code)


root = Path("demo")
paths = {f.name: f for f in root.glob("*.py")}

page = select_page()
show_demo(page)
