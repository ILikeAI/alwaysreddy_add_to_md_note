from utils import to_clipboard
from actions.base_action import BaseAction
from config_loader import config
from pathlib import Path
from datetime import datetime

class AddToDailyNote(BaseAction):
    def setup(self):
        self.AR.add_action_hotkey("ctrl+alt+f", 
                            pressed=self.transcribe_to_note,
                            held_release=self.transcribe_to_note,
                            double_tap=self.AR.save_clipboard_text)
        self.notes_directory = Path(r"")#Path to the directory where the notes are stored

    def transcribe_to_note(self):
        """Handle the transcription process."""
        recording_filename = self.AR.toggle_recording(self.transcribe_to_note)
        if recording_filename:  # If the recording has only just been started, recording_filename will be None
            transcript = self.AR.transcription_manager.transcribe_audio(recording_filename)

            if self.AR.clipboard_text:
                transcript = f"""**This text copied in the clipboard at the time:**\n```\n{self.AR.clipboard_text}\n```\n\n**NOTE:**\n{transcript}"""
                self.AR.clipboard_text = None

            if transcript:
                print("Transcription:\n", transcript)
                self.append_to_note(transcript, self.notes_directory)

    def append_to_note(self, text, notes_directory):
        """Append the transcribed text to today's note file."""
        today = datetime.now().strftime("%m-%d-%y")
        filename = f"{today}.md"
        filepath = notes_directory / filename

        timestamp = datetime.now().strftime("%I:%M %p")
        formatted_text = f"{timestamp}\n{text}\n\n---\n"

        if filepath.exists():
            # Append to existing file
            with filepath.open("a", encoding="utf-8") as file:
                file.write(formatted_text)
        else:
            # Create new file with header
            with filepath.open("w", encoding="utf-8") as file:
                file.write(f"# Notes for {today}\n")
                file.write(formatted_text)