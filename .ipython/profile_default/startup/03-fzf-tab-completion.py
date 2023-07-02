"""
Implement a custom completer that uses FZF to display and select completions.

Things to investigate:
    * Extending whatever class is used for the CLI options TerminalInteractiveShell.display_completions
    * Using the _ipython_display_() magic method to implement side-effect-based completion
    * Explicitly binding <Tab> (i.e., <C-I>) to call FZF with list of completions, as in the history widget above
    * event.current_buffer.{complete_state,complete_next,start_completion}
"""
from prompt_toolkit.completion import CompleteEvent, get_common_complete_suffix, Completion
from asyncio import Task
from prompt_toolkit.application.run_in_terminal import in_terminal

def display_completions_with_fzf(event):
    b = event.current_buffer
    if b.completer is None:
        return
    complete_event = CompleteEvent(completion_requested=True)
    completions = list(b.completer.get_completions(b.document, complete_event))
    if completions:
        _display_completions_with_fzf(event.app, completions)

def _display_completions_with_fzf(app, completions):
    async def run_fzf():
        async with in_terminal(render_cli_done=True):
            # Do FZF stuff
            pass
    return app.create_background_task(run_fzf)
