
virtualenv env
.\env\Scripts\activate
deactivate

python -m pip install pymongo --proxy http://127.0.0.1:8011

<!-- freeze requirement -->
pip3 freeze > requirements.txt




## afterward
pip install flask flask-sqlalchemy --proxy http://127.0.0.1:8011




pip install ruamel.yaml --proxy http://127.0.0.1:8011


pip install pandas --proxy http://127.0.0.1:8011

