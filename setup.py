from skbuild import setup


setup(
    name="dll",
    version="1.0.0",
    packages=["dll", "dll.sub"],
    package_dir={"dll.sub": "dll/sub"},
    package_data={
        "dll": ["lib.dll"]
    },
)
