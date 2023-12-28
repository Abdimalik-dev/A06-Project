import json
import re
import requests
import sys
import webbrowser

from urllib.parse import quote

OPEN_IN_BROWSER = True


def custom_block(block):
    """Formatting for a custom My Block"""
    proccode = block["mutation"]["proccode"].replace("%s", "{}").replace("%b", "{}")
    placeholders = re.findall("%[sb]", block["mutation"]["proccode"])
    inputs = json.loads(block["mutation"]["argumentids"])
    for i, input_id in enumerate(inputs):
        if input_id not in block["inputs"]:
            block["inputs"][input_id] = [1, [10, ""]] if placeholders[i] == "%s" else [1, ["BOOL", ""]]
    return proccode, inputs


FIELDS = {
    "_mouse_": "mouse-pointer",
    "_random_": "random position",
    "PAN": "pan left/right",
}

BLOCKS = {

    # Motion
    "motion_movesteps": ("move {} steps", ["STEPS"]),
    "motion_turnright": ("turn right {} degrees", ["DEGREES"]),
    "motion_turnleft": ("turn left {} degrees", ["DEGREES"]),
    "motion_goto": ("go to {}", ["TO"]),
    "motion_gotoxy": ("go to x: {} y: {}", ["X", "Y"]),
    "motion_glideto": ("glide {} secs to {}", ["SECS", "TO"]),
    "motion_glidesecstoxy": ("glide {} secs to x: {} y: {}", ["SECS", "X", "Y"]),
    "motion_pointindirection": ("point in direction {}", ["DIRECTION"]),
    "motion_pointtowards": ("point towards {}", ["TOWARDS"]),
    "motion_changexby": ("change x by {}", ["DX"]),
    "motion_setx": ("set x to {}", ["X"]),
    "motion_changeyby": ("change y by {}", ["DY"]),
    "motion_sety": ("set y to {}", ["Y"]),
    "motion_ifonedgebounce": ("if on edge, bounce", []),
    "motion_setrotationstyle": ("set rotation style [{} v]", [["STYLE", {}]]),

    # Looks
    "looks_sayforsecs": ("say {} for {} seconds", ["MESSAGE", "SECS"]),
    "looks_say": ("say {}", ["MESSAGE"]),
    "looks_thinkforsecs": ("think {} for {} seconds", ["MESSAGE", "SECS"]),
    "looks_think": ("think {}", ["MESSAGE"]),
    "looks_switchcostumeto": ("switch costume to {}", ["COSTUME"]),
    "looks_nextcostume": ("next costume", []),
    "looks_switchbackdropto": ("switch backdrop to {}", ["BACKDROP"]),
    "looks_nextbackdrop": ("next backdrop", []),
    "looks_changesizeby": ("change size by {}", ["CHANGE"]),
    "looks_setsizeto": ("set size to {} %", ["SIZE"]),
    "looks_changeeffectby": ("change [{} v] effect by {}", [["EFFECT", {}], "CHANGE"]),
    "looks_seteffectto": ("set [{} v] effect to {}", [["EFFECT", {}], "VALUE"]),
    "looks_cleargraphiceffects": ("clear graphic effects", []),
    "looks_show": ("show", []),
    "looks_hide": ("hide", []),
    "looks_gotofrontback": ("go to [{} v] layer", [["FRONT_BACK", {}]]),
    "looks_goforwardbackwardlayers": ("go [{} v] {} layers", [["FORWARD_BACKWARD", {}], "NUM"]),

    # Sound
    "sound_playuntildone": ("play sound {} until done", ["SOUND_MENU"]),
    "sound_play": ("start sound {}", ["SOUND_MENU"]),
    "sound_stopallsounds": ("stop all sounds", []),
    "sound_changeeffectby": ("change [{} v] effect by {}", [["EFFECT", FIELDS], "VALUE"]),
    "sound_seteffectto": ("set [{} v] effect to {}", [["EFFECT", FIELDS], "VALUE"]),
    "sound_cleareffects": ("clear sound effects", []),
    "sound_changevolumeby": ("change volume by {}", ["VOLUME"]),
    "sound_setvolumeto": ("set volume to {} %", ["VOLUME"]),

    # Events
    "event_whenflagclicked": ("when flag clicked", []),
    "event_whenkeypressed": ("when [{} v] key pressed", [["KEY_OPTION", {}]]),
    "event_whenthisspriteclicked": ("when this sprite clicked", []),
    "event_whenbackdropswitchesto": ("when backdrop switches to [{} v]", [["BACKDROP", {}]]),
    "event_whengreaterthan": ("when [{} v] > {}", [["WHENGREATERTHANMENU", FIELDS], "VALUE"]),
    "event_whenbroadcastreceived": ("when I receive [{} v]", [["BROADCAST_OPTION", {}]]),
    "event_whenstageclicked": ("when stage clicked", []),

    # check these two
    "event_broadcast": ("broadcast {}", ["BROADCAST_INPUT"]),
    "event_broadcastandwait": ("broadcast {} and wait", ["BROADCAST_INPUT"]),

    # Control
    "control_wait": ("wait {} seconds", ["DURATION"]),
    "control_repeat": ("repeat {}", ["TIMES"]),
    "control_if": ("if {} then", ["CONDITION"]),
    "control_if_else": ("if {} then", ["CONDITION"]),
    "control_forever": ("forever", []),
    "control_repeat_until": ("repeat until {}", ["CONDITION"]),
    "control_stop": ("stop [{} v]", [["STOP_OPTION", {}]]),
    "control_start_as_clone": ("when I start as a clone", []),
    "control_create_clone_of": ("create clone of {}", ["CLONE_OPTION"]),
    "control_delete_this_clone": ("delete this clone", []),
    "control_wait_until": ("wait until {}", ["CONDITION"]),


