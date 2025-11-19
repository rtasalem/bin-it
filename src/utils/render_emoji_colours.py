from constants.emoji_bin_colours import emoji_bin_colours

def render_emoji_colours(bin_colours):
  result_emojis = [emoji_bin_colours[c] for bin_colour in bin_colours if bin_colour in bin_colours]

  output = ''.join(result_emojis)

__all__ = ['render_emoji_colours']
