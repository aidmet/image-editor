import image_editor as editor

# Load the image using the DrawingImg class
image = editor.load('img.jpg')

# Perform operations using the class methods
image.stroke(10, 10, 200, 200, width='5px', style='fountain pen')\
     .rectangle(50, 50, 150, 150, outline='red', fill='blue')\
     .add_text("Hello World", (100, 100), font_size=30, color='white')\
     .blur(radius=5)\
     .save('edited_image.png')