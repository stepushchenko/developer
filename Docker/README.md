### DOCKER

```bash
docker ps
docker-compose up -d --build  # apply changes if sources had changed
docker-compose up -d  # run
docker-compose down  # stop
docker-compose restart # reload
docker system prune # удаляет ненужные артефакты (запускать когда все запущено)
docker container ls # список портов
docker rm -f [number] # убить контейнер
docker container prune # очищает контейнеры докера
docker image prune # очищает образы докера
docker system prune # очищает все в докере
```