import os
import shutil
import my_classes

my_class = my_classes.classes

for file in os.listdir('/home/kevin/Downloads'):
    try:
        filename = os.fsdecode(file)
        source = f'/home/kevin/Documents/Uni/{filename}'
        
        for item in my_class:
            if(item[0] in filename.lower()):
                if not(os.path.exists(item[1])):
                    os.mkdir(item[1])
                destination = f'{item[1]}/{filename}'
                match item[0]:
                    case "kn":
                        shutil.move(source, destination)
                    case "pdp":
                        shutil.move(source, destination)
                    case "fg":
                        shutil.move(source, destination)
                    case "ana2":
                        shutil.move(source, destination)
                    case "algo":
                        shutil.move(source, destination)
                    case "adm":
                        shutil.move(source, destination)
                    case "eidf":
                        shutil.move(source, destination)
                    case "es":
                        shutil.move(source, destination)
                    case "gdrn":
                        shutil.move(source, destination)
                    case "we":
                        shutil.move(source, destination)
                    case "mathe1":
                        shutil.move(source, destination)
            continue
        else:    
            _, extension = os.path.splitext(filename)
            destination = '/home/kevin/'
            match extension:
                case '.jpg' | '.jpeg' | '.png' | '.gif' | '.tiff':
                    destination = destination + f'Pictures'
                    shutil.move(source, destination)
                case '.mp4' | '.avi':
                    destination = destination + f'Videos'
                    shutil.move(source, destination)
                case '.pdf' | '.zip' | '.rar' | '.doc' | '.docx' | '.csv' | '.pptx' | '.ppt' | '.txt':
                    destination = destination + f'Documents'
                    shutil.move(source, destination)
                case '.mp3':
                    destination = destination + f'Music'
                    shutil.move(source, destination)
                case _:
                    print("the case is not made for: " +filename)
    except:
        print("Das muss so, trust me bro")