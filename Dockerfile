FROM python:3.9

ADD faker_api_workflow.py .
ADD faker/ /faker/
ADD requirements.txt .

RUN pip install -r requirements.txt

CMD [ "python", "./faker_api_workflow.py" ]
