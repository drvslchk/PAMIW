FROM terrillo/python3flask:latest

ENV STATIC_URL /static
ENV STATIC_PATH /app/static

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

# NGINX setup
COPY ./nginx.sh /nginx.sh
RUN chmod +x /nginx.sh

ENV PYTHONPATH=/app

ENTRYPOINT ["/nginx.sh"]

# Start Server
CMD ["/start.sh"]

EXPOSE 80 443
