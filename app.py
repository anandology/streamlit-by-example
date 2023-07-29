import streamlit as st
from pathlib import Path
import re

st.set_page_config(page_title="Streamlit by Example")
st.title("Streamlit by Example")


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

def show_example(name):
    doc, code = read_file(name)

    st.divider()
    st.markdown(doc)

    with st.expander("Show Code"):
        st.code(code)
    st.divider()
    exec(code)

root = Path("examples")
paths = {f.name: f for f in root.glob("*.py")}

page = st.selectbox("Select Page", paths.keys())
show_example(page)
