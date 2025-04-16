FROM python:3.12.1-bookworm
WORKDIR /usr/src/app
COPY app .
COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
RUN chmod +x /usr/local/bin/docker-entrypoint.sh \
&& pip install --no-cache-dir --break-system-packages -r requirements.txt
ENV id_municipio = "41083"
ENV municipio = "Dos Hermanas"
ENV api_key = "xxx"
ENV client_id = "xxx"
ENV client_secret = "xxx"
ENV access_token = "xxx"
ENV api_base_url = "https://mastodon.social"
CMD /usr/local/bin/docker-entrypoint.sh