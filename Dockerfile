FROM docker.io/library/python:3.12-slim-bookworm

RUN useradd -m -s /bin/bash runner
WORKDIR /app/webui
ENV PATH /env/bin:$PATH

ENTRYPOINT [\
    "streamlit", \
    "run", \
    "entry.py" \
]

ADD --chown=runner ./requirements.txt /app/requirements.txt
ADD --chown=runner ./pyproject.toml /app/pyproject.toml
RUN python -m venv /env &&\
    pip install --no-cache-dir -r /app/requirements.txt

ADD --chown=runner webui /app/webui/
RUN pip install -e /app

CMD [\
    "--browser.gatherUsageStats=false" \
]

EXPOSE 8501
USER runner
