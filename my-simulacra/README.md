Directions
==========
Please recover the sensitive information from this redacted document.

https://nostradamus.imfast.io/My_Simulacra.png

Writeup
=======
Run `exiftool`, find that there is thumbnail data.
Extract with `exiftool -b -ThumbnailImage My_Simulacra.png > thumbnail`.

`file` tells us that the thumbnail is a JPEG:
`mv thumbnail thumbnail.jpg`

Suffer through a blurry mess.
