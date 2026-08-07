import streamlit as st


# start with Celsius converter
# make a mad lib kind of thing

# celsius = st.number_input("Enter temp in Celsius: ")
# fahrenheit = (celsius * 9/5) + 32
# st.write(f"{celsius}°C is equal to {fahrenheit}°F")

nomIn = st.text_input("Give me a name, for example: Milana")
if nomIn:
    st.write("you wrote: (", nomIn, ") for your noun")
nameIN = nomIn

plIn = st.text_input("Give me a place, for example: Italy")
if plIn:
    st.write("you wrote: (", plIn, ") for your place")
placeIN = plIn

emIn = st.text_input("Give me an emotion, for example: Nervous")
if emIn:
    st.write("you wrote: (", emIn, ") for your emotion")
emotionIN = emIn

numIn = st.text_input("Give me a number greater than 5, for example: 8")
if numIn:
    st.write("you wrote: (", numIn, ") for your number")
numberIN = numIn

foIn = st.text_input("Give me a food at a restaurant, for example: Steak")
if foIn:
    st.write("you wrote: (", foIn, ") for your food")
foodIN = foIn

if st.button("finish"):
    st.write(
        nameIN, " went to go",
        placeIN, " because",
        nameIN, " was going to see a friend.",
        nameIN, " was feeling very",
        emotionIN, "to see this friend because, this friend had once eaten",
        numberIN, foodIN, "s and left",
        nameIN, "with the bill"
    )
    st.balloons()
