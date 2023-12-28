from pytube import YouTube
print('\033[0;31m       Download De MP4 e MP3(Videos e Áudios)\033[m')
print('\033[0;34m1\033[m - MP4 (720p)')
print('\033[0;34m2\033[m - MP3 (160kbps)')
while True:
    opcao = input('Digite a Opção de Download: ')
    if opcao == '1' or opcao == '2':
        opcao = int(opcao)
        break
    print('Opção selecionada incorretamente. Escolha um número entre 1 ou 2')
video = input('\033[0;32mDigite um ou mais links do YT\n(\033[0;33mPara fazer mais de um download separa com um ","\033[m):\n').split(',')
lista_de_link = list(video)

if opcao == 1:
    for i in lista_de_link:
        #   Download para MP4
        yt = YouTube(i).streams.filter(res=('720p')).first().download()

else:
    for i in lista_de_link:
        #   Download para MP3
        yt = YouTube(i).streams.filter(only_audio=True, abr=('160kbps')).first().download()

