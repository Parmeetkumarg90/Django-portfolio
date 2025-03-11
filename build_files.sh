# Use Python 3 explicitly
pip install --upgrade pip
pip install -r requirements.txt

# Collect static files
python3.12 manage.py collectstatic --noinput

# Run database migrations
python3.12 manage.py migrate --noinput