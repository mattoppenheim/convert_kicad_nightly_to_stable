$FILENAME=convert_kicad_footprint.py
while inotifywait -e close_write $FILENAME; do make; done
