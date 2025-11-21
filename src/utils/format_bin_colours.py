def format_bin_colours(bin_colours):
  if len(bin_colours) == 1:
    return bin_colours[0]

  if len(bin_colours) == 2:
    return f'{bin_colours[0]} and {bin_colours[1]}'
