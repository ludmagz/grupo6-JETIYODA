# JETIYODA: TestCase Ride!!!

> No jogo “JETIYODA: TestCase Ride!!!”, o jogador controla Juliano Iyoda, professor do Centro de Informática, que, buscando ajudar um aluno a terminar a lista de Introdução à Programação, parte em direção ao CIn. Sabendo do trânsito que o aguarda nas ruas movimentadas do Recife, o professor, com o intuito de chegar rapidamente e conter o desespero do aluno, opta por usar uma mochila a jato (Jetpack) e tornar mais eficiente a sua trajetória. Porém, enquanto já estava voando em direção à faculdade, Juliano nota a CHOCANTE ausência de seu crachá, o que, caso não houvesse inúmeros fragmentos de crachá espalhados pelos ares recifenses, teria causado a impossibilidade de adentrar as maravilhosas instalações do CIn. Logo, percebendo os fragmentos espalhados e contabilizando quantos seriam necessários para formar sua identificação completa, Juliano percebe que, caso ele coletasse 350 fragmentos e desviasse de todos os empecilhos que, com certeza, querem o impedir de ajudar seu querido aluno, ele alcançaria seu objetivo. Sabendo que o grande Juliano Iyoda não é um homem de falhas, ele não aceitará menos do que uma chegada triunfante ao Centro de Informática e um “Submission Accepted” vindo do “Dikastis” de seu aluno.

