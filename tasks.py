from crewai import Task
from textwrap import dedent


class ViralContentCreationTasks:
    def topic_analysis(self, agent, niche):
        return Task(
            description=dedent(
                f"""\
				Encontre pesquisas/tópicos populares relacionados ao nicho: {niche}.
				
				Compile essas informações numa lista estruturada de tópicos e pesquisas. 
				Cada item da lista deve incluir uma breve descrição e pontos de relevância 
				para orientar os esforços de criação de conteúdo em torno dessas tendências. 
				Certifique-se de que a lista final de tópicos de tendências é clara, acionável e pronta para informar
				estratégias de desenvolvimento de conteúdo."""
            ),
            expected_output="Lista de topicos e pesquisas no formato: [tópico1, tópico2, ...]",
            agent=agent,
        )

    def content_research(self, agent, niche):
        return Task(
            description=dedent(
                f"""\
				Faça pesquisas aprofundadas de todos os tópicos de tendência e pesquisas.
				Para cada topico relacionado com - {niche}, pesquise 
					os sites de maior autoridade e relevância dentro do nicho de {niche}.
					Crie uma lista de sites para visitar para cada tópico de tendência.
					
					Compile detalhes abrangentes para cada tópico, incluindo:
						- Um resumo do significado do tópico.
						- Dados estatísticos ou estudos recentes relacionados ao tema.
						- Pontos de discussão ou controvérsias atuais.
						- Previsões ou tendências que indicam como este tema poderá evoluir.
						- Possíveis ângulos ou ganchos para criação de conteúdo.
						
					O número máximo de pesquisas no Google que você pode fazer é 10."""
            ),
            expected_output=dedent(
                f"""\
						Um mapa do tópicos de tendência para detalhes de pesquisa estruturados para esse tópico.
						Este relatório servirá de base para criar posts no Twitter direcionadas, informadas e envolventes"""
            ),
            agent=agent,
        )

    def create_twitter_posts(self, agent, niche):
        return Task(
            description=dedent(
                f"""\
				Primeiro filtre os tópicos relacionados ao {niche} e remova os não relacionados.
				A seguir, crie 3 postagens no Twitter relacionadas a {niche} usando a pesquisa de conteúdo feita para cada um deles. 
					o tópico de tendência / pesquise e crie posts evolventes no Twitter, valiosas e acionáveis ​​​​que estão prontas para 
					que sejam publicados. Tente usar a seguinte estrutura:
					1. Comece com um gancho forte: comece com uma pergunta intrigante, um fato surpreendente ou 
							declaração envolvente para chamar a atenção.
					2. Agregue valor ou insights: incorpore informações úteis e relevantes, como estatísticas, 
							dicas rápidas ou observações esclarecedoras ou fatos interessantes.
					3. Call to Action (CTA): Incentive os leitores a se envolverem ainda mais, experimentando uma dica, 
							compartilhando o post ou deixando comentários. E forneça-lhes algum link útil e relevante para um
					  		blog, site ou vídeo.
					4. Use hashtags apropriadas: inclua 2 a 3 hashtags relevantes para aumentar a visibilidade 
							mas evite o uso excessivo.

					Postagem de exemplo:
					"Você sabia que 10 minutos de meditação diariamente podem aumentar significativamente o seu foco? 
						🧘‍♂️✨ A meditação breve e consistente melhora a concentração e os níveis de estresse, mesmo durante o horário de trabalho. 
						Não é bom apenas para a sua mente – é um impulsionador da produtividade!
						Experimente amanhã de manhã e veja a diferença por si mesmo! 
						🌞🚀 Compartilhe essa dica com alguém que precisa de um reforço de foco. 
						#Dicas de Produtividade #Mindfulness #SaúdeMental"

				Observação: certifique-se de que cada postagem seja independente e forneça todo o contexto necessário, pois os usuários podem 
					  não ver outras postagens relacionadas. Compile essas postagens num documento ou lista, com cada entrada claramente 
					  rotulada com o tema que aborda. Este documento será usado por outro agente para lidar com 
					  o post real no Twitter.
					  
				Após executar esta tarefa, você deverá imprimir o resultado.
				A tarefa deve retornar um array contendo todas as 3 postagens do Twitter escritas em PT-pt (Português de Portugal)."""
            ),
            expected_output="Lista contendo todos os posts do Twitter no formato: [post_1, post_2, ...]",
            agent=agent,
        )

    # def publish_twitter_posts(self, agent, tweets):
    # 	return Task(
    # 		description=dedent("""\
    # 			Print all the tweets created by previous task in the logs.
    # 			Publish all the tweets to Twitter.
    # 			"""),
    # 		expected_output="Posting status of all the tweets.",
    # 		agent=agent
    # 	)
