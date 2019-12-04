---
layout: post
title: "New Windows Terminal"
categories: tech
---
[Windows Terminal](https://www.microsoft.com/en-us/p/windows-terminal-preview/9n0dx20hk701) is a new command line terminal app from Microsoft. Continuing their recent trend, it is also [open source](https://github.com/microsoft/terminal). It's got tabs, and supports WSL, CMD, and PowerShell. It's configurable, similar to how VSCode config is done. I needed to figure out a few simple config options.

Open the preferences.

### Default terminal
Change `"defaultProfile"` attribute to the guid of your preferred terminal.

### Adding a new profile
Each profile is identified by a unique guid (aka Global __Unique__ IDentifier). You can generate a new guid by running `New-Guid` in a PowerShell. Rest of the profile configs is described in the docs: [Adding profiles for third-party tools](https://github.com/microsoft/terminal/blob/master/doc/user-docs/ThirdPartyToolProfiles.md).

### Visual Studio Command Prompt
Commandlines with special characters and whitespace in paths need to be escaped with a `^` (caret). Here are my settings for a Visual Studio CMD prompt.
```json
{
    "guid": "{0e711e5a-26b4-4d54-8db3-6a8b6548a2a7}",
    "name": "Visual Studio CMD",
    "commandline": "cmd.exe /k \"C:\\Program^ Files^ ^(x86)\\Microsoft^ Visual^ Studio\\2017\\Professional\\VC\\Auxiliary\\Build\\vcvars64.bat\"",
    "fontFace": "Droid Sans Mono",
    "fontSize": 10,
    "colorScheme": "One Half Dark",
    "hidden": false
},
```

### Keybindings
I had to dig a bit to find the names for arrow keys. `right`, `left`, `up`, `down`.
```json
"keybindings": 
[
    { "command": "nextTab", "keys": ["alt+shift+right"]},
    { "command": "prevTab", "keys": ["alt+shift+left"]},
    { "command": "newTab", "keys": ["ctrl+shift+t"]}
]
```

### Additional links
[profiles.json docs](https://github.com/microsoft/terminal/blob/master/doc/cascadia/SettingsSchema.md)<br>
[Editing JSON settings](https://github.com/microsoft/terminal/blob/master/doc/user-docs/UsingJsonSettings.md)<br>

