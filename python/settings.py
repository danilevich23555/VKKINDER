def tokens():
    with open('tokens\\vk_token_communities.txt', 'r') as token_vk_communities:
        token_vk_communities = token_vk_communities.read().strip()
    with open('tokens\\vk_token.txt', 'r') as vk_token:
        vk_token = vk_token.read().strip()
        if vk_token == '':
            vk_token = input('Введите токен для авторизаии, файл vk_token.txt пустой')
    return [token_vk_communities, vk_token]