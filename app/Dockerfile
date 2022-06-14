#=============Build Layer==============#
FROM public.ecr.aws/lambda/python:3.8 as build

RUN yum install -y unzip && \
    curl -Lo "/tmp/chrome-linux.zip" "https://www.googleapis.com/download/storage/v1/b/chromium-browser-snapshots/o/Linux_x64%2F992733%2Fchrome-linux.zip?alt=media" && \
    unzip /tmp/chrome-linux.zip -d /opt/

#=============Run Layer==============#
FROM public.ecr.aws/lambda/python:3.8

WORKDIR ${LAMBDA_TASK_ROOT}

COPY . ${LAMBDA_TASK_ROOT}

COPY --from=build /opt/chrome-linux /opt/chrome

RUN yum install atk cups-libs gtk3 libXcomposite alsa-lib \
    libXcursor libXdamage libXext libXi libXrandr libXScrnSaver \
    libXtst pango at-spi2-atk libXt xorg-x11-server-Xvfb \
    xorg-x11-xauth dbus-glib dbus-glib-devel -y
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD [ "app.lambda_handler" ]
