# This is a Glitch startup script
ROOT_ENV=.rootenv
VIRTUALENV=.venv
if [ ! -d $ROOT_ENV ]; then
  python3 -m venv $ROOT_ENV
fi
if [ ! -f $ROOT_ENV/bin/pip ]; then
  curl --silent --show-error --retry 5 https://bootstrap.pypa.io/get-pip.py | $ROOT_ENV/bin/python
  $ROOT_ENV/bin/pip install virtualenv
fi
if [! -d $VIRTUALENV]; then
    virtualenv $VIRTUALENV
fi
cp .env.example .env
source $VIRTUALENV/bin/activate
pip install -r requirements.txt
python app.py 