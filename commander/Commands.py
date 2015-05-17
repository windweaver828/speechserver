#!/usr/bin/env python

# Examples to help under the if name == main clause down below

import subprocess
from CommandsDict import CommandsDict

# ------------------------------------------------------- #
# Add functions to call here                              #


def shellcommand(command):
    subprocess.Popen(command, shell=True)


def open_url(url):
    import webbrowser
    browser = webbrowser.get()
    browser.open_new_tab(url)

commands = CommandsDict()
# ------------------------------------------------------- #
# Add command definitions here                            #

commdef = [['left'], ['click']]
func = shellcommand
args = ['xdotool click 1']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['right'], ['click']]
func = shellcommand
args = ['xdotool click 3']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['double'], ['click']]
func = shellcommand
args = ['xdotool click 1 click 1']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['cancel']]
func = shellcommand
args = ['xdotool key Escape']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['mouse'], ['grid']]
func = shellcommand
args = ['$HOME/bin/mousegrid']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['open', 'show', 'start'],
           ['terminal', 'console', 'shell']]
func = shellcommand
args = ['gnome-terminal --working-directory=$HOME --display=:0']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['press'], ['one']]
func = shellcommand
args = ['xdotool key 1']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['press'], ['two']]
func = shellcommand
args = ['xdotool key 2']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['press'], ['three']]
func = shellcommand
args = ['xdotool key 3']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['press'], ['four']]
func = shellcommand
args = ['xdotool key 4']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['press'], ['five']]
func = shellcommand
args = ['xdotool key 5']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['press'], ['six']]
func = shellcommand
args = ['xdotool key 6']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['press'], ['seven']]
func = shellcommand
args = ['xdotool key 7']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['press'], ['eight']]
func = shellcommand
args = ['xdotool key 8']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['press'], ['nine']]
func = shellcommand
args = ['xdotool key 9']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['show', 'vnc'], ['ryann']]
func = shellcommand
args = ['$HOME/bin/vncryann']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['show', 'vnc'], ['jayme']]
func = shellcommand
args = ['$HOME/bin/vncjayme']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['new', 'create'], ['folder', 'directory']]
func = shellcommand
args = ['xdotool key ctrl+shift+n']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['save']]
func = shellcommand
args = ['xdotool key ctrl+s']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['send', 'move'], ['right'], ['monitor', 'screen']]
func = shellcommand
args = ['xdotool key ctrl+shift+Right']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['send', 'move'], ['left'], ['monitor', 'screen']]
func = shellcommand
args = ['xdotool key ctrl+shift+Left']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['press', 'go'], ['up']]
func = shellcommand
args = ['xdotool key Up']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['press', 'go'], ['down']]
func = shellcommand
args = ['xdotool key Down']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['press', 'go'], ['right']]
func = shellcommand
args = ['xdotool key Right']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['press', 'go'], ['left']]
func = shellcommand
args = ['xdotool key Left']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['close', 'kill'], ['window']]
func = shellcommand
args = ['xdotool getactivewindow windowkill']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['open', 'show'], ['recycle', 'trash']]
func = shellcommand
args = ['nemo trash:///']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['empty'], ['trash']]
func = shellcommand
args = ['trash-empty']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['my', 'show', 'open'], ['document', 'documents']]
func = shellcommand
args = ['nemo $HOME/Documents/']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['my', 'open', 'show'], ['download', 'downloads']]
func = shellcommand
args = ['nemo $HOME/Downloads/']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['show', 'open'], ['movie', 'movies'], ['folder', 'directory']]
func = shellcommand
args = ['nemo /media/External-4.0/Media/Movies']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['show', 'open'], ['kid', 'kids'], ['folder', 'directory']]
func = shellcommand
args = ['nemo /media/External-4.0/Media/Lyndas']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['open', 'show'], ['tv', 't v'], ['folder', 'directory']]
func = shellcommand
args = ['nemo /media/External-4.0/Media/TV']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['open', 'show'], ['project', 'projects']]
func = shellcommand
args = ['nemo $HOME/Projects/']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['scroll'], ['up', 'left']]
func = shellcommand
args = ['xdotool click --repeat 5 4']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['scroll'], ['down', 'right']]
func = shellcommand
args = ['xdotool click --repeat 5 5']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['switch', 'swap', 'change'], ['window', 'application']]
func = shellcommand
args = ['xdotool key alt+Tab']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['cut']]
func = shellcommand
args = ['xdotool key ctrl+x']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['copy']]
func = shellcommand
args = ['xdotool key ctrl+c']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['paste']]
func = shellcommand
args = ['xdotool key ctrl+v']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['undo']]
func = shellcommand
args = ['xdotool key ctrl+z']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['rename'], ['change', 'name']]
func = shellcommand
args = ['xdotool key F2']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['select'], ['all']]
func = shellcommand
args = ['xdotool key ctrl+a']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['help', 'menu']]
func = shellcommand
args = ['xdotool key F1']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['minimize'], ['all']]
func = shellcommand
args = ['xdotool key Super+d']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['minimize'], ['window']]
func = shellcommand
args = ['xdotool getactivewindow windowminimize']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['maximize'], ['window']]
func = shellcommand
args = ['xdotool key Super+Up Super+Up']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['show', 'all']]
func = shellcommand
args = ['xdotool key ctrl+alt+Up']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['browse', 'open'], ['netflix']]
func = shellcommand
args = ['google-chrome http://www.netflix.com']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['browse', 'open'], ['facebook']]
func = open_url
args = ['http://www.facebook.com']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['browse', 'open'], ['school', 'college']]
func = open_url
args = ['http://www.mgccc.edu']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['browse', 'open'], ['ice'], ['films']]
func = open_url
args = ['http://www.icefilms.info']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['close'], ['tab']]
func = shellcommand
args = ['xdotool key ctrl+w']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['press'], ['delete']]
func = shellcommand
args = ['xdotool key Delete']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['press'], ['enter']]
func = shellcommand
args = ['xdotool key Return']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['show', 'list'], ['commands']]
func = shellcommand
args = ['$HOME/bin/commandslist']
commfunc = [func, args]
commands[commdef] = commfunc
