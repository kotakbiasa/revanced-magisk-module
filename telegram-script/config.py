class Config:
    REVANCED_APKS_RELEASE_URL = (
        "https://api.github.com/repos/kotakbiasas/revanced-magisk-module/releases/latest"
    )
    MICROG_RELEASE_URL = (
        "https://github.com/ReVanced/GmsCore/releases/latest"
    )
    REVANCED_CHANGES_URL = (
        "https://api.github.com/repos/revanced/revanced-patches"
    )
    REVANCED_EXTENDED_CHANGES_URL = (
        "https://api.github.com/repos/inotia00/revanced-patches"
    )
    
    CREDITS_MESSAGE = "Credits to our upstream repository [j-hc/revanced-magisk-module](https://github.com/j-hc/revanced-magisk-module)"

    RELEASE_MESSAGE = """📑 *RELEASE* {release_name}

[Release notes and changelogs (What's New)]({changelogs_url})

📦 *Downloads* 

{nonroot_files}

{credits_message}
    
@KotakReVanced"""
