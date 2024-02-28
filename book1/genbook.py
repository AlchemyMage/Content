import pypandoc
from pathlib import Path

# Define the output EPUB file
output_file = "my_book.epub"

# Define the input Markdown files
markdown_files = [
    str(file) for file in Path('.').glob('**/*.md')
]

# Convert the Markdown files to EPUB
output = pypandoc.convert_file(
    source_file=markdown_files,
    to='epub',
    outputfile=output_file,
    extra_args=['--toc', '--toc-depth=2']
)

print("EPUB has been generated.")