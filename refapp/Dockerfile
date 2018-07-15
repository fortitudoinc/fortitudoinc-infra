FROM isears/refapp-production:2.7.0

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
COPY ./omods/* /usr/local/tomcat/.OpenMRS/modules/