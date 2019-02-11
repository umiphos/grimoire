#!/bin/sh
set -x
    sftp downloads@files.vauxoo.com <<EOT
    ls absa120/auto6
    EOT
    # get superpet100/auto/superpet100_deactivated_20171026_080006_20171026_110039.tar.bz2
    # quit
set +x
