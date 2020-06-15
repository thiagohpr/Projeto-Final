_____SOBREVIVÊNCIA LINK_____

VIDEO MOSTRANDO O JOGO: https://www.youtube.com/watch?v=7J3tLQjHEsQ&feature=youtu.be

OBS: PARA RODAR O JOGO BASTA EXECUTAR O ARQUIVO "zelda.py"

---Sobrevivência Link é um jogo cujo objetivo é sobreviver a infinitas hordas de inimigos e obter a maior pontuação possível. Quanto mais tempo o herói durar e quanto mais inimigos ele derrotar, maior a sua pontuação.
---O jogador possui a barra azul de poder, capaz de atirar flechas com a barra de espaço do teclado. Cada flecha gasta 1/3 da barra, sendo que para enche-lá é necessário apenas se movimentar pelo mapa. 
---A barra vermelha corresponde à barra de vida do jogador, composta por 270 pixels. Evidentemente, se a barra zerar, o jogador morre.
---Para sobreviver o jogador deve enfrentar 2 tipos de inimigos. O primeiro tipo são os inimigos comuns. Estes nascem andando no eixo horizontal até que o jogador entre em sua área de perseguição. Cada um desses inimigos surgem de 500 a 500 pontos e tiram 75 dos 270 pontos de vida do jogador. Já os chefes são os inimigos grandes que possuem uma barra de vida própria. Eles seguem o jogador pelo mapa inteiro, de forma lenta, e podem o matar com apenas um golpe, mas em compensação surgem apenas de 5000 a 5000 pontos. Além disso, para matá-lo, o jogador precisa acertá-lo com 5 flechas.
---Além dos inimigos, o jogador também pode perder sua vida passando em cima das lavas. Diferentemente dos inimigos comuns, aslavas não somem do mapa se o jogador colide com ela. A cada frame em cima da lava, o jogador perde 2 dos 270 pontos de vida. Dessa forma, o jogador deve apenas evitar o máximo possível passar pela lava, já que a flecha não faz efeito nela.
---Ao final da partida, se o jogador fizer uma pontuação maior que as 5 melhores, ele poderá inserir seu nome para que seu recorde fique salvo no computador, sendo que as 5 melhores  pontuações aparecem ao final de toda partida. O programa verifica se a sua pontuação está entre as melhores e a substitui no lugar correto (por exemplo, se a sua pontuação é a segunda melhor, ela tem que estar entre a primeira e a antiga segunda, empurrando todas pontuações abaixo uma posição a menos e apagando a antiga quinta pontuação), no entanto um aviso importante é que ele não funciona de forma adequada se houver nomes iguais na lista de recordes. Dessa forma, atente-se ao colocar o nome se fizer uma pontuação boa.
---Outro aviso importante é: não mexa no arquivo recordes.txt. Ele atualiza automaticamente, guardando os nomes e as pontuações de cada recorde. Ao ler o arquivo, ele separa os  nomes e recordes a cada ---, dessa forma se for retirado apenas um -, ele irá interpretar de forma equivocada e salvar os próximos recordes erroneamente. 



Jogo feito por Thiago Rocha e Fabrizio Milan - Projeto final de Design de Software
Turma B
Insper