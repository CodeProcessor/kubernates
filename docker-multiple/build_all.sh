VERSION=v1.1

docker build -t cubecai/kube:servicelatest -f service/Dockerfile service
docker tag cubecai/kube:servicelatest cubecai/kube:caiservice${VERSION}
docker push cubecai/kube:caiservice${VERSION}
echo "Pushed cubecai/kube:caiservice${VERSION}"

docker build -t cubecai/kube:enginelatest -f engine/Dockerfile engine
docker tag cubecai/kube:enginelatest cubecai/kube:caiengine${VERSION}
docker push cubecai/kube:caiengine${VERSION}
echo "Pushed cubecai/kube:caiengine${VERSION}"