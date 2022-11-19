# backend_sample_python
```bash
python -m venv .\code\venv\
```
/var/kubectl/kubectl", "get", "ing", "-A", "-o=jsonpath='{.items..spec..host}'
/var/kubectl/kubectl get ing -A -o=jsonpath='{.items..spec..host}
./kubectl get ing -A -o=jsonpath='{.items..spec..host}

kubectl get ing -A -o json
kubectl get ing -A -o=jsonpath='{.items..spec..host}'
kubectl get ing -A -o=jsonpath='{.items..spec.rules[]}'

kubectl get ing -A no -o json | jq -r '[.items[] | {host:.spec..host}]'


./kubectl get ing -A -o=jsonpath='{.items..spec..host}'