import re

CD_REGEX = re.compile(r"\$ cd (.+)")
LS_REGEX = re.compile(r"\$ ls")
LS_CONTENT_DIR = re.compile(r"dir (.+)")
LS_CONTENT_FILE = re.compile(r"(\d+) (.+)")

class Node:
    def __init__(self, name):
        self.children = list()
        self.name = name
        self.parent = None

    def get_child_by_name(self, name):
        for child in self.children:
            if child.name == name:
                return child

    def set_parent(self, parent):
        self.parent = parent

    def add_child(self, child):
        child.set_parent(self)
        self.children.append(child)

    def is_child_already_added(self, name):
        return name in [child.name for child in self.children]

    def path(self):
        raise NotImplementedError

    def get_size(self):
        raise NotImplementedError

class File(Node):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    def content(self):
        return None

    def get_size(self):
        return self.size

    def path(self):
        return f"{self.parent.path()}{self.name}"

    def __str__(self):
        return f"{self.path()} ({self.size})"

class Directory(Node):
    def __init__(self, name):
        super().__init__(name)

    def content(self):
        return { str(child): child.content() for child in self.children }

    def get_size(self):
        return sum([child.get_size() for child in self.children])

    def path(self):
        if self.parent == None:
            return f"{self.name}"

        return f"{self.parent.path()}{self.name}/"

    def __str__(self):
        return self.path()

class Filesystem:
    def __init__(self):
        self.root = Directory("/")
        self.cwd = None
        self.directories = dict()
        self.directories[self.root.path()] = self.root

    def cd(self, dirname):
        if dirname == "..":
            self.cwd = self.cwd.parent
            return

        if dirname == "/":
            self.cwd = self.root
            return

        self.cwd = self.cwd.get_child_by_name(dirname)

    def ls_content_dir(self, name):
        if self.cwd.is_child_already_added(name):
            return

        directory = Directory(name)
        self.cwd.add_child(directory)
        self.directories[directory.path()] = directory

    def ls_content_file(self, name, size):
        if self.cwd.is_child_already_added(name):
            return

        self.cwd.add_child(File(name, size))

    def smallest_directory_to_delete(self, needed_space, total_space):
        used_space = self.root.get_size()
        free_space = total_space - used_space
        need_to_free = needed_space - free_space

        big_enough_dirs = filter(lambda d: d.get_size() >= need_to_free, self.directories.values())
        sorted_dirs = sorted(big_enough_dirs, key=lambda d: d.get_size())

        return sorted_dirs[0]

    def as_dict(self):
        return { str(self.root): self.root.content() }

    def get_total_size_of_dirs_with_max_size(self, max_size):
        dirs = filter(lambda d: d.get_size() <= max_size, self.directories.values())
        return sum([d.get_size() for d in dirs])

def parse_line(filesystem, line):
    match = CD_REGEX.match(line)
    if match:
        dirname = match.group(1)
        filesystem.cd(dirname)

    match = LS_REGEX.match(line)
    if match:
        return

    match = LS_CONTENT_DIR.match(line)
    if match:
        dirname = match.group(1)
        filesystem.ls_content_dir(dirname)

    match = LS_CONTENT_FILE.match(line)
    if match:
        filesize = int(match.group(1))
        filename = match.group(2)
        filesystem.ls_content_file(filename, filesize)

def parse_filesystem(input):
    filesystem = Filesystem()

    lines = input.strip().splitlines()
    for line in lines:
        parse_line(filesystem, line)

    return filesystem


if __name__ == "__main__":
    from input.input_seven import INPUT

    filesystem = parse_filesystem(INPUT)

    total_size_of_dirs_with_max_size_100000 = filesystem.get_total_size_of_dirs_with_max_size(100000)
    print(f"total_size_of_dirs_with_max_size_100000: {total_size_of_dirs_with_max_size_100000}")

    smallest_dir_to_get_3000000_space_out_of_7000000 = filesystem.smallest_directory_to_delete(30000000, 70000000)
    print(f"smallest_dir_size_to_get_3000000_space_out_of_7000000: {smallest_dir_to_get_3000000_space_out_of_7000000.get_size()}")
