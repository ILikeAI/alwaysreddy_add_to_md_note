from utils import to_clipboard
from actions.base_action import BaseAction
from config_loader import config
from pathlib import Path
from datetime import datetime

class AddToMarkDownNote(BaseAction):
    def setup(self):
        self.AR.add_action_hotkey("ctrl+alt+f", 
                            pressed=self.transcribe_to_note,
                            held_release=self.transcribe_to_note,
                            double_tap=self.AR.save_clipboard_text)
        
        # Configuration options
        self.notes_directory = Path(r"")
        self.use_daily_notes = True  # Set to False to use a fixed note
        self.fixed_note_name = "fixed_note.md"  # Name of the fixed note if not using daily notes
        self.daily_note_format = "%m-%d-%y"  # Format for daily note filenames

        # Uncomment and modify these lines to use different date formats
        # self.daily_note_format = "%Y-%m-%d"
        # self.daily_note_format = "%d-%m-%Y"
        # self.daily_note_format = "%B %d, %Y"

        self.use_add_tags_or_bullet_points = True
        self.user_instructions = """
        I sometimes take notes about AlwaysReddy, but the transcription system processes it as "always ready", if seem me say about "always ready" make sure to tag it as "AlwaysReddy".
        Use tags like: "#idea", "#thought"
        Only add bullet points if the note is longer than a few sentences.
        Always use camel case for the tags.
        """
        
        # Load the system prompt and inject user instructions
        system_prompt_path = Path(__file__).parent / "system_prompt.txt"
        self.system_prompt = system_prompt_path.read_text()
        self.system_prompt = self.system_prompt.replace("{USER_INSTRUCTIONS}", self.user_instructions)

    def transcribe_to_note(self):
        """Handle the transcription process."""
        recording_filename = self.AR.toggle_recording(self.transcribe_to_note)
        if recording_filename:
            text = self.AR.transcription_manager.transcribe_audio(recording_filename)
            
            if text:
                print("Transcription:\n", text)

                if self.AR.clipboard_text:
                    text = f"""**This text copied in the clipboard at the time:**\n```\n{self.AR.clipboard_text}\n```\n\n**NOTE:**\n{text}"""
                    self.AR.clipboard_text = None
                
                if self.use_add_tags_or_bullet_points:
                    text = self.add_tags_or_bullet_points(text)
                self.append_to_note(text)

    def add_tags_or_bullet_points(self, text):
        """Add tags or bullet points to the text."""
        messages = [{"role": "system", "content": self.system_prompt},{"role": "user", "content": f"HERE IS MY NOTE:\n{text}"}]

        completion = self.AR.completion_client.get_completion(messages, model=config.COMPLETION_MODEL)


        if completion:
            if completion.startswith("NA"):
                return text
            return text + "\n" + completion
        else:
            print("Failed to get completion for tags or bullet points.")
            return text

    def append_to_note(self, text):
        """Append the transcribed text to the appropriate note file."""
        if self.use_daily_notes:
            filename = datetime.now().strftime(f"{self.daily_note_format}.md")
        else:
            filename = self.fixed_note_name

        filepath = self.notes_directory / filename

        timestamp = datetime.now().strftime("%I:%M %p")
        formatted_text = f"{timestamp}\n{text}\n\n---\n"

        if filepath.exists():
            # Append to existing file
            filepath.open("a", encoding="utf-8").write(formatted_text)
        else:
            # Create new file with header
            with filepath.open("w", encoding="utf-8") as file:
                if self.use_daily_notes:
                    file.write(f"# Notes for {datetime.now().strftime(self.daily_note_format)}\n")
                else:
                    file.write(f"# {self.fixed_note_name[:-3]} Notes\n")
                file.write(formatted_text)