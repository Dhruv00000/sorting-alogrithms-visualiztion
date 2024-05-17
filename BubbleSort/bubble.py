#TODO: Make the sound functionaliy cross-platform.
#      Set the window to be maximized by default.
#      Make audios play concurrently with the sorting algorithm, otherwise the audio will either sound awkward or it will be a bottleneck.

from matplotlib import pyplot, rcParams
from numpy import random, ndarray, arange
# from winsound import Beep

# This variable controls the number of bars.
amount = 25

rcParams["toolbar"] = "None"
pyplot.figure(facecolor="black")
pyplot.subplots_adjust(left = 0, right = 1, bottom = 0)
pyplot.get_current_fig_manager().window.state('zoomed')

if isinstance(amount, int):

    lst: ndarray = random.randint(20, 150, amount)
    x = arange(0, amount, 1)

    for sorted_elements, i in enumerate(range(len(lst))):
        for j in range(len(lst) - i - 1):

            if amount >= 3:

                barGraph = pyplot.bar(x, lst)
                pyplot.axis('off') # Removing this line breaks the entire plot for some reason.

                for barIndex in range(len(barGraph)):
                    if (barIndex + 1) <= (len(barGraph) - sorted_elements): barGraph[barIndex].set_color("white")
                    else: barGraph[barIndex].set_color("green")

                # Beep((700 + int(800 * ((lst[j] - 20) / 130))), 40)

                if lst[j] > lst[j + 1]:

                    barGraph[j].set_color('b')
                    barGraph[j + 1].set_color('r')

                    lst[j], lst[j + 1] = lst[j + 1], lst[j]

                else:
                    barGraph[j].set_color('r')
                    barGraph[j + 1].set_color('b')

                pyplot.pause(0.000000001)
                if sorted_elements < len(barGraph) - 2: pyplot.clf()
                else:
                    for Bar in barGraph: Bar.set_color("green")
            
            else: print("\nAmount must be a non-zero integer greater than two.\n")

    if amount >= 3: pyplot.show()

else: print("\nAmount must be a non-zero integer greater than two.\n")

# n = len(lst)
# swapped = False
# # new_n = 0
# while not swapped: # n <= 1

#     swapped = False
#     # new_n = 0

#     for i in range(1, n -1):

#             barPlot = pyplot.bar(x, lst)
#             pyplot.axis('off')
#             for Bar in barPlot: Bar.set_color("white")

#             if lst[i - 1] > lst[i]:
                    
#                     barPlot[i].set_color('g')
#                     barPlot[i + 1].set_color('r')

#                     lst[i - 1], lst[i] = lst[i], lst[i -1]
#                     swapped = True
#                     # new_n = i
            
#             else:
#                 barPlot[i].set_color('r')
#                 barPlot[i + 1].set_color('g')

#             n -= 1
#             # n = new_n

#             pyplot.pause(0.000000001)
#             pyplot.clf()