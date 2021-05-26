FROM python:3.9

MAINTAINER gtaiyou24<https://github.com/gtaiyou24> gtaiyou24@gmail.com

ENV TZ=Asia/Tokyo

ARG project_dir=/market-data-curator
COPY . $project_dir
WORKDIR $project_dir

ENV PYTHONPATH=$project_dir

# パッケージをインストール
RUN pip install --upgrade pip && pip install -r requirements.txt
