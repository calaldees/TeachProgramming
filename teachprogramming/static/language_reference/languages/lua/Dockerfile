FROM alpine

RUN apk add --no-cache \
    lua

WORKDIR /lua/

COPY *.lua ./

CMD ["lua", "lua.lua"]
