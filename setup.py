from cx_Freeze import setup, Executable


setup(
    name = "dailyscrum",
    version = "0.1",
    description = "",
    executables = [Executable("dailyscrum.py")]
)
