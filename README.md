## Script
Запуск:
```
python script/sec_2_human_readable.py
```

## Kubernetes

Чарты для сервисов Nginx, Prometheus и Grafana в директории kubernetes:
```
cd kubernetes
```

Установка чартов (устанавливать в один неймспейс!):
```
helm install nginx-server ./sbermarket-task-chart
helm install prometheus ./prometheus
helm install grafana ./grafana
```

Для доступа к сервисам по доменному имени `my-site.example.local`:

1. Найти cluster-ip (колонна `ADDRESS`) в `kubectl get ingress`:
   ```
    NAME                      CLASS    HOSTS                              ADDRESS        PORTS   AGE
    sbermarket-task-ingress   nginx    my-site.example.local              192.168.49.2   80      13h
   ```
2. Добавить записи в `/etc/hosts`:
   ```
    <CLUSTER-IP> my-site.example.local
    <CLUSTER-IP> grafana.my-site.example.local
    <CLUSTER-IP> prometheus.my-site.example.local
   ```

3. Сервисы теперь доступны в браузере по урлам:
   ```
   my-site.example.local - nginx-server
   prometheus.my-site.example.local - Prometheus web-UI
   grafana.my-site.example.local - Grafana web-UI
   ```