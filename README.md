Convert Kicad-nightly v6.99 build footprints to kicad stable v6.0.7.
Uses Python to apply regular expressions to the footprint file.

Creates a directory called kicad_convered with the edited files in them. The files retain their original name.

The script converts:

```(stroke (width 0.15)(type solid))```

to

```(width 0.15)```

also

```(stroke (width 0)(type solid))```

to

```(width 0)```

Look in convert_footprint.py for the regular expressions used.
Pytest tests in test_convert_kicad_footprint.py. Requires pytest and pytest-mock.

I didn't get all the footprint features converted successfully. I manually deleted arcs (fp_arc) and redrew these as I only had a handful in my design.

To run:

```python convert_kicad_footprint.py <input_footprint>```

To run on all files in the current directory:

```find . -name '*.kicad_mod' -exec python ./convert_kicad_footprint.py {} \;```

matt@mattoppenheim.com

Licence: Attribution 4.0 International (CC BY 4.0)

Matt Oppenheim October 2022