## COMO ACESSAR O JOGO
1.	Certifique-se de ter o [Python](https://www.python.org/) instalado na sua máquina;
2.	Caso ainda não possua a biblioteca [PyGame](https://www.pygame.org/) instalada, abra o terminal do seu computador e execute o comando “pip install pygame”;
3.	Acesse, nesse repositório, o arquivo .zip referente ao projeto e faça o download;
4.	Retire a pasta PROJETO_IP e, em sua IDE de preferência, execute o arquivo “codigo_principal”;
5.	Para acessar às instruções do jogo, você pode clicar “i” no menu inicial ou [ler aqui](https://github.com/ludmagz/grupo6-JETIYODA/blob/main/README.md#instru%C3%A7%C3%B5es-de-jogabilidade)

## MEMBROS E SUAS RESPECTIVAS FUNÇÕES:
- [Fernando Luís Campelo dos Anjos (flca)](https://github.com/flca-cin) –
Contribuição na correção da possibilidade de os coletáveis colidirem entre si e correção de bugs.

- [Ludmila Cabral Lopes Magnani (lclm)](https://github.com/ludmagz) –
Design e implementação da lógica no código referente à tela inicial, à tela de instruções, à tela de vitória, e aos possíveis game overs, criação das artes do background do jogo (cidade + UFPE), criação da barra de progressão do jogo, participação na implementação do PyGame na base do código, elaboração do README.md e correção de bugs.

- [Luísa de Mendonça Simões (lmsm2)](https://github.com/lmsm2) –
Design das sprites do personagem (nas formas “Professor” e “Robocin”) e de todos os coletáveis, aplicação dos “Foguinhos” e “Fragmentos de crachás” no código, animação do personagem no jogo, introdução da trilha sonora e efeitos sonoros, participação na implementação do PyGame na base do código, elaboração dos slides e correção de bugs.


- [Luiz Felipe Vicente da Silva (lfvs2)](https://github.com/lfvs2) –
Implementação da progressividade dos fundos no jogo e correção de bugs.


- [Matheus Miranda Cabral de Menezes (mmcm2)](https://github.com/mmcm2-cin) –
Contribuição na correção da possibilidade de os coletáveis colidirem entre si, participação na implementação do PyGame na base do código e correção de bugs.



- [Miguel Câmara Raposo Andrade (mcra)](https://github.com/mcra3287) –
Implementação da funcionalidade dos coletáveis “Robocin” e “Corações”, organização do código em módulos e repartição em funções, criação do sistema de voo e gravidade e correção de bugs.




## ARQUITETURA DO PROJETO:


## CAPTURAS DE TELA:
### tela inicial
![Captura de tela 2024-08-04 213208](https://github.com/user-attachments/assets/119f9164-38e7-43d3-8c5c-1e7b117cb9b0)
### instruções
![Captura de tela 2024-08-04 213230](https://github.com/user-attachments/assets/a62ad060-4c63-402d-a661-06e4f14d17db)
### início do jogo
![Captura de tela 2024-08-04 213303](https://github.com/user-attachments/assets/83a44437-8cf1-40cf-8f40-cd4aeb7d5aec)
### CIn
![Captura de tela 2024-08-04 220606](https://github.com/user-attachments/assets/3fd574ad-b40d-48b1-b858-7816b9a371df)
### game over 1
### game over 2
### vitória







## FERRAMENTAS, BIBLIOTECAS E SEUS USOS:
Para a criação deste projeto, foi utilizada a biblioteca PyGame, por meio da qual foi possível estruturar o código visando a criação de um jogo. Essa biblioteca proporcionou a possibilidade de reconhecer as teclas digitadas pelos usuários como input para a execução do game, além de criar a tela de display, a hitbox do personagem, obstáculos e coletáveis, permitir a manipulação das sprites e muitas outras funcionalidades relacionadas à jogabilidade. Além disso, foram também utilizadas a biblioteca Sys, que permitiu a interrupção do código quando o usuário clica no “X” no canto superior esquerdo da tela, a biblioteca Random para a geração dos coletáveis e obstáculos de maneira aleatória e a biblioteca Time para o controle do tempo de jogo.  Ademais, foi utilizada a plataforma online [Pixilart](https://www.pixilart.com/) para a criação da parte artística do trabalho.




## CONCEITOS DA DISCIPLINA UTILIZADOS NO PROJETO:
No projeto, foram utilizados diversos conceitos abordados na disciplina de Introdução à Programação, entre eles, pode-se destacar:
- Estruturas condicionais (if, elif e else);
- Laços de repetição (for e while);
- Listas e Tuplas;
- Funções;

Desse modo, é perceptível o caráter educativo da disciplina, permitindo ao grupo aplicar o que foi ensinado durante o semestre somado à busca constante pela manutenção das boas práticas no ambiente python no desenvolvimento de JETIYODA: TestCase Ride!!!

## DESAFIOS E ERROS ENFRENTADOS DURANTE A EXECUÇÃO DO PROJETO:

Entre os diversos desafios que se opuseram, sem sucesso, à finalização do jogo, é importante destacar a utilização do Git e do GitHub, uma vez que os membros da equipe nunca haviam tido contato com tais recursos. Além disso, o aprendizado de PyGame, a compreensão de como fazer, sem que houvesse uma sensação visual de cansaço para o usuário, o fundo passar em loop e a lógica para que diferentes coletáveis não se sobrepusessem foram outros entraves evidentes.
Já sobre os erros cometidos durante a execução, o principal deles foi a falta de modularização inicial do código, o que culminou em uma dificuldade na compreensão do que estava sendo exposto. Porém, a equipe conseguiu reverter essa situação e aplicar melhor as Boas Práticas à produção.  



## INSTRUÇÕES DE JOGABILIDADE:

- Aperte a tecla “espaço” para voar;
- Para vencer o jogador deve coletar 350 fragmentos de crachás e chegar ao CIn;
- Caso o jogador bata três vezes em “Foguinhos”, ele perde;
- Ao coletar corações é aumentada uma vida (a quantidade de vidas aparece no canto direito da tela e indica em quantos foguinhos o jogador pode bater sem que perca o jogo);
- Ao coletar o “Robocin”, o personagem adquire imunidade aos “Foguinhos” por 6 segundos (no canto superior esquerdo é indicado em uma barra verde o quanto falta para que esse efeito seja desfeito);
- Na parte de cima da tela de display do jogo se situa uma barra de progressão, que indica o quanto falta para que o jogador chegue ao CIn.




