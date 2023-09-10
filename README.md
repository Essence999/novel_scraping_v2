# Versão atualizada do novel_scrapping

# Melhorias básicas comparado ao antigo:

- Código separado por módulos (mais organizado)
- Usa o selenium somente para pegar o número de capítulos e todos os títulos.
    - Antigamente usava o selenium para fazer o scrapping inteiro, o que era ineficiente, pois levava cerca de 10 minutos, considerando que as novels eram deveras grandes. Além disso, não era flexível, só funcionava nas novels que escolhi.

# Melhorias notáveis:

- A partir dos títulos adquiridos, formata todos os títulos para a URL de cada capítulo no padrão aparente do site readnovel (permite que o código funcione em qualquer novel).
- Uso das libs asyncio e aiohttp para fazer requisições assíncronas do conteúdo textual de cada capítulo a partir das URLs adquiridas.
    - Velocidade de execução total do código foi de cerca de 10 minutos para uns 37 segundos em 1619 requisições (funções assíncronas são realmente impressionantes).
    - Nota: usar a lib requests seria tão ineficiente quanto usar somente o selenium, de acordo com os testes.
- Formata os textos para adquirir os seguintes dados: quantidade de palavras, caracteres, caracteres sem espaços, caracteres sem pontuações, e sem ambos.
    - Usei a função sub da lib re para formatar os textos de forma mais eficiente e com menos código.
    - Usei dicionários invés de listas para criar uma estrutura de dados mais agradável.
    - Adquire a soma total de todos os aspectos e calcula a quantidade média de cada por capítulo.
- Cria arquivos json com todos os dados organizados.
- A precisão dos dados adquiridos aumentou de 97% para 100% comparado a anteriormente.

Esse projeto demorou bem mais tempo do que o primeiro, especialmente porque eu estava aprendendo enquanto fazia, mas foi legal ver o resultado final.
