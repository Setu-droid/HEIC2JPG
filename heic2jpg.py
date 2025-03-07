#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path
from PIL import Image
from pillow_heif import register_heif_opener
import concurrent.futures
import time

def convert_heic_to_jpg(heic_path, output_root, quality=90):
    """Convert single HEIC file to JPG with path preservation"""
    try:
        relative_path = heic_path.relative_to(input_root)
        jpg_path = output_root / relative_path.with_suffix('.jpg')
        
        jpg_path.parent.mkdir(parents=True, exist_ok=True)
        
        with Image.open(heic_path) as img:
            img.convert('RGB').save(jpg_path, "JPEG", quality=quality)
            
        return (True, heic_path, jpg_path)
        
    except Exception as e:
        return (False, heic_path, str(e))

def main():
    parser = argparse.ArgumentParser(description='Bulk HEIC to JPG Converter for macOS')
    parser.add_argument('-i', '--input', required=True, help='Input directory containing HEIC files')
    parser.add_argument('-o', '--output', required=True, help='Output directory for JPG files')
    parser.add_argument('-q', '--quality', type=int, default=90, 
                       help='JPEG quality (1-100, default: 90)')
    parser.add_argument('-j', '--jobs', type=int, default=4,
                       help='Number of parallel workers (default: 4)')
    
    args = parser.parse_args()
    
    global input_root
    input_root = Path(args.input).expanduser().resolve()
    output_root = Path(args.output).expanduser().resolve()
    
    register_heif_opener()
    
    print(f"[*] Scanning {input_root} for HEIC files...")
    heic_files = list(input_root.rglob("*.[hH][eE][iI][cC]"))
    
    if not heic_files:
        print("[-] No HEIC files found")
        sys.exit(1)
        
    print(f"[+] Found {len(heic_files)} HEIC files")
    print(f"[*] Starting conversion with {args.jobs} workers...")
    
    start_time = time.time()
    success_count = 0
    failure_count = 0
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.jobs) as executor:
        futures = {executor.submit(convert_heic_to_jpg, f, output_root, args.quality): f 
                  for f in heic_files}
        
        for future in concurrent.futures.as_completed(futures):
            status, heic_path, result = future.result()
            
            if status:
                print(f"[✓] Converted {heic_path} -> {result}")
                success_count += 1
            else:
                print(f"[✗] Failed {heic_path}: {result}")
                failure_count += 1
                
    total_time = time.time() - start_time
    
    print(f"\n[+] Conversion complete")
    print(f"    Success: {success_count}")
    print(f"    Failures: {failure_count}")
    print(f"    Time: {total_time:.2f} seconds")
    print(f"    Output directory: {output_root}")

if __name__ == "__main__":
    main()

