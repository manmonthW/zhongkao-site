import os
import re

subjects = ['daofa', 'huaxue', 'lishi', 'shuxue', 'wuli', 'yingyu', 'yuwen']
base_dir = '/home/ekewang/projects/zhongkao'

def get_html_files(directory):
    html_files = set()
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, directory)
                html_files.add(rel_path)
    return html_files

def check_reference(file_path, target_rel_path):
    if not os.path.exists(file_path):
        return False
    # Use just the filename part for matching, or the relative path
    # Search for the path in quotes to match href="path"
    filename = os.path.basename(target_rel_path)
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            if target_rel_path in content or filename in content:
                # Basic check to see if it's likely a link
                if f'"{target_rel_path}"' in content or f'"{filename}"' in content or \
                   f"'{target_rel_path}'" in content or f"'{filename}'" in content or \
                   f'>{target_rel_path}<' in content or f'>{filename}<' in content:
                    return True
    except Exception:
        pass
    return False

results = []
summary = {}

for sub in subjects:
    sub_dir = os.path.join(base_dir, sub)
    site_sub_dir = os.path.join(base_dir, 'site', sub)
    
    sub_files = get_html_files(sub_dir)
    site_files = get_html_files(site_sub_dir)
    
    extra_files = sorted(list(sub_files - site_files))
    
    sub_summary = {'total': len(extra_files), 'referenced': 0, 'unreferenced': 0}
    
    root_index = os.path.join(base_dir, 'index.html')
    sub_index = os.path.join(base_dir, sub, 'index.html')
    site_sub_index = os.path.join(base_dir, 'site', sub, 'index.html')
    
    for extra in extra_files:
        ref_by = []
        
        # 1. root index.html
        if check_reference(root_index, f"{sub}/{extra}"):
            ref_by.append('root/index.html')

        # 2. sub/index.html
        if check_reference(sub_index, extra):
            ref_by.append(f'{sub}/index.html')
            
        # 3. site/sub/index.html
        if check_reference(site_sub_index, extra):
            ref_by.append(f'site/{sub}/index.html')
            
        referenced = 'Y' if ref_by else 'N'
        if referenced == 'Y':
            sub_summary['referenced'] += 1
        else:
            sub_summary['unreferenced'] += 1
            
        results.append([sub, extra, referenced, ', '.join(ref_by)])
    
    summary[sub] = sub_summary

print(f"{'subject':<10} | {'extra_file':<40} | {'ref?':<4} | {'referenced_by'}")
print("-" * 100)
for row in results:
    print(f"{row[0]:<10} | {row[1]:<40} | {row[2]:<4} | {row[3]}")

print("\nSummary Statistics:")
print(f"{'subject':<10} | {'extra总量':<10} | {'被引用数':<10} | {'未引用数':<10}")
print("-" * 50)
for sub in subjects:
    s = summary[sub]
    print(f"{sub:<10} | {s['total']:<10} | {s['referenced']:<10} | {s['unreferenced']:<10}")
