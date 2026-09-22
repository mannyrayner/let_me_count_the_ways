"""Verify private output paths without passing native absolute paths to Git."""
from pathlib import Path
import subprocess


def git_probe_argument(output, root):
    """Inputs are resolved paths; the returned Git argument is repository-relative."""
    try:
        return (output / 'privacy-check.json').relative_to(root).as_posix()
    except ValueError as exc:
        raise ValueError('Private output must be inside the repository') from exc


def require_ignored_output(output, root):
    root = Path(root).resolve()
    probe = git_probe_argument(Path(output).resolve(), root)
    result = subprocess.run(['git', 'check-ignore', '-q', '--', probe],
                            cwd=root, capture_output=True, text=True)
    if result.returncode == 1:
        raise ValueError('Private output is not Git-ignored: ' + probe)
    if result.returncode != 0:
        raise ValueError('Git could not verify private output: ' + result.stderr.strip())
