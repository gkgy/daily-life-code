import os
import random
import chardet

authors = ['1', '2', '3']
insert_count = 4
folder = r'D:\software\anaconda\envs\ai\codev1\Texttest' 

for filename in os.listdir(folder):
    if filename.endswith('.txt'):
        
        file_path = os.path.join(folder, filename)
        
        detected = chardet.detect(open(file_path, 'rb').read())
        encoding = detected['encoding']

        with open(file_path, encoding=encoding, errors='ignore') as f:
            
            content = f.read()
            
            if len(content) == 0: 
                continue # 跳过空文件
                
            for i in range(insert_count):
                
                author = random.choice(authors)
                
                if len(content) == 0:
                    insert_line = 0
                else:
                    lines = len(content.splitlines())
                    insert_line = random.randint(0, lines)
                
                content = content.split('\n')
                content.insert(insert_line, author)
                content = '\n'.join(content)
                    
        with open(file_path, 'w', encoding=encoding) as f:
            f.write(content)
        
print('完成!')