#!/usr/bin/env bash
#Script tha authenticaye without password
file { '/home/your_username/.ssh/config':
content => "\
Host ubuntu@54.144.151.196
  IdentityFile ~/.ssh/school
  PasswordAuthentication no
  SendEnv LANG LC_*
  HashKnownHosts yes
  GSSAPIAuthentication yes
  GSSAPIDelegateCredentials no
",
}
