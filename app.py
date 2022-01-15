import streamlit as st 
import pandas as pd 
from PIL import Image
import os
import altair as alt


st.set_page_config(page_title="Choix de stage",layout='wide')

st.markdown("""<h1 style='text-align: center; font-weight:bold;padding-bottom:15px; margin-bottom:70px;color:rgba(10,10,180,1);'>
                Contact pour les stages</h1>""", unsafe_allow_html=True)

path = os.path.dirname(__file__)
my_file = path+'/hec.png'
st.sidebar.image(Image.open(my_file))

st.sidebar.markdown("<hr style=' text-align : center; border-color : grey; margin-top: 15px; margin-bottom: 15px;'>", unsafe_allow_html = True)

annuaire = pd.read_csv('Annuaire.csv', sep=';', encoding='utf8')

secteurs_stages1 = list(annuaire['Secteur du stage 1'].unique())
secteurs_stages2 = list(annuaire['Secteur 2'].unique())

for i in secteurs_stages2:
    if i not in secteurs_stages1:
        secteurs_stages1.append(i)
        
entreprise1 = list(annuaire['Entreprise 1'].unique())
entreprise2 = list(annuaire['Entreprise 2'].unique())

for i in entreprise2:
    if i not in entreprise1:
        entreprise1.append(i)
        
select = st.sidebar.radio('Choix de la selection :', ['Par secteur', 'Par entreprise'])

if select == 'Par secteur':
    secteur = st.sidebar.multiselect('Secteur', secteurs_stages1)
    dt = annuaire.loc[(annuaire['Secteur du stage 1'].isin(secteur)) | (annuaire['Secteur 2'].isin(secteur))]
    st.write(dt)
    st.markdown("<hr style=' text-align : center; border-color : rgba(0,0,0,0); margin-top: 15px; margin-bottom: 15px;'>",unsafe_allow_html = True)
    st.download_button('Télécharger les infos', dt.to_csv())
    
else : 
    entreprise = st.sidebar.multiselect('Entreprise', entreprise1, 'BCG')
    dt = annuaire.loc[(annuaire['Entreprise 1'].isin(entreprise)) | (annuaire['Entreprise 2'].isin(entreprise))]
    st.write(dt)
    st.markdown("<hr style=' text-align : center; border-color : rgba(0,0,0,0); margin-top: 15px; margin-bottom: 15px;'>",unsafe_allow_html = True)
    st.download_button('Télécharger les infos', dt.to_csv())

st.markdown("<hr style=' text-align : center; border-color : rgba(0,0,0,0); margin-top: 15px; margin-bottom: 15px;'>",unsafe_allow_html = True)
st.markdown("<hr style=' text-align : center; border-color : rgba(0,0,0,0); margin-top: 15px; margin-bottom: 15px;'>",unsafe_allow_html = True)
bar_stage1 = alt.Chart(annuaire).mark_bar().encode(
        alt.X("Secteur du stage 1:N",
              axis=alt.Axis(labelAngle=-20),
              sort=alt.EncodingSortField(field="Secteur du stage 1", op="count", order='descending')),
        alt.Y("count(Secteur du stage 1):Q"),
        tooltip = ['Secteur du stage 1',alt.Tooltip('count(Secteur du stage 1):Q',title='Total de stages')],
    )

st.altair_chart(bar_stage1.interactive()
                    .properties(title = f'Nombre total de stage par secteur en première partie'),
                    use_container_width = True)

st.markdown("<hr style=' text-align : center; border-color : rgba(0,0,0,0); margin-top: 15px; margin-bottom: 15px;'>",unsafe_allow_html = True)
st.markdown("<hr style=' text-align : center; border-color : rgba(0,0,0,0); margin-top: 15px; margin-bottom: 15px;'>",unsafe_allow_html = True)

bar_stage2 = alt.Chart(annuaire).mark_bar().encode(
        alt.X("Secteur 2:N",
              axis=alt.Axis(labelAngle=-20),
              sort=alt.EncodingSortField(field="Secteur 2", op="count", order='descending')),
        alt.Y("count(Secteur 2):Q"),
        tooltip = ['Secteur 2',alt.Tooltip('count(Secteur 2):Q',title='Total de stages')],
    )

st.altair_chart(bar_stage2.interactive()
                    .properties(title = f'Nombre total de stage par secteur en deuxième partie'),
                    use_container_width = True)