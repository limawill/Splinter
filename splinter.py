import time
from splinter import Browser
arq = open('/home/will/Documentos/Python/musica.txt', 'r') 
texto = arq.readlines() 

for linha in texto:
    nome,user,senha,data,sexo = linha.split(";")	
    with Browser() as browser:
        # Visit URL
        url = "http://fund.bedream.me/join?project=1713"
        browser.visit(url)
        #browser.fill('q', 'splinter - python acceptance testing for web applications')
        # Find and click the 'search' button
        button = browser.find_by_id('create-acc')
        # Interact with elements
        button.click()
        browser.find_by_id('registration_email').fill(nome) 
        browser.find_by_id('registration_username').fill(user) 
        browser.find_by_id('registration_password').fill(senha)
        browser.find_by_id('registration_birthday').fill(data)
        browser.select("registration[gender]", sexo)
        browser.check ("term") 
        browser.find_by_text('Criar minha conta!').click()
        time.sleep (5)
        browser.quit()
arq.close() 
