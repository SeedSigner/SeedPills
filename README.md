# SeedPills
Create your own set of 3D-printable BIP39 bitcoin lottery pieces!

This Python program generates code compatible with OpenSCAD modeling software (https://openscad.org).

Users will need to manually modify the progam to indicate the number of vertical columns, horizontal rows, and the starting BIP39 seed word for their grid of Seed Pills.

To generate the OpenSCAD code for your grid, just run the seedpills.py program and use ">>" to direct the output to a text file of your choosing:

<img src="/pictures/execute.png">

Then, just copy and paste the contents of the text file to OpenSCAD "Editor" window. In OpenSCAD, you will need to select "Preview" to view your generated grid:

<img src="/pictures/5x5.png">

If you are satisfied with your grid, select "Render" and then "Export as STL" in OpenSCAD to obtain a 3D-printable file. (Note that rendering the model can be a lengthy process depending on the size of your model and the processing capability of your computer.)

Notes:
- The pills will be two-sided so take this into account when printing (a full set will be 1024 pieces)
- The pills are interlocked to help with bed adhesion, and so you can verify the words after removing them from the printer 
