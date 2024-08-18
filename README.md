Here's the updated README with the requested changes:

# AlwaysReddy Add to Daily Note
This is an extension for the [AlwaysReddy Voice Assistant](https://github.com/ILikeAI/AlwaysReddy), it allows you to easily transcribe voice recordings to note taking system.
This code was created as a part of this video: https://youtu.be/X0Bd20EDxfQ

### How it works:
1. Press the hotkey to start recording ("ctrl+alt+f" by default)
2. Press it again to stop recording
3. Your voice recording will be transcribed and appended to the end a note with todays date as the name in the directory you specify. Exmaple file name: `08-18-24.md`

You can also add the content of your clipboard alongside your transcript, to do this just double tap the hotkey when you start recording: "ctrl+alt+f+f"
### How to set it up:
1. Set up AlwaysReddy by following the steps [here](https://github.com/ILikeAI/AlwaysReddy?tab=readme-ov-file#setup).
2. Navigate to the actions directory in the AlwaysReddy code base `cd actions`
3. Clone this repo into the actions directory `git clone https://github.com/ILikeAI/alwaysreddy_add_to_daily_note`
4. Open the main.py file in `alwaysreddy_add_to_daily_note` and add the path to your daily notes folder into the `notes_directory` parameter, example: `self.notes_directory = Path(r"C:\Users\Josh\Documents\My Notes\Daily Notes")`
