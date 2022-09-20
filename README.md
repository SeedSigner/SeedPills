# SeedPills
Create your own set of 3D-printable BIP39 bitcoin lottery pieces

This Python program generates code compatible with OpenSCAD modeling software (https://openscad.org).

Users will need to manually modify the progam to indicate the number of vertical columns, horizontal rows, and the starting BIP39 seed word for their grid of Seed Pills.

To generate the OpenSCAD code for your grid, just run the seedpills.py program and use ">>" to direct the output to a text file of your choosing. Then, just copy and paste the contents of the text file to OpenSCAD "Editor" window. In OpenSCAD, you will need to select "Preview", "Render", and then "Export as STL" to obtain a 3D-printable file. Note that rendering the model can be a lengthy process depending on the size of your model and the processing capability of your computer.
