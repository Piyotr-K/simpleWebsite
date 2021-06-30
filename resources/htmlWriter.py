def template():
    out = ""
    out += "<!DOCTYPE html>\n"
    return out

def generate_head():
    out = ""
    out += "<head>\n"
    out += "<title>Great Books</title>\n"
    out += "<link rel=\"stylesheet\" type=\"text/css\" href=\"bookstyle.css\">\n"
    out += "</head>\n"
    return out

def generate_body(data):
    out = ""
    out += "<body>\n"
    out += "<ul>\n"
    out += generate_list(data)
    out += "</ul>\n"
    out += "</body>\n"
    return out

def generate_list(data):
    out = ""
    for line in data:
        out += "<li>"
        try:
            rank, title, author, image = line.split(",")
            out += rank.strip() + ". "
            out += title.strip() + ", "
            out += author.strip() + ", "
            out += generate_img(image.strip())
        except ValueError:
            for item in line.split(","):
                if "https" in item.strip():
                    out += generate_img(item.strip())
                else:
                    out += item.strip() + ", "
        except TypeError:
            continue
        out += "</li>\n"
    return out

def generate_img(link):
    out = ""
    out += "\n"
    out += "<br/>"
    out += "<img src=\""
    out += link
    out += "\"/>\n"
    return out


def read_from_file(filename):
    f = open(filename, "r")
    out = f.readlines()
    f.close()
    return out

def write_to_file(string):
    f = open("books2.html", "w")
    f.write(string)
    f.close()

def main():
    text = read_from_file("top-books.txt")

    final = ""
    final += template()
    final += generate_head()
    final += generate_body(text)
    final += "\n</html>"
    write_to_file(final)

main()