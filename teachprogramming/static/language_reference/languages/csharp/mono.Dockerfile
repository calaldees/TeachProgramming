FROM mono
WORKDIR /csharp
COPY *.cs ./
CMD mcs csharp.cs && mono csharp.exe
# docker build --tag csharp . && docker run --rm -it csharp