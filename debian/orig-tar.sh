#!/bin/sh -e

# $2 version
TAR=../shinken_$2.orig.tar.gz
DIR=shinken_$2
DEBIAN_EXCLUDE="debian/orig-tar.exclude"

tar zxfv $3
mv naparuba-shinken-* $DIR
tar -zcf $3 -X $DEBIAN_EXCLUDE $DIR
rm -rf $DIR

exit 0
