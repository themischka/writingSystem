import streamlit as st

# imports for search system
import chromadb
client = chromadb.PersistentClient(path="./my_db")

disThres = float(0.64)
talk = True

# start with Celsius converter
# make a mad lib kind of thing

# celsius = st.number_input("Enter temp in Celsius: ")
# fahrenheit = (celsius * 9/5) + 32
# st.write(f"{celsius}°C is equal to {fahrenheit}°F")
st.write("this is a mad-lib maker.")
st.write("enter text into the following prompts, then press finish to see your mad-lib.")

nomIn = st.text_input("Give me a name, for example: Milana")
if nomIn:
    st.write("you wrote: (", nomIn, ") for your name")
nameIN = nomIn

plIn = st.text_input("Give me a city, for example: Vancouver")
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

st.write(
    "currently testing a new part where the madlibs made will be added to the dict"
    " and you can search about prev madlibs."
)


# making a collection (a table of data) holds all the knowledge
# funcs: add(), query()
collection = client.get_or_create_collection("animals")
sentences = [
    "Good dogs, like Snoopy are the best.",
    "Snoopy is a good dog.",
    "Dogs are not good",
    "The smoke is strong today."
    # "Милана хочет есть.",
    # "Milana wants to eat.",
    # "Милана думала что там есть яблока здесь.",
    # "там нет яблоко здешь."
    # "니 생일은 언재?",
    # "내 생일은 어제였"
]

# unique tags
tags = ["1", "2", "3", "4"]
collection.add(documents=sentences, ids=tags)

while talk:
    # queries
    question = st.text_input("Ask a question, or say /bye to quit: ")
    if question == "/bye":
        talk = False
    else:
        result = collection.query(query_texts=question, n_results=2)

        # results of distance aren't floats, so they cannot be compared

        # prints the sentences that are most similar to the query
        st.write(result["documents"])
        # prints the ids, the tag that was assigned to the sentences
        st.write(result["ids"])
        # prints the "distance" between the query and the sentences in the database
        st.write(result["distances"])
        # if result["distances"] > disThres:
        #     print("the results may not be accurate, I may be hallucinating")

