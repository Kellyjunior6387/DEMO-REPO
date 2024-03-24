file { '/home/your_username/.ssh/config':
content => "\
Host ubuntu@54.144.151.196
  IdentityFile ~/.ssh/school
  PasswordAuthentication no
",
}
