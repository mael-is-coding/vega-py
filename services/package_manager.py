import subprocess

PACKAGE_MANAGER="pacman"
INSTALL_KEYWORD="-S"
VETTING_KEYWORD="-Ss"
UNINSTALL_KEYWORD="-Rs"

class PackageManager:
    """
    A wrapper around the system package manager to install dependencies that vega configures.
    """

    @staticmethod
    def vet(sys_package: str):
        print(f"Checking if {sys_package} exists in {PACKAGE_MANAGER}'s repos...")
        subprocess.run([PACKAGE_MANAGER, VETTING_KEYWORD, sys_package])

    @staticmethod
    def install(sys_package: str):
        """
        Calls the OS package manager to install the package described by the `sys_package` param.
        Mainly used to **install** tools that vega configures (e.g : `waybar|ironbar`, `swaync|mako`...)
        """
        PackageManager.vet(sys_package)
        print(f"Installing : {sys_package} using {PACKAGE_MANAGER}")
        subprocess.run([PACKAGE_MANAGER, INSTALL_KEYWORD, sys_package])

    @staticmethod
    def uninstall(sys_package: str):
        print(f"Removing : {sys_package}")
        subprocess.run([PACKAGE_MANAGER, UNINSTALL_KEYWORD, sys_package])

    @staticmethod
    def install_batch(sys_packages: list[str]):
        for sys_pkg in sys_packages:
            PackageManager.install(sys_pkg)