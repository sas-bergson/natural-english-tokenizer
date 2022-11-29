from pygments.lexer import RegexLexer, DelegatingLexer, bygroups
from pygments.lexers import RubyLexer
from pygments.token import Text, Other, Keyword, Number

class PryPrefixLexer(RegexLexer):
    """
       Strips the prompt off each line, and renders it as boring "Text".
       The remainder of the line is yielded to the RubyLexer by PryLexer.
    """
    tokens = {
        'root' : [
          # Headings from various pry commands
          (r'^([A-Z][a-z ]+)(:\n|: .*\n)', bygroups(Keyword, Text)),
          # line-numbered code listings
          (r'^( *(?:=> *)?)(\d+)(: )(.*\n)', bygroups(Text, Number, Text, Other)),
          # Match the default prompt: [1] pry(main)>
          # the continuation prompt:  [1] pry(main)*
          # and output hash-rocket:   =>
          (r'(.*?(?:\)>|=>|\)\*) )(.*\n)', bygroups(Text, Other)),
          # trailing prompt
          (r'(.*?(?:\)>|=>|\)\*)\n)', bygroups(Text)),
        ]
    }

class PryLexer(DelegatingLexer):
    """
        Lexes pry sessions by stripping off the prompts with PryPrefexLexer
        and forwarding the rest of the output to the RubyLexer
    """
    name = 'Pry'
    aliases = ['pry']
    filenames = ['*.pry']

    def __init__(self, **options):
        super(PryLexer, self).__init__(RubyLexer, PryPrefixLexer, **options)

