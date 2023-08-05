
# A wrapper class for direct CorBoard instructions, called 'sentences'.
class Sentence:
    def __init__(self, target=None, operation=None, source=None):
        self.target = target
        self.operation = operation
        self.source = source
    def __str__(self):
        return self.target + ' ' + self.operation + ' ' + self.source
    def __repr__(self):
        return str(self)


# A wrapper class for CorBoard polynomials which are broken down to lists of direct instructions.
# A list of direct instructions is called a 'paragraph'.
class Polynomial:
    def __init__(self, target=None, polynomial=None):
        self.target = target
        self.polynomial = polynomial


# Takes a corboard program with polynomial paragraphs
# and breaks them down to direct instruction paragraphs.
def breakdown(chapter):

    # A full CorBoard program is a list of paragraphs and is called a 'chapter'.
    for paragraph in chapter:

        # Direct instruction paragraphs are passed along untouched.
        if type(paragraph) == type(list()):
            yield paragraph

        # Breaks down polynomial paragraphs.
        elif type(paragraph) == type(Polynomial()):
            # Unwraps the Polynomial object.
            target = paragraph.target
            polynomial = paragraph.polynomial

            # Sets the target to zero initially.
            direct_paragraph = [Sentence(target, '=', 'zero$global')]

            # Multiplies out each monomial.
            for monomial in polynomial.split(' '):
                sign = monomial[0]
                first_term = True

                # The product is built up in a temporary scoreboard objective.
                for term in monomial[1:].split('*'):
                    operation = '=' if first_term else '*='
                    direct_paragraph.append(Sentence('temp', operation, term))
                    first_term = False

                # Adds each product to the target.
                direct_paragraph.append(Sentence(target, sign + '=', 'temp'))

            # The newly created paragraph of direct instructions.
            yield direct_paragraph


# Takes a broken down CorBoard program and adds some extra scaling instructions
# to make multiplication and division floating-point friendly.
def add_scaling(broken_chapter):

    # Reads the chapter paragraph by paragraph.
    for paragraph in broken_chapter:

        # Stores the new floating-point friendly paragraph.
        scaled_paragraph = []

        # Reads the paragraph sentence by sentence.
        for sentence in paragraph:

            # Handles multiplication sentences.
            if sentence.operation == '*=':
                scaled_paragraph.append(sentence)
                # De-scales the product which would be double-scaled otherwise.
                scaled_paragraph.append(Sentence(sentence.target, '/=', 'scale$global'))

            # Handles division sentences.
            elif sentence.operation == '/=':
                # Pre-scales the target since the scaling would cancel otherwise.
                scaled_paragraph.append(Sentence(sentence.target, '*=', 'scale$global'))
                scaled_paragraph.append(sentence)

            # Other sentences are passed along unchanged.
            else: scaled_paragraph.append(sentence)

        # The newly created floating-point friendly paragraph.
        yield scaled_paragraph


# Distinguishes individual and global scoreboard objectives.
def parse_objective(name):

    # Global objective format is 'DUMMY_PLAYER$OBJECTIVE'
    if '$' in name: return name.replace('$', ' ')

    # Individual objectives are held by armor stands.
    return '@s ' + name


# Compiles a CorBoard program into Minecraft scoreboard commands.
def compile(chapter, verbose=False):

    # Breaks down the chapter, adds scaling, then reads it paragraph by paragraph.
    for paragraph in add_scaling(breakdown(chapter)):

        # Stores the scoreboard commands.
        command_paragraph = []

        # Reads the paragraph sentence by sentence.
        for sentence in paragraph:

            # Reformats a CorBoard instruction as a Minecraft scoreboard command.
            command = 'execute as @e[type=minecraft:armor_stand] run scoreboard players operation '
            command += parse_objective(sentence.target)
            command += ' ' + sentence.operation + ' '
            command += parse_objective(sentence.source)

            # Adds the scoreboard command to the growing paragraph.
            command_paragraph.append(command)

            # Verbosity.
            if verbose: print(command)

        yield command_paragraph

        # Verbosity.
        if verbose: print(' ')