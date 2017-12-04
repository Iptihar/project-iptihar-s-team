-----------------Graphical User Interface-----------Marcus

The Graphical User Interface that was integrated into the project using the TKinter module that comes native to the
Python framework. We thought it was ideally basic to implement so that time would not be spent struggling to learn any
of the more advanced GUI frameworks or platforms that may be far more powerful than what TKinter has to offer.

Coming from IDE's that are equipped with GUI Design Editors for easily accessed visual design of user-created interfaces,
designing the GUI from code certainly felt like a trip to the dark-ages. While it was a mild inconvenience to write the
GUI in this way, the process is not an unfamiliar one. I understood the struggles having to manually integrate the GUI in
the source code itself as opposed to using an interface editor so it did not take as long for me to take care of the process
by tapping into my knowledge of past projects that demanded the writing of the GUI in this fashion.

Though my past experience faciliated the creation of the interface, TKinter had a handful of quirks that defied some of
the conventions that I had learned throughout previous projects. Such as the Width and Height of simple TKinter Widgets like
Buttons and Dropdowns. Before, I had thought that the quantities were in terms of the number of pixels across the parent container.
Instead, TKinter seems to measure X and Width in the length of the number of text characters (i.e. a width of 5 would stretch
the widget to match the length of a 5 letter word as if it were to appear on the screen); while it measures Height in terms of the
length of a number of lines of text laid out vertically. Its not hard to imagine entering a Y offset value of 30 which I initially
expected to move the widget downward 30 pixels, but to be completely confused by it's absence when in actuality, it is 30 lines down
and virtually located 12 inches off of the computer screen. Because of this unexpected convention, I ended up wasting a great deal
of time trying to figure out how the number system actually behaved as opposed to the more familiar convention of pixel quantities.

My Python experience was very minimal coming into this project, so this would naturally lead to even more pitfalls and road-blocks
to progress. The notion of variable scopes escaped me when doing work in Python, so I had assumed that all variables were global
unless they had an object preceding it that one intended to access. When one of TKinter's Button events were fired and called
a function I had designated for it to run when this occurs, the global variables I had attempted to reference would mysteriously
cease to exist, throwing errors in the program's output. This caused even more baffling disorientation and confusion, burning
even more precious time. Oddly enough, some variables were still available such as the Root container which holds all of the
other widgets in the GUI so I did what, to me, seemed like a novel, outside-of-the-box solution to my problem which is most likely
considered child's-play to seasoned Python professionals: instead of storing the variable in the 'global' scope, I placed the
the variables that I needed remote access for in the Root object. It was an effective tactic, but anyone who has even used Python
probably understands this concept; except me, apparently. Its just one more thing to add to the list of bumps that were encountered
while getting used to both TKinter and Python.

The integrated design of the 3 other Image Processing components created by my teammates was straight-forward and intuitive.
The execution of each function took a loadable Image on the left as an input, some additional arguments, and a press of
the Render button pushes the processed image into the output panel on the right side based on the context of the function tab.
They explained each of their tasks for me and designated what arguments they needed in order to effectively utilize the
component each of them were individually constructing. There were not any conflicts on how the arguments should be arranged
and I was in agreement with all of their requests. Color Model Transformation required me to learn to use Radio Buttons
and how to use them in a group with each Radio Button pointing to the desired Color Model. Smoothing and Sharpening required
the use of numeric variables with maximum and minimum limits so the logical widget for these arguments would be Spinboxes
that respect the appropriate range of values. Psuedo Image Processing required the use of an array of colors for input.
While there was a functionality for asking the user to choose a color, there was not an immediate widget for storing an array
of colors so I was responsible for creating that on my own.

The overall layout of the widgets and the context sensitive tab make for an intuitive and effective layout for easily executing
these useful Image Processing operations.
