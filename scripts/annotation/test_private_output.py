"""Cygwin Git must receive portable relative paths from Windows Python."""
from pathlib import Path, PureWindowsPath
import subprocess
import tempfile
import unittest
from scripts.annotation.private_output import git_probe_argument, require_ignored_output

class PrivateOutputTests(unittest.TestCase):
    def test_windows_drive_is_not_sent_to_git(self):
        root=PureWindowsPath('C:/cygwin64/home/github/let_me_count_the_ways')
        for prefix in ['results/review_private','results/annotation_private']:
            self.assertEqual(prefix+'/new-run/privacy-check.json',
                             git_probe_argument(root/prefix/'new-run',root))
    def test_outside_repository_rejected(self):
        with self.assertRaises(ValueError):
            git_probe_argument(PureWindowsPath('D:/outside'),PureWindowsPath('C:/repo'))
    def test_real_git_checks_missing_ignored_directories_and_rejects_public_outputs(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td)
            subprocess.run(['git','init','-q'],cwd=root,check=True)
            (root/'.gitignore').write_text('/results/review_private/\n/results/annotation_private/\n')
            for prefix in ['results/review_private','results/annotation_private']:
                directory=root/prefix/'not-created-yet'
                self.assertFalse(directory.exists())
                require_ignored_output(directory,root)
            with self.assertRaisesRegex(ValueError,'not Git-ignored'):
                require_ignored_output(root/'results/public',root)
    def test_git_failure_is_not_misreported_as_missing_ignore_rule(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td)
            with self.assertRaisesRegex(ValueError,'Git could not verify'):
                require_ignored_output(root/'output',root)

if __name__=='__main__':unittest.main()
