from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import matplotlib.pyplot as plt
# import the circlify library
import circlify
import pandas as pd

circleValues = [3, 4, 6, 10]
df = pd.DataFrame({
    'Name': ['Ambiguity', 'Fear', 'Goals', 'Rundown'],
    'Value': circleValues
})

# compute circle positions:
circles = circlify.circlify(
    df['Value'].tolist(), 
    show_enclosure=True, 
    target_enclosure=circlify.Circle(x=0, y=0, r=1)
)

# Create just a figure and only one subplot
fig, ax = plt.subplots(figsize=(10,10))

# Title
ax.set_title('Basic circular packing')

# Remove axes
ax.axis('off')

# Find axis boundaries
lim = max(
    max(
        abs(circle.x) + circle.r,
        abs(circle.y) + circle.r,
    )
    for circle in circles
)
plt.xlim(-1, 1)
plt.ylim(-1, 1)
# list of labels
labels = df['Name']

# print circles
count = 0
print(circles)
for circle, label in zip(circles, labels):
    print(circle)
    x, y, r = circle
    count += 1
    ax.add_patch(plt.Circle((x, y), r, alpha=0.2, linewidth=2))
    plt.annotate(
          label, 
          (x,y),
          va='center',
          ha='center'
     )


class MyApp(App):

   def build(self):
        box = BoxLayout()
        graph = FigureCanvasKivyAgg(plt.gcf())
        box.add_widget(graph)
        return box

if __name__ == "__main__":
    MyApp().run()