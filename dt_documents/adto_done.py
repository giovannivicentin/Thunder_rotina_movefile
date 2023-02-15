import os
import shutil

# Function to move files from one folder to another based on keyword
def move_files(source_dir, destinations):
    for filename in os.listdir(source_dir):
        for keyword, destination_dir in destinations:
            # Check if keyword is in the filename
            if keyword in filename.split("-")[1]:
                # Move the file to the destination folder
                shutil.move(os.path.join(source_dir, filename), os.path.join(destination_dir, filename))
                break
            
# Move files from ExtratosA folder
source_dir = "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\ExtratosA"
destinations = [("ExtratoMensal", "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\4@ DONE\\ExtratosA")]
move_files(source_dir, destinations)

# Move files from HoleritesA folder
source_dir = "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\DominioWebDocumentos\\3@ DOING\\HoleritesA"
destinations = [("RecibodePagamento", "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\4@ DONE\\HoleritesA")]
move_files(source_dir, destinations)

# Move files from LiquidosA folder
source_dir = "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\DominioWebDocumentos\\3@ DOING\\LiquidosA"
destinations = [("RelatóriodeLíquidos", "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\4@ DONE\\LiquidosA")]
move_files(source_dir, destinations)