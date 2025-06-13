gesture_command_map = {
    "0": "play",
    "1": "pause",
    "2": "volume_up",
    "3": "volume_down",
    "4": "mute",
    "5": "fullscreen",
    "6": "next_video",
    "7": "previous_video",
    "8": "exit",
    "9": "brightness_up",
    "10": "brightness_down",
    "11": "mode_toggle",
    "12": "progress_bar"
}

def gesture_to_command(gesture_id):
    return gesture_command_map.get(gesture_id, "unknown")
