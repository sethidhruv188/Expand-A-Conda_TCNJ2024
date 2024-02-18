"""This function creates a legend to be used in tandem with our open cv display
this allows the end user to understand what the different masks theyre looking at
refer to"""
import cv2
import numpy as np
from PIL import Image

def apply_gradient_filled_rectangle(background, top_left, bottom_right, color1, color2, vertical=True, alpha=0.8):
  
    x0, y0 = top_left
    x1, y1 = bottom_right
    if vertical:
        for i, alpha in enumerate(np.linspace(0, 1, y1 - y0)):
            color = tuple([int((1 - alpha) * c1 + alpha * c2) for c1, c2 in zip(color1, color2)])
            cv2.line(background, (x0, y0 + i), (x1, y0 + i), color, 1)
    else:
        for i, alpha in enumerate(np.linspace(0, 1, x1 - x0)):
            color = tuple([int((1 - alpha) * c1 + alpha * c2) for c1, c2 in zip(color1, color2)])
            cv2.line(background, (x0 + i, y0), (x0 + i, y1), color, 1)

def draw_rounded_rectangle(img, top_left, bottom_right, color, corner_radius, thickness):
   
    x0, y0 = top_left
    x1, y1 = bottom_right
    cv2.rectangle(img, (x0 + corner_radius, y0), (x1 - corner_radius, y1), color, thickness)
    cv2.rectangle(img, (x0, y0 + corner_radius), (x1, y1 - corner_radius), color, thickness)
    cv2.circle(img, (x0 + corner_radius, y0 + corner_radius), corner_radius, color, thickness)
    cv2.circle(img, (x1 - corner_radius, y0 + corner_radius), corner_radius, color, thickness)
    cv2.circle(img, (x0 + corner_radius, y1 - corner_radius), corner_radius, color, thickness)
    cv2.circle(img, (x1 - corner_radius, y1 - corner_radius), corner_radius, color, thickness)

def draw_legend(img, used_labels, mask_colors):
    if not used_labels:
        return img

    
    font = cv2.FONT_HERSHEY_SIMPLEX
    base_font_scale = 0.5
    font_thickness = 1
    corner_radius = 10
    legend_padding = 10
    box_height = 20
    box_width = 20
    text_offset_x = 10
    inter_item_spacing = 10

    
    text_widths = [cv2.getTextSize(label, font, base_font_scale, font_thickness)[0][0] for label in used_labels]
    max_text_width = max(text_widths)
    legend_width = max_text_width + box_width + text_offset_x + legend_padding * 2
    legend_height = len(used_labels) * (box_height + inter_item_spacing) + legend_padding * 2 - inter_item_spacing

    
    start_x, start_y = img.shape[1] - legend_width - 20, 20
    overlay = img.copy()
    apply_gradient_filled_rectangle(overlay, (start_x, start_y), (start_x + legend_width, start_y + legend_height),
                                    (60, 30, 70), (130, 50, 200), vertical=True, alpha=0.4)
    cv2.addWeighted(overlay, 0.6, img, 0.4, 0, img)

    draw_rounded_rectangle(img, (start_x, start_y), (start_x + legend_width, start_y + legend_height), (255, 255, 255), corner_radius, -1)

    
    shadow_offset = 5
    cv2.rectangle(img, (start_x + shadow_offset, start_y + shadow_offset), (start_x + legend_width + shadow_offset, start_y + legend_height + shadow_offset), (0, 0, 0), -1)

   
    for idx, label in enumerate(used_labels):
        item_y = start_y + legend_padding + idx * (box_height + inter_item_spacing)
        color_rgb = Image.new('RGB', (1, 1), mask_colors[label]).getpixel((0, 0))
        color_bgr = color_rgb[::-1]
        cv2.rectangle(img, (start_x + legend_padding, item_y), (start_x + legend_padding + box_width, item_y + box_height), color_bgr, -1)
        cv2.putText(img, label, (start_x + legend_padding + box_width + text_offset_x, item_y + box_height // 2 + 7), font, base_font_scale, (255, 255, 255), font_thickness)

    return img
