# https://stackoverflow.com/questions/46065777/is-it-possible-to-compile-a-single-c-sharp-code-file-with-the-net-core-roslyn-c
# These containers are a mess .. you have to use Google to find the containers on dockerhub.
# an absolute joke of a process
# https://softchris.github.io/pages/dotnet-dockerize.html#create-a-dockerignore-file


# https://medium.com/@jeroenverhaeghe/creating-smaller-and-more-secure-docker-images-for-net-core-8c74101e9027

# https://hub.docker.com/r/microsoft/dotnet-sdk
#  This says there is an alpine container, but I can't see how they are named
FROM mcr.microsoft.com/dotnet/sdk:9.0-alpine
#FROM mcr.microsoft.com/dotnet/sdk:8.0-alpine
#FROM mcr.microsoft.com/dotnet/sdk:latest
#FROM mcr.microsoft.com/dotnet/sdk
#FROM bitnami/dotnet:latest  ?

WORKDIR /csharp/

COPY . .
CMD dotnet run

#FROM mcr.microsoft.com/dotnet/sdk:2.0
#FROM mcr.microsoft.com/dotnet/core/sdk:2.0
# https://stackoverflow.com/a/47697996/3356840
#COPY HelloWorld.cs ./
#RUN dotnet \
#    /usr/share/dotnet/sdk/${DOTNET_SDK_VERSION}/Roslyn/csc.exe \
#        -r:/usr/share/dotnet/shared/Microsoft.NETCore.App/${ASPNET_VERSION}/System.Private.CoreLib.dll \
#        -r:/usr/share/dotnet/shared/Microsoft.NETCore.App/${ASPNET_VERSION}/System.Console.dll \
#        -r:/usr/share/dotnet/shared/Microsoft.NETCore.App/${ASPNET_VERSION}/System.Runtime.dll \
#    HelloWorld.cs
#CMD HelloWorld.exe

