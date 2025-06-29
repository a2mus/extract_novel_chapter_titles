import os

def save_chapters_to_markdown(chapter_titles, dest_folder, filename):
    """
    Saves a list of chapter titles to a Markdown file.

    Args:
        chapter_titles (list): A list of strings, where each string is a chapter title.
        dest_folder (str): The path to the destination folder.
        filename (str): The name of the file.
    """
    try:
        # Ensure the destination folder exists
        if not os.path.exists(dest_folder):
            os.makedirs(dest_folder)

        # Ensure the filename has a .md extension
        if not filename.endswith('.md'):
            filename += '.md'

        file_path = os.path.join(dest_folder, filename)
        
        # Get the title from the filename (without extension)
        title = os.path.splitext(filename)[0]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(f"# {title}\n\n")
            for chapter in chapter_titles:
                f.write(f"- {chapter}\n")
        
        print(f"Successfully saved chapters to {file_path}")

    except IOError as e:
        print(f"Error writing to file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")