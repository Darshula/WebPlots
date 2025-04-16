FROM r-base:latest

RUN groupadd dockeruser

RUN useradd -m -g dockeruser -G staff -s /bin/bash dockeruser

RUN mkdir -p /home/dockeruser/backend/scripts

RUN mkdir -p /home/dockeruser/backend/static/plots

RUN chown -R dockeruser:dockeruser /home/dockeruser/backend

RUN apt-get update && apt-get install -y --no-install-recommends              \
    r-base r-base-dev                                                         \
    libssl-dev libcurl4-openssl-dev libssh2-1-dev libpq-dev zlib1g-dev pandoc \
    python3 pip python3-matplotlib python3-numpy                              \
    python3-flask python3-flask-cors                                          \
    && rm -rf /var/lib/apt/lists/*

RUN Rscript -e "install.packages(c('htmlwidgets', 'rgl', 'plotly', 'ggplot2', 'readxl', 'dplyr', 'tidyr', 'ggfortify', 'DT', 'reshape2', 'knitr', 'lubridate', 'pwr', 'psy', 'car', 'doBy', 'imputeMissings', 'RcmdrMisc', 'questionr', 'vcd', 'multcomp', 'KappaGUI', 'rcompanion', 'FactoMineR', 'factoextra', 'corrplot', 'ltm', 'goeveg', 'corrplot', 'FSA', 'MASS', 'scales', 'nlme', 'psych', 'ordinal', 'lmtest', 'ggpubr', 'dslabs', 'stringr', 'assist', 'ggstatsplot', 'forcats', 'styler', 'remedy', 'snakecaser', 'addinslist', 'esquisse', 'here', 'summarytools', 'magrittr', 'tidyverse', 'funModeling', 'pander', 'cluster', 'abind', 'gapminder', 'devtools'), repos='https://cloud.r-project.org')"

WORKDIR /home/dockeruser/backend/

COPY . /home/dockeruser/backend/

USER dockeruser

RUN pip install --no-cache-dir -r requirements.txt --break-system-packages

EXPOSE 65535

CMD ["python3", "service.py"]
