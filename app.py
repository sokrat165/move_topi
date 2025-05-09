!pip install joblib
import streamlit as st
from PIL import Image
from joblib import load
pipeline = load('pipeline_tuned_stem.joblib')
category_images = {
    'Alice in Borderland': ['product_alice in pordant/0.jpg',
                  'product_alice in pordant/1.jpg',
                 'product_alice in pordant/2.jpg',
                 'product_alice in pordant/3.jpg',
                 'product_alice in pordant/4.jpg',
                 'product_alice in pordant/5.jpg',
                 'product_alice in pordant/6.jpg',
                 'product_alice in pordant/7.jpg'],
    'Physical: 100': ['product_alice in pordant/0.jpg', 'product_alice in pordant/1.jpg'],
    'Squid Game': ['product_alice in pordant/0.jpg',
                     'product_alice in pordant/1.jpg',
                     'product_alice in pordant/2.jpg',
                     'product_alice in pordant/3.jpg',
                     'product_alice in pordant/4.jpg']
}
# Load the fitted model
st.title("Text Classification and Image Display")
user_input = st.text_area("COMMENT PLEASE")
if user_input:
    # الحصول على التصنيف
    predicted_category = pipeline.predict([user_input])[0]
    
    # عرض التصنيف المتوقع
    st.write(f"التصنيف المتوقع: {predicted_category}")
    
    # عرض الصور بناءً على التصنيف
    if predicted_category in category_images:
        for image_path in category_images[predicted_category]:
            st.image(image_path, use_column_width=True, caption=f"صورة من تصنيف {predicted_category}")
    else:
        st.write("لا توجد صور لهذا التصنيف.")
