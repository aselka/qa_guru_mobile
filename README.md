## Проект Mobile автотестов для приложения Wikipedia

<!-- Технологии -->

### Используемые технологии
<p  align="center">
  <code><img width="5%" title="Pycharm" src="./attachments/logo/pycharm.png"></code>
  <code><img width="5%" title="Python" src="./attachments/logo/python.png"></code>
  <code><img width="5%" title="Pytest" src="./attachments/logo/pytest.png"></code>
  <code><img width="5%" title="Selene" src="./attachments/logo/selene.png"></code>
  <code><img width="5%" title="GitHub" src="./attachments/logo/github.png"></code>
  <code><img width="5%" title="Browserstack" src="./attachments/logo/browserstack.png"></code>
  <code><img width="5%" title="Appium" src="./attachments/logo/appium.png"></code>
  <code><img width="5%" title="Selenium" src="./attachments/logo/selenium.png"></code>

</p>

### Что выполняет тест:
![This is an image](attachments/screenshots/test1.png)


### Видео о прохождении одного из тестов
![This is an image](attachments/video/video.gif)


## :computer: Запуск тестов из терминала
```bash
env -S "context=browserstack" pytest .
env -S "context=emulation" pytest .
```

<!-- Jenkins -->

### <img width="3%" title="Jenkins" src="attachments/logo/jenkins.png"> Запуск проекта в Jenkins

### [Job](https://jenkins.autotests.cloud/job/qa_guru_mobile_new/)

##### При нажатии на "Собрать сейчас" начнется сборка тестов и их прохождение


<!-- Browserstack -->

### <img width="3%" title="Browserstack" src="./attachments/logo/browserstack.png"> Запуск проекта в [Browserstack](https://app-automate.browserstack.com/dashboard/v2/builds/3f67a07716e00de80faea53fa149a79d79b02ff6/sessions/4c7048636db735420b8d18f6207b4c34f773fd8e)
##### Где в реальном времени можно следить за прохождением теста через логи.

![This is an image](attachments/screenshots/browserstack.png)



<!-- Telegram -->

### <img width="3%" title="Telegram" src="attachments/logo/tg.png"> Telegram

##### Настроен телеграм-бот, после прохождения тестов в Jenkins присылает уведомление с отчетом в Телеграм

##### Скриншот отчета в телеграм
![This is an image](attachments/screenshots/telegram2.png)

