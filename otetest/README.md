---
title: OTETest
permalink: /otetest/index.html
---

# OTETest

### OpenType Layout test fonts in OpenType TT (.ttf) format

Digital data copyright (c) 2005 by Adam Twardoch. Based on Nimbus Roman, Copyright (c) 1999 by (URW)++ Design & Development. Licensed under [GPL2](./LICENSE).

The fonts are located in the [ttf](https://github.com/twardoch/test-fonts/tree/master/otetest/ttf/) folder.

These fonts are intended for testing OpenType Layout features and lookups.
* **otefea1.ttf** replaces the `a` glyph by a ligature glyph that shows the name of the feature applied.
* **otefea2.ttf** replaces the glyphs `a-z` with ligature glyphs showing the name of the feature applied.
* **otefea3.ttf** replaces the glyphs `one`, `two`, `three`, `four` or `five` with ligature glyphs showing the name of the feature applied.
* **otefea4.ttf** replaces the glyphs `a-zA-K` with ligature glyphs showing the name of the feature applied.
* The **otegsub?.ttf** and **otegpos?.ttf** fonts perform various substitutions or positionings to the glyphs `a-d`, mapped to many features, depending on the `GSUB` or `GPOS` LookupType indicated by the filename.

These fonts are intended for testing of OpenType Layout features support
in an application. Consult the [TTX or FEA source code](https://github.com/twardoch/test-fonts/tree/master/otetest/src/) of the `GSUB` or `GPOS` tables for details.
