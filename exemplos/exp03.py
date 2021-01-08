import rpa as r

r.init(visual_automation = True)

r.url('url')

senha=input("Digite sua email:")
r.type('//*[@name="login"]', '{}'.format)
senha=input("Digite sua senha:")
r.type('//*[@name="senha"]', '{}[enter]'.format(senha))

r.wait(6.6)

r.url('url')
r.type('//*[@name="instagram_id"]', 'aliciakarls')
r.wait(2)

r.click('//*[@id="iniciarTarefas"]')
r.click('//*[@id="conectar_step_4"]')
r.wait(6.6)
# r.click('//*[@placeholder="Pesquisar"]')
print(r.exist('//*[@placeholder="Pesquisar"]'))

# r.wait(6.6)

r.close()