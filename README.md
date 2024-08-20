# AlwaysReddy Add to Daily Note
This is an extension for the [AlwaysReddy Voice Assistant](https://github.com/ILikeAI/AlwaysReddy) that allows you to easily transcribe voice recordings to your note-taking system.
This code was created as part of this video: https://youtu.be/X0Bd20EDxfQ

### Automatically tag and summarize entries
This system is now capable of tagging and summarizing each entry. You can modify the prompt to customize how this works to suit your preferred summarization and tagging style.
The default instructions are just an example designed for you to overwrite:
```python   
self.user_instructions = """
AlwaysReddy is the name of one of my projects. If you see the words "always reddy" tag the note with "#alwaysReddy", only do this when the note explicitly mentions the project.
Only add bullet points if the note is longer than a few sentences.
Always use camel case for the tags."""
```

### How it works:
1. Press the hotkey to start recording ("ctrl+alt+f" by default)
2. Press it again to stop recording
3. Your voice recording will be transcribed and appended to the end of a note with today's date as the name in the directory you specify. Example file name: `08-18-24.md`

You can also add the content of your clipboard alongside your transcript. To do this, just double tap the hotkey when you start recording: "ctrl+alt+f+f"

### How to set it up:
1. Set up AlwaysReddy by following the steps [here](https://github.com/ILikeAI/AlwaysReddy?tab=readme-ov-file#setup).
2. Navigate to the actions directory in the AlwaysReddy code base: `cd actions`
3. Clone this repo into the actions directory: `git clone https://github.com/ILikeAI/alwaysreddy_add_to_daily_note`
4. Open the main.py file in `alwaysreddy_add_to_daily_note` and add the path to your daily notes folder into the `notes_directory` parameter, example: `self.notes_directory = Path(r"C:\Users\Josh\Documents\My Notes\Daily Notes")`

## Optional settings:
Use static note instead of daily note:
```python
self.use_daily_notes = False  # Set to False to use a fixed note
self.fixed_note_name = "fixed_note.md"  # Name of the fixed note if not using daily notes
```