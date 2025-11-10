import pandas as pd

df = pd.read_csv('interactions_full_df.csv')  # nome do arquivo enviado
print(df.shape)
print(df.head())

popularidade = df.groupby('game')['hours'].sum().sort_values(ascending=False)
print(popularidade.head(10))



from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 1. Popularidade (mais horas somadas)
popularidade = df.groupby('game')['hours'].sum().sort_values(ascending=False)

# 2. Conteúdo (similaridade pelo nome do jogo)
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['game'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Função: recomendar jogos parecidos
def recomendacao_por_jogo(nome_jogo, top_n=5):
    indices = pd.Series(df.index, index=df['game']).drop_duplicates()
    idx = indices[nome_jogo]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]
    jogos_indices = [i[0] for i in sim_scores]
    return df.iloc[jogos_indices][['game','hours']]

# Função híbrida (popularidade + conteúdo)
def recomendacao_hibrida(nome_jogo, top_n=5, alpha=0.5):
    base = recomendacao_por_jogo(nome_jogo, top_n*2)
    base['pop_score'] = base['game'].map(lambda x: popularidade.get(x,0))
    base['score'] = alpha*base['hours'] + (1-alpha)*base['pop_score']
    return base.sort_values('score',ascending=False).head(top_n)

    # Top 10 jogos mais populares
print("top 10 jogos mais jogados")
print(popularidade.head(10))

    #jogos parecidos

print("jogos parecidos")
print(recomendacao_por_jogo('Counter-Strike', top_n=5))

# Recomendações híbridas:

print("hibrido")
print(recomendacao_hibrida('Counter-Strike', top_n=5))