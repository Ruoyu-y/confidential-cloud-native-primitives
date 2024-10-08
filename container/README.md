# Docker Image Builder

There are several docker image files in the sub directories of current directory. Each sub directory contains Dockerfile of an image. Please find description of each image as follows.

|  Sub directory | Image name  | Description  | 
|---|---|---|
|  cima-webhook | cima-webhook | CIMA webhook |
|  cima-server | cima-server | CIMA server |
|  cima-example | cima-example  | Example image of getting eventlog and measurement using CIMA SDK |
|  pccs | pccs  | PCCS docker image for Intel® TDX remote attestation. Not required for CIMA usage.|
|  qgs | qgs  | QGS docker image for Intel® TDX remote attestation. Not required for CIMA usage. |


### Build Docker images

`build.sh` is a tool to build all above images and push them to a user-specified image registry. It supports below parameters for different use scenarios.

|  Parameter | Description  | Options  | Default Value  | Required\|Optional  |
|---|---|---|---|---|
|  -a | Action the script will execute: `all` means build and publish images; `build` means build images only; `publish` means publish images; `save` means docker save images to local file.  | build\|publish\|save\|all  | all  | Optional  |
|  -r |  Image registry. Images will be pushed to this image registry. |   |   | Required  |
|  -c | Image name to build. Image names will be the same as sub directory names under directory `container`. By default it will be `all` meaning build all images under `container` | Sub directory name under directory `container`.  |  all |  Optional |
|  -g | Image tag  |   |  latest |  Optional |
|  -f | Flag to build images with parameter "--no-cache"  |   |  |  Optional |
|  -p | Flag to build pccs docker image. Building pccs docker image requires interactive configuration. Please refer to [README.md](../container/pccs/README.md).  |   |   |  Optional |
|  -q | Flag to build qgs docker image. Please refer to [README.md](../container/qgs/README.md).  |  |   |  Optional |
|  -h | Show this usage guide.  |  |   |  Optional |

_NOTE: The script need to run on a server with docker installed._

_NOTE: please set `HTTP_PROXY`, `HTTPS_PROXY`, `NO_PROXY` in docker daemon if they are needed. Please refer to [Configure the Docker daemon to use a proxy server](https://docs.docker.com/config/daemon/systemd/#httphttps-proxy)._

Below are usage examples for different scenarios. Please replace the parameters with your input.

```
# Build all CIMA images with tag latest and push them to remote registry test-registry.intel.com
$ sudo ./build.sh -r test-registry.intel.com/test -g latest

# Build images only with tag latest
$ sudo ./build.sh -a build -g latest

# Build cima-measurement-server image with tag latest and push them to remote registry test-registry.intel.com
$ sudo ./build.sh -c cima-measurement-server -r test-registry.intel.com/test -g latest

# Build pccs image with tag latest and push it to remote registry test-registry.intel.com
$ sudo ./build.sh -c pccs -r test-registry.intel.com/test -g latest -p

# Build qgs image with tag latest and push it to remote registry test-registry.intel.com
$ sudo ./build.sh -c qgs -r test-registry.intel.com/test -g latest -q
```

Note: For detailed PCCS and QGS service usage guide, please refer [PCCS Guide](pccs/README.md) and [QGS Guide](qgs/README.md).

After the script is running successfully, it's supposed to see corresponding CIMA docker images.

```
$ sudo docker images
cima-example                    <your image tag>
cima-server                     <your image tag>
cima-webhook                    <your image tag>
```
