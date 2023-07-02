"""
Use FZF for tab completions
From https://github.com/prompt-toolkit/python-prompt-toolkit/issues/843
"""
from subprocess import check_output

from IPython import get_ipython
from prompt_toolkit.enums import DEFAULT_BUFFER
from prompt_toolkit.filters import HasFocus, ViInsertMode

ip = get_ipython()


def inline_fzf(event):
    try:
        file = check_output(
            "fzf -m --reverse --height 40% --preview 'bat --style=numbers --color=always --line-range :500 {}'",
            shell=True,
            text=True,
        ).strip()
        event.cli.current_buffer.text += file
        event.cli.current_buffer.cursor_position = len(event.cli.current_buffer.text)
    except Exception:
        pass
    event.cli.reset()


if hasattr(ip, "pt_app"):
    registry = ip.pt_app.key_bindings

    # Inline FZF with ctrl+space
    registry.add_binding("c-@", filter=(HasFocus(DEFAULT_BUFFER) & ViInsertMode()))(
        inline_fzf
    )
