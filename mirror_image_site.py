import streamlit as st
import streamlit.components.v1 as components    
st.title('Website Flipped')

ur = st.text_input('Enter your url here:',"https://v3.mutalyzer.nl/namechecker/NG_012337.1(NM_003002.2):c.274G%3ET")
st.write('Your url is:', ur)
string_html = '<iframe style="transform: scaleX(-1); -webkit-transform: scaleX(-1);" src="' + ur + '" width="100%" height="500px" allowfullscreen="true"></iframe>'
components.html(
string_html,width=2000, height=2000, scrolling=True)
