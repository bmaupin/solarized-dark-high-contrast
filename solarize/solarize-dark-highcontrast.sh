#!/bin/sh
#
# Shell script for setting Gnome Terminal to Solarized dark high contrast theme
# (http://ethanschoonover.com/solarized)

gconftool-2 --set "/apps/gnome-terminal/profiles/Default/use_theme_background" --type bool false
gconftool-2 --set "/apps/gnome-terminal/profiles/Default/use_theme_colors" --type bool false
gconftool-2 --set "/apps/gnome-terminal/profiles/Default/palette" --type string "#070736364242:#D3D301010202:#858599990000:#B5B589890000:#26268B8BD2D2:#D3D336368282:#2A2AA1A19898:#FDFDF6F6E3E3:#00002B2B3636:#CBCB4B4B1616:#65657B7B8383:#838394949696:#9393A1A1A1A1:#6C6C7171C4C4:#EEEEE8E8D5D5:#FDFDF6F6E3E3"
gconftool-2 --set "/apps/gnome-terminal/profiles/Default/background_color" --type string "#00002B2B3636"
gconftool-2 --set "/apps/gnome-terminal/profiles/Default/foreground_color" --type string "#9393A1A1A1A1"
