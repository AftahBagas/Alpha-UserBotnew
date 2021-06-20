# Alpha
FROM biansepang/weebproject:buster

# Dockerfile
# Alpha
# Dockerfile
RUN git clone -b Alpha https://github.com/AftahBagas/Alpha-Userbot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/AftahBagas/Alpha-Userbot/Alpha/requirements.txt

CMD ["python3","-m","userbot"]
