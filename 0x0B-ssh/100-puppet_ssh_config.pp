# SSH config puppet
exec {'ssh_congig':
       path    => '/bin',
       command => 'echo "PasswordAuthentication no" >> /etc/ssh/ssh_config; echo "IdentifyFile ~/.ssh/school" >> /etc/ssh/ssh_config',
}