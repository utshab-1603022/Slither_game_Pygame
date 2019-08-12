import cx_Freeze

executables = [cx_Freeze.Executable("Slither.py")]

cx_Freeze.setup(
    name = "Slither",
    options = {"build_exe":{"packages":["pygame"],"include_files":["Apple2.png","SnakeHead.png"]}},

    description = "Slither Game",
    executables = executable
    )
