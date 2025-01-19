function u(s)
    local r = 0

    for i = #s, 1, -1 do
        r = r * 256
        r = r + string.byte(string.sub(s, i, i))
    end

    return r
end

function sw(t, a, b)
    local x = t[a]
    t[a] = t[b]
    t[b] = x
end

function s(k)
    local r = {}

    for i = 0, 255 do
        r[i] = i
    end

    local j = 0
    local idx = 0

    for i = 0, 255 do
        idx = (i % #k) + 1
        j = (j + r[i] + k:sub(idx, idx):byte()) % 256
        sw(r, i, j)
    end

    return r
end

function e(p, k)
    local i = 0
    local j = 0
    local r = ""

    for l = 1, 3072 do
        i = (i + 1) % 256
        j = (j + k[i]) % 256
        sw(k, i, j)
        t = (k[i] + k[j]) % 256
    end

    for l = 1, #p do
        i = (i + 1) % 256
        j = (j + k[i]) % 256
        sw(k, i, j)
        t = (k[i] + k[j]) % 256
        r = r .. string.char(p:sub(l, l):byte() ~ k[t])
    end

    return r
end

local f = assert(io.open("moon.bmp", "r"))
local d = f:read("*all")
f:close()

local t = os.time()
math.randomseed(t)

local o = u(string.sub(d, 11, 14)) + 1
local p = string.sub(d, o, #d)

for i = 1, 1000000000000000 do
    math.random()
end

local ks = s(tostring(math.random(0, 2^32 - 1)))
local ct = e(p, ks)

f = assert(io.open("chall.bmp", "w"))
f:write(string.sub(d, 0, o - 1) .. ct .. os.date("!%d %h %Y, %H:%M", t))
f:close()
