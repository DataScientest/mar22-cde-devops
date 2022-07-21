# MAR22 CDE DevOps

Pour lancer l'application:

```sh

git clone https://github.com/DataScientest/mar22-cde-devops.git
cd mar22-cde-devops

python3 -m venv venv

source venv/bin/activate

pip3 install -r requirements.txt

python3 -m uvicorn main:api --host=0.0.0.0 --reload
```
