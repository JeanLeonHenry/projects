import std/json
import std/strutils

# Declarations
const
    ERR = "Error fetching subs."
    NONE = "None live."
    BAD_ICON = "bell-slash"
    GOOD_ICON = "bell"

type
    Streamer = object
        user_name: string

# Read data and create output
var output: string
try:
    let data = readFile("~/.cache/wtwitch/subscription-cache.json")
    let jsonNode = parseJson(data)["data"]

    doAssert len(jsonNode) != 0
    var live: seq[string]
    for streamer in jsonNode:
        let curr_streamer = streamer.to(Streamer)
        live.add(curr_streamer.user_name)
    output = join(live, " ")
except AssertionDefect:
    output = ""
except:
    output = ERR

# JSON output creation
var json_output: JsonNode
if output != "": # ERR or normal
    let state = if output == ERR: "Critical" else: "Good"
    let icon = if output == ERR: BAD_ICON else: GOOD_ICON
    json_output = %*{"icon": icon, "text": output, "state": state}
else:
    json_output = %*{"text": NONE, "icon": BAD_ICON}
echo json_output
