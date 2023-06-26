def logo(logoname,quality):
    from PIL import Image
    import streamlit as st
    image = Image.open(logoname)
    # Improve image quality
    image.save("image_name2.jpg", quality=quality)
    image = Image.open('image_name2.jpg')
    image = image.resize((100, 100))
    st.image(image)


