from models.calcular import Calcular
import PySimpleGUI as sg


def main() -> None:
    login()


def login() -> None:
    score_s: int = 5
    attempts_s: int = 0

    layout1 = [[sg.Text("Informe seu nome para jogar: "), sg.Input(key='name')],
               [sg.Text('Informe a dificuldade desejada [1, 2, 3]: '), sg.Input(key='difficulty')],
               [sg.Button('OK'), sg.Button('Exit')]]

    window = sg.Window('Inicio', layout1)
    event, values = window.read()

    if event is None or event == 'Exit':
        window.close()

    name = values['name']
    difficulty = int(values['difficulty'])

    if name and difficulty:
        window.close()
        jogar(name, difficulty, score_s, attempts_s)


def jogar(name: str, difficulty: int, score: int, attempts: int):
    obj = Calcular(difficulty)
    problem = obj.gerar_operacao()

    layout2 = [[sg.Text(f'Jogador: {name} | Pontos Faltando: {score} | Tentativas: {attempts}')],
               [sg.Text(f'Problema {attempts + 1}: {problem}'), sg.Input(key='answer')],
               [sg.Text('Resposta = '), sg.Text(key='-verifica-')],
               [sg.Button('OK'), sg.Button('Exit')]]

    window = sg.Window('GAME', layout2)
    event, values = window.read()

    if event == 'Exit':
        exit(1)
        window.close()

    test = obj.checar_resultado(int(values['answer']))
    if test:
        score -= 1
        attempts += 1
        window['-verifica-'].update('CORRETA')
    else:
        attempts += 1
        window['-verifica-'].update('ERRADA')

    window.read()
    window.close()
    if score:
        jogar(name, difficulty, score, attempts)

if __name__ == '__main__':
    main()
    