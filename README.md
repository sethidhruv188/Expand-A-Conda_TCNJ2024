# Expand-a-Conda: Vision System for Search and Rescue

![Expand-a-Conda in Action](/path/to/your/Screenshot_2024-02-18_at_10.41.31_AM.png)

## Inspiration

Moved by firsthand accounts from relatives in post-earthquake Turkey, we were was inspired to create the Expand-a-Conda for our hackathon project. In response to stories of friends lost and agonizing waits for rescue, we developed an innovation born from real-life experiences, designed to swiftly detect and locate individuals buried in debris. This initiative combines technology with empathy, offering a lifeline in the aftermath of disasters.

## What It Does

Expand-a-Conda is ingeniously designed to detect people buried in debris using image segmentation and AI-powered pathfinding. It incorporates soft robotics by building a cheap and indestructible vine robot, capable of navigating through inaccessible terrains.

## How We Built It

We leveraged a finetuned version of the NVIDIA MIT-B5 model to detect humans trapped in rubble. Utilizing 3D printing technologies, we mounted a camera on our indestructible vine robot. The video feed from the camera is reverse-proxied through Cloudflare and processed by Google Cloud.

## Challenges We Ran Into

Our sole challenge was computing power. With limited resources, we endeavored to maintain accuracy while achieving acceptable performance. Currently, we face a low frame rate, which we aim to improve by integrating local GPUs for enhanced computing capabilities.

## Accomplishments That We're Proud Of

We're proud to have designed a solid proof of concept and developed a fully-functional prototype that demonstrates its feasibility and potential impact in disaster scenarios.

## What We Learned

The constraint of limited computing power pushed us to optimize our algorithms and processes rigorously. This endeavor sharpened our problem-solving skills and taught us to innovate within real-world constraints.

## What's Next for Expand-a-Conda

Our roadmap includes scaling up the computing power to achieve a higher frame rate, resulting in faster and more accurate detection capabilities. Additionally, we plan to incorporate a user identification system using the OpenCV library, which will aid in the swift identification of victims.

---

🚧 **Under Construction** 🚧

This project is no longer being developed, and new features are not being constructed!

