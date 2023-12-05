Aluno:

Nome: Gabriel Bonati Dias
RA: 11202130340

Algoritmo Escolhido:
Para este projeto, escolhi implementar o algoritmo Deep Q Network (DQN), uma técnica popular de aprendizado por reforço para problemas de controle em ambientes complexos.

Bibliotecas Necessárias:
Retro Gym: Para interação com o ambiente do Super Mario World.

Instalação: pip install gym-retro
TensorFlow: Para a implementação da rede neural do DQN.

Instalação: pip install tensorflow
NumPy: Para manipulação eficiente de arrays e operações numéricas.

Instalação: pip install numpy
Instruções de Instalação e Execução:
Instalar Retro Gym:

Execute o comando pip install gym-retro para instalar a biblioteca Retro Gym.
Instalar TensorFlow:

Execute pip install tensorflow para instalar a biblioteca TensorFlow.
Instalar NumPy:

Instale NumPy com o comando pip install numpy.
Copiar ROM do Jogo:

Copie a ROM do jogo para o diretório site-packages/retro/data/stable/SuperMarioWorldSnes/ com o nome rom.sfc.
Executar o Código de Treinamento:

Execute o comando python train.py para iniciar o treinamento do agente DQN. O código permite continuar o treinamento desde a última execução.
Executar o Código de Jogo:

Após o treinamento, execute python play.py para assistir o agente treinado jogar a fase YoshiIsland2.
Observações Importantes:
Certifique-se de ter as permissões adequadas para acessar e modificar os diretórios e arquivos necessários.
Este readme assume que você possui o Python e o pip instalados na sua máquina.
