import twitter
api = twitter.Api(
    consumer_key = 'XdGOGUjMbEBkR7BYcsyp7e8Fd',
    consumer_secret = '9Fqw31VWFSMfJMDsdNZZgACM50VS2ZPK8r1jvBCJ020mcRQfwt',
    access_token_key = '190673194-p4ubf7dtQs7v03Gd2653CVCA8thrJoOboC3s1cVK',
    access_token_secret = 'DrnO8y9D8VcVzGRm7K2HzcyUbmRYBeaeU66g25GYsJMyu')

# Verificando se as credenciais funcionaram
#print(api.VerifyCredentials())

# Imprimindo todos os amigos
#amigos = api.GetFriends()
#print([a.name for a in amigos])

# Imprimindo todas as mensagens públicas de um usuario
#status_user = api.GetUserTimeline('cauemoura')
#print([s.text for s in status_user])

# Postando no meu perfil
status = api.PostUpdate('Estudando a API do Twitter!!')
print(status.text)
