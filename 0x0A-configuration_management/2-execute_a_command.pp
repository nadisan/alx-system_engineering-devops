# create a manifest that kills a process named killmenow.
exec{'killmenow':
command => 'pkill -f my_process.py',
onlyif  => 'pgrep -f my_process.py',
}
