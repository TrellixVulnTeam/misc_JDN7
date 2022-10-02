# python 3 only !!
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
            import urllib.request
            import shutil
            # download_path should == s_packed
            # download_path, _ = urllib.urlretrieve(s_url, s_packed)
            with urllib.request.urlopen(s_url) as r, open(s_packed, 'wb') as f:
                shutil.copyfileobj(r, f)
            print('Successfully downloaded', s_packed)
            print("size:", os.path.getsize(s_packed), 'bytes.')

        # uppack downloaded source file
        print("extracting file:", s_packed)
        if s_ext == ".tar.gz":
            import tarfile
            with tarfile.open(s_packed, "r:*") as f:
                def is_within_directory(directory, target):
                    
                    abs_directory = os.path.abspath(directory)
                    abs_target = os.path.abspath(target)
                
                    prefix = os.path.commonprefix([abs_directory, abs_target])
                    
                    return prefix == abs_directory
                
                def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
                
                    for member in tar.getmembers():
                        member_path = os.path.join(path, member.name)
                        if not is_within_directory(path, member_path):
                            raise Exception("Attempted Path Traversal in Tar File")
                
                    tar.extractall(path, members, numeric_owner) 
                    
                
                safe_extract(f, s_dir)
        elif s_ext == ".bz2":
            # only single file!! need file name
            s = os.path.join(s_dir, os.path.basename(s_dir))
            import bz2
            data = bz2.BZ2File(s_packed).read()
            with open(s, "w") as s_unpack:
                s_unpack.write(data)
        elif s_ext == ".zip":
            import zipfile
            with zipfile.ZipFile(s_packed, "r") as z:
                z.extractall(s_dir)
        elif s_ext == ".gz":
            # only single file!! need file name
            s = os.path.join(s_dir, os.path.basename(s_dir))
            import gzip
            with gzip.open(s_packed, "rb") as f, open(s, "wb") as s_unpack:
                s_unpack.write(f.read())
        elif s_ext == "":
            print("no file extention")
        else:
            raise ValueError("unknown compressed file")
        print("successfully extracted file:")

    return s_dir

p = maybe_download("~/Downloads/text-classification", "rt-polaritydata.tar.gz", "http://www.cs.cornell.edu/people/pabo/movie-review-data/rt-polaritydata.tar.gz")
print(p)
