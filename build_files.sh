# Use Python 3 explicitly
pip3 install --upgrade pip
pip3 install -r requirements.txt

# Collect static files
python3.10 manage.py collectstatic --noinput

# Run database migrations
python3.10 manage.py migrate --noinput
