### BASH

1. chmod +x [path_to_file] `сделать файл исполняемым`

### DOCKER

1. `docker ps`
2. `docker-compose up -d --build` apply changes if sources had changed
3. `docker-compose up -d`  run
4. `docker-compose down`  stop
5. `docker-compose restart` reload
6. `docker system prune` удаляет ненужные артефакты (запускать когда все запущено)

7. `docker container ls` список портов
8. `docker rm -f [number]` убить контейнер

9. `docker container prune` очищает контейнеры докера
10. `docker image prune` очищает образы докера
11. `docker system prune` очищает все в докере

### ENV

1. `python3 -m venv env`
2. `source env/bin/activate`
3. `pip install -r requirements.txt`
4. `deactivate`

### Git

1. `git init`  создать git
2. `git status`  проверить статус файлов
3. `git add .`  добавить все файлы в отслеживаемые
4. `git commit -m [commit text]`  коммит
5. `git push`  залить на github

6. `git branch`  все ветки
7. `git branch [branch_title]`  создать верку
8. `git checkout [branch_title]`  переключиться на ветку
9. `git merge [branch_title]`  сливаем ветку в мастер
10. `git branch -D [branch_title]`  удалить ветку

11. `git clone -b docker [url_to_git_repo]` 

### Pytest

1. `—setup-show`
