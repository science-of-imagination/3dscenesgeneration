import subprocess

def main():
	#meshtool --load_collada "path_to_\964_244.dae" --save_rotate_screenshots "path_to_\964_244.jpg" 8 512 512
	subprocess.Popen(["meshtool", "--load_collada", "path_to_\964_244.dae", "--save_rotate_screenshots", "path_to_\964_244.jpg", "8", "512", "512"])
	
main()