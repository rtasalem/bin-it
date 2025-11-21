from constants.bin_colour_emojis import bin_colour_emojis

def render_bin_colour_emojis(bin_colours):
  result_emojis = [bin_colour_emojis[bin_colour] for bin_colour in bin_colours if bin_colour in bin_colour_emojis]

  output = ''.join(result_emojis)

  return output
