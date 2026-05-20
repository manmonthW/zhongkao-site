import os
import hashlib

def get_file_hash(filepath):
    if not os.path.isfile(filepath): return None
    hasher = hashlib.md5()
    try:
        with open(filepath, 'rb') as f:
            for chunk in iter(lambda: f.read(65536), b""):
                hasher.update(chunk)
        return hasher.hexdigest()
    except: return None

root_dir = '/home/ekewang/projects/zhongkao'
site_dir = os.path.join(root_dir, 'site')

site_files = {}
for root, dirs, files in os.walk(site_dir):
    for name in files:
        full_path = os.path.join(root, name)
        rel_path = os.path.relpath(full_path, site_dir)
        site_files[rel_path] = full_path

only_in_site = []
both_same = []
both_different = []
only_in_root = []

root_files_seen = set()
for root, dirs, files in os.walk(root_dir):
    if 'site' in dirs: dirs.remove('site')
    if '.git' in dirs: dirs.remove('.git')
    for name in files:
        full_path = os.path.join(root, name)
        rel_path = os.path.relpath(full_path, root_dir)
        root_files_seen.add(rel_path)

for rel_path, site_path in site_files.items():
    root_path = os.path.join(root_dir, rel_path)
    if os.path.exists(root_path) and os.path.isfile(root_path):
        if get_file_hash(site_path) == get_file_hash(root_path):
            both_same.append(rel_path)
        else:
            both_different.append(rel_path)
    else:
        only_in_site.append(rel_path)

for rel_path in root_files_seen:
    if rel_path not in site_files:
        only_in_root.append(rel_path)

def write_report(filename, only_site, same, diff, only_root):
    with open(filename, 'w') as f:
        f.write(f"SUMMARY:\n")
        f.write(f"only_in_site: {len(only_site)}\n")
        f.write(f"both_same: {len(same)}\n")
        f.write(f"both_different: {len(diff)}\n")
        f.write(f"only_in_root: {len(only_root)}\n\n")
        f.write("--- only_in_site ---\n")
        for p in sorted(only_site): f.write(f"{p}\n")
        f.write("\n--- both_different ---\n")
        for p in sorted(diff): f.write(f"{p}\n")
        f.write("\n--- both_same ---\n")
        for p in sorted(same): f.write(f"{p}\n")
        f.write("\n--- only_in_root ---\n")
        for p in sorted(only_root): f.write(f"{p}\n")

write_report('merge_report_before.txt', only_in_site, both_same, both_different, only_in_root)
print(f"only_in_site: {len(only_in_site)}")
print(f"both_different: {len(both_different)}")
