import os
from PIL import Image

# Path to the folder containing PNG images
folder_path = "content/"
output_folder_path = 'captions'
target_product = 'cable'


# Iterate through each file in the directory
for product in os.listdir(folder_path):
    if product == target_product:
        product_folder_path = os.path.join(folder_path, product)

        test_folder_path = os.path.join(product_folder_path, "test")
        for anomaly_type in os.listdir(test_folder_path):
            if anomaly_type != "good":
                image_folder_path = os.path.join(test_folder_path, anomaly_type)
                for filename in os.listdir(image_folder_path):
                    if filename.endswith(".png"):
                        image_path = os.path.join(image_folder_path, filename)
                        text_content = "A close up of an anomalous " + product  + " that is " + anomaly_type
                        
                        # Get the image name without the extension
                        name = product + "_" + anomaly_type + "_" + os.path.splitext(filename)[0] 
                        
                        # Create a text file and write the content to it
                        text_file_path = os.path.join(output_folder_path, f"{name}.txt")
                        image_file_path = os.path.join(output_folder_path, f"{name}.png")
                        
                        # Save the content to a text file
                        with open(text_file_path, 'w') as text_file:
                            text_file.write(text_content)
                        image = Image.open(image_path)
                        image.save(image_file_path)
        image_folder_path = os.path.join(product_folder_path, "train", "good")
        anomaly_type = "good"
        for filename in os.listdir(image_folder_path):
            if filename.endswith(".png"):
                image_path = os.path.join(image_folder_path, filename)
                text_content = "A close up of a normal " + product
                
                # Get the image name without the extension
                name = product + "_" + anomaly_type + "_" + os.path.splitext(filename)[0] 
                
                # Create a text file and write the content to it
                text_file_path = os.path.join(output_folder_path, f"{name}.txt")
                image_file_path = os.path.join(output_folder_path, f"{name}.png")
                
                # Save the content to a text file
                with open(text_file_path, 'w') as text_file:
                    text_file.write(text_content)
                image = Image.open(image_path)
                image.save(image_file_path)
print("Text files created successfully.")