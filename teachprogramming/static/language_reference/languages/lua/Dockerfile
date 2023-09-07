FROM alpine

RUN apk add --no-cache \
    lua-dev

WORKDIR /lua/

COPY *.lua ./

CMD ["lua", "lua.lua"]
