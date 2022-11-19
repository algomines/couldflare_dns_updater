# backend_sample_python
```bash
python -m venv .\code\venv\
```

kubectl get ing -A -o json
kubectl get ing -A -o=jsonpath='{.items..spec..host}'
kubectl get ing -A -o=jsonpath='{.items..spec.rules[]}'

kubectl get ing -A no -o json | jq -r '[.items[] | {host:.spec..host}]'