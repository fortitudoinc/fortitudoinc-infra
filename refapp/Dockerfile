FROM isears/refapp-production:latest

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
COPY ./omods/* /usr/local/tomcat/.OpenMRS/modules/