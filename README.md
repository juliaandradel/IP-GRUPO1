# 🌍⚽ Copa do Mundo

Bem-vindo à **Copa do Mundo**, um jogo de aventura e ação no qual você assume o papel de uma lenda do futebol e enfrenta grandes desafios para conquistar o troféu da Copa do Mundo!

---

## 1. Título e membros da equipe
**Copa dos Craques**  
**Membros:**  
- 🇵🇹 Cristiano Ronaldo  
- 🇦🇷 Lionel Messi
- 🇧🇷 Neymar Jr.  

---

## 2. Arquitetura do Projeto

O jogo foi desenvolvido com Pygame e estruturado em diferentes arquivos para melhor organização:

- **main.py**: controla o loop principal do jogo, eventos e lógica geral.
- **classes_jogador.py**: contém as classes relacionadas ao jogador e aos tiros.
- **classes_inimigo.py**: define o comportamento dos inimigos.
- **classes_jogo.py**: lida com telas de escolha e lobby de fases.
- **classes_coletaveis.py**: trata dos itens que podem ser coletados.

### Organização:
- O jogador é instanciado no início e se movimenta com as teclas `WASD`.
- O jogo é dividido em menus, lobby e fases com inimigos.
- A lógica de colisão define quando o jogador coleta itens, derrota inimigos ou interage com o troféu.
- Cada classe possui responsabilidades bem definidas, facilitando a manutenção e expansão.

---

## 3. Capturas de Tela

> (Adicionar aqui capturas de tela do sistema em funcionamento, mostrando menus, gameplay e a vitória após pegar o troféu.)

---

## 4. Ferramentas, bibliotecas e frameworks utilizados

- **Python 3**
- **Pygame**: biblioteca principal usada para renderização, eventos e lógica do jogo.

### Justificativa:
O Pygame é leve, fácil de aprender e ideal para protótipos rápidos de jogos 2D.

---

## 5. Divisão de trabalho

- 

---

## 6. Conceitos da disciplina utilizados

- **Programação Orientada a Objetos**: todo o jogo é baseado em classes com encapsulamento e herança.
- **Tratamento de eventos**: uso intensivo de eventos do Pygame.
- **Listas e estruturas de dados**: armazenam balas, inimigos e itens coletáveis.
- **Controle de fluxo**: loops aninhados para menus, fases e transições.
- **Modularização**: separação do código em múltiplos arquivos.

---

## 7. Desafios, erros e lições aprendidas

### Erro maior:
Mudança de lógica de movimentação do jogador muito tarde (de cenário fixo para o personagem fixo no centro), o que exigiu reestruturar grande parte do código em pouco tempo.

### Maior desafio:
Implementar essa nova movimentação e, ao mesmo tempo, manter a lógica de colisão, spawn de inimigos e coleta de itens funcionando.

### Lições aprendidas:
- Refatorar o código cedo evita retrabalho.
- Organização no GitHub ajuda no progresso coletivo.
- Dividir tarefas e manter comunicação clara no grupo é essencial.

---

## 8. Como jogar

### Requisitos:
- Python 3.x instalado
- Pygame instalado (`pip install pygame`)

### Instruções:

```bash
git clone https://github.com/seu-usuario/jogo-copa-do-mundo.git
cd jogo-copa-do-mundo
python main.py
```

Use as teclas `W`, `A`, `S`, `D` para movimentar-se e o mouse para atirar.
