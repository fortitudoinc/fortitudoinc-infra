# Build refapp image, including omods from submodules
DOCKER_IMAGE_NAME=fortitudoinc-infra-refapp

docker image rm $DOCKER_IMAGE_NAME

for module in $(ls ./external-modules/)
do
    echo "Building:" $module
    cd ./external-modules/$module && mvn clean package -DskipTests
    cd -
    cp ./external-modules/$module/omod/target/*.omod ./refapp/omods/
done

docker build ./refapp/ -t $DOCKER_IMAGE_NAME