import pandas as pd

def player_stats(player:str, data:pd.DataFrame):

    # Ajustando os dados para que, em qualquer caso de digitação tudo seja padronizado para que aceite qualquer forma do nome do player
    player = player.lower().strip()
    
    data["playername"] = data["playername"].str.lower()

    # Aqui eu tenho todos os dados completos de um único jogador
    player_data = data[data["playername"] == player].copy()

    # Impedindo casos de divisão por 0 (existem jogos onde o jogar morre 0 vezes e nesses casos o 0 equivale a 1 na conta do KDA)
    adjusted_deaths = player_data["deaths"].clip(lower=1)
    player_data["kda"] = (player_data["kills"]+player_data["assists"])/adjusted_deaths

    # criando as listas de colunas para acesso futuro
    colunas_desempenho_jg = ["kda","monsterkills","xpdiffat10","xpdiffat15","xpdiffat20","xpdiffat25","golddiffat10","golddiffat15","golddiffat20","golddiffat25","wardsplaced","wpm","wardskilled","wcpm","controlwardsbought","visionscore","vspm"]

    top_picks = [x for x in player_data["champion"].value_counts().nlargest(5).index]

    if player_data["position"].unique() == "jng":
        
        qtd_partidas = player_data.shape[0]
    
        for column in player_data.columns:
            if column in ['playername', 'teamname', 'league']:
                print(f"{column}: {player_data[column].unique()}")
            # Para usar a lista completa, preciso colocar ( ) ao redor da lista, senão ela ignora a iteração
            elif column in (colunas_desempenho_jg):
                print(f"{column}_mean: {round(player_data[column].mean(),2)}")
            else:
                pass

        print(
            f"""
            Pool: {player_data["champion"].unique().shape[0]}
            Top picks: {[x for x in player_data["champion"].value_counts().nlargest(5).index]}
            Partidas jogadas com os Top Picks: {player_data["champion"].value_counts().nlargest(5).values}
            """
        )

        player_data_top_champs = player_data[player_data["champion"].isin(top_picks)]
    
        for campeao in top_picks:
            vitorias = player_data_top_champs[["champion","result"]][(player_data_top_champs["champion"] == campeao) & (player_data_top_champs["result"] == 1)].shape[0]
            total_partidas = player_data_top_champs[["champion"]][player_data_top_champs["champion"] == campeao].shape[0]
            win_rate = round((vitorias/total_partidas)*100, 2)

            print(
                f"""
                    Campeão: {campeao}
                    WinRate: {win_rate}%
                """
                )

    else:
        
        qtd_partidas = player_data.shape[0]
        team = player_data["teamname"].unique()
        liga = player_data["league"].unique()
        qtd_pool = player_data["champion"].unique().shape[0]
        top_picks = [x for x in player_data["champion"].value_counts().nlargest(3).index]
        qtd_match_top_picks = player_data["champion"].value_counts().nlargest(3).values
        kda_mean = round(player_data["kda"].mean(),2)
        xp_diff_10 = round(player_data["xpdiffat10"].mean(),2)
        xp_diff_15 = round(player_data["xpdiffat15"].mean(),2)
        xp_diff_20 = round(player_data["xpdiffat20"].mean(),2)
        xp_diff_25 = round(player_data["xpdiffat25"].mean(),2)
        gold_diff_10 = round(player_data["golddiffat10"].mean(),2)
        gold_diff_15 = round(player_data["golddiffat15"].mean(),2)
        gold_diff_20 = round(player_data["golddiffat20"].mean(),2)
        gold_diff_25 = round(player_data["golddiffat25"].mean(),2)

        print(
            f"""
            Jogador: {player}\n
            Equipe: {team}\n
            Liga: {liga}\n
            Quantidade de partidas: {qtd_partidas}\n
            Quantidade de pool: {qtd_pool}\n
            Campeões mais usados: {top_picks}\n
            Quantidade de partidas jogadas com os campeões: {qtd_match_top_picks}\n
            KDA médio por partida: {kda_mean}\n
            Média XP Diff 10m: {xp_diff_10}\n
            Média XP Diff 15m: {xp_diff_15}\n
            Média XP Diff 20m: {xp_diff_20}\n
            Média XP Diff 25m: {xp_diff_25}\n
            Média Gold Diff 10m: {gold_diff_10}\n
            Média Gold Diff 15m: {gold_diff_15}\n
            Média Gold Diff 20m: {gold_diff_20}\n
            Média Gold Diff 25m: {gold_diff_25}\n
            """
        )
    
if __name__ == "__main__":
    import pandas as pd
    data = pd.read_csv("C:/Users/yandrade/Documents/GitHub/data-analysis-python/lol/data/full_data/2026_LoL_esports_match_data_from_OraclesElixir.csv")
    print("Teste:", player_stats("tatu", data))