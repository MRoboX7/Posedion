import base64

# Read image from local drive
with open('x.jpg', 'rb') as f:
    image_data = f.read()

# Encode image data as base64
image_base64 = base64.b64encode(image_data)

# Print encoded image data
print(image_base64.decode('utf-8'))

