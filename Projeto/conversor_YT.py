from pytube import YouTube
print('\033[0;31m       Download De MP4(Videos) e MP3(Áudios)\033[m')
print('\033[0;34m1\033[m - MP4')
print('\033[0;34m2\033[m - MP3')
while True:
    opcao = input('Digite a Opção de Download: ')
    if opcao == '1' or opcao == '2':
        opcao = int(opcao)
        break
    print('Opção Selecionada Incorreta. Por Favor escolha um número entre 1 ou 2')
video = input('\033[0;32mDigite um ou mais links de video do YT\n(\033[0;33mPara baixar mais de um video separa com um "ESPACE"\033[m):\n').split(' ')
lista_de_link = list(video)

if opcao == 1:
    for i in lista_de_link:
        yt = YouTube(i).streams.get_highest_resolution().download()

else:
    for i in lista_de_link:
        yt = YouTube(i).streams.get_audio_only().download()
