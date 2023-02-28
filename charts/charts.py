import matplotlib.pyplot as plot


def generate_pie_chart():
  labels = ['A', 'B', 'C']
  values = [ 300, 432, 620 ]

  fig, ax = plot.subplots()
  ax.pie(values, labels=labels)
  plot.savefig('my_pie.png')
  plot.close()
