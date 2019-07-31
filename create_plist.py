import plistlib

from shortcuts import shortcuts

full_shortcuts = [{'phrase': v, 'shortcut': '\\' + k} for k, v in shortcuts.items()]
full_shortcuts += [{'phrase': v, 'shortcut': 'v' + k} for k, v in shortcuts.items()]
with open('Text Substitutions.plist', 'wb') as f:
    f.write(plistlib.dumps(full_shortcuts, sort_keys=False))
