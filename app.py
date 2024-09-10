import streamlit as st
import pandas as pd
import os

# File path for storing reviews
REVIEWS_FILE = 'reviews.csv'

# Load or initialize reviews
if os.path.exists(REVIEWS_FILE):
    reviews = pd.read_csv(REVIEWS_FILE)
    # Ensure all expected columns are present
    for col in ['Name', 'Product', 'Satisfaction', 'Feedback']:
        if col not in reviews.columns:
            reviews[col] = pd.NA
else:
    reviews = pd.DataFrame(columns=['Name', 'Product', 'Satisfaction', 'Feedback'])

# Initialize reviews in session state
if 'reviews' not in st.session_state:
    st.session_state['reviews'] = reviews.to_dict(orient='records')

# Custom CSS for styling
st.markdown("""
    <style>
    body {
        background-color: #f4f4f9;
        font-family: 'Arial', sans-serif;
    }
    .title {
        text-align: center;
        color: #4a90e2;
        font-size: 3.5rem;
        font-family: 'Georgia', serif;
        margin-top: 20px;
    }
    .header {
        text-align: center;
        color: #4a90e2;
        font-size: 2.5rem;
        font-family: 'Georgia', serif;
        margin-top: 20px;
    }
    .form {
        border: 1px solid #ddd;
        padding: 25px;
        border-radius: 15px;
        background-color: #fff;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin: 20px;
    }
    .review {
        margin-top: 15px;
        padding: 15px;
        border-radius: 10px;
        background-color: #fff;
        border: 1px solid #ddd;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .rating {
        color: #f5a623;
    }
    .footer {
        text-align: center;
        font-size: 1rem;
        color: #888;
        margin-top: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# Page Title
st.markdown("<h1 class='title'>Slipper Shop Reviews</h1>", unsafe_allow_html=True)

# Form for submitting reviews
with st.form(key='review_form', clear_on_submit=True):
    st.markdown("<h2 class='header'>We Value Your Feedback</h2>", unsafe_allow_html=True)
    name = st.text_input("Your Name", placeholder="John Doe")
    product_name = st.text_input("Slipper Model", placeholder="Enter slipper model")
    satisfaction = st.slider("Product Satisfaction (1 to 5)", 1, 5, 3)
    feedback = st.text_area("Additional Feedback", placeholder="Share your thoughts here...")
    submit_button = st.form_submit_button("Submit Review")

    if submit_button:
        new_review = {
            'Name': name,
            'Product': product_name,
            'Satisfaction': satisfaction,
            'Feedback': feedback
        }
        st.session_state['reviews'].append(new_review)
        # Append to CSV file
        pd.DataFrame(st.session_state['reviews']).to_csv(REVIEWS_FILE, index=False)
        st.success("Thank you for your feedback!")

# Display reviews
st.markdown("<h2 class='header'>What Our Customers Say</h2>", unsafe_allow_html=True)
for review in st.session_state['reviews']:
    product_name = review.get('Product', 'Unknown Product')
    st.markdown(f"""
        <div class='review'>
            <strong>{review['Name']}</strong> reviewed the <strong>{product_name}</strong>
            <p class='rating'>Satisfaction: {review.get('Satisfaction', 'N/A')} ⭐</p>
            <p>{review.get('Feedback', 'No feedback provided.')}</p>
        </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("<div class='footer'>Thank you for visiting our Slipper Shop!</div>", unsafe_allow_html=True)




