```
choco install dotnet-sdk
dotnet tool install --global Microsoft.dotnet-interactive
dotnet interactive jupyter install
```
https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.vscode-dotnet-pack

TODO - gitpod .net interactive c#


PATH=$PATH:~/.dotnet/tools


eval $(gp env -e PATH=$PATH:~/.dotnet/tools)

/home/gitpod/.local/share/jupyter/kernels/.net-csharp/kernel.json


https://github.com/dotnet/dotnet-docker/issues/520



Installing C# dependencies...
Platform: linux, x86_64, name=ubuntu, version=20.04

Downloading package 'OmniSharp for Linux (.NET 6 / x64)' (40810 KB).................... Done!
Validating download...
Integrity Check succeeded.
Installing package 'OmniSharp for Linux (.NET 6 / x64)'

Downloading package '.NET Core Debugger (linux / x64)' (3479 KB).................... Done!
Installing package '.NET Core Debugger (linux / x64)'

Downloading package 'Razor Language Server (Linux / x64)' (61682 KB).................... Done!
Installing package 'Razor Language Server (Linux / x64)'

Finished



tasks:  
  # "Python init prebuild not working #7078" - https://github.com/gitpod-io/gitpod/issues/7078
  - name: dotnet
# https://docs.microsoft.com/en-us/dotnet/core/install/linux-ubuntu#2004
# "Be able to set PATH environment variable for all shell (terminal) windows in VSCode from .gitpod.yml #9275" - https://github.com/gitpod-io/gitpod/issues/9275#issuecomment-1098275529
# "Ensure global tools dir is on the PATH #520" - https://github.com/dotnet/dotnet-docker/issues/520

    before: |
      printf 'export PATH="$PATH:%s"\n' "/home/gitpod/.dotnet/tools" >> $HOME/.bashrc
    init: |
      PATH=$PATH:~/.dotnet/tools

      wget https://packages.microsoft.com/config/ubuntu/20.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
      sudo dpkg -i packages-microsoft-prod.deb
      rm packages-microsoft-prod.deb
      sudo apt-get update
      sudo apt-get install -y apt-transport-https
      sudo apt-get update
      sudo apt-get install -y dotnet-sdk-6.0

      dotnet tool install --global Microsoft.dotnet-interactive
      dotnet interactive jupyter install

#gp sync-done dotnet
#command: 
#- name: dotnet-interactive
#  init: |
#    gp sync-await dotnet
#    dotnet tool install --global Microsoft.dotnet-interactive
#    dotnet interactive jupyter install



vsix:release:package:platform-specific


https://serverfault.com/a/589528
sudo apt install libarchive-tools   # for bsdtar

VVV=".NET Core Debugger (linux / x64)" cat ../package.json | jq --arg kt "$VVV" -r '.runtimeDependencies[] | select(.description==$kt) | .url'

DESCRIPTION=".NET Core Debugger (linux / x64)" && \
wget -qO- \
$( \
    cat ../package.json \
    | \
    jq -r --arg DESCRIPTION "$DESCRIPTION" \
        '.runtimeDependencies[] | select(.description==$DESCRIPTION) | .url, .installPath ' \
) \
| \
bsdtar -xvf-


https://www.codeproject.com/Tips/1209935/VS-Code-NET-Core-Offline-Installation-of-Extension

