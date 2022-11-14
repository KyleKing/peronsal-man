# VHS documentation
#
# Output:
#   Output <path>.gif               Create a GIF output at the given <path>
#   Output <path>.mp4               Create an MP4 output at the given <path>
#   Output <path>.webm              Create a WebM output at the given <path>
#
# Settings:
#   Set FontSize <number>           Set the font size of the terminal
#   Set FontFamily <string>         Set the font family of the terminal
#   Set Height <number>             Set the height of the terminal
#   Set Width <number>              Set the width of the terminal
#   Set LetterSpacing <float>       Set the font letter spacing (tracking)
#   Set LineHeight <float>          Set the font line height
#   Set Theme <string>              Set the theme of the terminal (JSON)
#   Set Padding <number>            Set the padding of the terminal
#   Set Framerate <number>          Set the framerate of the recording
#   Set PlaybackSpeed <float>       Set the playback speed of the recording
#
# Sleep:
#   Sleep <time>                    Sleep for a set amount of <time> in seconds
#
# Type:
#   Type[@<time>] "<characters>"    Type <characters> into the terminal with a
#                                   <time> delay between each character
#
# Keys:
#   Backspace[@<time>] [number]     Press the Backspace key
#   Down[@<time>] [number]          Press the Down key
#   Enter[@<time>] [number]         Press the Enter key
#   Space[@<time>] [number]         Press the Space key
#   Tab[@<time>] [number]           Press the Tab key
#   Left[@<time>] [number]          Press the Left Arrow key
#   Right[@<time>] [number]         Press the Right Arrow key
#   Up[@<time>] [number]            Press the Up Arrow key
#   Down[@<time>] [number]          Press the Down Arrow key
#   Ctrl+<key>                      Press the Control key + <key> (e.g. Ctrl+C)
#
# Display:
#   Hide                            Hide the subsequent commands from the output
#   Show                            Show the subsequent commands in the output

Output docs/demo.gif
Set PlaybackSpeed 0.25

Set Theme "SpaceGray Eighties"
Set FontFamily "Hack Nerd Font Mono"

Set FontSize 15
Set Width 1200
Set Height 800

Type "export PMAN_DOC_PATH=$PWD/.pman"  Sleep 500ms  Enter

Hide
Type "./tests/setup_test_dir.sh"  Enter
Show

Enter Type "pman"  Sleep 1s  Enter  Sleep 1s
Enter Type "pman --help"  Sleep 1s  Enter  Sleep 2s

Enter Type "pman show --help"  Sleep 1s  Enter  Sleep 1s
Enter Type "pman show"  Sleep 1s  Enter  Sleep 2s
Enter Type "pman show wezterm"  Sleep 1s  Enter  Sleep 5s
Enter Type "pman show i"  Sleep 1s  Enter  Sleep 500ms  Down@500ms 2  Sleep 500ms  Enter  Sleep 5s

Enter Type "pman search"  Sleep 1s  Enter  Sleep 1s
Enter Type "pman search --help"  Sleep 1s  Enter  Sleep 2s
Enter Type "pman search ine"   Sleep 1s  Enter  Sleep 5s  Enter

Sleep 5s

Hide
Type "rm -rf $PMAN_DOC_PATH"  Enter
Show
