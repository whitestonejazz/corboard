from programs import *
from locomotion import absolute_locomotion
from corboard import compile
from schematicizer import schematicize

# Chaos attractor.
schematicize(compile(chencel_chapter, verbose=True), 'chencel')

# Movement engine.
schematicize(absolute_locomotion(), 'locomotion_engine')
