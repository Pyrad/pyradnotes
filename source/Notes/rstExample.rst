.. This is an example to show usages of reStructuedtext


Twenty Thousand Leagues Under the Sea
=====================================

.. warning:: 
    This is just several short paragraphs for short description of the
    syntax of reStructuedtext.

Chapter 1 A Runaway Reef
------------------------

*THE YEAR* 1866 was marked by a bizarre development, an unexplained and
downrightinexplicable phenomenon that surely no one has forgotten.

Without getting into those **rumors** that upset civilians in the *seaports
andderanged* the public mind even far inland,

it must be said that ``professional`` seamen were especially alarmed.

.. _myRefAnchor:

Traders, shipowners, captains of vessels, skippers, and master mariners
from Europe and America, naval officers from every country, and at their
heels the various national governments on these two continents, were all
extremely disturbed by the business.

In essence, over a period of time several ships had encountered "an enormous
thing" at sea, a long spindle-shaped object, sometimes giving off a
phosphorescent glow, infinitely bigger and faster than any whale.

The relevant data on this apparition, as recorded in various logbooks,
agreed pretty closely as to the structure of the object or creature in
question, its unprecedented speed of movement, its startling locomotive
power, and the unique vitality with which it seemed to be gifted.

.. note:: 
    This is the first Chapter


Chapter 2 The Pros and Cons
---------------------------

And indeed, unless this reef had an engine in its belly, how could it
move about with such prodigious speed?

Also discredited was the idea of a floating hull or some other enormouswreckage,
and again because of this speed of movement.

So only two possible solutions to the question were left, creating two
very distinct groups of supporters:

on one side, those favoring a monster of colossal strength; on the other,
those favoring an "underwater boat" of tremendous motor power.

Now then, although the latter hypothesis was completely admissible, it
couldn't stand up toinquiries conducted in both the New World and the Old.

That a private individual had such a mechanism at his disposal was less
than probable. Where and when had he built it, and how could he have built
it in secret?

Only some government could own such an engine of destruction, and in these
disaster-filled times,

when men tax their ingenuity to build increasingly powerful aggressive weapons,
it was possible that,

unknown to the rest of the world, some nation could have been testing such a
fearsome machine.

.. tip:: 
    This is the second chapter


\.\.\. this is to be continued \.\.\.

.. error:: 
    This is not all of this novel


Lists
---------------------------

chapters to be continued

* chapter 3
* chapter 4
* chapter 5

#. chapter 6
#. chapter 7
#. chapter 8

Images
---------------------------

An image of Riho

.. image:: /_static/riho.jpg

Code blocks
---------------------------

This is an example of Tcl code

.. code:: tcl

    proc isDesiredContext { m } {
        set res 0
        if { $m eq "Red-black tree" } {
            set res 1
        }
        return $res
    }


Tables
---------------------------

================ =============== ===== ===========
Platform         Self-Contained? Cost  Flexibility
================ =============== ===== ===========
Raspberry        No              $30   Limitless
Lego Mindstorms  Yes             $350  Medium
================ =============== ===== ===========

+----------------+---------------+-----+-----------+
|Platform        |Self-          |     |           |
|                |Contained?     |Cost |Flexibility|
+================+===============+=====+===========+
|Raspberry       |No             |$30  |Limitless  |
+----------------+---------------+-----+-----------+
|Lego Mindstorms |Yes            |$350 |Medium     |
+----------------+---------------+-----+-----------+

.. list-table:: Comparison
    :widths: 20 10 10 15
    :header-rows: 1

    * - Platform
      - Self-Contained?
      - Cost
      - Flexibility
    * - Raspberry Pi
      - No
      - $30
      - Limitless
    * - Lego Mindstorms
      - Yes
      - $350
      - Medium

.. csv-table:: Comparison
    :header: Platform, Self-Contained?, Cost, Flexibility
    :widths: 15 10 30 30

    Raspberry, No, $30, Limitless
    Lego Mindstorms, Yes, $350, Medium


Links
---------------------------

External links

My Github page: https://pyrad.github.io/

My Github page: `Pyrad Notes <https://pyrad.github.io/>`_

Link to my file: :doc:`/Git/gitcmd`

Link to my file: :doc:`Chinese Poetry </ChinesePoetry/shici>`

Linke to paragraph: :ref:`4th Paragraph in Chapter 1 <myRefAnchor>`