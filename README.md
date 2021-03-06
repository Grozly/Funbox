<h1><a id="user-content-квалификационное-задание-для-разработчиков-python" class="anchor" aria-hidden="true" href="#квалификационное-задание-для-разработчиков-python"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Квалификационное задание для разработчиков Python</h1>
<h2><a id="user-content-задание" class="anchor" aria-hidden="true" href="#задание"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Задание</h2>
<p>Реализуйте web-приложение для простого учета посещенных (неважно, как, кем и когда)
ссылок. Приложение должно удовлетворять следующим требованиям.</p>
<ul style="list-style-type: square">
<li>Приложение написано на языке Python версии ~&gt; 3.7.</li>
<li>Приложение предоставляет JSON API по HTTP.</li>
<li>Приложение предоставляет два HTTP ресурса.</li>
</ul>
<pre><code>Запрос:
POST /visited_links
 {
    "links": [
    "https://ya.ru",
    "https://ya.ru?q=123",
    "funbox.ru",
    "https://stackoverflow.com/questions/11828270/how-to-exit-the-vim-editor"
    ]
}
Ответ:
{
    "status": "ok"
}
</code></pre>
<pre><code>Запрос:
GET /visited_domains?from=1545221231&amp;to=1545217638
Ответ:
{
    "domains": [
    "ya.ru",
    "funbox.ru",
    "stackoverflow.com"
    ],
    "status": "ok"
}
</code></pre>
<ul style="list-style-type: square">
<li>Первый ресурс служит для передачи в сервис массива ссылок в POST-запросе. Временем их посещения считается время получения запроса сервисом.</li>
<li>Второй ресурс служит для получения GET-запросом списка уникальных доменов,
посещенных за переданный интервал времени.</li>
<li>Поле status ответа служит для передачи любых возникающих при обработке запроса
ошибок.</li>
<li>Для хранения данных сервис должен использовать БД Redis.</li>
<li>Код должен быть покрыт тестами.</li>
<li>Инструкции по запуску должны находиться в файле README.</li>
</ul>
<h2><a id="user-content-требования-к-системе" class="anchor" aria-hidden="true" href="#требования-к-системе"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Требования к системе</h2>
<p>Для работы с контейнерами в системе должен быть установлен Docker Desktop</p>
<h2><a id="user-content-инструкция-по-запуску" class="anchor" aria-hidden="true" href="#инструкция-по-запуску"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Инструкция по запуску</h2>
<p>Убедитесь, что Docker сейчас работает в системе</p>
<p>Скопируйте репозиторий командой <code>git clone https://github.com/Grozly/Funbox.git</code></p>
<p>Откройте папку репозитория Funbox, где в корне находится docker-compose.yml и запустите команду <code>docker-compose up</code></p>
<p>Дождитесь сборки образов и их запуска</p>
<p>Образ redis работает на порту 6379</p>
<p>Сервис доступен по адресу http://127.0.0.1:8000/api/</p>
<p>Пример curl для post запроса</p>
<pre><code>curl --location --request POST 'http://127.0.0.1:8000/api/visited_links/' --header 'Content-Type: application/json' --data-raw '{"links": ["https://ya.ru", "https://ya.ru?q=123", "funbox.ru", "https://stackoverflow.com/questions/11828270/how-to-exit-the-vim-editor"]}'</code></pre>
<p>Пример curl для get запроса, где <code>?from=&to=</code> - интервал времени для получения статистики, например <code>?from=1612355442&to=1612359542</code></p>
<pre><code>curl --location --request GET 'http://127.0.0.1:8000/api/visited_domains/?from=&to=' --data-raw ''</code></pre>

<h2><a id="user-content-тестирование" class="anchor" aria-hidden="true" href="#тестирование"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Тестирование</h2>
<p>Откройте папку репозитория Funbox, где в корне находится docker-compose.yml и запустите команду <code>docker-compose exec django sh</code></p>
<p>Запустите команду <code>pytest</code></p>
