# Versão atualizada do novel_scraping
# Melhorias básicas em comparação com a versão anterior:
- Organização por Módulos: O código foi reestruturado em módulos para uma melhor organização.
- Uso Eficiente do Selenium: Agora, o Selenium é utilizado apenas para obter o número de capítulos e todos os títulos.
    - Antes, a coleta de dados era realizada inteiramente pelo Selenium, o que era ineficiente e demorava cerca de 10 minutos, especialmente em novels extensas. Além disso, era restrito a um conjunto específico de novels.

# Melhorias Notáveis:
- Formatação de Títulos: A partir dos títulos obtidos, o código formata os títulos para as URLs dos capítulos no padrão do site ReadNovelFull, tornando-o compatível com qualquer novel.
- Requisições Assíncronas: As bibliotecas asyncio e aiohttp são utilizadas para realizar requisições assíncronas do conteúdo textual de cada capítulo a partir das URLs obtidas.
    - Isso resultou em uma redução significativa no tempo de execução do código, de aproximadamente 15 minutos para cerca de 37 segundos, para 1619 requisições. Para efeito de comparação, o código foi testado em quatro novels diferentes, que levaram aproximadamente 170 segundos para concluir a raspagem de dados.
    - Vale ressaltar que a utilização da biblioteca requests teria sido tão ineficiente quanto o uso exclusivo do Selenium, de acordo com os testes realizados.
- Utilização do Beautiful Soup: O Beautiful Soup é usado para fazer a análise do HTML e extrair os dados necessários.
- Formatação de Dados: Os textos são formatados para extrair informações como quantidade de palavras, caracteres, caracteres sem espaços, caracteres sem pontuações e ambos.
    - A função sub da biblioteca re é utilizada para formatar os textos de forma eficiente e concisa.
    - Dicionários foram usados em vez de listas para criar uma estrutura de dados mais legível.
    - O código calcula a soma total de cada aspecto e a quantidade média de cada aspecto por capítulo.
- Geração de Arquivos JSON: Arquivos JSON são criados para armazenar todos os dados de forma organizada.
- Precisão dos Dados: A precisão dos dados coletados aumentou de 97% para 100% em comparação com a versão anterior.

Esse projeto demorou bem mais tempo do que o primeiro, principalmente porque eu estava aprendendo enquanto fazia, no entanto gostei do resultado final.
