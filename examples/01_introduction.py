"""
## Introduction

**Title**

Typically, the first thing you do in a streamlit app is set the title of a page using `st.title`.

**Headings**

You can use `st.header` and `st.subheader` to add heading and subheadngs for sections.

**Writing Content**

The `st.write` function can be used to write any text, pandas dataframe or any python object.

If you would like to write formatted text, you can use `st.markdown`.
"""
import streamlit as st

st.title("Hello, world!")

st.header("1. Plain Text")
st.write("contents of section 1...")

st.header("2. Markdown Text")
st.markdown("**Bold** and *Italic*")
