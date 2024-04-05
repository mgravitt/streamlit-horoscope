import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
import os
import calendar
from dotenv import load_dotenv

load_dotenv()

# api_key = os.getenv('OPENAI_API_KEY')

def main():
    st.title("Daily Horoscope")

    # Input for month and day of the month
    month = st.selectbox("Month", list(calendar.month_name)[1:])
    day = st.number_input("Day of Month", min_value=1, max_value=31, step=1)  # Simplified validation

    # Dropdown for selecting the category
    category = st.selectbox("Select a category", ["family", "romance", "luck", "fighting", "business"])

    # Button to submit the selections
    if st.button("Get Advice"):
        llm = OpenAI()

        horoscope_prompt = PromptTemplate(
            template="""
            Identify the astrological symbol for the date of birth {month} {day}.
            Write a very short horoscope for the astrological symbol.
            Include advice for the topic of {category}
            """,
            input_variables=["month", "day", "category"]
        )

        horoscope_chain = LLMChain(
            llm=llm,
            prompt=horoscope_prompt,
            output_key="horoscope"
        )

        result = horoscope_chain({
            "month": month,
            "day": day,
            "category": category
        })
        
        # For demonstration, just display the selected values
        st.write(f"Month: {month}, Day: {day}, Category: {category}")
        st.write(result["horoscope"])
        
        # Here, you can add logic to fetch or generate advice based on the selected values

if __name__ == "__main__":
    main()