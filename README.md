# Docker-Fibonacci

Реализовать веб-сервис, который возвращает числа Фибоначчи.
Сервис должен по GET запросу с параметром k возвращать k-ое число Фибоначчи.
Необходимо реализовать кеширование, то есть, если число уже было запрошено, результат должен браться из кеша, а не пересчитываться.
Кеширование необходимо реализовать с помощью memcached (или redis), фреймворк для веб-сервиса используйте на ваше усмотрение, однако для такого небольшого проекта брать Django скорее перебор.
Приложение должно запускаться в Docker.

1.	Скачать репозиторий репозиторий.
2.	Если не устоновлен Docker, установить.
3.	Собрать контейнеры:
3.1. Windows:  командой docker-compose build 
3.2. Linux: командой sudo docker-compose build
4.	Запустить контейнеры:
4.1. Windows: команда docker-compose up.
4.2. Linux: команда sudo docker-compose up.

Implement a web service that returns Fibonacci numbers.
The service should return the k-th Fibonacci number on a GET request with the k parameter.
It is necessary to implement caching, that is, if a number has already been requested, the result should be taken from the cache, and not recalculated.
Caching must be implemented using memcached (or redis), use the framework for the web service at your discretion, but for such a small project, taking Django is rather overkill.
The application must run in Docker.

1. Download the repository repository.
2. If Docker is not installed, install.
3. Collect containers:
3.1. Windows: with the docker-compose build command
3.2. Linux: with the sudo docker-compose build command
4. Start containers:
4.1. Windows: docker-compose up command.
4.2. Linux: sudo docker-compose up command.
