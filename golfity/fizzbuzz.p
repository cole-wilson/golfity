
"
" ______ _         ____
"|  ____(_)       |  _ \
"| |__   _ _______| |_) |_   _ ________
"|  __| | |_  /_  /  _ <| | | |_  /_  /
"| |    | |/ / / /| |_) | |_| |/ / / /
"|_|    |_/___/___|____/ \__,_/___/___|
"
"
"This is the expanded version...

"a(100, I) {
"    $(
"        g([#I\1\2\4],
"            +(!(%I2), ?(%I3){
"                Z
"            }{
"                2
"            }
"        ))
"    )
"}
"
"...and this is the ugly version:
"
a100I$g[#I\1\2\4]+!%I2?%I3Z2