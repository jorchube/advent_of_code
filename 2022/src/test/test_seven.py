from src.seven import parse_filesystem

def test_moves_to_root_directory():
    test_input = "$ cd /"

    filesystem = parse_filesystem(test_input)

    assert filesystem.cwd.name == "/"
    assert filesystem.as_dict() == {
        "/": {}
    }

def test_moves_to_root_directory_and_lists_content():
    test_input = """\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
"""

    filesystem = parse_filesystem(test_input)

    assert str(filesystem.cwd) == "/"
    assert filesystem.as_dict() == {
        "/": {
            "/a/": {},
            "/b.txt (14848514)": None,
            "/c.dat (8504156)": None,
            "/d/": {}
        }
    }

def test_moves_to_subdirectory_directory_and_lists_content():
    test_input = """\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
"""

    filesystem = parse_filesystem(test_input)

    assert str(filesystem.cwd) == "/a/"
    assert filesystem.as_dict() == {
        "/": {
            "/a/": {
                "/a/e/": {},
                "/a/f (29116)": None,
                "/a/g (2557)": None,
                "/a/h.lst (62596)": None
            },
            "/b.txt (14848514)": None,
            "/c.dat (8504156)": None,
            "/d/": {}
        }
    }

def test_moves_up():
    test_input = """\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""

    filesystem = parse_filesystem(test_input)

    assert str(filesystem.cwd) == "/d/"
    assert filesystem.as_dict() == {
        "/": {
            "/a/": {
                "/a/e/": {
                    "/a/e/i (584)": None
                },
                "/a/f (29116)": None,
                "/a/g (2557)": None,
                "/a/h.lst (62596)": None
            },
            "/b.txt (14848514)": None,
            "/c.dat (8504156)": None,
            "/d/": {
                "/d/j (4060174)": None,
                "/d/d.log (8033020)": None,
                "/d/d.ext (5626152)": None,
                "/d/k (7214296)": None,
            }
        }
    }

def test_gets_directory_size():
    test_input = """\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""

    filesystem = parse_filesystem(test_input)

    assert filesystem.directories["/a/e/"].get_size() == 584
    assert filesystem.directories["/a/"].get_size() == 94853
    assert filesystem.directories["/d/"].get_size() == 24933642
    assert filesystem.directories["/"].get_size() == 48381165

def test_gets_total_size_of_directories_of_at_most_100000_size():
    test_input = """\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""

    filesystem = parse_filesystem(test_input)
    total_size = filesystem.get_total_size_of_dirs_with_max_size(100000)

    assert total_size == 95437

def test_gets_data_after_traversing_twice_the_filesystem():
    test_input = """\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""

    filesystem = parse_filesystem(test_input)

    assert filesystem.directories["/a/e/"].get_size() == 584
    assert filesystem.directories["/a/"].get_size() == 94853
    assert filesystem.directories["/d/"].get_size() == 24933642
    assert filesystem.directories["/"].get_size() == 48381165

    total_size = filesystem.get_total_size_of_dirs_with_max_size(100000)

    assert total_size == 95437

def test_returns_size_of_smallest_directory_that_leaves_free_space_of_30000000_of_total_70000000():
    test_input = """\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""

    needed_space = 30000000
    total_space = 70000000

    filesystem = parse_filesystem(test_input)

    directory = filesystem.smallest_directory_to_delete(needed_space, total_space)

    assert directory.get_size() == 24933642
