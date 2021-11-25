TODO

https://docs.microsoft.com/en-us/dotnet/core/docker/introduction
https://hub.docker.com/_/microsoft-dotnet-sdk/
    docker pull mcr.microsoft.com/dotnet/sdk:5.0


JSON in .NET Core
https://stackoverflow.com/a/67910524/3356840

.NET Fiddle

https://dotnetfiddle.net/mo1qvw


apt-cache search mono

```bash
sudo apt instal mono-vbnc mono-mcs
# add to `.bash_profile` or `.bashrc`
function csharp { mcs "$1" && clear && mono "${1%.*}.exe" && rm "${1%.*}.exe"; }
function vb { vbnc "$1" && clear && mono "${1%.*}.exe" && rm "${1%.*}.exe"; }
# use
csharp myfile.cs
```

https://linuxize.com/post/how-to-install-mono-on-ubuntu-20-04/
Difference between `csc` and `msc`?

What about
https://docs.microsoft.com/en-us/dotnet/core/install/linux
`sudo apt-get install dotnet-sdk-6.0`
