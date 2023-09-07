# https://stackoverflow.com/questions/46065777/is-it-possible-to-compile-a-single-c-sharp-code-file-with-the-net-core-roslyn-c
# These containers are a mess .. you have to use Google to find the containers on dockerhub.
# an absolute joke of a process
# https://softchris.github.io/pages/dotnet-dockerize.html#create-a-dockerignore-file

FROM mcr.microsoft.com/dotnet/sdk

WORKDIR /app/

COPY * ./
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

