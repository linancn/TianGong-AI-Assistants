# TianGong AI Assistants

## Env Preparing

### VSCode Dev Contariners

[Tutorial](https://code.visualstudio.com/docs/devcontainers/tutorial)

Python 3 -> Additional Options -> 3.11-bullseye -> ZSH Plugins (Last One) -> Trust @devcontainers-contrib -> Keep Defaults

### Local Env

Install `Python 3.11`

```bash
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.11
```

Setup `venv`:

```bash
python3.11 -m venv .venv
source .venv/bin/activate
```

Install requirements:

```bash
pip install --upgrade pip
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install -r requirements.txt --upgrade
```

```bash
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install -y libmagic-dev poppler-utils tesseract-ocr libreoffice pandoc
```

Install Cuda (optional):

```bash
sudo apt install nvidia-cuda-toolkit
```

### Auto Build

The auto build will be triggered by pushing any tag named like v$version. For instance, push a tag named as v0.0.1 will build a docker image of 0.0.1 version.

```bash
#list existing tags
git tag
#creat a new tag
git tag v0.0.1
#push this tag to origin
git push origin v0.0.1
```

### sphinx

```bash

sphinx-apidoc --force -o sphinx/source/ src/
sphinx-autobuild sphinx/source docs/
```

### Production Run

```bash
docker run --detach \
    --name tiangong-agent \
    --restart=always \
    --expose 8501 \
    --net=tiangongbridge \
    --env ui=tiangong-en \
    --env VIRTUAL_HOST=YourURL \
    --env VIRTUAL_PORT=8501 \
    --env LETSENCRYPT_HOST=YourURL \
    --env LETSENCRYPT_EMAIL=YourEmail \
    image:tag
```
