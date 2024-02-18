import requests
import cv2
from PIL import Image, ImageOps
from io import BytesIO
import numpy as np
from api_utils import query
from image_utils import decode_base64_image
from constants import API_URL, API_TOKEN, headers, mask_colors
from draw_legend import draw_legend

while True:
    response = requests.get('https://hackathon.shawnhaque.com/capture')
    if response.status_code == 200:
        image_data = BytesIO(response.content)
        image = Image.open(image_data)

        buffered = BytesIO()
        image.save(buffered, format="JPEG")
        img_str = buffered.getvalue()

        output = query(img_str, API_URL, headers)

        if output is None:
            print("Skipping frame due to API error")
            continue

        original_img = image.convert("RGBA")
        mask_overlay = Image.new("RGBA", original_img.size)
        used_labels = set()  # Track which labels are actually used

        for item in output:
            label = item.get("label")
            mask_base64 = item.get("mask")
            if mask_base64 and label in mask_colors:
                used_labels.add(label)
                mask_img = decode_base64_image(mask_base64).convert("L")
                mask_img = mask_img.resize(original_img.size, Image.BILINEAR)
                colored_mask = ImageOps.colorize(mask_img, "black", mask_colors[label])
                colored_mask = colored_mask.convert("RGBA")
                alpha = mask_img.point(lambda p: int(p * 0.5))
                colored_mask.putalpha(alpha)
                mask_overlay = Image.alpha_composite(mask_overlay, colored_mask)

        final_img = Image.alpha_composite(original_img, mask_overlay).convert("RGB")

        # Convert PIL Image to OpenCV format
        final_img_cv = cv2.cvtColor(np.array(final_img), cv2.COLOR_RGB2BGR)

        # Scale the final image to twice its original size for larger display
        scaling_factor = 2.0  # Adjust scaling factor as needed
        final_img_cv_resized = cv2.resize(final_img_cv, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_LINEAR)

        # Draw the enhanced legend on the resized final image
        final_img_cv_resized = draw_legend(final_img_cv_resized, used_labels, mask_colors)

        # Display the result in a larger window
        cv2.imshow("Segmented Image with Enhanced Legend", final_img_cv_resized)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit the loop
            break
    else:
        print(f"Failed to fetch the image. Status code: {response.status_code}")

cv2.destroyAllWindows()
