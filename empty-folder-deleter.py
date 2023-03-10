import unreal

# Get a reference to the Unreal Editor's asset library
editor_asset_lib = unreal.EditorAssetLibrary()

# Set the directory to search for empty folders in
source_dir = "/Game/"

# Set whether to include subfolders in the search
include_subfolders = True


# Initialize a count for how many folders were deleted
deleted_folders = 0

# List all assets in the specified directory, including folders
assets = editor_asset_lib.list_assets(source_dir, recursive=include_subfolders, include_folder=True)

# Filter out only the folder assets
folders = [asset for asset in assets if editor_asset_lib.does_directory_exist(asset)]

# Iterate through each folder and check if it contains any assets
# If a folder does not contain any assets, delete it
for folder in folders:
    has_assets = editor_asset_lib.does_directory_have_assets(folder)

    if not has_assets:
        editor_asset_lib.delete_directory(folder)
        deleted_folders += 1
        unreal.log("Folder {} without assets was deleted". format(folder))

# Log how many folders were deleted
unreal.log("Deleted {} folders without assets".format(deleted_folders))
