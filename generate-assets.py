import os
import argparse
from PIL import Image

def create_empty_image(output_path, size):
    img = Image.new('RGB', size, (255, 255, 255))
    img.save(output_path)

def process_images(input_dir):
    if not os.path.exists(input_dir):
        os.makedirs(input_dir)

    image_specs = [
        ("store_page_header_capsule_image", (920, 430)),
        ("store_page_small_capsule_image", (462, 174)),
        ("store_page_main_capsule_image", (1232, 706)),
        ("store_page_vertical_capsule", (748, 896)),
        ("store_page_background", (1438, 810)),
        ("store_page_steam_broadcast", (155, 337)),
        ("store_page_about_section_banners", (616, 616)),
        ("store_page_screenshot_small", (1280, 720)),
        ("store_page_screenshot_large", (1920, 1080)),
        ("library_capsule", (600, 900)),
        ("library_hero", (3840, 1240)),
        ("library_logo", (1280, 720)),
        ("library_header_capsule", (920, 430)),
        ("community_group_header", (460, 215)),
        ("community_icons", (184, 184)),
        ("community_client_icons", (32, 32)),
        ("developer_page_logo", (184, 184)),
        ("developer_page_background_image", (1500, 220)),
        ("trading_card_small", (206, 184)),
        ("trading_card_large", (1920, 1080)),
        ("trading_card_badge", (80,80)),
        ('game_achievement_achieved', (256,256)),
        ('game_achievement_unachieved', (256,256)),
        ('steam_workshop', (948,203))
    ]

    for name, size in image_specs:
        output_name = f"{name}_{size[0]}x{size[1]}.png"
        output_path = os.path.join(input_dir, output_name)
        create_empty_image(output_path, size)

def main():
    parser = argparse.ArgumentParser(description="Create all empty images for Steam Store page.")
    parser.add_argument("directory", type=str, help="Directory to save the created images.")
    args = parser.parse_args()

    input_dir = args.directory

    process_images(input_dir)

if __name__ == "__main__":
    main()
