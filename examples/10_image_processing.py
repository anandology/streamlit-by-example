"""
## Image Processing

Example of simple image processing operations using `numpy`.
"""

import streamlit as st
from PIL import Image
import numpy as np

image = Image.open("examples/images/rose.jpg")
imgdata = np.array(image)

brightness = st.slider(
    "Brightness",
    min_value=-100,
    max_value=100,
    value=0,
    step=1)

def update_brightness(imgdata, brightness):
    import numpy as np
    # delta will be from -255 to 255
    delta = 255 * brightness/100
    x = imgdata + delta
    x = x.clip(0, 255).astype(np.uint8)
    return x

c1, c2 = st.columns(2)
with c1:
    st.image(imgdata, "Original Image")

with c2:
    imgdata2 = update_brightness(imgdata, brightness)
    st.image(imgdata2, "Updated Image")