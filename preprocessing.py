from sklearn.model_selection import train_test_split
import cv2
import os
import yaml

root_dir="dataset/"
valid_formats=[".jpg",".jpeg",".png",".txt"]


def file_paths(root,valid_formats):
    file_paths=[]
    for dirpath,dirnames,filenames in os.walk(root):
       # print("dirpath:",dirpath)
        #print("dirnames:",dirnames)#names of the directories inside the dataset
        #print("filenames:",filenames)  #names of all the files inside the dataset

        for filename in filenames:
            extension=os.path.splitext(filename)[1].lower()
            #print(filename,extension)
            if extension in valid_formats:
                file_paths.append(os.path.join(dirpath,filename))
    return file_paths


label_paths=file_paths(root_dir+"labels",valid_formats[-1])
image_paths=file_paths(root_dir+"images",valid_formats[:3])

x_train,x_valid_test,y_train,y_valid_test=train_test_split(image_paths,label_paths,test_size=0.3,random_state=42)
x_valid,x_test,y_valid,y_test=train_test_split(x_valid_test,y_valid_test,test_size=0.7,random_state=42)



def write_to_file(image_paths,label_paths,x):
    os.makedirs(image_paths,exist_ok=True)
    os.makedirs(label_paths,exist_ok=True)
    for image_path in x:
        # Use os.path.basename() for cross-platform compatibility
        img_name=os.path.splitext(os.path.basename(image_path))[0]
        img_ext=os.path.splitext(os.path.basename(image_path))[1]

        image=cv2.imread(image_path)
        cv2.imwrite(os.path.join(image_paths, f"{img_name}{img_ext}"), image)

        # Use os.path.join() for cross-platform path handling
        label_file_path = os.path.join(root_dir, "labels", f"{img_name}.txt")
        f=open(os.path.join(label_paths, f"{img_name}.txt"), "w")
        label_file=open(label_file_path, "r")
        f.write(label_file.read())
        f.close()
        label_file.close()
       
        



write_to_file(os.path.join("dataset", "images", "train"), os.path.join("dataset", "labels", "train"), x_train)
write_to_file(os.path.join("dataset", "images", "valid"), os.path.join("dataset", "labels", "valid"), x_valid)
write_to_file(os.path.join("dataset", "images", "test"), os.path.join("dataset", "labels", "test"), x_test)

                
data={
    "path":"../dataset",
    "train":"images/train",
    "val":"images/valid",
    "test":"images/test",
    
    "names":["number plate"]
}  

yaml_str = yaml.dump(data, sort_keys=False)
if not yaml_str:
    raise ValueError("yaml.dump returned empty string—check your `data` structure!")

with open("number_plate.yaml", "w", encoding="utf-8") as f:
    f.write(yaml_str)






