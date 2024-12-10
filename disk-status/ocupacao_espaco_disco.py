import os
import pandas as pd
import plotly.express as px

def get_directory_size(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

def list_files_and_directories(path):
    data = []
    for dirpath, dirnames, filenames in os.walk(path):
        for dirname in dirnames:
            dir_full_path = os.path.join(dirpath, dirname)
            dir_size = get_directory_size(dir_full_path)
            data.append((dir_full_path, dir_size, 'Directory'))
        
        for filename in filenames:
            file_full_path = os.path.join(dirpath, filename)
            file_size = os.path.getsize(file_full_path)
            data.append((file_full_path, file_size, 'File'))
    
    return pd.DataFrame(data, columns=['Path', 'Size', 'Type'])

def generate_graphs(df):
    fig = px.bar(df, x='Path', y='Size', color='Type', title='Ocupação do Espaço em Disco')
    fig.write_html('ocupacao_espaco_disco.html')
    fig.show()

def main():
    path = input("Digite o caminho do diretório: ")
    df = list_files_and_directories(path)
    generate_graphs(df)

if __name__ == "__main__":
    main()
