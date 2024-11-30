import os

labels_dir = "./dataset/train/labels"

class_ids = set()

for label_file in os.listdir(labels_dir):
    file_path = os.path.join(labels_dir, label_file)
    with open(file_path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        class_id = int(line.split()[0])
        class_ids.add(class_id)

print(f"Classes found: {sorted(class_ids)}")
print(f"Total classes: {len(class_ids)}")
