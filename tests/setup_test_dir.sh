#!/bin/bash -e

mkdir -p $PMAN_DOC_PATH/containers
mkdir -p $PMAN_DOC_PATH/python
touch $PMAN_DOC_PATH/containers/colima.md
touch $PMAN_DOC_PATH/containers/kubectl.md
touch $PMAN_DOC_PATH/containers/podman.md
touch $PMAN_DOC_PATH/exa.md
touch $PMAN_DOC_PATH/gh.md
touch $PMAN_DOC_PATH/navi.md
touch $PMAN_DOC_PATH/neovim.md
touch $PMAN_DOC_PATH/python/fastapi.md
touch $PMAN_DOC_PATH/python/python.md
touch $PMAN_DOC_PATH/ripgrep.md
touch $PMAN_DOC_PATH/rust.md
touch $PMAN_DOC_PATH/sql.md
touch $PMAN_DOC_PATH/sublime.md
touch $PMAN_DOC_PATH/wezterm.md

echo -e '# Neovim\n- `<>` indicates that the inner keys need to be typed. `C-` is `ctrl` and `M-` is for meta (`cmd`).\n- `<:wq>` is save and quit vs. `<:q!>` quit and discard changes. Press `<ENTER>` to apply\n- `<ESC>` normal mode\n- Clicking does move the cursor in WezTerm\n- Individual Keys (only works in normal mode)\n    - `h (left) j (down has `_`) k (up) l (right)\n    - `i` insert\n    - `A` append\n    - `r` replace\n    - `c` change (when followed by count/motion, will delete and then begin `insert` mode)\n    - `x` delete char under cursor\n    - `u` undo and `U` undo all changes on the same line\n    - `<C-r>` (`Ctrl r`) to redo\n    - `p` put (paste) after/below cursor or `P` before/above cursor\n    - `<C-g>` display cursor position\n    - `G` to go end of file and `gg` to go to top or `#G` for go to line\n- `operator`: leader character\n    - `d`: delete\n- `count`: repeats the prior (or subsequent) `operator` and/or `motion`\n' > $PMAN_DOC_PATH/neovim.md

echo -e '# Wezterm\n\n## Keyboard Copy Mode\n\n[Copy Mode - Wez Terminal Emulator](https://wezfurlong.org/wezterm/copymode.html)\n\n- `<C-Shift-x>`: activate\n- `<C-Shift-c>`: copy\n- `<ESC>`: exit\n- `<v>` cell mode and `<V>` full line\n    - `<o>` start/end of selection\n    - `<C-v>` rectangular mode (select width and height!)\n- `<0>` start and `<$>` end of line\n- `<tab>` one word or `<alt-tab>`\n- `<g>` start of scroll back and `<G>` end\n- `<C-b>` move up one screen and `<C-f>` down\n' > $PMAN_DOC_PATH/wezterm.md
