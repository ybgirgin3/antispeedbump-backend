docker build -t antispeedbump-backend .
docker run --name antispeedbump -p 80:80 antispeedbump-backend
