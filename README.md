Take-A-Break
============
TakeABreak is an gnome indicator app that displays the number of minutes for which you have been working  and reminds you to take a break after every 1hr or so. Improve your productivity and keep your eyes healthy. 

### Installation

Currently the installation has to be done manually.Setup file will be added soon.
Follow these steps to run the Appindicator in your system.

```
git clone https://github.com/nishanthvijayan/Take-A-Break.git
cd Take-A-Break
sudo chmod +x breaktimeIndicator.py
nohup ./breaktimeIndicator.py &
```
If you want the indicator to run at startup , add an entry for the indicator at Startup Applications.
In the command field select the breaktimeIndicator.py file using Browse.

### Improvements

- Add pause/continue 
- Option to change alert, snooze, idle limit times 
- ~~Monitor idleness and adjust time accordingly~~

