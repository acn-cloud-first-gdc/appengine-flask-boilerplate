environment="local"
cp configurations/${environment}.yaml env_variables.yaml

nosetests tests
(dev_appserver.py app.yaml --port=8081)