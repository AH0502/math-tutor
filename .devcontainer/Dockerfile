FROM python:3.12.9
WORKDIR /app

COPY requirements2.txt .

RUN python -m venv /opt/venv && \
    . /opt/venv/bin/activate && \
    pip install -r requirements2.txt

ENV PATH="/opt/venv/bin:$PATH"

COPY . .

CMD [ "streamlit", "run", "Home.py" ]
