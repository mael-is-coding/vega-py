# VEGA-PY

Vega is meant to be hopefully only the first of a suite of tools (CLI and UI) that make Arch and Linux
in general easier to use.
For now, i'm only trying to make it work for Arch based distros first, but i'm aware that the beauty of Linux is that it comes with so many different flavours, and i'd like my projects to reflect it as it goes on !

## Quick explanation
Vega will be a CLI tool that allows you to handle Arch Linux front tools in an easy, config based way.
The user describes what their taskbar, notif center, app launcher and Window Manager should look like, what backends to use, and Vega applies all that. Vega is also meant as a theme managing tool !

For now, Vega will be built around :
- sway-scroll (which is almost fully sway compatible, so w/ Vega it will behave like Sway)
- Waybar
- WOFI
- SwayNC
- Greetd and Regreet

So basically, the goal will be that if you're a user that just dropped into the barren Arch TTY, you can run vega to install everything for you and make it work on next connexion.
If you're already using those tools or if you've just configured them using Vega, you can also write several themes in TOML then switch between them using a command like `vega switch <theme>`

Right now it's in development, and there are many things to determine, that's why the idea isn't as precise as possible

## Why Python ?
I don't particularily like Python, but i know my way around it, and additionnally from being pretty relevant for developping CLI tools, its easy syntax allows to focus on the logics of the app.
I'm not proficient enough in C++ or Rust yet to create a whole project with it, so i prefer to map out the project logics first, to then re-do it in Rust or C++ if it ever amounts to something interesting to use.