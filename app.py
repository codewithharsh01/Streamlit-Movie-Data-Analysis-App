# heading 
# search functionality mid
# sliders -like filtering based on year ranges 
# filters 
# visualizations 


# import libraries
import streamlit as st
import pandas as pd     
import matplotlib.pyplot as plt    
import plotly.express as px 


# loading the dataset
def load_dataset():
    return pd.read_csv("data.csv")  

df=load_dataset()

# title of the page
st.title("Indian Movies Analysis Dashboard")

# search movie -partial or full 
st.subheader("Search for a movie")
search_query=st.text_input("Enter a movie name(partial or full, case-insensitive)")
# search_query="da"
if search_query:
    search_results=df[df["Movie Name"].str.contains(search_query, case=False,na=False)] # 
    #filter condition: df["Movie Name"].str.contains(search_query, case=False,na=False)
    # df[filter condition]
    # df[ df["moviename"]]
    if not search_results.empty: 
        st.write(f" Found {len(search_results)} movie(s)")
        st.dataframe(search_results[["Movie Name", "Year", "Rating(10)", "Votes","Genre","Language"]])
    else:
        st.write("No movies found matching your query!!!! ")


st.sidebar.header("Filters")

genre_filter=st.sidebar.multiselect("Select Genre", df["Genre"].unique(),default=[])
# genre_filter=drama, thriller
if genre_filter:
    # df[filter condition]
    # df['Genre'].isin(["Drama", "Thriller"])
    df=df[df['Genre'].isin(genre_filter)]

language_filter=st.sidebar.multiselect("Select Language", df["Language"].unique(),default=[])

if language_filter:
    # df[filter condition]
    df=df[df['Language'].isin(language_filter)]

# filter by year
year_filter=st.sidebar.slider("Select Year Range ", int(df["Year"].min()),int(df["Year"].max()), (1950,2025))
# st.sidebar.slider(text, min_val, max_val, default_val)
# (2000,2005) >=2000 and <=2005
# between(2000, 2005) 
# * and ** 
df=df[df["Year"].between(*year_filter)]


# filter by rating
rating_filter=st.sidebar.slider("Select Rating Range ", float(df["Rating(10)"].min()),float(df["Rating(10)"].max()), (0.0,10.0)) 
df=df[df["Rating(10)"].between(*rating_filter)]

# votes- filter hmwrk
votes_filter = st.sidebar.slider("Select Voting Range", int(df["Votes"].min()), int(df["Votes"].max()), (0, 1900))
df = df[df["Votes"].between(*votes_filter)]



st.subheader("Filtered Movies Data")

st.dataframe(df)


st.subheader("Visualizations")
visualization_option=st.selectbox("Select a visualization or analysis condition",     
             [
                 "Top 10 Movies by Rating",
                 "Top 10 Movies by Votes",
             ])

if visualization_option=="Top 10 Movies by Rating":
    st.markdown("### Top 10 Movies by Rating")
    top_movies_by_rating=df.sort_values(by="Rating(10)",ascending=False).head(10)
    st.write("Table: Top 10 Movies by Rating")
    st.dataframe(top_movies_by_rating)
    st.write("Bar Chart: Top 10 Movies by Rating")
    fig=px.bar(top_movies_by_rating, x="Movie Name", y="Rating(10)", title="Top 10 Movies by Rating")
    st.plotly_chart(fig)

elif visualization_option=="Top 10 Movies by Votes":
    st.markdown("### Top 10 Movies by Votes")
    top_movies_by_votes=df.sort_values(by="Votes",ascending=False).head(10)
    st.write("Table: Top 10 Movies by Votes")
    st.dataframe(top_movies_by_votes)
    st.write("Pie Chart: Top 10 Movies by Votes")
    fig=px.pie(top_movies_by_votes, names="Movie Name", values="Votes", title="Top 10 Movies by Votes")
    st.plotly_chart(fig)




