#External imports
import cx_Freeze

executables = [cx_Freeze.Excecutable("Main.py")]

cx_Freeze.setup(
				name="Labyrinth",
				options={"build_exe": {"packages": ["pygame"], "included_files": ["../assets/images/L1.png"]}},
				executables=executables
				)