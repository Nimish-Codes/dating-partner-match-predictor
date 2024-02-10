import streamlit as st

def get_user_info():
    age = st.slider("Age", 18, 100, step=1)
    status = st.selectbox(prefix + "Marital Status", ["Single", "Married", "Divorced", "Already have a partner"])
    sex = st.selectbox(prefix + "Sex", ["Male", "Female"])
    education = st.selectbox(prefix + "Education", ["10th", "12th", "Bachelor", "Masters", "PhD", "Uneducated"])
    orientation = st.selectbox(prefix + "Orientation", ["Straight", "Gay", "Lesbian", "Bisexual"])
    body_type = st.selectbox(prefix + "Body Type", ["Average", "Fit", "Athletic", "Thin", "Curvy", "Fatty", "Hamburger"])
    diet = st.selectbox(prefix + "Diet", ["Only Veg", "Only Non-Veg", "Mostly Veg", "Mostly Non-Veg", "Mixed Balanced"])
    diet_routine = st.selectbox(prefix + "Diet Routine", ["Anytime", "Strictly Timed"])
    drinks_alcohol = st.selectbox(prefix + "Drinks Alcohol", ["Never", "Sometimes", "With friends or party only", "Often", "Regular"])
    drugs = st.selectbox(prefix + "Drugs", ["Never", "Sometimes", "Regular"])
    ethnicity = st.selectbox(prefix + "Ethnicity", ["White", "Black", "Asian", "Indian"])
    
    return {
        "age": age,
        "status": status,
        "sex": sex,
        "education": education,
        "orientation": orientation,
        "body_type": body_type,
        "diet": diet,
        "diet_routine": diet_routine,
        "drinks_alcohol": drinks_alcohol,
        "drugs": drugs,
        "ethnicity": ethnicity
    }

def get_partner_info(prefix=""):
    age = st.slider("Age", 18, 100, step=1)
    status = st.selectbox(prefix + "Marital Status", ["Single", "Married", "Divorced", "Already have a partner"])
    sex = st.selectbox(prefix + "Sex", ["Male", "Female"])
    education = st.selectbox(prefix + "Education", ["10th", "12th", "Bachelor", "Masters", "PhD", "Uneducated"])
    orientation = st.selectbox(prefix + "Orientation", ["Straight", "Gay", "Lesbian", "Bisexual"])
    body_type = st.selectbox(prefix + "Body Type", ["Average", "Fit", "Athletic", "Thin", "Curvy", "Fatty", "Hamburger"])
    diet = st.selectbox(prefix + "Diet", ["Only Veg", "Only Non-Veg", "Mostly Veg", "Mostly Non-Veg", "Mixed Balanced"])
    diet_routine = st.selectbox(prefix + "Diet Routine", ["Anytime", "Strictly Timed"])
    drinks_alcohol = st.selectbox(prefix + "Drinks Alcohol", ["Never", "Sometimes", "With friends or party only", "Often", "Regular"])
    drugs = st.selectbox(prefix + "Drugs", ["Never", "Sometimes", "Regular"])
    ethnicity = st.selectbox(prefix + "Ethnicity", ["White", "Black", "Asian", "Indian"])
    
    return {
        "age": age,
        "status": status,
        "sex": sex,
        "education": education,
        "orientation": orientation,
        "body_type": body_type,
        "diet": diet,
        "diet_routine": diet_routine,
        "drinks_alcohol": drinks_alcohol,
        "drugs": drugs,
        "ethnicity": ethnicity
    }

def calculate_match(user1, user2):
    match_score = 0
    total_questions = 0
    
    for key in user1.keys():
        if key != "age":
            total_questions += 1
            if user1[key] == user2[key]:
                match_score += 1
                
    match_percentage = (match_score / total_questions) * 100
    return match_percentage

def main():
    st.title("Partner Match Predictor")
    st.write("Provide your information honestly:")
    user1_info = get_user_info()
    
    st.write("\nNow provide your partner's information:")
    user2_info = get_partner_info("Partner's ")
    
    match_percentage = calculate_match(user1_info, user2_info)
    st.write(f"\nMatch Percentage: {match_percentage:.2f}%")

    if match_percentage < 51:
      st.error("Have mercy on your life, run away and find another partner.")
    if match_percentage > 50:
      st.write("Get along.")
    if match_percentage == 100:
      st.write("A divine match.")

if __name__ == "__main__":
    main()
