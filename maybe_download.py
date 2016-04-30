from __future__ import print_function
import os


def maybe_download(data_dir, s_name, s_url):
    """download and unpack the source file if not exists.

    args:
        data_dir (str): paht of directory for storing data.
        s_name (str): name of compressed source file.
        s_url (str): where to download source file.

    return:
        str: path of unpacked source file directory.
    """
    data_dir = os.path.expanduser(data_dir)
    if not os.path.isdir(data_dir):
        os.mkdir(data_dir)
        print("created data_dir:", data_dir)

    s_packed = os.path.join(data_dir, s_name)
    print("source path:", s_packed)
    # split twice for .tar.**
    s_dir, s_ext = os.path.splitext(s_packed)
    if s_dir.endswith(".tar"):
        s_dir, e = os.path.splitext(s_dir)
        s_ext = e + s_ext

    # always create a new directory for unpacked files
    if not os.path.isdir(s_dir):
        os.mkdir(s_dir)
        print("created source dir:", s_dir)

    if os.listdir(s_dir):
        print("file already exists:", s_dir)
    else:
        if not os.path.isfile(s_packed):
            print("downloading", s_name, "...")
            import urllib
            # download_path should == s_packed
            download_path, _ = urllib.urlretrieve(s_url, s_packed)
            print('Successfully downloaded', download_path)
            print("size:", os.path.getsize(download_path), 'bytes.')

        # uppack downloaded source file
        print("extracting file:", s_packed)
        if s_ext == ".tar.gz":
            import tarfile
            with tarfile.open(s_packed, "r:*") as f:
                f.extractall(s_dir)
        elif s_ext == ".bz2":
            # only single file!! need file name
            source = os.path.join(s_dir, os.path.basename(s_dir))
            import bz2
            data = bz2.BZ2File(s_packed).read()
            with open(source, "w") as new_source:
                new_source.write(data)
        elif s_ext == ".zip":
            import zipfile
            with zipfile.ZipFile(s_packed, "r") as z:
                z.extractall(s_dir)
        elif s_ext == "":
            print("no file extention")
        else:
            raise ValueError("unknown compressed file")
        print("successfully extracted file:")

    return s_dir


p = maybe_download("~/Downloads/text-classification", "rt-polaritydata.tar.gz", "http://www.cs.cornell.edu/people/pabo/movie-review-data/rt-polaritydata.tar.gz")
print(p)
