import streamlit as st

def get_user_info():
    age = st.slider("Age", 18, 100, step=1, key="one")
    status = st.selectbox("Marital Status", ["Single", "Married", "Divorced", "Already have a partner"])
    sex = st.selectbox("Sex", ["Male", "Female"])
    education = st.selectbox("Education", ["10th", "12th", "Bachelor", "Masters", "PhD", "Uneducated"])
    orientation = st.selectbox("Orientation", ["Straight", "Gay", "Lesbian", "Bisexual"])
    body_type = st.selectbox("Body Type", ["Average", "Fit", "Athletic", "Thin", "Curvy", "Fatty", "Hamburger"])
    diet = st.selectbox("Diet", ["Only Veg", "Only Non-Veg", "Mostly Veg", "Mostly Non-Veg", "Mixed Balanced"])
    diet_routine = st.selectbox("Diet Routine", ["Anytime", "Strictly Timed"])
    drinks_alcohol = st.selectbox("Drinks Alcohol", ["Never", "Sometimes", "With friends or party only", "Often", "Regular"])
    drugs = st.selectbox("Drugs", ["Never", "Sometimes", "Regular"])
    ethnicity = st.selectbox("Ethnicity", ["White", "Black", "Asian", "Indian"])
    
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
    agep = st.slider("Age", 18, 100, step=1, key="two")
    statusp = st.selectbox(prefix + "Marital Status", ["Single", "Married", "Divorced", "Already have a partner"])
    sexp = st.selectbox(prefix + "Sex", ["Male", "Female"])
    educationp = st.selectbox(prefix + "Education", ["10th", "12th", "Bachelor", "Masters", "PhD", "Uneducated"])
    orientationp = st.selectbox(prefix + "Orientation", ["Straight", "Gay", "Lesbian", "Bisexual"])
    body_typep = st.selectbox(prefix + "Body Type", ["Average", "Fit", "Athletic", "Thin", "Curvy", "Fatty", "Hamburger"])
    dietp = st.selectbox(prefix + "Diet", ["Only Veg", "Only Non-Veg", "Mostly Veg", "Mostly Non-Veg", "Mixed Balanced"])
    diet_routinep = st.selectbox(prefix + "Diet Routine", ["Anytime", "Strictly Timed"])
    drinks_alcoholp = st.selectbox(prefix + "Drinks Alcohol", ["Never", "Sometimes", "With friends or party only", "Often", "Regular"])
    drugsp = st.selectbox(prefix + "Drugs", ["Never", "Sometimes", "Regular"])
    ethnicityp = st.selectbox(prefix + "Ethnicity", ["White", "Black", "Asian", "Indian"])
    
    return {
        "age": agep,
        "status": statusp,
        "sex": sexp,
        "education": educationp,
        "orientation": orientationp,
        "body_type": body_typep,
        "diet": dietp,
        "diet_routine": diet_routinep,
        "drinks_alcohol": drinks_alcoholp,
        "drugs": drugsp,
        "ethnicity": ethnicityp
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
    user2_info = get_partner_info("partner's")

    if st.button("Let's see"):
    
        match_percentage = calculate_match(user1_info, user2_info)
        st.write(f"\nMatch Percentage: {match_percentage:.2f}%")

        if match_percentage < 51:
          st.error("Have mercy on your life, run away and find another partner.")
        for match_percentage in range(51, 99):
          st.write("Get along.")
            break
        if match_percentage == 100:
          st.success("A divine match. 36=36 :-)")

if __name__ == "__main__":
    main()
