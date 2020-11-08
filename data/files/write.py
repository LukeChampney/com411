def run():
  def search(file_path):
    print("Searching...")
    sections = []
    books = []
    with open(file_path) as file:
      for line in file:
        if line.startswith("Section"):
          section_name = line.split(":")[1]
          sections.append(section_name.strip())
        else:
          books.append(line.strip())
    print("Done!")
    return (sections, books)

  def save(file_path, data):
    print("Saving...")
    with open("output.txt", "w") as file:
      file.write(f"Sections: {data[0]}")
      file.write(f"Books: {data[1]}")
    print("Done")

  def run():
    data = search("data/files/txt/books.txt")
    save("data/files/txt/section-books.txt", data)

  run()


