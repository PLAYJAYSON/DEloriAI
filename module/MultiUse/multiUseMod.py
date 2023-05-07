import os
def dirUser(userId):
    uId = str(userId)

    if __name__ != '__main__':
        mainPath = os.path.abspath(os.getcwd())
        print(mainPath)
        myBotUsersPath = f'{mainPath}/cache/multiUse/Users'
    elif __name__ == '__main__':
        myBotUsersPath = ''  #  full abspath to dir

    userDir = myBotUsersPath + f'/{uId}'
    print(userDir)
    if os.path.isdir(userDir):
        print('Директория пользователя существует')
    else:
        print('Директория пользователя не существует')
        os.makedirs(userDir+'/cache', 0o754)
        with open(f'{userDir}/cache/flag_RPS.txt', 'w') as flagRPS_file:
            flagRPS_file.write('False')
        with open(f'{userDir}/cache/flag_echo.txt', 'w') as flagEcho_file:
            flagEcho_file.write('False')
        with open(f'{userDir}/cache/flag_YT.txt', 'w') as flagYT_file:
            flagYT_file.write('False')
        with open(f'{userDir}/cache/flag_wiki.txt', 'w') as flagWiki_file:
            flagWiki_file.write('False')

        print('Директория пользователя создана')
    return uId

if __name__ == '__main__':
    dirUser()