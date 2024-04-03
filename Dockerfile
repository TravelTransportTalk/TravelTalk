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
RUN python -m venv /env &&\
    pip install --no-cache-dir -r /app/requirements.txt

CMD [\
    "--browser.gatherUsageStats=false" \
]

ADD --chown=runner webui /app/webui/
EXPOSE 8501
USER runner
