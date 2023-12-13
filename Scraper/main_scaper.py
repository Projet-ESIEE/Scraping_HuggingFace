import os


def folder_checker() -> None:
    """
    This function checks if the spider folder exists,
    if not run a shell script "init_scraper.sh" to make it
    :return: None
    """
    if not os.path.exists("twitch_crawler"):
        print("Creating twitch_crawler folder...")
        print(f"{RUN} init_scraper.{EXT}")
        # FIXME: The Run command should work on unix systems
        #    For win in powershell there is prbs
        # Check : the directory name


if __name__ == "__main__":
    if os.name == "nt":
        OS = "Windows"
        EXT = "ps1"
        RUN = "powershell.exe"
    elif os.name == "posix":
        OS = "Linux"
        EXT = "sh"
        RUN = "bash"

    folder_checker()
