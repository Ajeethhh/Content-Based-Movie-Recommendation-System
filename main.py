import streamlit as st
import pickle

df = pickle.load(open('movies_df.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

def movie_recommend(movie_title):
    ind = df[df['title'] == movie_title].index[0]
    sorted_similarity = sorted(list(enumerate(similarity[ind])),key = lambda x: x[1], reverse = True)
    recom_movies = []
    for i in sorted_similarity[1:6]:
        recom_movies.append(df['title'].iloc[i[0]])
    return recom_movies


page_bg = """
<style>
    div[data-testid="stAppViewContainer"] {
        background-image: url("https://media.newyorker.com/photos/5dbafcc91b4a6700085a7a9b/master/w_1920,c_limit/Baker-FightClub.jpg");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
    }
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)


st.title('MOVIE RECOMMENDER SYSTEM')

input_movie = st.selectbox("Which Movie?",df['title'].values)

if st.button('Recommend'):
    recommendations = movie_recommend(input_movie)
    for i in recommendations:
        st.write(i)

