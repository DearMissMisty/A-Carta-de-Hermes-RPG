#A carta de Hermes

import time
def acao(texto):
    print(texto)
    time.sleep(4)

def falar(texto):
    print("\033[1m" + texto + "\033[0m")
    time.sleep(4)

input("Pressione Enter para começar a jogar...")
print('Bem-vindo(a) ao RPG "A carta de Hermes", caro jogador!')
time.sleep(1.3)
print("Antes de iniciarmos, gostaria de saber seu nome: ")
nome = input("> ")
time.sleep(1.3)
print("Só mais uma coisinha, qual é a sua bebida favorita?")
bebida = input("> ")
print(f'Obrigada, {nome}! Prepare-se para uma aventura emocionante!')
time.sleep(1.3)

inventario = ["A carta para Apolo", "20 Dracmas", f"{bebida}", "Mapa da cidade de Koritzia", "Chave do templo do lago sul", "Espada de bronze"]

acao("=======================\nA CARTA DE HERMES\n=======================")
print("Era uma manhã tranquila.")
time.sleep(2)
acao("Depois de dias de trabalho árduo, você finalmente tinha conseguido tirar um tempo para descansar.")
acao("Você havia encontrado um lugar confortável à sombra de uma árvore e, pela primeira vez em dias, não tinha absolutamente nenhuma obrigação.")
acao("Até ouvir uma voz familiar atrás de você.")
falar(f"— Você faria um favor para mim, {nome}?")
acao("Você se vira e vê Hermes, o mensageiro dos deuses, parado atrás de você.")
falar(f"— Preciso que entregue isso para mim, {nome}. É uma carta muito importante e você não pode se dar ao luxo de perdê-la.")
acao("Oque você faz?\n [1] Aceitar a missão\n [2] Recusar a missão")
inicio = int(input("> "))

while inicio != 1 and inicio != 2:
    acao("Opção inválida. Por favor, escolha uma opção válida.")
    acao("Oque você faz?\n [1] Aceitar a missão\n [2] Recusar a missão")
    inicio = int(input("> "))
if inicio == 1:
    falar(f"— Ótimo! Eu sabia que podia contar com você, darling! Hahaha!.")
    falar(f"— Sabe, eu sou um deus muito ocupado, então não posso me dar ao luxo de perder tempo com coisas pequenas. Por isso, preciso que você entregue essa carta para mim o mais rápido possível.")
    falar(f"— Você irá até o templo do lago sul, e entregrá essa carta para meu irmaozinho, Apolo. Ele é um deus muito ocupado também, então não se atrase!")
    falar(f"— Espero encontrá-lo ao por do sol com a carta já em mãos!")
    falar(f"— Ah, sim! E antes que eu me esqueça... não se preocupe com o caminho, eu já deixei um mapa e umas coisinhas para você na sua mochila.")
    falar(f"— Boa sorte, {nome}! Hahaha!")
    acao("Hermes desaparece em um piscar de olhos, deixando você sozinho com a carta e a mochila.")
    acao(f"Curioso com oque Hermes te deixou, você abre a mochila e encontra:")
    for item in inventario:
        print("- " + item)
    acao(f"Ok, sem perder tempo! Você pega o seu mapa e verifica o destinatário.")
    acao(f"Para chegar ao templo do lago sul, você precisa atravessar toda a cidade de Koritzia, e depois seguir pela trilha que leva até o templo.")
    acao(f"A travessia demora cerca de 3 horas. Você chegaria no destino ao por do sol, então você não pode se atrasar!")
    acao(f"Esse seria o caminho mais seguro, mas você também pode pegar um atalho pela floresta...")
    acao(f"Mas atenção! O caminho é sinuoso e as lendas dizem que a floresta é assombrada por espíritos malignos.")
    acao(f"Por onde ir? \n [1] Seguir pelo caminho seguro, a cidade\n [2] Seguir pelo atalho na floresta")
    caminho = int(input("> "))
    while caminho != 1 and caminho != 2:
        acao("Opção inválida. Por favor, escolha uma opção válida.")
        acao(f"Por onde ir? \n [1] Seguir pelo caminho seguro, a cidade\n [2] Seguir pelo atalho na floresta")
        caminho = int(input("> "))
    if caminho == 1:
            acao(f"Você decide seguir pelo caminho seguro, atravessando a cidade de Koritzia.")
            acao(f"Durante a travessia, você encontra algumas pessoas amigáveis que te ajudam a encontrar o caminho certo.")
            acao(f"Após algumas horas de caminhada, você finalmente chega ao templo do lago sul, com a carta em mãos.")
            acao(f"Você entrega a carta para Apolo, que agradece e te recompensa com uma quantia generosa de dracmas.")
            acao("=======================\nFINAL BOM\n=======================\n Parabéns! Você completou a missão com sucesso e foi recompensado por isso. Você sobreviveu e cumpriu sua missão!")
    elif caminho == 2:
            acao(f"Você decide seguir pelo atalho na floresta, mesmo sabendo dos perigos que ela esconde.")
            acao(f"Enquanto caminha pela trilha sinuosa, você sente uma presença estranha ao seu redor.")
            acao(f"De repente, um espírito maligno aparece diante de você, bloqueando seu caminho.")
            acao(f"Você tenta lutar contra o espírito, mas ele é muito poderoso e você acaba sendo derrotado.")
            acao("=======================\nFINAL RUIM\n=======================\n Você morreu ao enfrentar o espírito maligno na floresta. Tente novamente e escolha o caminho seguro para ter uma chance de sobreviver.")

elif inicio == 2:
    falar(f"— Me perdoe, grande deus Hermes, filho de Zeus, mas eu não posso aceitar essa missão.")
    acao(f"Hermes te olha com uma expressão de desapontamento e raiva.")
    falar(f"— Como ousas recusar uma missão de um deus, {nome}?! É uma pena, eu gostava tanto de você...")
    falar("— Eu...")
    acao(f"Hermes se aproxima de você, e com um gesto rápido, ele segura seu rosto com uma mão.")
    acao(f"Os olhos de Hermes brilham com uma luz sinistra.")
    falar(f"— Pela sua ignorância, você não me dá outra escolha a não ser puni-lo. Adeus, {nome}.")
    acao(f"Você sente uma dor cortante percorrer sua garganta. Você tenta gritar, mas não consegue emitir nenhum som.")
    acao(f"O deus se desintegra em uma luz ofuscante. Você fecha seus olhos o mais rápido que consegue, mas você fica tão atordoado que cai no chão.")
    acao("=======================\nFINAL RUIM\n=======================\n Você morreu por recusar a missão de Hermes. Tente novamente e aceite a missão para ter uma chance de sobreviver.")
