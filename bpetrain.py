import os
import glob

txt_files = glob.glob(os.path.join('data', '*.txt'))
corpus=[]
def read_file_with_fallback(file_path):
    encodings = ['utf-8', 'utf-8-sig', 'latin-1', 'cp1252']
    for enc in encodings:
        try:
            with open(file_path, 'r', encoding=enc) as file:
                return file.read()
        except UnicodeDecodeError:
            continue
    raise UnicodeDecodeError(f"Could not decode {file_path} with tried encodings.")

for file_path in txt_files:
    try:
        content = read_file_with_fallback(file_path)
        corpus.append(content)
        print("===")
        #print("\n")
    except Exception as e:
        print(f"Failed to read {file_path}: {e}")

output_file = 'lawrawdata_corpus.txt'
with open(output_file, 'w', encoding='utf-8') as f:
    f.write('\n\n'.join(corpus))
print(f"Combined corpus saved to {output_file}")
