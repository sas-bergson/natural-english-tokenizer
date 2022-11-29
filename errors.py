class TokenizerError(Exception):
    """ Base class for exceptions """


class PhraseStartError(TokenizerError):
    """ Sentence doesn't respects the starting condition """


class PhraseEndError(TokenizerError):
    """ Sentence doesn't respects the ending condition """
