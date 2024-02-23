FROM postgres:14.9-bookworm
COPY ./postgresql.conf /etc/postgresql.conf

CMD ["postgres", "-c", "config_file=/etc/postgresql.conf"]
