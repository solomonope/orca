FROM python:3.10 as builder

WORKDIR /opt/orca

COPY . .

RUN pip install  poetry

RUN poetry build -f wheel


FROM python:3.10-alpine

COPY --from=builder  /opt/orca/dist/*.whl  /opt/orca/

RUN pip install /opt/orca/*.whl

ENTRYPOINT ["orca"]