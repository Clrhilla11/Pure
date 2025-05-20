#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import os

# Create the output directory if it doesn't exist
output_dir = "Pure/Assets.xcassets/AppIcon.appiconset"
os.makedirs(output_dir, exist_ok=True)

# Define the icon sizes needed
icon_sizes = [
    (20, 1), (20, 2), (20, 3),  # Notification
    (29, 1), (29, 2), (29, 3),  # Settings
    (40, 1), (40, 2), (40, 3),  # Spotlight
    (60, 2), (60, 3),          # iPhone App
    (76, 1), (76, 2),          # iPad App
    (83.5, 2),                 # iPad Pro App
    (1024, 1)                  # App Store
]

# Define colors
background_color = (59, 130, 246)  # Blue
text_color = (255, 255, 255)       # White

# Generate icons for each size
for size, scale in icon_sizes:
    pixel_size = int(size * scale)
    img = Image.new('RGB', (pixel_size, pixel_size), background_color)
    draw = ImageDraw.Draw(img)
    
    # Add a simple design - a white circle
    circle_radius = pixel_size * 0.4
    circle_center = (pixel_size / 2, pixel_size / 2)
    circle_bbox = (
        circle_center[0] - circle_radius,
        circle_center[1] - circle_radius,
        circle_center[0] + circle_radius,
        circle_center[1] + circle_radius
    )
    draw.ellipse(circle_bbox, fill=text_color)
    
    # Add a letter "P" in the middle
    if pixel_size >= 60:
        try:
            # Try to use a built-in font
            font_size = int(pixel_size * 0.4)
            font = ImageFont.truetype("Arial", font_size)
            text = "P"
            text_bbox = draw.textbbox((0, 0), text, font=font)
            text_width = text_bbox[2] - text_bbox[0]
            text_height = text_bbox[3] - text_bbox[1]
            text_position = (
                (pixel_size - text_width) / 2,
                (pixel_size - text_height) / 2 - text_height * 0.1  # Slight adjustment for centering
            )
            draw.text(text_position, text, font=font, fill=background_color)
        except Exception:
            # Fallback if font doesn't work
            pass
    
    # Save the icon
    filename = f"AppIcon-{size}x{size}@{scale}x.png"
    img.save(os.path.join(output_dir, filename))
    print(f"Created {filename}")

# Update the Contents.json file
contents = {
    "images": [
        # iOS icons
        {"size": "20x20", "idiom": "iphone", "filename": "AppIcon-20x20@2x.png", "scale": "2x"},
        {"size": "20x20", "idiom": "iphone", "filename": "AppIcon-20x20@3x.png", "scale": "3x"},
        {"size": "29x29", "idiom": "iphone", "filename": "AppIcon-29x29@2x.png", "scale": "2x"},
        {"size": "29x29", "idiom": "iphone", "filename": "AppIcon-29x29@3x.png", "scale": "3x"},
        {"size": "40x40", "idiom": "iphone", "filename": "AppIcon-40x40@2x.png", "scale": "2x"},
        {"size": "40x40", "idiom": "iphone", "filename": "AppIcon-40x40@3x.png", "scale": "3x"},
        {"size": "60x60", "idiom": "iphone", "filename": "AppIcon-60x60@2x.png", "scale": "2x"},
        {"size": "60x60", "idiom": "iphone", "filename": "AppIcon-60x60@3x.png", "scale": "3x"},
        # iPad icons
        {"size": "20x20", "idiom": "ipad", "filename": "AppIcon-20x20@1x.png", "scale": "1x"},
        {"size": "20x20", "idiom": "ipad", "filename": "AppIcon-20x20@2x.png", "scale": "2x"},
        {"size": "29x29", "idiom": "ipad", "filename": "AppIcon-29x29@1x.png", "scale": "1x"},
        {"size": "29x29", "idiom": "ipad", "filename": "AppIcon-29x29@2x.png", "scale": "2x"},
        {"size": "40x40", "idiom": "ipad", "filename": "AppIcon-40x40@1x.png", "scale": "1x"},
        {"size": "40x40", "idiom": "ipad", "filename": "AppIcon-40x40@2x.png", "scale": "2x"},
        {"size": "76x76", "idiom": "ipad", "filename": "AppIcon-76x76@1x.png", "scale": "1x"},
        {"size": "76x76", "idiom": "ipad", "filename": "AppIcon-76x76@2x.png", "scale": "2x"},
        {"size": "83.5x83.5", "idiom": "ipad", "filename": "AppIcon-83.5x83.5@2x.png", "scale": "2x"},
        # App Store icon
        {"size": "1024x1024", "idiom": "ios-marketing", "filename": "AppIcon-1024x1024@1x.png", "scale": "1x"},
        # macOS icons
        {"size": "16x16", "idiom": "mac", "filename": "AppIcon-16x16@1x.png", "scale": "1x"},
        {"size": "16x16", "idiom": "mac", "filename": "AppIcon-16x16@2x.png", "scale": "2x"},
        {"size": "32x32", "idiom": "mac", "filename": "AppIcon-32x32@1x.png", "scale": "1x"},
        {"size": "32x32", "idiom": "mac", "filename": "AppIcon-32x32@2x.png", "scale": "2x"},
        {"size": "128x128", "idiom": "mac", "filename": "AppIcon-128x128@1x.png", "scale": "1x"},
        {"size": "128x128", "idiom": "mac", "filename": "AppIcon-128x128@2x.png", "scale": "2x"},
        {"size": "256x256", "idiom": "mac", "filename": "AppIcon-256x256@1x.png", "scale": "1x"},
        {"size": "256x256", "idiom": "mac", "filename": "AppIcon-256x256@2x.png", "scale": "2x"},
        {"size": "512x512", "idiom": "mac", "filename": "AppIcon-512x512@1x.png", "scale": "1x"},
        {"size": "512x512", "idiom": "mac", "filename": "AppIcon-512x512@2x.png", "scale": "2x"}
    ],
    "info": {
        "version": 1,
        "author": "xcode"
    }
}

import json
with open(os.path.join(output_dir, "Contents.json"), "w") as f:
    json.dump(contents, f, indent=2)

print("Updated Contents.json")
print("Done! App icons have been generated.") 