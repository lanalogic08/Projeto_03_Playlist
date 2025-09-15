import  streamlit as st 

#  python -m streamlit run app.py 

#---------------------------------------------------------------------------------------------Sidebar

st.sidebar.image("logo.png")
st.sidebar.title('Lana Playlist')

#Dados de exemplo
generos_musicais = ["Pop", "Eletrônica", "Trap", "MPB"]

#Dicionário relacionado aos generos e aos cantores
cantores_por_generos_musicais = {
    "Pop": ["Justin Bieber", "Rihanna","Michael Jackson"],
    "Eletrônica": ["Calvin harris", "David Guetta"],
    "Trap": ["Yunk vino", "Matuê"],
    "MPB" : ["Rita Lee", "Caeteano Veloso"]
}
#Selectbox para escolher o gênero
genero_selecionado = st.sidebar.selectbox("Selecione o gênero", generos_musicais)

#Selectbox para escolher o cantor (apenas do genero selecionado)
if genero_selecionado:
    cantor_selecionado = st.sidebar.selectbox(
        "Selecione um cantor:",
        cantores_por_generos_musicais[genero_selecionado]
    )

#Mostrar genero selecionado 
if genero_selecionado == "Pop" and cantor_selecionado == "Justin Bieber":
    st.markdown('### Justin Bieber')
    st.markdown ("Cantor e compositor canadense, começou a carreira ainda adolescente no YouTube e rapidamente se tornou um fenômeno global. Conhecido por hits como Sorry e Peaches, mistura pop, R&B e eletrônica.")
    st.video ("https://www.youtube.com/watch?v=kffacxfA7G4&list=RDkffacxfA7G4&start_radio=1")
    st.link_button(label="Spotify", url=" https://open.spotify.com/intl-pt/artist/1uNFoZAHBGtllmzznpCI3s ")

elif genero_selecionado == "Pop" and cantor_selecionado == "Rihanna":
    st.markdown('### Rihanna')
    st.markdown ("Cantora, compositora e empresária de Barbados, é uma das artistas mais premiadas do mundo. Seu estilo vai do pop ao R&B, passando pelo dancehall, com sucessos como Umbrella e Diamonds.")
    st.video ("https://www.youtube.com/watch?v=kOkQ4T5WO9E&list=RDkOkQ4T5WO9E&start_radio=1")
    st.link_button(label="Spotify", url="https://open.spotify.com/intl-pt/artist/5pKCCKE2ajJHZ9KAiaK11H")

elif genero_selecionado == "Pop" and cantor_selecionado == "Michael Jackson":
    st.markdown('### Michael Jackson')
    st.markdown("Foi o “Rei do Pop”, cantor e dançarino que revolucionou a música e ficou famoso por sucessos como Thriller e o passo moonwalk.")
    st.video("https://www.youtube.com/watch?v=Zi_XLOBDo_Y&list=RDZi_XLOBDo_Y&start_radio=1")
    st.link_button(label="Spotify", url= "https://open.spotify.com/intl-pt/artist/3fMbdgg4jU18AjLCKBhRSm")



elif genero_selecionado == "Eletrônica" and cantor_selecionado == "Calvin harris":
    st.markdown('### Calvin harris')
    st.markdown ("DJ, produtor e compositor escocês, é um dos maiores nomes da música eletrônica. Conhecido por colaborações com grandes artistas e por hits que dominam as pistas de dança.")
    st.video ("https://www.youtube.com/watch?v=ebXbLfLACGM&list=RDebXbLfLACGM&start_radio=1")
    st.link_button(label="Spotify", url="https://open.spotify.com/playlist/5qcVzlldialLNtzAl15kbb")

elif genero_selecionado == "Eletrônica" and cantor_selecionado == "David guetta":
    st.markdown('### David guetta')
    st.markdown ("DJ e produtor francês, considerado um dos pioneiros na popularização da música eletrônica no pop. Criou sucessos mundiais como Titanium e Hey Mama.")
    st.video ("https://www.youtube.com/watch?v=5dbEhBKGOtY&list=RD5dbEhBKGOtY&start_radio=1")
    st.link_button(label="Spotify", url=" https://open.spotify.com/playlist/5Bl1hF6LIi9rgl7LYLpjSH")

elif genero_selecionado == "Trap" and cantor_selecionado == "Yunk vino":
     st.markdown('### Yunk vino')
     st.markdown("Rapper brasileiro que se destaca no trap nacional, com letras que misturam lifestyle, emoção e críticas sociais, conquistando cada vez mais fãs jovens.")
     st.video("https://www.youtube.com/watch?v=ZRMxYBz40hE&list=RDZRMxYBz40hE&start_radio=1")
     st.link_button(label="Spotify", url="https://open.spotify.com/intl-pt/artist/460m2YG30duLCuHwFdiLgX")

elif genero_selecionado == "Trap" and cantor_selecionado == "Matuê":
     st.markdown('### Matuê')
     st.markdown("Um dos maiores nomes do trap no Brasil, conhecido por seu estilo único e pela forma de contar histórias em suas músicas. Álbuns como Máquina do Tempo marcaram o gênero.")
     st.video("https://www.youtube.com/watch?v=ZPcG9PCfagM&list=RDZPcG9PCfagM&start_radio=1")
     st.link_button(label="Spotify", url="https://open.spotify.com/intl-pt/artist/5nP8x4uEFjAAmDzwOEc9b8")

elif genero_selecionado == "MPB" and cantor_selecionado == "Rita lee":
    st.markdown('### Rita lee')
    st.markdown('Rainha do rock brasileiro, compositora, cantora e escritora. Sua música mistura irreverência, crítica social e experimentação sonora. Um ícone da MPB e do rock.')
    st.video("https://www.youtube.com/watch?v=L60qWVke-Sc&list=RDL60qWVke-Sc&start_radio=1")
    st.link_button(label="Spotify", url= "https://open.spotify.com/intl-pt/artist/7dnT2FUXhjirperXaH22IJ")

elif genero_selecionado == "MPB" and cantor_selecionado == "Caetano Veloso":
      st.markdown('### Caetano veloso')
      st.markdown("Cantor, compositor e escritor baiano, um dos fundadores do movimento Tropicalista. Sua obra é marcada pela poesia e pela mistura de ritmos, sendo um dos maiores nomes da música brasileira")
      st.video("https://www.youtube.com/watch?v=j9UbE1slI-Q&list=RDj9UbE1slI-Q&start_radio=1")
      st.link_button(label="Spotify", url= "https://open.spotify.com/playlist/4acEqtLj8N8dJgyynnL42R")

