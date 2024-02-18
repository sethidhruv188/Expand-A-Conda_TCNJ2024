API_URL = "https://api-inference.huggingface.co/models/matei-dorian/segformer-b5-finetuned-human-parsing"
API_TOKEN = "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"  # Use your actual Hugging Face API token
headers = {"Authorization": f"Bearer {API_TOKEN}"}

mask_colors = {
    "Hair": "green",
    "Hat": "darkred",
    "Sunglasses": "black",
    "Upper-clothes": "yellow",
    "Skirt": "blue",
    "Pants": "purple",
    "Dress": "magenta",
    "Belt": "grey",
    "Left-shoe": "olive",
    "Right-shoe": "teal",
    "Face": "red",
    "Left-leg": "orange",
    "Right-leg": "pink",
    "Left-arm": "lightgreen",
    "Right-arm": "lightblue",
    "Bag": "brown",
    "Scarf": "cyan"
}
