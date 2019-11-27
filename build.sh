# Build mobile gateway
echo "Building mobile gateway..."

cd mobile-gateway/
./gradlew build

cd -

# Build refapp image, including omods from submodules
echo "Building refapp modules..."

for module in $(ls ./external-modules/)
do
    echo "Building:" $module
    cd ./external-modules/$module && mvn clean install -DskipTests
    cd -
    cp ./external-modules/$module/omod/target/*.omod ./refapp/omods/
done
